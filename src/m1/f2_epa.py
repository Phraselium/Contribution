"""M1-F2 · Agrega los microdatos trimestrales públicos de la EPA (2005T1-último) a celdas anuales, sin red.

Cada celda (año, provincia, definición de origen, grupo, sexo, edad, educación, años de residencia, segunda generación) lleva
sumas ponderadas (FACTOREL / nº de trimestres del año: medias anuales) de población de 16 y más, activos, ocupados, parados,
asalariados, temporales, a tiempo parcial, horas efectivas, ocupados en ocupaciones de alta cualificación (CNO 1-3) y
elementales (CNO 9), titulados superiores en ocupaciones 4-9 (sobrecualificación) y el número de observaciones muestrales
(persona-trimestre). Salidas: data/processed/epa_celdas.csv.gz y data/processed/epa_sectores.csv.gz (ocupados por sector CNAE
a 1 dígito).

Grupos de origen (decisión D6, aproximación fijada antes de mirar datos; REGNA1 / EXREGNA1):
115 → UE-14 (UE-15) · 125, 127, 128, 100 → UE-13 y otros de Europa · 200 → África (Magreb y resto juntos) ·
310, 350 → América Latina · 400, 410, 420 → Asia · 300, 500, 999 → Resto. Nacionalidad: NAC1 1 o 2 (doble) → España.
Segunda generación: nacido en España con padre o madre conviviente (NPADRE, NMADRE) nacido fuera; con_padres marca a quien
convive con alguno de sus padres (la comparación válida es entre quienes conviven). Diseño: solo FACTOREL.
"""
from __future__ import annotations

import io
import re
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import PROC, RAW  # noqa: E402

REG = {"115": "UE-14", "125": "UE-13 y otros de Europa", "127": "UE-13 y otros de Europa", "128": "UE-13 y otros de Europa",
       "100": "UE-13 y otros de Europa", "200": "África", "310": "América Latina", "350": "América Latina", "400": "Asia",
       "410": "Asia", "420": "Asia", "300": "Resto", "500": "Resto", "999": "Resto"}
COLS = ["CICLO", "PROV", "NVIVI", "NPERS", "EDAD5", "EDAD1", "SEXO1", "NPADRE", "NMADRE", "PRONA1", "REGNA1", "NAC1",
        "EXREGNA1", "ANORE1", "NFORMA", "OCUP1", "ACT1", "SITU", "DUCON1", "PARCO1", "HORASE", "AOI", "FACTOREL"]
# Nivel de formación: códigos de 2005-2020 (AN…SU) y CNED-2014 a 2 dígitos (2021-)
EDUC_ANT = {"AN": "baja", "P1": "baja", "P2": "baja", "S1": "baja", "SG": "media", "SP": "media", "SU": "alta"}


def educ(v: pd.Series) -> pd.Series:
    out = v.map(EDUC_ANT)
    num = pd.to_numeric(v.where(out.isna()), errors="coerce")
    # CNED-2014 (dos dígitos): 01-24 hasta primera etapa de secundaria; 31-41 segunda etapa y postsecundaria; 51-81 superior
    out = out.fillna(pd.Series(np.select([num < 30, num < 50, num >= 50], ["baja", "media", "alta"], None), index=v.index)
                     .where(num.notna()))
    return out


def edad6(e: pd.Series) -> pd.Series:
    return pd.cut(e, [15, 24, 34, 44, 54, 64, 200], labels=["16-24", "25-34", "35-44", "45-54", "55-64", "65+"]).astype(str)


def resid(a: pd.Series, nativo: pd.Series) -> pd.Series:
    r = pd.cut(a, [-1, 4, 9, 19, 200], labels=["0-4", "5-9", "10-19", "20+"]).astype(str)
    return r.where(~nativo, "nativo").where(~(~nativo & a.isna()), "no consta")


def trimestre(ruta: Path) -> pd.DataFrame:
    with zipfile.ZipFile(ruta) as z:
        n = [x for x in z.namelist() if re.match(r"(?i)^csv/.*\.(csv|txt|tab)$", x)][0]
        d = pd.read_csv(io.BytesIO(z.read(n)), sep="\t", dtype=str, usecols=lambda c: c in COLS, keep_default_na=False)
    d = d.apply(lambda s: s.str.strip())
    m = re.search(r"datos_(\d)t(\d\d)", ruta.name)
    d["anio"], d["trim"] = 2000 + int(m.group(2)), int(m.group(1))
    d["edad"] = pd.to_numeric(d["EDAD1"] if "EDAD1" in d else d["EDAD5"], errors="coerce")
    d = d[d["edad"] >= 16].copy()
    d["w"] = pd.to_numeric(d["FACTOREL"], errors="coerce")
    nativo = d["REGNA1"].eq("")
    d["g_nac"] = np.where(nativo, "España", d["REGNA1"].map(REG).fillna("Resto"))
    d["g_ncl"] = np.where(d["NAC1"].isin(["1", "2"]), "España", d["EXREGNA1"].map(REG).fillna("Resto"))
    # segunda generación: padre o madre conviviente nacido fuera
    clave = d["NVIVI"] + "_" + d["NPERS"]
    nac_fuera = pd.Series(~nativo.values, index=clave.values)
    nac_fuera = nac_fuera[~nac_fuera.index.duplicated()]

    def fuera(col):
        k = d["NVIVI"] + "_" + d[col]
        return k.map(nac_fuera).fillna(False).astype(bool) & ~d[col].isin(["", "00"])
    d["sg"] = nativo & (fuera("NPADRE") | fuera("NMADRE"))
    d["con_padres"] = ~d["NPADRE"].isin(["", "00"]) | ~d["NMADRE"].isin(["", "00"])
    d["nacionalizado"] = ~nativo & d["NAC1"].isin(["1", "2"])
    d["sexo"] = d["SEXO1"].map({"1": "hombre", "6": "mujer"})
    d["edad6"] = edad6(d["edad"])
    d["educ"] = educ(d["NFORMA"]).fillna("no consta")
    d["resid"] = resid(pd.to_numeric(d["ANORE1"], errors="coerce"), nativo)
    aoi = d["AOI"]
    d["act"] = aoi.isin(["03", "04", "05", "06"]).astype(float)
    d["ocu"] = aoi.isin(["03", "04"]).astype(float)
    d["par"] = aoi.isin(["05", "06"]).astype(float)
    d["asal"] = (d["ocu"] == 1) & d["SITU"].isin(["07", "08"])
    d["temp"] = d["asal"] & d["DUCON1"].eq("6")
    d["parc"] = (d["ocu"] == 1) & d["PARCO1"].eq("6")
    h = pd.to_numeric(d["HORASE"], errors="coerce")
    h = (h // 100 + (h % 100) / 60).where(h < 9999)
    d["horas"] = h.where(d["ocu"] == 1).fillna(0.0)
    oc = d["OCUP1"]
    d["ocu_alta"] = (d["ocu"] == 1) & oc.isin(["1", "2", "3"])
    d["ocu_elem"] = (d["ocu"] == 1) & oc.eq("9")
    d["sobrecual"] = (d["ocu"] == 1) & d["educ"].eq("alta") & oc.isin(["4", "5", "6", "7", "8", "9"])
    d["sector"] = d["ACT1"].where(d["ocu"] == 1)
    return d


VARS = ["act", "ocu", "par", "asal", "temp", "parc", "horas", "ocu_alta", "ocu_elem", "sobrecual"]


def agregar_trimestre(ruta: str):
    d = trimestre(Path(ruta))
    for v in VARS:
        d[v] = d[v].astype(float) * d["w"]
    d["pob"] = d["w"]
    d["n"] = 1
    filas = []
    for od, g in (("nacimiento", "g_nac"), ("nacionalidad", "g_ncl")):
        dims = ["anio", "trim", "PROV", g, "sexo", "edad6", "educ", "resid", "sg", "con_padres", "nacionalizado"]
        a = d.groupby(dims, dropna=False)[["pob"] + VARS + ["n"]].sum().reset_index().rename(columns={g: "grupo"})
        a["origen_def"] = od
        filas.append(a)
    sec = d[d["sector"].notna()].groupby(["anio", "trim", "PROV", "g_nac", "sector"])[["ocu", "n"]].sum().reset_index()
    return pd.concat(filas), sec


def main() -> int:
    zips = sorted(str(p) for p in (RAW / "epa" / "grandes").glob("datos_?t??.zip"))
    with ProcessPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(agregar_trimestre, zips))
    c = pd.concat([r[0] for r in res], ignore_index=True)
    s = pd.concat([r[1] for r in res], ignore_index=True)
    ntrim = c.groupby("anio")["trim"].nunique()
    dims = ["anio", "PROV", "origen_def", "grupo", "sexo", "edad6", "educ", "resid", "sg", "con_padres", "nacionalizado"]
    c = c.groupby(dims, dropna=False)[["pob"] + VARS + ["n"]].sum().reset_index()
    for v in ["pob"] + VARS:
        c[v] = c[v] / c["anio"].map(ntrim)
    c = c.rename(columns={"PROV": "prov", "n": "n_obs"})
    c["n_trimestres"] = c["anio"].map(ntrim)
    s = s.groupby(["anio", "PROV", "g_nac", "sector"])[["ocu", "n"]].sum().reset_index()
    s["ocu"] = s["ocu"] / s["anio"].map(ntrim)
    s = s.rename(columns={"PROV": "prov", "g_nac": "grupo", "n": "n_obs"})
    c.to_csv(PROC / "epa_celdas.csv.gz", index=False)
    s.to_csv(PROC / "epa_sectores.csv.gz", index=False)
    print(f"f2_epa: {len(zips)} trimestres, {len(c)} celdas, años {c.anio.min()}-{c.anio.max()} "
          f"(trimestres por año: {ntrim.to_dict()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
