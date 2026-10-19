"""M1-F2 · Normaliza los microdatos transversales de la ECV (INE) 2009-2025 a un fichero de personas, sin red.

Lee data/raw/ecv/grandes/datos_<año>.zip (ficheros esudbAAd/h/p/r.csv, formato Eurostat UDB) y escribe
data/processed/ecv_personas.csv.gz con una fila por persona (todas las edades) y las variables de origen, renta, impuestos,
cotizaciones, prestaciones y vivienda que necesitan las fases 3 y 4.

Origen (lo que permite la fuente; docs/fuentes_publicas.md):
- 2021-2025: RB280 (país de nacimiento) y RB290 (nacionalidad) para todas las personas: 1 España, 2 resto de la UE, 3 resto del mundo.
- 2009-2020: PB210 y PB220A solo para mayores de 16 años (códigos «ES», «EU», «OTH»); los menores toman el origen de la
  madre, si no del padre, si conviven (marcado en origen_imputado). Para la contabilidad fiscal solo se usan 2021-2025.
Segunda generación: nacidos en España con al menos un progenitor conviviente nacido fuera (solo identificable si convive).
Diseño: pesos RB050 (personas), PB040 (adultos), DB090 (hogares). DB060 (UPM) solo en algunos años: se conserva si existe.
"""
from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import PROC, RAW  # noqa: E402

VR = ["RB010", "RB030", "RB050", "RB080", "RB081", "RB090", "RB200", "RB220", "RB230", "RB280", "RB290"]
VP = ["PB030", "PB040", "PB210", "PB220A", "PE040", "PE041", "PL031", "PL032", "PL060", "PL073", "PL074", "PL075", "PL076",
      "PY010G", "PY020G", "PY021G", "PY030G", "PY035G", "PY050G", "PY080G", "PY090G", "PY100G", "PY110G", "PY120G", "PY130G",
      "PY140G"]
VH = ["HB030", "HY010", "HY020", "HY022", "HY023", "HY040G", "HY050G", "HY060G", "HY070G", "HY080G", "HY090G", "HY100G", "HY110G",
      "HY120G", "HY130G", "HY140G", "HY145N", "HH010", "HH021", "HH030", "HH060", "HH070", "HS120"]
VD = ["DB030", "DB040", "DB060", "DB090", "DB100"]
COD3 = {"1": "España", "2": "Resto UE", "3": "Resto del mundo", "ES": "España", "EU": "Resto UE", "OTH": "Resto del mundo",
        "LOC": "España"}


def _csvs(zpath: Path, aa: str) -> dict[str, pd.DataFrame]:
    out = {}

    def leer(zf):
        for n in zf.namelist():
            base = n.rsplit("/", 1)[-1].lower()
            if base.endswith(".zip"):
                with zipfile.ZipFile(io.BytesIO(zf.read(n))) as z2:
                    leer(z2)
            for t in "dhpr":
                exacto = base == f"esudb{aa}{t}.csv"
                variante = base.startswith(f"esudb{aa}{t}_") and base.endswith(".csv") and "nuevoarope" not in base
                if exacto or (variante and t not in out):
                    out[t] = pd.read_csv(io.BytesIO(zf.read(n)), dtype=str, keep_default_na=False)
    with zipfile.ZipFile(zpath) as zf:
        leer(zf)
    return out


def _num(df, cols):
    for c in cols:
        if c in df:
            df[c] = pd.to_numeric(df[c].str.strip().replace("", np.nan), errors="coerce")
    return df


def anio(a: int) -> pd.DataFrame | None:
    z = RAW / "ecv" / "grandes" / f"datos_{a}.zip"
    if not z.exists():
        return None
    f = _csvs(z, f"{a % 100:02d}")
    if set(f) != set("dhpr"):
        print(f"ecv {a}: faltan ficheros {set('dhpr') - set(f)}")
        return None
    r = f["r"][[c for c in VR if c in f["r"]]].copy()
    p = f["p"][[c for c in VP if c in f["p"]]].copy()
    h = f["h"][[c for c in VH if c in f["h"]]].copy()
    d = f["d"][[c for c in VD if c in f["d"]]].copy()
    for df in (r, p, h, d):
        for c in df.columns:
            df[c] = df[c].str.strip()
    r = r.merge(p, left_on="RB030", right_on="PB030", how="left")
    r["hid"] = (pd.to_numeric(r["RB030"]) // 100).astype("int64").astype(str)
    h["hid"], d["hid"] = h["HB030"], d["DB030"]
    r = r.merge(h.drop(columns=["HB030"]), on="hid", how="left").merge(d.drop(columns=["DB030"]), on="hid", how="left")
    if "RB280" in r:
        r["nacimiento3"], r["nacionalidad3"] = r["RB280"].map(COD3), r["RB290"].map(COD3)
    else:
        r["nacimiento3"], r["nacionalidad3"] = r["PB210"].map(COD3), r["PB220A"].map(COD3)
    r["origen_imputado"] = r["nacimiento3"].isna()
    idx = r.set_index("RB030")
    for v in ("nacimiento3", "nacionalidad3"):
        madre = r["RB230"].map(idx[v]) if "RB230" in r else np.nan
        padre = r["RB220"].map(idx[v]) if "RB220" in r else np.nan
        r[v] = r[v].fillna(madre).fillna(padre)
    m = r["RB230"].map(idx["nacimiento3"]) if "RB230" in r else pd.Series(np.nan, index=r.index)
    pa = r["RB220"].map(idx["nacimiento3"]) if "RB220" in r else pd.Series(np.nan, index=r.index)
    r["segunda_gen"] = (r["nacimiento3"] == "España") & ((m.isin(["Resto UE", "Resto del mundo"])) |
                                                       (pa.isin(["Resto UE", "Resto del mundo"])))
    num = [c for c in r.columns if c[:2] in ("RB", "PB", "PY", "HY", "HH", "DB", "PL", "HS", "PE") and c not in
           ("RB280", "RB290", "PB210", "PB220A", "DB040")]
    r = _num(r, num)
    r["anio"] = a
    r["anio_renta"] = a - 1
    r["edad"] = r["RB081"] if "RB081" in r and r["RB081"].notna().any() else (a - 1 - r["RB080"])
    r["nacionalizado"] = (r["nacimiento3"] != "España") & (r["nacionalidad3"] == "España")
    return r.drop(columns=[c for c in ("PB030", "RB220", "RB230", "PB210", "PB220A", "RB280", "RB290") if c in r])


def main() -> int:
    partes = []
    for a in range(2009, 2026):
        d = anio(a)
        if d is not None:
            partes.append(d)
            print(f"ecv {a}: {len(d)} personas; origen sin dato {d['nacimiento3'].isna().mean():.3f}", flush=True)
    df = pd.concat(partes, ignore_index=True)
    df.to_csv(PROC / "ecv_personas.csv.gz", index=False)
    print("f2_ecv:", len(df), "personas-año")
    return 0


if __name__ == "__main__":
    sys.exit(main())
