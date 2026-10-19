"""M1-F2 · Normaliza la Encuesta de Presupuestos Familiares (INE, microdatos públicos) 2022-2024 para imputar impuestos indirectos
por hogar, sin red.

Para cada hogar: gasto monetario anual (GASTOMON / FACTOR, porque el INE publica los importes elevados), IVA soportado estimado
con los tipos efectivos por grupo ECOICOP de docs/supuestos/impuestos_indirectos_coicop.csv (prefijo más largo) y una base de
impuestos especiales (gasto × peso_especial). El nivel se calibra después con la recaudación (fase 4); aquí solo se construye la
distribución. Origen del sustentador principal: PAISNACSP (1 España, 2 resto UE-27, 3 resto de Europa, 4 resto del mundo) y
NACIONASP (1 española, 2 extranjera, 3 ambas). Salida: data/processed/epf_hogares.csv.gz.
"""
from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import DOCS, PROC, RAW  # noqa: E402

HOGAR = ["ANOENC", "NUMERO", "CCAA", "FACTOR", "NMIEMB", "UC2", "PAISNACSP", "NACIONASP", "EDADSP", "SEXOSP", "IMPEXAC", "GASTOT",
         "GASTMON", "REGTEN"]


def _tab(z: zipfile.ZipFile, interior: str, usecols=None) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(z.read(interior))) as z2:
        n = [x for x in z2.namelist() if x.lower().endswith((".tab", ".csv")) and x.upper().startswith("CSV/")][0]
        return pd.read_csv(io.BytesIO(z2.read(n)), sep="\t", dtype=str, keep_default_na=False,
                           usecols=lambda c: usecols is None or c in usecols)


def tipos() -> pd.DataFrame:
    t = pd.read_csv(DOCS / "supuestos" / "impuestos_indirectos_coicop.csv", dtype={"prefijo_coicop": str})
    return t.sort_values("prefijo_coicop", key=lambda s: -s.str.len())


def asignar(codigos: pd.Series, t: pd.DataFrame) -> pd.DataFrame:
    iva = pd.Series(np.nan, index=codigos.index)
    esp = pd.Series(np.nan, index=codigos.index)
    for _, r in t.iterrows():
        m = iva.isna() & codigos.str.startswith(r["prefijo_coicop"])
        iva[m], esp[m] = r["tipo_iva_efectivo"], r["peso_especial"]
    return pd.DataFrame({"iva": iva.fillna(0.21), "esp": esp.fillna(0.0)})


def anio(a: int, t: pd.DataFrame) -> pd.DataFrame:
    with zipfile.ZipFile(RAW / "epf" / "grandes" / f"datos_{a}.zip") as z:
        h = _tab(z, "EPFhogar.zip", HOGAR)
        g = _tab(z, "EPFgastos.zip", ["NUMERO", "CODIGO", "GASTOMON", "GASTMON", "FACTOR"])
    g = g.rename(columns={"GASTMON": "GASTOMON"})   # 2024 cambia el nombre de la columna
    for c in ("FACTOR", "NMIEMB", "UC2", "IMPEXAC", "GASTOT", "GASTMON", "EDADSP"):
        if c in h:
            h[c] = pd.to_numeric(h[c].str.replace(",", "."), errors="coerce")
    g["gm"] = pd.to_numeric(g["GASTOMON"].str.replace(",", "."), errors="coerce").fillna(0) / pd.to_numeric(g["FACTOR"])
    s = asignar(g["CODIGO"].str.strip(), t)
    # el gasto incluye el IVA: IVA = gasto × t / (1 + t)
    g["iva"] = g["gm"] * s["iva"] / (1 + s["iva"])
    g["base_especiales"] = g["gm"] * s["esp"]
    agg = g.groupby("NUMERO")[["gm", "iva", "base_especiales"]].sum().rename(columns={"gm": "gasto_monetario"})
    h = h.merge(agg, left_on="NUMERO", right_index=True, how="left")
    h["gasto_total_hogar"] = h["GASTOT"] / h["FACTOR"]
    h["ingreso_anual_neto"] = h["IMPEXAC"] * 12
    h["origen_sp"] = h["PAISNACSP"].map({"1": "España", "2": "Resto UE", "3": "Resto del mundo", "4": "Resto del mundo"})
    h["origen_sp4"] = h["PAISNACSP"].map({"1": "España", "2": "Resto UE-27", "3": "Resto de Europa", "4": "Resto del mundo"})
    h["anio"] = a
    return h


def main() -> int:
    t = tipos()
    df = pd.concat([anio(a, t) for a in (2022, 2023, 2024) if (RAW / "epf" / "grandes" / f"datos_{a}.zip").exists()])
    df.to_csv(PROC / "epf_hogares.csv.gz", index=False)
    r = df.groupby(["anio", "origen_sp"]).apply(lambda x: pd.Series({
        "iva_sobre_ingreso": np.average(x.iva, weights=x.FACTOR) / np.average(x.ingreso_anual_neto, weights=x.FACTOR),
        "n": len(x)}), include_groups=False)
    print("f2_epf:", len(df), "hogares;\n", r.round(4))
    return 0


if __name__ == "__main__":
    sys.exit(main())
