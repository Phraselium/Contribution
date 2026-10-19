"""M1 · Consolida output/cifras/*.csv en output/cifras_clave.csv, la única fuente de cifras difundibles.

Cada fila lleva id, valor (e intervalo si lo hay), unidad, descripción, capa, clasificación (solo efectos), fuente, periodo,
ámbito, grupo de origen, nivel de ajuste y script. Uso: python3 src/m1/cifras.py [--comprobar]
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import CAPAS, CIFRAS_COLS, CLASIFICACIONES, OUT  # noqa: E402

DESTINO = OUT / "cifras_clave.csv"


def consolidar() -> pd.DataFrame:
    partes = [pd.read_csv(p, dtype={"clasificacion": str}, keep_default_na=False, na_values=[""])
              for p in sorted((OUT / "cifras").glob("*.csv"))]
    if not partes:
        return pd.DataFrame(columns=CIFRAS_COLS)
    df = pd.concat(partes, ignore_index=True)[CIFRAS_COLS]
    df["clasificacion"] = df["clasificacion"].fillna("")
    return df.sort_values("id").reset_index(drop=True)


def errores(df: pd.DataFrame) -> list[str]:
    e = []
    if df["id"].duplicated().any():
        e.append(f"ids duplicados: {sorted(df.loc[df['id'].duplicated(), 'id'].unique())[:10]}")
    for _, r in df.iterrows():
        if r["capa"] not in CAPAS:
            e.append(f"{r['id']}: capa {r['capa']}")
        if r["clasificacion"] not in CLASIFICACIONES:
            e.append(f"{r['id']}: clasificación {r['clasificacion']}")
        if r["capa"] == "C3" and r["clasificacion"] != "IDENTIFICADO":
            e.append(f"{r['id']}: C3 sin IDENTIFICADO")
        if r["clasificacion"] == "IDENTIFICADO" and r["capa"] != "C3":
            e.append(f"{r['id']}: IDENTIFICADO fuera de C3")
        for c in ("fuente", "periodo", "ambito", "grupo_origen", "unidad"):
            if pd.isna(r[c]) or str(r[c]).strip() == "":
                e.append(f"{r['id']}: falta {c}")
    return e


def main() -> int:
    df = consolidar()
    err = errores(df)
    if "--comprobar" in sys.argv:
        actual = pd.read_csv(DESTINO, keep_default_na=False, na_values=[""]) if DESTINO.exists() else pd.DataFrame(columns=CIFRAS_COLS)
        if len(actual) != len(df) or set(actual["id"]) != set(df["id"]):
            err.append("output/cifras_clave.csv no coincide con output/cifras/*.csv: ejecute python3 src/m1/cifras.py")
    else:
        df.to_csv(DESTINO, index=False)
    print("\n".join(err) or f"cifras_clave: {len(df)} cifras válidas")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
