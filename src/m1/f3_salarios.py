"""M1-F3 · Salarios por origen (descriptivo; capas C1 y C4). Sin red.

Fuente principal: Encuesta de Estructura Salarial (2010-2022; nacionalidad España / resto del mundo, NUTS1). Segunda fuente:
ECV (rendimientos del trabajo por cuenta ajena PY010G de asalariados a jornada completa todo el año, por país de nacimiento).
Tercera: tablas de deciles de la EPA por nacionalidad (t66240).
Tres niveles para el logaritmo del salario por hora: bruto; edad y sexo; además estudios y región (NUTS1). Los años de
residencia no están en la EES ni en la ECV: ese nivel queda NO ESTIMABLE con datos públicos (haría falta la MCVL).
Errores agrupados por establecimiento (conglomerado del diseño de la EES).
Descomposiciones: Oaxaca-Blinder de la media del log y DFL en los deciles. Salidas en output/f3/salarios_*.csv.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
from comun import OUT, PROC, RAW, Cifras, cuantil_pond  # noqa: E402
from niveles import _dummies  # noqa: E402

O = OUT / "f3"
EES = "Encuesta de Estructura Salarial (INE)"
DEC = (0.1, 0.25, 0.5, 0.75, 0.9)


def ees() -> pd.DataFrame:
    d = pd.read_csv(PROC / "ees.csv.gz", dtype={"nuts1": str, "edad": str, "estudios": str, "cno1": str, "cnace": str,
                                                "establecimiento": str})
    d = d[(d.salario_hora > 1) & (d.salario_hora < 500) & (d.factor > 0)].copy()
    d["lw"] = np.log(d.salario_hora)
    d["grupo"] = np.where(d.extranjero, "Resto del mundo (nacionalidad)", "España (nacionalidad)")
    return d


def niveles_ees(x: pd.DataFrame) -> list[dict]:
    g = x.extranjero.to_numpy(float)
    w, y = x.factor.to_numpy(float), x.lw.to_numpy(float)
    cl = (x.anio.astype(str) + "_" + x.establecimiento.astype(str)).to_numpy()   # conglomerado del diseño: establecimiento
    c = np.ones((len(x), 1))
    x = x.assign(es=x.edad + "|" + x.sexo)
    out = []
    for nivel, X in (("bruto", np.column_stack([c, g])), ("edad y sexo", np.column_stack([c, g, _dummies(x, ["es"])])),
                     ("completo", np.column_stack([c, g, _dummies(x, ["es", "estudios", "nuts1"])])),
                     ("completo + ocupación, sector, contrato y jornada (informativo)",
                      np.column_stack([c, g, _dummies(x, ["es", "estudios", "nuts1", "cno1", "cnace", "contrato", "jornada"])]))):
        r = econ.ols(y, X, cl, w)
        out.append({"nivel_ajuste": nivel, "brecha_log": r["b"][1], "ee": r["se"][1], "brecha_pct": 100 * (np.exp(r["b"][1]) - 1)})
    return out


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f3_salarios", "src/m1/f3_salarios.py")
    d = ees()
    filas, dec, ox = [], [], []
    for a in sorted(d.anio.unique()):
        x = d[d.anio == a]
        n_ext = int(x.extranjero.sum())
        for r in niveles_ees(x):
            filas.append({"anio": a, **r, "n_muestral": n_ext})
        # deciles y DFL (composición: edad, sexo, estudios, NUTS1)
        X = _dummies(x.assign(es=x.edad + "|" + x.sexo), ["es", "estudios", "nuts1"])
        res = econ.dfl(x.lw.to_numpy(), X, x.extranjero.to_numpy(), x.factor.to_numpy(), cuantiles=DEC)
        for q, v in res.items():
            dec.append({"anio": a, "cuantil": q, **v, "n_muestral": n_ext})
        o = econ.oaxaca(x.lw.to_numpy(), X, x.extranjero.to_numpy(), x.factor.to_numpy())
        ox.append({"anio": a, "brecha": o["brecha"], "composicion": o["explicada"], "resto": o["no_explicada"], "n_muestral": n_ext})
    niv = pd.DataFrame(filas)
    niv.to_csv(O / "salarios_tres_niveles.csv", index=False)
    pd.DataFrame(dec).to_csv(O / "salarios_deciles_dfl.csv", index=False)
    pd.DataFrame(ox).to_csv(O / "salarios_oaxaca.csv", index=False)
    u = 2022
    for _, r in niv[niv.anio == u].iterrows():
        cap = "C1" if r.nivel_ajuste == "bruto" else "C4"
        cf.add(f"F3_SAL_BRECHA_{r.nivel_ajuste.split(' ')[0].replace(',', '')}_{'inf' if 'informativo' in r.nivel_ajuste else 'b'}_{u}"
               .replace("_b_", "_"), round(r.brecha_pct, 1), "% del salario por hora",
               f"Brecha de salario por hora de extranjeros frente a españoles ({r.nivel_ajuste})", cap, EES, "octubre 2022", "España",
               "nacionalidad extranjera", nivel_ajuste=r.nivel_ajuste,
               ic_inf=round(100 * (np.exp(r.brecha_log - 1.96 * r.ee) - 1), 1), ic_sup=round(100 * (np.exp(r.brecha_log + 1.96 * r.ee) - 1), 1))
    dd = pd.DataFrame(dec)
    for q in (0.1, 0.5, 0.9):
        v = dd[(dd.anio == u) & (dd.cuantil == q)].iloc[0]
        cf.add(f"F3_SAL_BRECHA_P{int(q * 100)}_{u}", round(100 * (np.exp(v.brecha) - 1), 1), "%",
               f"Brecha de salario por hora en el percentil {int(q * 100)} (extranjeros frente a españoles)", "C1", EES, "octubre 2022",
               "España", "nacionalidad extranjera")
        cf.add(f"F3_SAL_COMPOSICION_P{int(q * 100)}_{u}", round(100 * v.composicion / v.brecha, 0) if v.brecha != 0 else np.nan,
               "% de la brecha", f"Parte de la brecha en el percentil {int(q * 100)} explicada por composición (edad, sexo, estudios, región; DFL)",
               "C4", EES, "octubre 2022", "España", "nacionalidad extranjera")
    oo = pd.DataFrame(ox).set_index("anio").loc[u]
    cf.add(f"F3_SAL_OAXACA_COMPOSICION_{u}", round(100 * oo.composicion / oo.brecha, 0), "% de la brecha media del log",
           "Parte de la brecha media explicada por composición (Oaxaca-Blinder; edad, sexo, estudios, región)", "C4", EES, "octubre 2022",
           "España", "nacionalidad extranjera")
    # segunda fuente: ECV, asalariados a jornada completa todo el año (renta del trabajo del año anterior)
    e = ecv_salarios()
    e.to_csv(O / "salarios_ecv.csv", index=False)
    er = e[e.anio == e.anio.max()].set_index("nacimiento3")
    for g in ("Resto UE", "Resto del mundo"):
        cf.add(f"F3_SAL_ECV_BRECHA_{g.replace(' ', '_')}_{int(e.anio.max()) - 1}", round(100 * (er.loc[g, "mediana"] / er.loc["España", "mediana"] - 1), 1),
               "% de la mediana", f"Brecha de la mediana de rendimientos del trabajo anuales de asalariados a jornada completa todo el año ({g} frente a nacidos en España)",
               "C1", "ECV (INE)", str(int(e.anio.max()) - 1), "España", g)
    # tercera: tablas de la EPA por nacionalidad y decil
    t = epa_deciles()
    t.to_csv(O / "salarios_epa_deciles.csv", index=False)
    cf.escribir()
    print("f3_salarios: hecho;", len(cf.filas), "cifras")
    return 0


def ecv_salarios() -> pd.DataFrame:
    d = pd.read_csv(PROC / "ecv_personas.csv.gz", usecols=["anio", "nacimiento3", "PB040", "PY010G", "PL073", "PL074", "edad"])
    d = d[(d.PL073 >= 12) & (d.PY010G > 1000) & d.edad.between(16, 64) & d.nacimiento3.notna()]
    r = d.groupby(["anio", "nacimiento3"]).apply(lambda g: pd.Series({
        "media": np.average(g.PY010G, weights=g.PB040), "mediana": cuantil_pond(g.PY010G, g.PB040, 0.5),
        "p10": cuantil_pond(g.PY010G, g.PB040, 0.1), "p90": cuantil_pond(g.PY010G, g.PB040, 0.9), "n_muestral": len(g)}),
        include_groups=False).reset_index()
    r.loc[r.n_muestral < 50, ["media", "mediana", "p10", "p90"]] = np.nan
    return r


def epa_deciles() -> pd.DataFrame:
    d = pd.read_csv(RAW / "ine_tablas" / "t66240.csv", sep=";", dtype=str, encoding="utf-8-sig")
    d["valor"] = pd.to_numeric(d["Total"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")
    return d


if __name__ == "__main__":
    sys.exit(main())
