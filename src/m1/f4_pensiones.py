"""M1-F4 · Pensiones y demografía: proyección con y sin flujos migratorios (C2, contabilidad demográfica con supuestos). Sin red.

EUROPOP2023 (Eurostat) para España y la UE-27, variantes BSL (base), LMIGR / HMIGR (−33 % / +33 % de migración neta) y NMIGR
(sin migración). Tasa de dependencia de mayores (65+ / 20-64) y gasto en pensiones / PIB con una regla mecánica: el gasto en
pensiones de 2024 (COFOG GF1002 + GF1003, prestaciones monetarias) / PIB se multiplica por la tasa de dependencia relativa,
manteniendo constantes la tasa de empleo, la tasa de cobertura y la pensión media relativa a la productividad. Lo que hace el
código (aclaración a posteriori): gasto/PIB(t) = gasto/PIB(2024) × [65+/20-64](t) / [65+/20-64](base, 2025). Equivale a un PIB
proporcional a la población de 20-64 años (PIB endógeno: cada residente adicional en edad de trabajar aporta el empleo y la
productividad medios) y a un gasto proporcional a la población de 65 y más con la pensión media ligada al PIB por persona en edad de
trabajar. No es un PIB fijo: con PIB fijo la migración solo añadiría pensionistas y no reduciría el cociente. Es una cota
demográfica, no una proyección del sistema: el Ageing Report 2024 y la AIReF modelizan además empleo, reformas y revalorización.
Se compara con las cifras del Ageing Report 2024 recogidas en docs/literatura/fiscal.md (España: 17,3 % del PIB en 2050 en la
base; 16,1 % con +33 % de migración y 18,7 % con −33 %).
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, RAW, Cifras  # noqa: E402
from f4_fiscal import cuentas  # noqa: E402

O = OUT / "f4"


def dependencia(geo: str) -> pd.DataFrame:
    p = pd.read_csv(RAW / "eurostat" / f"proj_23np_{'ES' if geo == 'ES' else 'UE27'}.csv.gz")
    p = p[(p.sex == "T") & (p.unit == "PER")]
    p = p[p.age.str.match(r"^Y\d+$") | p.age.isin(["Y_LT1", "Y_GE100", "Y_OPEN"])].copy()
    p["e"] = pd.to_numeric(p.age.str.replace("Y_LT1", "Y0").str.extract(r"(\d+)")[0], errors="coerce")
    g = p.groupby(["projection", "TIME_PERIOD"]).apply(lambda x: pd.Series({
        "pob_20_64": x.loc[x.e.between(20, 64), "OBS_VALUE"].sum(), "pob_65_mas": x.loc[x.e >= 65, "OBS_VALUE"].sum(),
        "pob_total": x.OBS_VALUE.sum()}), include_groups=False).reset_index()
    g["tasa_dependencia"] = g.pob_65_mas / g.pob_20_64
    g["geo"] = geo
    return g


def main() -> int:
    cf = Cifras("f4_pensiones", "src/m1/f4_pensiones.py")
    c = cuentas(2024)
    gasto = (c["d62"]["GF1002"] + c["d62"]["GF1003"]) / c["pib"]
    out = []
    for geo in ("ES", "EU27"):
        d = dependencia(geo)
        base = d[(d.projection == "BSL") & (d.TIME_PERIOD == 2025)].tasa_dependencia.iloc[0]
        d["gasto_pensiones_pib_mecanico"] = 100 * gasto * d.tasa_dependencia / base if geo == "ES" else np.nan
        out.append(d)
    d = pd.concat(out)
    d.to_csv(O / "pensiones_demografia.csv", index=False)
    es = d[d.geo == "ES"].set_index(["projection", "TIME_PERIOD"])
    cf.add("F4_PEN_GASTO_PIB_2024", round(100 * gasto, 1), "% del PIB",
           "Gasto en pensiones de vejez y supervivencia (prestaciones monetarias COFOG) en 2024", "C1", "Eurostat gov_10a_exp", "2024",
           "España", "todos")
    for a in (2050, 2070):
        for v in ("BSL", "NMIGR", "LMIGR", "HMIGR"):
            cf.add(f"F4_PEN_DEPENDENCIA_{v}_{a}", round(100 * es.loc[(v, a), "tasa_dependencia"], 1), "65+ por cada 100 de 20-64",
                   f"Tasa de dependencia de mayores en EUROPOP2023, variante {v}", "C2", "Eurostat proj_23np", str(a), "España", "todos")
            cf.add(f"F4_PEN_GASTO_MECANICO_{v}_{a}", round(es.loc[(v, a), "gasto_pensiones_pib_mecanico"], 1), "% del PIB",
                   f"Gasto en pensiones / PIB con la regla mecánica demográfica (variante {v}; empleo, cobertura y pensión relativa "
                   "constantes)", "C2", "Eurostat proj_23np y gov_10a_exp", str(a), "España", "todos")
    cf.add("F4_PEN_DIF_SIN_MIGRACION_2050", round(es.loc[("NMIGR", 2050), "gasto_pensiones_pib_mecanico"] -
                                                     es.loc[("BSL", 2050), "gasto_pensiones_pib_mecanico"], 1), "pp del PIB",
           "Diferencia de gasto en pensiones / PIB entre la variante sin migración y la base en 2050 (regla mecánica)", "C2",
           "Eurostat proj_23np", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_BASE_2050", 17.3, "% del PIB", "Ageing Report 2024: gasto en pensiones de España en 2050, escenario base "
           "(cifra publicada, ficha de docs/literatura/fiscal.md)", "C2", "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_MAS_MIGRACION_2050", 16.1, "% del PIB", "Ageing Report 2024: escenario con 33 % más de migración (publicado)",
           "C2", "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_MENOS_MIGRACION_2050", 18.7, "% del PIB", "Ageing Report 2024: escenario con 33 % menos de migración (publicado)",
           "C2", "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    cf.add("F4_PEN_MEC_DIF_LMIGR_HMIGR_2050", round(es.loc[("LMIGR", 2050), "gasto_pensiones_pib_mecanico"] -
                                                       es.loc[("HMIGR", 2050), "gasto_pensiones_pib_mecanico"], 1), "pp del PIB",
           "Diferencia de gasto en pensiones / PIB en 2050 entre las variantes con menos y con más migración (regla mecánica; comparable "
           "con la del Ageing Report)", "C2", "Eurostat proj_23np", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_DIF_MIGRACION_2050", round(18.7 - 16.1, 1), "pp del PIB", "Ageing Report 2024: diferencia de gasto en "
           "pensiones en 2050 entre el escenario con un tercio menos y con un tercio más de migración (publicado)", "C2",
           "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    # escenarios equivalentes (congelación, a posteriori): misma variación de la migración que el Ageing Report 2024 (±33 % frente a la
    # base); la variante sin migración no tiene equivalente publicado en el Ageing Report ni en la AIReF
    for v, nom in (("LMIGR", "un tercio menos"), ("HMIGR", "un tercio más")):
        cf.add(f"F4_PEN_MEC_DIF_{v}_BSL_2050", round(es.loc[(v, 2050), "gasto_pensiones_pib_mecanico"] - es.loc[("BSL", 2050), "gasto_pensiones_pib_mecanico"], 1),
               "pp del PIB", f"Regla mecánica: gasto en pensiones / PIB en 2050 con {nom} de migración menos el de la variante base (escenario "
               "equivalente al del Ageing Report 2024; a posteriori)", "C2", "Eurostat proj_23np", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_DIF_MENOS_BASE_2050", round(18.7 - 17.3, 1), "pp del PIB", "Ageing Report 2024: escenario con un tercio menos de "
           "migración menos la base en 2050 (tablas publicadas; a posteriori)", "C2", "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    cf.add("F4_PEN_AR2024_DIF_MAS_BASE_2050", round(16.1 - 17.3, 1), "pp del PIB", "Ageing Report 2024: escenario con un tercio más de "
           "migración menos la base en 2050 (tablas publicadas; a posteriori)", "C2", "Comisión Europea, Ageing Report 2024", "2050", "España", "todos")
    cf.escribir()
    print(d[(d.geo == "ES") & d.TIME_PERIOD.isin([2025, 2050, 2070])][["projection", "TIME_PERIOD", "tasa_dependencia",
                                                                          "gasto_pensiones_pib_mecanico"]].round(3).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
