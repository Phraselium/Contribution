"""M1 · Utilidades comunes: rutas, semilla, grupos de origen, supresión de celdas, Registry, correcciones múltiples y resultado.json.

Las definiciones de origen están fijadas en docs/plan.md (sección A) ANTES de mirar datos:
país de nacimiento como principal, nacionalidad como sensibilidad, y ocho grupos.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20261019
RAIZ = Path(__file__).resolve().parents[2]
RAW = RAIZ / "data" / "raw"
PROC = RAIZ / "data" / "processed"
OUT = RAIZ / "output"
DOCS = RAIZ / "docs"
UMBRAL_CELDA = 50   # supresión: menos de 50 observaciones muestrales

# ── Grupos de origen (sección A) ──────────────────────────────────────────────────────────────────────────────────────────
GRUPOS = ["España", "UE-14", "UE-13 y otros de Europa", "América Latina", "Magreb", "Resto de África", "Asia", "Resto"]

UE14 = {"AT", "BE", "DK", "FI", "FR", "DE", "GR", "IE", "IT", "LU", "NL", "PT", "SE", "GB"}   # UE-15 sin España; Reino Unido se
# mantiene en UE-14 en todo el periodo para que el grupo no cambie de composición con el Brexit (decisión D1).
UE13 = {"BG", "HR", "CY", "CZ", "EE", "HU", "LV", "LT", "MT", "PL", "RO", "SK", "SI"}
OTROS_EUROPA = {"AL", "AD", "BY", "BA", "FO", "GI", "IS", "XK", "LI", "MK", "MD", "MC", "ME", "NO", "RU", "SM", "RS", "CH", "UA",
                "VA", "TR"}
AMERICA_LATINA = {"AR", "BO", "BR", "CL", "CO", "CR", "CU", "DO", "EC", "SV", "GT", "HN", "MX", "NI", "PA", "PY", "PE", "PR", "UY",
                  "VE", "HT"}
MAGREB = {"MA", "DZ", "TN", "LY", "MR", "EH"}
ASIA = {"CN", "IN", "PK", "BD", "PH", "JP", "KR", "KP", "VN", "TH", "ID", "MY", "SG", "NP", "LK", "IR", "IQ", "SY", "LB", "JO",
        "IL", "PS", "SA", "AE", "QA", "KW", "BH", "OM", "YE", "AF", "AM", "AZ", "GE", "KZ", "KG", "TJ", "TM", "UZ", "MN", "MM", "KH",
        "LA", "TW", "HK", "MO", "BT", "MV", "BN", "TL"}


def grupo_iso2(iso2: str | None) -> str:
    """Grupo de origen de un código ISO 3166-1 alfa-2 (ES → España). África no magrebí → Resto de África."""
    if not iso2:
        return "Resto"
    c = iso2.upper()
    if c == "ES":
        return "España"
    for conj, g in ((UE14, "UE-14"), (UE13 | OTROS_EUROPA, "UE-13 y otros de Europa"), (AMERICA_LATINA, "América Latina"),
                    (MAGREB, "Magreb"), (ASIA, "Asia")):
        if c in conj:
            return g
    if c in AFRICA_RESTO:
        return "Resto de África"
    return "Resto"


AFRICA_RESTO = {"AO", "BJ", "BW", "BF", "BI", "CV", "CM", "CF", "TD", "KM", "CG", "CD", "CI", "DJ", "EG", "GQ", "ER", "SZ", "ET",
                "GA", "GM", "GH", "GN", "GW", "KE", "LS", "LR", "MG", "MW", "ML", "MU", "MZ", "NA", "NE", "NG", "RW", "ST", "SN",
                "SC", "SL", "SO", "ZA", "SS", "SD", "TZ", "TG", "UG", "ZM", "ZW"}


# ── Supresión ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
def suprimir(df: pd.DataFrame, col_n: str = "n_muestral", cols_valor: list[str] | None = None,
             umbral: int = UMBRAL_CELDA) -> pd.DataFrame:
    """Pone a NaN los valores de las celdas con menos de `umbral` observaciones muestrales y marca `suprimida`."""
    d = df.copy()
    cols = cols_valor or [c for c in d.columns if c not in (col_n,) and pd.api.types.is_numeric_dtype(d[c])]
    mask = d[col_n] < umbral
    d.loc[mask, cols] = np.nan
    d["suprimida"] = mask
    return d


# ── Estimadores ponderados de encuesta ────────────────────────────────────────────────────────────────────────────────────
def media_pond(x, w) -> float:
    x, w = np.asarray(x, float), np.asarray(w, float)
    m = ~np.isnan(x) & ~np.isnan(w)
    return float(np.sum(x[m] * w[m]) / np.sum(w[m])) if m.any() and w[m].sum() > 0 else np.nan


def cuantil_pond(x, w, q: float) -> float:
    x, w = np.asarray(x, float), np.asarray(w, float)
    m = ~np.isnan(x) & ~np.isnan(w)
    x, w = x[m], w[m]
    if len(x) == 0:
        return np.nan
    o = np.argsort(x)
    cw = np.cumsum(w[o]) / w.sum()
    return float(x[o][np.searchsorted(cw, q)])


# ── Correcciones múltiples ────────────────────────────────────────────────────────────────────────────────────────────────
def holm(pvals: dict) -> dict:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, out, run = len(items), {}, 0.0
    for i, (k, p) in enumerate(items):
        run = max(run, min(1.0, (m - i) * p))
        out[k] = run
    return out


def bh(pvals: dict) -> dict:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, out, run = len(items), {}, 1.0
    for i in range(m - 1, -1, -1):
        k, p = items[i]
        run = min(run, p * m / (i + 1))
        out[k] = min(1.0, run)
    return out


# ── Registry (adaptado de Econometr-a: escritura atómica al final del proceso) ─────────────────────────────────────────────
class Registry:
    COLS = ["fase", "pregunta", "modelo_id", "especificacion", "muestra", "n", "coef", "ee", "p", "notas"]

    def __init__(self, path):
        import atexit
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.rows: list = []
        atexit.register(self.flush)

    def log(self, fase, pregunta, modelo_id, especificacion, muestra, n, coef=np.nan, ee=np.nan, p=np.nan, notas=""):
        self.rows.append([fase, pregunta, modelo_id, especificacion, muestra, n, coef, ee, p, notas])

    def frame(self) -> pd.DataFrame:
        return pd.DataFrame(self.rows, columns=self.COLS)

    def flush(self):
        if not self.rows:
            return
        tmp = self.path.with_name(f".{self.path.name}.{os.getpid()}.tmp")
        self.frame().to_csv(tmp, index=False)
        os.replace(tmp, self.path)


# ── Salidas ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
RESULTADO_CAMPOS = ["pregunta", "capa", "clasificacion", "datos", "N", "metodo", "estimacion", "ic95", "p_ajustado",
                    "diagnosticos", "notas"]


def escribir_resultado(ruta: Path, **campos) -> None:
    faltan = [c for c in RESULTADO_CAMPOS if c not in campos]
    if faltan:
        raise ValueError(f"resultado.json incompleto: faltan {faltan}")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(campos, ensure_ascii=False, indent=1, default=_json) + "\n", encoding="utf-8")


def _json(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if np.isnan(o) else float(o)
    if isinstance(o, (dt.date,)):
        return o.isoformat()
    return str(o)


CIFRAS_COLS = ["id", "valor", "ic_inf", "ic_sup", "unidad", "descripcion", "capa", "clasificacion", "fuente", "periodo",
               "ambito", "grupo_origen", "nivel_ajuste", "script"]
CAPAS = {"C1", "C2", "C3", "C4"}
CLASIFICACIONES = {"", "IDENTIFICADO", "SUGESTIVO", "ASOCIACIÓN", "NO ESTIMABLE"}


class Cifras:
    """Acumula cifras difundibles de una fase y las escribe en output/cifras/<fase>.csv (cifras_clave.csv se consolida con
    src/m1/cifras.py)."""

    def __init__(self, fase: str, script: str):
        self.fase, self.script, self.filas = fase, script, []

    def add(self, id, valor, unidad, descripcion, capa, fuente, periodo, ambito, grupo_origen="todos", nivel_ajuste="bruto",
            clasificacion="", ic_inf=np.nan, ic_sup=np.nan):
        if capa not in CAPAS:
            raise ValueError(f"capa inválida {capa}")
        if clasificacion not in CLASIFICACIONES:
            raise ValueError(f"clasificación inválida {clasificacion}")
        if capa == "C3" and clasificacion != "IDENTIFICADO":
            raise ValueError("C3 exige IDENTIFICADO")
        self.filas.append(dict(id=id, valor=valor, ic_inf=ic_inf, ic_sup=ic_sup, unidad=unidad, descripcion=descripcion, capa=capa,
                               clasificacion=clasificacion, fuente=fuente, periodo=periodo, ambito=ambito,
                               grupo_origen=grupo_origen, nivel_ajuste=nivel_ajuste, script=self.script))

    def escribir(self) -> Path:
        p = OUT / "cifras" / f"{self.fase}.csv"
        p.parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame(self.filas, columns=CIFRAS_COLS)
        if df["id"].duplicated().any():
            raise ValueError(f"ids duplicados: {df.loc[df['id'].duplicated(), 'id'].tolist()}")
        df.to_csv(p, index=False, quoting=csv.QUOTE_MINIMAL)
        return p


def sha256(ruta: Path) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def rng():
    return np.random.default_rng(SEED)
