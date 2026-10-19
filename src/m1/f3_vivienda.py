"""M1-F3 · Vivienda por origen (descriptivo; C1 con Eurostat como segunda fuente, C2 para la demanda de vivienda). Sin red.

ECV 2021-2025 (personas; origen = país de nacimiento propio, tres grupos): tenencia (HH021), densidad (personas por
habitación, HH030), sobrecarga del gasto en vivienda (gasto anual en vivienda neto de ayudas > 40 % de la renta disponible neta
de ayudas, definición de Eurostat), en los tres niveles (bruto; edad y sexo; además educación y región NUTS2). Eurostat
(ilc_lvho16, ilc_lvho26, ilc_lvps16) como segunda fuente para España y comparación europea.
Peso en la demanda de vivienda nueva por provincia (C2): aumento de población de cada grupo en el padrón 2015-2022 × tasa de
jefatura de hogar del grupo (hogares por persona, ECV de su región NUTS2) → aumento de hogares implicado por grupo.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import territorio  # noqa: E402
from comun import OUT, PROC, RAW, Cifras  # noqa: E402
from niveles import _dummies  # noqa: E402

O = OUT / "f3"
ECV = "ECV (INE, microdatos)"
GR = ["España", "Resto UE", "Resto del mundo"]


def cargar_ecv(anios=(2021, 2022, 2023, 2024, 2025)) -> pd.DataFrame:
    cols = ["anio", "RB030", "hid", "RB050", "RB090", "edad", "nacimiento3", "nacionalidad3", "PE041", "DB040", "HH021", "HH030",
            "HH070", "HY020", "HY070G", "HY060G", "HY050G", "HY140G", "HY010", "PY010G", "PY050G", "PY030G", "PY090G", "PY100G",
            "PY110G", "PY120G", "PY130G", "PY140G", "PB040", "segunda_gen", "nacionalizado", "HY040G", "HY090G", "HY080G",
            "HY110G", "HY120G", "HY130G", "PY080G", "PL032", "DB090"]
    d = pd.read_csv(PROC / "ecv_personas.csv.gz", usecols=lambda c: c in cols, low_memory=False)
    d = d[d.anio.isin(anios) & d.nacimiento3.notna()].copy()
    d["sexo"] = d.RB090.map({1: "hombre", 2: "mujer"})
    d["edad6"] = pd.cut(d.edad, [-1, 15, 24, 34, 44, 54, 64, 200],
                        labels=["0-15", "16-24", "25-34", "35-44", "45-54", "55-64", "65+"]).astype(str)
    d["educ"] = np.select([d.PE041 <= 200, d.PE041 < 500, d.PE041 >= 500], ["baja", "media", "alta"], "no consta")
    d.loc[d.edad < 16, "educ"] = "menor"
    d["n_hogar"] = d.groupby(["anio", "hid"]).RB030.transform("size")
    d["hid_anio"] = d.anio.astype(str) + "_" + d.hid.astype(str)
    return d


def niveles_ecv(d: pd.DataFrame, y: str, grupo="nacimiento3", w="RB050") -> pd.DataFrame:
    x = d.dropna(subset=[y])
    out = []
    G = np.column_stack([(x[grupo] == g).astype(float) for g in GR[1:]])
    c = np.ones((len(x), 1))
    x = x.assign(es=x.edad6 + "|" + x.sexo.astype(str), aa=x.anio.astype(str))
    for nivel, X in (("bruto", np.column_stack([c, G, _dummies(x, ["aa"])])),
                     ("edad y sexo", np.column_stack([c, G, _dummies(x, ["es", "aa"])])),
                     ("completo", np.column_stack([c, G, _dummies(x, ["es", "aa", "educ", "DB040"])]))):
        r = econ.ols(x[y].to_numpy(float), X, x.hid_anio.to_numpy(), x[w].to_numpy(float))
        for i, g in enumerate(GR[1:]):
            out.append({"variable": y, "grupo": g, "nivel_ajuste": nivel, "brecha": r["b"][1 + i], "ee": r["se"][1 + i],
                        "n_muestral": int((x[grupo] == g).sum())})
    o = pd.DataFrame(out)
    m = x.groupby(grupo).apply(lambda g: np.average(g[y], weights=g[w]), include_groups=False)
    o["media_grupo"], o["media_espana"] = o.grupo.map(m), m["España"]
    return o


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f3_vivienda", "src/m1/f3_vivienda.py")
    d = cargar_ecv()
    d["propietario"] = d.HH021.isin([1, 2]).astype(float)
    d["alquiler_mercado"] = (d.HH021 == 3).astype(float)
    d["personas_por_habitacion"] = d.n_hogar / d.HH030.where(d.HH030 > 0)
    d["densidad_alta"] = (d.personas_por_habitacion > 1).astype(float).where(d.personas_por_habitacion.notna())
    coste = (d.HH070 * 12 - d.HY070G.fillna(0)).clip(lower=0)
    renta = d.HY020 - d.HY070G.fillna(0)
    d["sobrecarga"] = (coste > 0.4 * renta).astype(float).where(renta > 0)
    tabs = pd.concat([niveles_ecv(d, v) for v in ("propietario", "alquiler_mercado", "densidad_alta", "sobrecarga")])
    tabs.to_csv(O / "vivienda_tres_niveles.csv", index=False)
    for _, r in tabs[tabs.nivel_ajuste == "bruto"].iterrows():
        cf.add(f"F3_VIV_{r.variable}_{r.grupo.replace(' ', '_')}_2021_2025", round(100 * r.media_grupo, 1), "% de personas",
               f"{r.variable.replace('_', ' ')}: personas nacidas en {r.grupo} (media 2021-2025)", "C1", ECV, "2021-2025", "España", r.grupo)
    for v in ("propietario", "sobrecarga"):
        cf.add(f"F3_VIV_{v}_España_2021_2025", round(100 * tabs[tabs.variable == v].media_espana.iloc[0], 1), "% de personas",
               f"{v}: personas nacidas en España (media 2021-2025)", "C1", ECV, "2021-2025", "España", "España")
        for _, r in tabs[(tabs.variable == v) & (tabs.nivel_ajuste == "completo")].iterrows():
            cf.add(f"F3_VIV_{v}_BRECHA_COMPLETO_{r.grupo.replace(' ', '_')}", round(100 * r.brecha, 1), "pp",
                   f"Brecha en {v} frente a nacidos en España, ajustada por edad, sexo, educación y región", "C4", ECV, "2021-2025",
                   "España", r.grupo, nivel_ajuste="completo", ic_inf=round(100 * (r.brecha - 1.96 * r.ee), 1),
                   ic_sup=round(100 * (r.brecha + 1.96 * r.ee), 1))
    # NUTS2
    reg = d.groupby(["DB040", "nacimiento3"]).apply(lambda g: pd.Series({
        "propietario": np.average(g.propietario, weights=g.RB050), "sobrecarga": np.average(g.sobrecarga.fillna(0), weights=g.RB050),
        "n_muestral": len(g)}), include_groups=False).reset_index()
    reg.loc[reg.n_muestral < 50, ["propietario", "sobrecarga"]] = np.nan
    reg.to_csv(O / "vivienda_nuts2.csv", index=False)
    # Eurostat (segunda fuente y Europa)
    eu = europa()
    eu.to_csv(O / "vivienda_europa.csv", index=False)
    es = eu[(eu.geo == "ES") & (eu.anio == eu[eu.geo == "ES"].anio.max())]
    for _, r in es.iterrows():
        cf.add(f"F3_VIV_EU_{r.tabla}_{r.c_birth}_ES_{int(r.anio)}", round(r.valor, 1), "%", f"{r.descripcion}, España, {r.c_birth}",
               "C1", f"Eurostat {r.tabla}", str(int(r.anio)), "España", r.c_birth)
    # demanda de vivienda (C2)
    dem = demanda(d)
    dem.to_csv(O / "vivienda_demanda_provincias.csv", index=False)
    tot = dem.groupby("grupo").hogares_implicados.sum()
    for etiqueta, val in (("FUERA", tot.drop("España").sum()), ("ESPANA", tot["España"])):
        cf.add(f"F3_VIV_DEMANDA_{etiqueta}_2015_2022", round(val / 1e3, 0), "miles de hogares",
               f"Hogares implicados por la variación de población 2015-2022 de los nacidos {'fuera' if etiqueta == 'FUERA' else 'en España'} "
               "a tasa de jefatura constante (ECV 2021-2025 por grupo y región); no incluye la formación de hogares por envejecimiento "
               "ni por cambios de la tasa de jefatura", "C2", "Padrón (INE) y ECV (INE)", "2015-2022", "España",
               "nacidos fuera" if etiqueta == "FUERA" else "España")
    cf.escribir()
    print("f3_vivienda: hecho;", len(cf.filas), "cifras")
    return 0


def europa() -> pd.DataFrame:
    out = []
    for tabla, desc, filtro in (("ilc_lvho16", "Tasa de hacinamiento (18+)", {"age": "Y_GE18", "sex": "T"}),
                                ("ilc_lvho26", "Tasa de sobrecarga del coste de la vivienda (18+)", {"age": "Y_GE18", "sex": "T"}),
                                ("ilc_lvps16", "Personas en vivienda en propiedad (18+)", {"tenure": "OWN", "age": "Y_GE18", "sex": "T"})):
        p = RAW / "eurostat" / f"{tabla}.csv.gz"
        x = pd.read_csv(p, low_memory=False)
        for k, v in filtro.items():
            if k in x:
                x = x[x[k] == v]
        if "unit" in x:
            x = x[x.unit.isin(["PC"])]
        x = x[x.c_birth.isin(["NAT", "FOR", "EU27_2020_FOR", "NEU27_2020_FOR"])]
        out.append(x.assign(tabla=tabla, descripcion=desc)[["tabla", "descripcion", "geo", "TIME_PERIOD", "c_birth", "OBS_VALUE"]])
    return pd.concat(out).rename(columns={"TIME_PERIOD": "anio", "OBS_VALUE": "valor"})


def demanda(d: pd.DataFrame) -> pd.DataFrame:
    """Hogares implicados por el aumento de población 2015-2022 de cada grupo (C2). Grupos de 3 en la ECV: los ocho del padrón se
    agregan a España / resto UE (UE-14 + UE-13) / resto del mundo para tomar su tasa de jefatura."""
    jef = d.assign(ref=1 / d.n_hogar).groupby(["DB040", "nacimiento3"]).apply(
        lambda g: np.average(g.ref, weights=g.RB050), include_groups=False).rename("tasa_jefatura").reset_index()
    p = pd.read_csv(PROC / "padron_grupos.csv.gz", dtype={"prov": str})
    p = p[(p.origen_def == "nacimiento") & p.anio.isin([2015, 2022])]
    tres = {"España": "España", "UE-14": "Resto UE", "UE-13 y otros de Europa": "Resto UE"}
    p["nacimiento3"] = p.grupo.map(tres).fillna("Resto del mundo")
    w = p.pivot_table(index=["prov", "grupo", "nacimiento3"], columns="anio", values="valor", aggfunc="sum").reset_index()
    w["variacion_poblacion"] = w[2022] - w[2015]
    w["DB040"] = w.prov.map(lambda x: territorio.PROV[x][2])
    w = w.merge(jef, on=["DB040", "nacimiento3"], how="left")
    w["hogares_implicados"] = w.variacion_poblacion * w.tasa_jefatura
    w["cuota_prov"] = w.hogares_implicados / w.groupby("prov").hogares_implicados.transform("sum")
    return w[["prov", "grupo", "variacion_poblacion", "tasa_jefatura", "hogares_implicados", "cuota_prov"]]


if __name__ == "__main__":
    sys.exit(main())
