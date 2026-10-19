"""M1-F5 · P3: servicios públicos (congestión). SOLO con la puerta prereg-m1 abierta (docs/preregistro.md §7 y adenda A8; techo
ASOCIACIÓN).

Educación: panel de 17 comunidades autónomas (sin Ceuta ni Melilla) × curso, de 2015-16 a 2021-22 (el último año con población
por país de nacimiento en el padrón es el 1-1-2022). Resultado: Δ alumnos por profesor equivalente a tiempo completo en los
centros públicos de régimen general (EDUCAbase, resumen 02). Tratamiento: Δ población nacida fuera de 5-19 años entre el 1 de
enero de los cursos consecutivos (ECP, t56948) / población de 5-19 años al inicio. Instrumento: shift-share de comunidad,
z = Σ_o s_o,c,1998 · ΔM_o,t / población 5-19 inicial, con s = cuota de la comunidad en los nacidos en o con nacionalidad
extranjera en 1998 y ΔM la variación nacional anual de nacidos en o (padrón 03006, todas las edades). Efectos fijos de curso,
pesos por población 5-19 inicial. Inferencia: wild cluster bootstrap restringido (Webb, 17 comunidades) de la forma reducida
(adenda A6: p ≤ 0,05 estricto); MC2E con errores agrupados por comunidad y F efectivo como diagnósticos. La ratio responde a
decisiones de contratación de profesorado: aunque el diseño fuera limpio, no separa congestión de respuesta de política
(techo ASOCIACIÓN).
Sanidad (listas de espera quirúrgicas): NO ESTIMABLE con datos públicos procesables (SISLE-SNS solo publica PDF por comunidad;
el dato que faltaría, espera por paciente y origen, solo existe en registros clínicos restringidos).
Salidas: output/f5/p3/P3-educacion/resultado.json, output/f5/p3/P3-sanidad/resultado.json y output/f5/p3_panel.csv.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import etiquetas  # noqa: E402
import px  # noqa: E402
from comun import OUT, PROC, RAW, Cifras, Registry, escribir_resultado  # noqa: E402
from f3_poblacion import ecp_enero  # noqa: E402
from territorio import PROV  # noqa: E402

O = OUT / "f5"
CURSOS = [f"{a}-{(a + 1) % 100:02d}" for a in range(2015, 2022)]


def ratios() -> pd.DataFrame:
    filas = []
    for cur in CURSOS:
        d = px.leer_px(RAW / "admin" / f"edu_{cur}_alumnos_profesor_resumen02.px")
        d = d[(d["Titularidad del centro"] == "CENTROS PÚBLICOS") & (d["Tipo de centro"] == "TOTAL")]
        ccaa = [c for c in d["Comunidad autónoma"].unique() if c != "Todos"]
        cod = {c: f"{i + 1:02d}" for i, c in enumerate(ccaa)}      # orden de EDUCAbase = códigos INE 01-19
        for _, r in d[d["Comunidad autónoma"] != "Todos"].iterrows():
            filas.append({"ccaa": cod[r["Comunidad autónoma"]], "anio": int(cur[:4]) + 1, "alumnos_profesor": float(r.valor)})
    return pd.DataFrame(filas)


def poblacion_5_19() -> pd.DataFrame:
    e = ecp_enero()
    e = e[e.prov.notna() & (e.edad != "Todas las edades") & e.nacimiento.isin(["Total", "Extranjero"])].copy()
    e["ini"] = e.edad.str.extract(r"(\d+)")[0].astype(int)
    e = e[e.ini.isin([5, 10, 15])]
    e["ccaa"] = e.prov.map(lambda p: PROV[p][1])
    return e.groupby(["ccaa", "anio", "nacimiento"]).valor.sum().unstack().reset_index()


def instrumento() -> pd.DataFrame:
    p = pd.read_csv(PROC / "padron_nacimiento.csv.gz", dtype={"prov": str})
    p = p[(p.sexo == "total") & (p.grupo != "España")]
    p["ccaa"] = p.prov.map(lambda x: PROV[x][1] if x in PROV else None)
    sh = p[(p.anio == 1998) & (p.nacionalidad == "extranjera")].pivot_table(index="ccaa", columns="pais", values="valor",
                                                                            aggfunc="sum").fillna(0)
    cuota = sh.div(sh.sum(0).where(sh.sum(0) > 0), axis=1).fillna(0)
    nat = p[p.nacionalidad == "total"].pivot_table(index="anio", columns="pais", values="valor", aggfunc="sum").fillna(0)
    filas = []
    for a in range(2016, 2023):
        dM = (nat.loc[a] - nat.loc[a - 1]).reindex(cuota.columns).fillna(0)
        for c, v in (cuota * dM).sum(1).items():
            filas.append({"ccaa": c, "anio": a, "shift_share": v})
    return pd.DataFrame(filas)


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    reg = Registry(O / "registro_p3.csv")
    cf = Cifras("f5_p3", "src/m1/f5_p3_servicios.py")
    r, pob, z = ratios(), poblacion_5_19(), instrumento()
    d = r.merge(pob, on=["ccaa", "anio"]).sort_values(["ccaa", "anio"])
    d = d[~d.ccaa.isin(["18", "19"])]
    d["pob0"] = d.groupby("ccaa").Total.shift(1)
    d["x"] = d.groupby("ccaa").Extranjero.diff() / d.pob0
    d["dy"] = d.groupby("ccaa").alumnos_profesor.diff()
    d = d.merge(z, on=["ccaa", "anio"], how="left")
    d["z"] = d.shift_share / d.pob0
    d = d.dropna(subset=["x", "dy", "z"])
    d.to_csv(O / "p3_panel.csv", index=False)
    W = np.column_stack([np.ones(len(d))] + [(d.anio == a).astype(float) for a in sorted(d.anio.unique())[1:]])
    y, x, zz, cl, w = d.dy.to_numpy(float), d.x.to_numpy(float), d.z.to_numpy(float), d.ccaa.to_numpy(), d.pob0.to_numpy(float)
    iv = econ.iv2sls(y, x, zz, W, cl, w)
    fe = econ.f_efectivo(x, zz, W, cl, w)
    Xrf = np.column_stack([zz, W])
    rf = econ.ols(y, Xrf, cl, w)
    wb = econ.wcr_boot(y, Xrf, 0, cl, B=9999, w=w)
    ols = econ.ols(y, np.column_stack([x, W]), cl, w)
    diag = {"F_efectivo": fe, "forma_reducida": float(rf["b"][0]), "p_wcb_forma_reducida": wb["p"], "G": wb["G"],
            "mco": float(ols["b"][0]), "ee_mco": float(ols["se"][0]), "ee_mc2e_cluster": float(iv["se"][0])}
    if fe < 10:
        ar = econ.ar_conjunto(y, x, zz, W, cl, w)
        diag["anderson_rubin"] = ar
    for k, b, se, p in (("mc2e", iv["b"][0], iv["se"][0], wb["p"]), ("mco", ols["b"][0], ols["se"][0], np.nan)):
        reg.log("F5", "P3-educacion", k, "17 CCAA × 6 cursos, efectos de curso", "2016-2022", len(d), b, se, p)
    clas = "ASOCIACIÓN"
    ic = [float(iv["b"][0] - 1.96 * iv["se"][0]), float(iv["b"][0] + 1.96 * iv["se"][0])]
    escribir_resultado(O / "p3" / "P3-educacion" / "resultado.json",
                       pregunta="P3 (educación): Δ alumnos por profesor en centros públicos por punto de aumento de la población "
                                "nacida fuera de 5-19 años sobre la población de 5-19 años, por comunidad autónoma",
                       capa="C4", clasificacion=clas, datos="EDUCAbase (Ministerio de Educación), ECP y padrón (INE)", N=len(d),
                       metodo="MC2E shift-share de comunidad (cuotas de 1998), efectos de curso; wild cluster bootstrap de la forma "
                              "reducida (Webb, 17 comunidades)", estimacion=float(iv["b"][0]), ic95=ic, p_ajustado=wb["p"],
                       diagnosticos=diag, notas="Techo ASOCIACIÓN pre-registrado (A6): la ratio responde a la contratación de "
                       "profesorado. IC por errores agrupados con 17 grupos (orientativo); la inferencia es el p del wild bootstrap.",
                       prereg=f"prereg-m1 {commit}")
    escribir_resultado(O / "p3" / "P3-sanidad" / "resultado.json",
                       pregunta="P3 (sanidad): listas de espera quirúrgicas y población nacida fuera por comunidad autónoma",
                       capa="C4", clasificacion="NO ESTIMABLE", datos="SISLE-SNS (solo PDF por comunidad)", N=0, metodo="—",
                       estimacion=None, ic95=[None, None], p_ajustado=None, diagnosticos={},
                       notas="No hay series públicas procesables. El dato que faltaría (espera y uso por paciente y origen) solo existe "
                             "en registros clínicos de acceso restringido.", prereg=f"prereg-m1 {commit}")
    cf.add("F5_P3_EDUC_beta", round(float(iv["b"][0]) / 100, 3), "alumnos por profesor por punto porcentual",
           f"P3 (educación): asociación entre el aumento de la población nacida fuera de 5-19 años y la ratio de alumnos por profesor "
           f"en centros públicos (MC2E por comunidad; F efectivo = {fe:.1f}; p wild bootstrap de la forma reducida = {wb['p']:.2f}; "
           "IC orientativo por errores agrupados en 17 comunidades)", "C4", "EDUCAbase, ECP y padrón", "2016-2022", "17 CCAA",
           "todos", clasificacion=clas, ic_inf=round(ic[0] / 100, 3), ic_sup=round(ic[1] / 100, 3))
    reg.flush()
    cf.escribir()
    print({"b": float(iv["b"][0]), **diag})
    return 0


if __name__ == "__main__":
    sys.exit(main())
