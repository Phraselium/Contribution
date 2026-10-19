"""M1-F2 · Normaliza dos fuentes para la fase 5, sin red (no estima nada):
1. ECP (t56948): población a 1 de enero por provincia y lugar de nacimiento (Total, España, Extranjero) en 15-64 años (los tramos
   quinquenales no permiten 16-64 exactos: 15-64 es la aproximación declarada) → data/processed/ecp_15_64.csv.gz.
2. Afiliados a la Seguridad Social en alta el último día de diciembre por provincia, 1999-2011 (Excel históricos de la TGSS,
   «Total sistema») → data/processed/afiliacion_hist.csv.gz. Los nombres de provincia del Excel se cruzan con los códigos INE con
   una tabla de alias versionada (solo coincidencias únicas).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import territorio  # noqa: E402
from comun import PROC, RAW  # noqa: E402
from f3_poblacion import ecp_enero  # noqa: E402

ALIAS = {"alava": "01", "araba": "01", "guipuzcoa": "20", "gipuzkoa": "20", "vizcaya": "48", "bizkaia": "48", "la coruna": "15",
         "a coruna": "15", "coruna": "15", "orense": "32", "ourense": "32", "gerona": "17", "girona": "17", "lerida": "25",
         "lleida": "25", "baleares": "07", "illes balears": "07", "islas baleares": "07", "castellon": "12", "alicante": "03",
         "valencia": "46", "las palmas": "35", "palmas las": "35", "s c tenerife": "38", "santa cruz de tenerife": "38",
         "sta cruz tenerife": "38", "tenerife": "38", "la rioja": "26", "rioja": "26", "navarra": "31", "asturias": "33",
         "cantabria": "39", "madrid": "28", "murcia": "30", "com de madrid": "28", "reg de murcia": "30", "ceuta": "51", "melilla": "52"}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]+", " ", s).strip()


def codigo(nombre: str) -> str | None:
    n = _norm(nombre)
    if n in ALIAS:
        return ALIAS[n]
    cand = [k for k, v in territorio.PROV.items() if _norm(v[0].split("/")[0]) == n]
    return cand[0] if len(cand) == 1 else None


def afiliacion() -> pd.DataFrame:
    filas = []
    for a in range(1999, 2012):
        f = RAW / "admin" / f"ss_hist_{a}_tot_prov_ud_AfiliadosUltimoDia12{a}.XLS"
        if not f.exists():
            cand = sorted((RAW / "admin").glob(f"ss_hist_{a}_tot_prov_ud_*12{a}.*"))
            if not cand:
                continue
            f = cand[0]
        x = pd.read_excel(f, header=None)
        for _, r in x.iterrows():
            c = codigo(r.iloc[0])
            tot = pd.to_numeric(r.iloc[-1], errors="coerce")
            if c and pd.notna(tot) and tot > 0:
                filas.append({"prov": c, "anio": a, "afiliados_dic": float(tot)})
    d = pd.DataFrame(filas).drop_duplicates(["prov", "anio"])
    return d


def main() -> int:
    e = ecp_enero()
    e = e[e.prov.notna() & e.nacimiento.isin(["Total", "España", "Extranjero"]) & (e.edad != "Todas las edades")].copy()
    e["ini"] = e.edad.str.extract(r"(\d+)")[0].astype(int)
    e = e[(e.ini >= 15) & (e.ini <= 60)]
    out = e.groupby(["prov", "anio", "nacimiento"]).valor.sum().reset_index()
    out.to_csv(PROC / "ecp_15_64.csv.gz", index=False)
    a = afiliacion()
    a.to_csv(PROC / "afiliacion_hist.csv.gz", index=False)
    print(f"f2_ecp_afiliacion: ECP {out.anio.min()}-{out.anio.max()}, {out.prov.nunique()} provincias; afiliación "
          f"{a.anio.min()}-{a.anio.max()}, provincias por año {a.groupby('anio').prov.nunique().to_dict()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
