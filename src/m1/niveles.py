"""M1 · Comparaciones en los tres niveles de la sección A y descomposición de la brecha bruta.

tres_niveles(): para cada grupo de origen frente a «España» (nacidos en España, o españoles con la definición de nacionalidad):
- bruto: diferencia de medias ponderadas;
- edad y sexo: coeficiente del grupo en MCO ponderado con efectos fijos de edad × sexo;
- completo: además educación, años de residencia (evaluado en la categoría de referencia «10-19 años» para los nacidos fuera;
  los nativos no tienen años de residencia) y región (provincia o NUTS2).
Errores agrupados por región. Se devuelve también el número de observaciones muestrales del grupo (n_muestral) para suprimir
celdas con menos de 50 (comun.suprimir). Las brechas son agregados: no describen a ninguna persona.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import econ
from comun import UMBRAL_CELDA


def _dummies(df: pd.DataFrame, cols: list[str]) -> np.ndarray:
    if not cols:
        return np.empty((len(df), 0))
    return pd.get_dummies(df[cols].astype(str), drop_first=True, dtype=float).to_numpy()


def tres_niveles(df: pd.DataFrame, y: str, peso: str, grupo: str = "grupo", ref: str = "España", n_col: str = "n_obs",
                 nivel1: tuple = ("edad6", "sexo"), nivel2: tuple = ("educ",), resid: str | None = "resid",
                 region: str | None = "prov", cluster: str | None = "prov") -> pd.DataFrame:
    d = df[df[peso] > 0].dropna(subset=[y]).copy()
    grupos = [g for g in d[grupo].unique() if g != ref]
    G = np.column_stack([(d[grupo] == g).astype(float) for g in grupos])
    w = d[peso].to_numpy(float)
    yv = d[y].to_numpy(float)
    cl = d[cluster].to_numpy() if cluster else None
    const = np.ones((len(d), 1))
    d["_c1"] = d[list(nivel1)].astype(str).agg("|".join, axis=1)
    X1 = _dummies(d, ["_c1"])
    X2 = _dummies(d, list(nivel2) + ([region] if region else []))
    Xr = np.empty((len(d), 0))
    if resid:
        r = d[resid].astype(str)
        Xr = np.column_stack([((r == k) & (d[grupo] != ref)).astype(float) for k in ("0-4", "5-9", "20+", "no consta")])
    out = []
    for nombre, X in (("bruto", np.hstack([const, G])), ("edad y sexo", np.hstack([const, G, X1])),
                      ("completo", np.hstack([const, G, X1, X2, Xr]))):
        r = econ.ols(yv, X, cl, w)
        for i, g in enumerate(grupos):
            out.append({"grupo": g, "nivel_ajuste": nombre, "brecha": r["b"][1 + i], "ee": r["se"][1 + i]})
    o = pd.DataFrame(out)
    base = d[d[grupo] == ref]
    media_ref = np.average(base[y], weights=base[peso])
    o["media_referencia"] = media_ref
    medias = d.groupby(grupo).apply(lambda x: np.average(x[y], weights=x[peso]), include_groups=False)
    o["media_grupo"] = o["grupo"].map(medias)
    o["n_muestral"] = o["grupo"].map(d.groupby(grupo)[n_col].sum())
    o.loc[o["n_muestral"] < UMBRAL_CELDA, ["brecha", "ee", "media_grupo"]] = np.nan
    return o


def oaxaca_celdas(df: pd.DataFrame, y: str, peso: str, grupo_a: str, grupo_col: str = "grupo", ref: str = "España",
                  covs: tuple = ("edad6", "sexo", "educ", "prov")) -> dict:
    """Oaxaca-Blinder (referencia agrupada) de la brecha media(grupo_a) - media(ref) con covariables discretas."""
    d = df[df[grupo_col].isin([grupo_a, ref]) & (df[peso] > 0)].dropna(subset=[y])
    X = _dummies(d, list(covs))
    r = econ.oaxaca(d[y].to_numpy(float), X, (d[grupo_col] == grupo_a).to_numpy(), d[peso].to_numpy(float))
    return {"brecha": r["brecha"], "composicion": r["explicada"], "resto": r["no_explicada"]}
