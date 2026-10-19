"""M1 · Utilidades de los Monte Carlo de herramientas (src/m1/montecarlo/). Solo datos simulados, nunca datos reales.

Cada script de herramienta declara su proceso generador (DGP) en un diccionario, lo simula con R ≥ 500 réplicas y semilla
derivada de SEED=20261019, y escribe output/montecarlo/<herramienta>/resultado.json con sesgo, RMSE, cobertura al 95 %,
tamaño y potencia. El veredicto sigue la regla común: APTO si cobertura ∈ [0,92; 0,98] y tamaño ≤ 0,08.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))  # src/m1 para «import econ» y «import comun»

SEED = 20261019
RAIZ = AQUI.parents[2]
OUT_MC = RAIZ / "output" / "montecarlo"
COB_MIN, COB_MAX, TAM_MAX = 0.92, 0.98, 0.08


def rng(*claves: int) -> np.random.Generator:
    """Generador determinista para un diseño concreto (independiente del orden en que se ejecuten los diseños)."""
    return np.random.default_rng([SEED, *claves])


def resumen(est, verdad: float, cubre=None, rechaza0=None, nulo: bool = True) -> dict:
    """Sesgo, RMSE, cobertura del IC95 del valor verdadero y tasa de rechazo de H0: beta = 0 (tamaño si nulo, potencia si no)."""
    est = np.asarray(est, float)
    ok = np.isfinite(est)
    d = {
        "R": int(len(est)),
        "R_validas": int(ok.sum()),
        "verdad": float(verdad),
        "media": float(np.mean(est[ok])),
        "sesgo": float(np.mean(est[ok]) - verdad),
        "mediana_sesgo": float(np.median(est[ok]) - verdad),
        "rmse": float(np.sqrt(np.mean((est[ok] - verdad) ** 2))),
        "de_mc": float(np.std(est[ok], ddof=1)),
    }
    if cubre is not None:
        d.update(cobertura(cubre))
    if rechaza0 is not None:
        d["tamano" if nulo else "potencia"] = float(np.asarray(rechaza0, bool).mean())
    return d


def cobertura(cubre) -> dict:
    c = np.asarray(cubre, bool)
    return {"cobertura95": float(c.mean()), "ee_mc_cobertura": float(np.sqrt(c.mean() * (1 - c.mean()) / len(c)))}


def apto(cobertura: float | None, tamano: float | None) -> bool:
    ok = True
    if cobertura is not None:
        ok &= COB_MIN <= cobertura <= COB_MAX
    if tamano is not None:
        ok &= tamano <= TAM_MAX
    return bool(ok)


def guardar(herramienta: str, dgp: dict, disenos: list, veredicto: str, condicion: str, t0: float, **extra) -> Path:
    p = OUT_MC / herramienta / "resultado.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    doc = {
        "herramienta": herramienta,
        "seed": SEED,
        "datos": "simulados (nunca datos reales)",
        "dgp": dgp,
        "disenos": disenos,
        "veredicto": veredicto,
        "condicion": condicion,
        "criterio": f"APTO si cobertura en [{COB_MIN}, {COB_MAX}] y tamaño ≤ {TAM_MAX}",
        "segundos": round(time.time() - t0, 1),
        **extra,
    }
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1, default=_json) + "\n", encoding="utf-8")
    return p


def _json(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if np.isnan(o) else float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return str(o)
