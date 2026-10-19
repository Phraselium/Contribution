"""M1-F5 · P1-E4: salarios de los españoles y cuota de nacidos fuera en celdas nacionales educación × edad (Borjas 2003). SOLO
con la puerta prereg-m1 abierta (docs/preregistro.md §2 y adenda A6: techo ASOCIACIÓN, sin instrumento).

Celdas: educación (baja, media, alta) × edad (20-29, 30-39, 40-49, 50-59, 60+; los tramos de la EES) × año de la EES (2010,
2014, 2018, 2022). Resultado: log del salario medio por hora de los asalariados de nacionalidad española (EES, pesos de
elevación). Exposición: cuota de nacidos fuera en la población activa de la celda (EPA, media de los cuatro trimestres del año).
Especificación pre-registrada: Δ log salario entre olas consecutivas sobre Δ cuota, con efectos fijos de celda y de ola, MCO
ponderado por el empleo de la celda, errores agrupados por celda y wild cluster bootstrap restringido (Webb, 15 celdas).
Sensibilidades: cuota por nacionalidad (la EES solo distingue nacionalidad) y la versión en niveles con efectos de celda y de año.
Corte de clasificación de estudios en la EES de 2010 (8 códigos) frente a 2014-2022 (7): se armoniza en tres niveles y los efectos
de ola absorben el cambio común. Salidas: output/f5/p1/P1-E4/resultado.json y output/f5/p1e4_celdas.csv.
"""
from __future__ import annotations

import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import etiquetas  # noqa: E402
from comun import OUT, PROC, RAW, Cifras, Registry, escribir_resultado  # noqa: E402
from f2_epa import trimestre  # noqa: E402

O = OUT / "f5"
OLAS = [2010, 2014, 2018, 2022]
EDAD_EES = {2: "20-29", 3: "30-39", 4: "40-49", 5: "50-59", 6: "60+"}


def educ_ees(anio: int, e: pd.Series) -> pd.Series:
    m = ({1: "baja", 2: "baja", 3: "baja", 4: "media", 5: "media", 6: "alta", 7: "alta", 8: "alta"} if anio == 2010 else
         {1: "baja", 2: "baja", 3: "baja", 4: "media", 5: "alta", 6: "alta", 7: "alta"})
    return e.map(m)


def salarios() -> pd.DataFrame:
    e = pd.read_csv(PROC / "ees.csv.gz", usecols=["anio", "edad", "estudios", "extranjero", "salario_hora", "factor"])
    e = e[e.anio.isin(OLAS) & ~e.extranjero & e.edad.isin(EDAD_EES) & (e.salario_hora > 0)].copy()
    e["educ"] = pd.concat([educ_ees(a, g.estudios) for a, g in e.groupby("anio")])
    e["edad_t"] = e.edad.map(EDAD_EES)
    g = e.groupby(["anio", "educ", "edad_t"])
    return pd.DataFrame({"log_salario": np.log(g.apply(lambda x: np.average(x.salario_hora, weights=x.factor), include_groups=False)),
                         "empleo_es": g.factor.sum(), "n_ees": g.size()}).reset_index()


def _celdas_trim(ruta: str) -> pd.DataFrame:
    d = trimestre(Path(ruta))
    d = d[(d.edad >= 20) & (d.educ != "no consta")].copy()
    d["edad_t"] = pd.cut(d.edad, [19, 29, 39, 49, 59, 200], labels=list(EDAD_EES.values())).astype(str)
    d["act_w"] = d.act * d.w
    d["fuera_nac"] = (d.g_nac != "España").astype(float) * d.act_w
    d["fuera_ncl"] = (d.g_ncl != "España").astype(float) * d.act_w
    d["n_act"] = d.act
    return d.groupby(["anio", "educ", "edad_t"])[["act_w", "fuera_nac", "fuera_ncl", "n_act"]].sum().reset_index()


def cuotas() -> pd.DataFrame:
    zips = [str(RAW / "epa" / "grandes" / f"datos_{t}t{a % 100:02d}.zip") for a in OLAS for t in range(1, 5)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        c = pd.concat(list(ex.map(_celdas_trim, zips)))
    c = c.groupby(["anio", "educ", "edad_t"]).sum().reset_index()
    c["cuota_fuera"] = c.fuera_nac / c.act_w
    c["cuota_extranjeros"] = c.fuera_ncl / c.act_w
    return c[["anio", "educ", "edad_t", "cuota_fuera", "cuota_extranjeros", "n_act"]]


def regresion(d: pd.DataFrame, x: str, en_niveles=False) -> dict:
    d = d.sort_values(["celda", "anio"]).copy()
    if en_niveles:
        y, xv, w, cl, anios = d.log_salario, d[x], d.empleo_es, d.celda, d.anio
    else:
        d["dy"] = d.groupby("celda").log_salario.diff()
        d["dx"] = d.groupby("celda")[x].diff()
        d = d.dropna(subset=["dy", "dx"])
        y, xv, w, cl, anios = d.dy, d.dx, d.empleo_es, d.celda, d.anio
    fe_c = pd.get_dummies(cl, drop_first=True, dtype=float).to_numpy()
    fe_a = pd.get_dummies(anios, drop_first=True, dtype=float).to_numpy()
    X = np.column_stack([xv.to_numpy(float), np.ones(len(y)), fe_c, fe_a])
    r = econ.ols(y.to_numpy(float), X, cl.to_numpy(), w.to_numpy(float))
    wb = econ.wcr_boot(y.to_numpy(float), X, 0, cl.to_numpy(), B=9999, w=w.to_numpy(float))
    return {"b": float(r["b"][0]), "se_cluster": float(r["se"][0]), "p_wcb": wb["p"], "G": wb["G"], "n": int(len(y))}


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    reg = Registry(O / "registro_p1e4.csv")
    cf = Cifras("f5_p1e4", "src/m1/f5_p1e4_borjas.py")
    d = salarios().merge(cuotas(), on=["anio", "educ", "edad_t"], how="inner")
    d["celda"] = d.educ + "|" + d.edad_t
    sup = d[(d.n_ees < 50) | (d.n_act < 50)]
    d = d[(d.n_ees >= 50) & (d.n_act >= 50)]
    d.to_csv(O / "p1e4_celdas.csv", index=False)
    pr = regresion(d, "cuota_fuera")
    sens = {"nacionalidad": regresion(d, "cuota_extranjeros"), "niveles": regresion(d, "cuota_fuera", en_niveles=True)}
    for k, r in [("principal", pr)] + list(sens.items()):
        reg.log("F5", "P1-E4", k, "", "15 celdas × 4 olas", r["n"], r["b"], r["se_cluster"], r["p_wcb"])
    # techo ASOCIACIÓN (adenda A6): sin instrumento, la covariación entre celdas no identifica el efecto
    clas = "ASOCIACIÓN"
    ic = [pr["b"] - 1.96 * pr["se_cluster"], pr["b"] + 1.96 * pr["se_cluster"]]
    escribir_resultado(O / "p1" / "P1-E4" / "resultado.json",
                       pregunta="P1-E4: Δ log salario por hora de los asalariados españoles por punto de Δ cuota de nacidos fuera en la "
                                "población activa de su celda nacional educación × edad",
                       capa="C4", clasificacion=clas, datos="EES 2010, 2014, 2018 y 2022; EPA microdatos (INE)", N=pr["n"],
                       metodo="MCO en primeras diferencias con efectos de celda y de ola, ponderado; errores agrupados por celda; "
                              "wild cluster bootstrap restringido (Webb)", estimacion=pr["b"], ic95=ic, p_ajustado=pr["p_wcb"],
                       diagnosticos={"principal": pr, **sens, "celdas_suprimidas": len(sup)},
                       notas="Techo ASOCIACIÓN pre-registrado (A6). La EES identifica nacionalidad, no país de nacimiento. "
                             "IC por errores agrupados con 15 celdas (orientativo); la inferencia es el p del wild bootstrap.",
                       prereg=f"prereg-m1 {commit}")
    cf.add("F5_P1_E4_beta", round(pr["b"], 3), "Δ log salario por punto de cuota", "P1-E4 (Borjas): asociación entre la cuota de "
           "nacidos fuera en la celda educación × edad y el salario por hora de los españoles (primeras diferencias; IC orientativo por "
           f"errores agrupados en 15 celdas; p wild bootstrap = {pr['p_wcb']:.2f})", "C4", "EES y EPA (INE)", "2010-2022", "España",
           "españoles (nacionalidad)", clasificacion=clas, ic_inf=round(ic[0], 3), ic_sup=round(ic[1], 3))
    reg.flush()
    cf.escribir()
    print({"principal": pr, **sens})
    return 0


if __name__ == "__main__":
    sys.exit(main())
