"""M1 · Herramientas econométricas propias (deterministas, SEED=20261019). Cada una se valida por Monte Carlo
(src/m1/montecarlo/) antes de usarse en la fase 5.

- ols / iv2sls: MCO y MC2E ponderados con errores agrupados CR1 (o robustos HC1 sin cluster).
- wcr_boot: wild cluster bootstrap restringido (pesos de Webb, 6 puntos) para H0: beta_k = 0 en MCO.
- ar_conjunto: conjunto de confianza de Anderson-Rubin (inversión del test agrupado) con un instrumento.
- f_efectivo: F efectivo de Montiel Olea y Pflueger (2013); con un instrumento coincide con el F de Wald robusto/agrupado.
- bhj: MC2E shift-share con errores robustos a la exposición mediante la regresión equivalente al nivel del shock
  (Borusyak, Hull y Jaravel 2022, prop. 3; numéricamente comparable a AKM 2019).
- rotemberg: pesos de Rotemberg de Goldsmith-Pinkham, Sorkin y Swift (2020) del instrumento de Bartik.
- conley: errores con dependencia espacial (núcleo uniforme hasta un radio en km) para MCO.
- oaxaca: descomposición de Oaxaca-Blinder de dos partes con coeficientes agrupados (Neumark/Oaxaca-Ransom).
- dfl: reponderación de DiNardo, Fortin y Lemieux (logit) para medias y cuantiles contrafactuales.
"""
from __future__ import annotations

import numpy as np

SEED = 20261019


def _w(n, w):
    return np.ones(n) if w is None else np.asarray(w, float)


def _meat(Xe_u, cl):
    """Suma por cluster de los productos X'u (k columnas)."""
    if cl is None:
        return Xe_u.T @ Xe_u, Xe_u.shape[0]
    _, inv = np.unique(cl, return_inverse=True)
    G = inv.max() + 1
    S = np.zeros((G, Xe_u.shape[1]))
    np.add.at(S, inv, Xe_u)
    return S.T @ S, G


def ols(y, X, cluster=None, w=None):
    y, X = np.asarray(y, float), np.asarray(X, float)
    n, k = X.shape
    w = _w(n, w)
    sw = np.sqrt(w)
    Xw, yw = X * sw[:, None], y * sw
    XtX_inv = np.linalg.pinv(Xw.T @ Xw)
    b = XtX_inv @ Xw.T @ yw
    u = y - X @ b
    M, G = _meat(X * (w * u)[:, None], cluster)
    if cluster is None:
        c = n / max(n - k, 1)
    else:
        c = G / max(G - 1, 1) * (n - 1) / max(n - k, 1)
    V = c * XtX_inv @ M @ XtX_inv
    return {"b": b, "V": V, "se": np.sqrt(np.diag(V)), "u": u, "G": G, "n": n}


def iv2sls(y, x, Z, W, cluster=None, w=None):
    """y sobre x (endógena, 1 columna) y W (exógenas, incluye constante/efectos fijos), instrumentos Z. b[0] es el de x."""
    y, x = np.asarray(y, float), np.asarray(x, float).reshape(-1, 1)
    Z, W = np.atleast_2d(np.asarray(Z, float).T).T, np.asarray(W, float)
    n = len(y)
    w = _w(n, w)
    X = np.hstack([x, W])
    ZZ = np.hstack([Z, W])
    sw = np.sqrt(w)
    Xw, Zw, yw = X * sw[:, None], ZZ * sw[:, None], y * sw
    PZ = Zw @ np.linalg.pinv(Zw.T @ Zw) @ Zw.T
    Xh = PZ @ Xw
    A = np.linalg.pinv(Xh.T @ Xw)
    b = A @ Xh.T @ yw
    u = y - X @ b
    Xh_unw = Xh / sw[:, None]
    M, G = _meat(Xh_unw * (w * u)[:, None], cluster)
    k = X.shape[1]
    c = (G / max(G - 1, 1) * (n - 1) / max(n - k, 1)) if cluster is not None else n / max(n - k, 1)
    V = c * A @ M @ A.T
    fs = ols(x.ravel(), ZZ, cluster, w)
    q = Z.shape[1]
    bz, Vz = fs["b"][:q], fs["V"][:q, :q]
    F = float(bz @ np.linalg.pinv(Vz) @ bz / q)
    return {"b": b, "V": V, "se": np.sqrt(np.diag(V)), "u": u, "G": G, "n": n, "F_primera": F, "pi": bz}


def f_efectivo(x, z, W, cluster=None, w=None):
    """F efectivo de Montiel Olea-Pflueger con UN instrumento: igual al F de Wald agrupado de la primera etapa."""
    fs = ols(x, np.column_stack([z, W]), cluster, w)
    return float(fs["b"][0] ** 2 / fs["V"][0, 0])


def wcr_boot(y, X, k, cluster, B=9999, w=None, seed=SEED):
    """Wild cluster bootstrap restringido (WCR, pesos de Webb) del t de beta_k; devuelve p bilateral."""
    rng = np.random.default_rng(seed)
    y, X = np.asarray(y, float), np.asarray(X, float)
    full = ols(y, X, cluster, w)
    t0 = full["b"][k] / full["se"][k]
    Xr = np.delete(X, k, axis=1)
    r = ols(y, Xr, cluster, w)
    yhat_r, ur = Xr @ r["b"], r["u"]
    _, inv = np.unique(cluster, return_inverse=True)
    G = inv.max() + 1
    webb = np.array([-np.sqrt(1.5), -1, -np.sqrt(0.5), np.sqrt(0.5), 1, np.sqrt(1.5)])
    n, kk = X.shape
    wv = _w(n, w)
    sw = np.sqrt(wv)
    Xw = X * sw[:, None]
    XtX_inv = np.linalg.pinv(Xw.T @ Xw)
    c = G / (G - 1) * (n - 1) / (n - kk)
    cnt = 0
    for _ in range(B):
        v = webb[rng.integers(0, 6, G)][inv]
        yb = yhat_r + ur * v
        bb = XtX_inv @ (Xw.T @ (yb * sw))
        ub = yb - X @ bb
        Su = np.zeros((G, kk))
        np.add.at(Su, inv, X * (wv * ub)[:, None])
        Vk = c * (XtX_inv @ (Su.T @ Su) @ XtX_inv)[k, k]
        if abs(bb[k] / np.sqrt(Vk)) >= abs(t0):
            cnt += 1
    return {"t": float(t0), "p": (cnt + 1) / (B + 1), "G": int(G)}


def ar_conjunto(y, x, z, W, cluster=None, w=None, rejilla=None, alfa=0.05):
    """Conjunto de Anderson-Rubin al (1-alfa) para el coeficiente de x con un instrumento z (test agrupado de z en y-b·x)."""
    from scipy import stats
    y, x, z = (np.asarray(a, float) for a in (y, x, z))
    if rejilla is None:
        iv = iv2sls(y, x, z, W, cluster, w)
        b, s = iv["b"][0], iv["se"][0]
        rejilla = np.linspace(b - 12 * s, b + 12 * s, 2401)
    G = len(np.unique(cluster)) if cluster is not None else len(y)
    crit = stats.t.ppf(1 - alfa / 2, G - 1) ** 2 if cluster is not None else stats.chi2.ppf(1 - alfa, 1)
    acept = []
    for b0 in rejilla:
        r = ols(y - b0 * x, np.column_stack([z, W]), cluster, w)
        acept.append(r["b"][0] ** 2 / r["V"][0, 0] <= crit)
    acept = np.array(acept)
    if not acept.any():
        return {"inf": np.nan, "sup": np.nan, "acotado": True, "vacio": True}
    idx = np.where(acept)[0]
    acotado = not (acept[0] or acept[-1])
    return {"inf": float(rejilla[idx[0]]) if acotado else -np.inf, "sup": float(rejilla[idx[-1]]) if acotado else np.inf,
            "acotado": bool(acotado), "vacio": False, "convexo": bool(idx[-1] - idx[0] + 1 == len(idx))}


def _resid(v, W, w):
    return v - W @ ols(v, W, None, w)["b"]


def bhj(y, x, S, g, W, w=None):
    """MC2E shift-share y = beta·x + W·gamma con instrumento z = S @ g (S: n×O cuotas, g: O shocks).
    Error robusto a la exposición por la regresión al nivel del shock (BHJ 2022): se residualizan y, x en W; se agregan a
    cada origen con pesos s_o = sum_l w_l S_lo; MC2E de y_o sobre x_o con instrumento g_o, ponderado por s_o, EE HC robustos.
    Devuelve beta (idéntico al MC2E de ubicación cuando W contiene la suma de cuotas), su EE y el F de primera etapa al nivel shock."""
    y, x, S, g, W = (np.asarray(a, float) for a in (y, x, S, g, W))
    n, O = S.shape
    w = _w(n, w)
    yr, xr = _resid(y, W, w), _resid(x, W, w)
    so = (w[:, None] * S).sum(0)
    keep = so > 0
    Sk, gk, so = S[:, keep], g[keep], so[keep]
    yo = (w[:, None] * Sk * yr[:, None]).sum(0) / so
    xo = (w[:, None] * Sk * xr[:, None]).sum(0) / so
    z = S @ g
    beta = float((w * z * yr).sum() / (w * z * xr).sum())
    eps_o = yo - beta * xo
    gd = gk - (so * gk).sum() / so.sum()   # shocks centrados ponderados (constante en la regresión de shocks)
    den = (so * gd * xo).sum()
    var = ((so * gd * eps_o) ** 2).sum() / den ** 2
    pi = (so * gd * xo).sum() / (so * gd * gd).sum()
    ufs = xo - (so * xo).sum() / so.sum() - pi * gd
    Fp = pi ** 2 / (((so * gd * ufs) ** 2).sum() / ((so * gd * gd).sum()) ** 2)
    return {"b": beta, "se": float(np.sqrt(var)), "F_shock": float(Fp), "O": int(keep.sum()),
            "hhi_inv": float(1 / ((so / so.sum()) ** 2).sum())}


def rotemberg(y, x, S, g, W, w=None):
    """Pesos de Rotemberg (GPSS 2020): alfa_o = g_o·S_o'x⊥ / sum_o g_o·S_o'x⊥ y beta_o = S_o'y⊥ / S_o'x⊥."""
    y, x, S, g, W = (np.asarray(a, float) for a in (y, x, S, g, W))
    w = _w(len(y), w)
    yr, xr = _resid(y, W, w), _resid(x, W, w)
    num = g * (S * (w * xr)[:, None]).sum(0)
    alfa = num / num.sum()
    sx = (S * (w * xr)[:, None]).sum(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        beta_o = (S * (w * yr)[:, None]).sum(0) / sx
    return alfa, beta_o


def conley(y, X, lat, lon, radio_km, w=None):
    """MCO con varianza de Conley (núcleo uniforme: pares a menos de radio_km)."""
    y, X = np.asarray(y, float), np.asarray(X, float)
    n, k = X.shape
    w = _w(n, w)
    r = ols(y, X, None, w)
    la, lo = np.radians(np.asarray(lat, float)), np.radians(np.asarray(lon, float))
    d = 6371 * 2 * np.arcsin(np.sqrt(np.sin((la[:, None] - la[None]) / 2) ** 2 +
                                     np.cos(la[:, None]) * np.cos(la[None]) * np.sin((lo[:, None] - lo[None]) / 2) ** 2))
    K = (d <= radio_km).astype(float)
    Xu = X * (w * r["u"])[:, None]
    M = Xu.T @ K @ Xu
    sw = np.sqrt(w)
    A = np.linalg.pinv((X * sw[:, None]).T @ (X * sw[:, None]))
    V = A @ M @ A * n / (n - k)
    return {"b": r["b"], "V": V, "se": np.sqrt(np.diag(V))}


def oaxaca(y, X, grupo, w=None):
    """Brecha media(A) - media(B), A = grupo True. Coeficientes de referencia: regresión agrupada con indicador de grupo
    (Jann 2008). Devuelve brecha, explicada (composición) y no explicada (resto) y la contribución de cada variable."""
    y, X, grupo = np.asarray(y, float), np.asarray(X, float), np.asarray(grupo, bool)
    w = _w(len(y), w)
    # Corrección (F5, Monte Carlo): sin constante en X la regresión agrupada no tenía término independiente y la parte
    # explicada quedaba sesgada; se añade una constante si X no la trae (su contribución a la parte explicada es 0).
    tiene_cte = bool(np.any(np.all(X == X[:1], axis=0)))
    Xc = X if tiene_cte else np.column_stack([X, np.ones(len(y))])
    bp = ols(y, np.column_stack([Xc, grupo.astype(float)]), None, w)["b"][:X.shape[1]]
    xa = np.average(X[grupo], axis=0, weights=w[grupo])
    xb = np.average(X[~grupo], axis=0, weights=w[~grupo])
    ya, yb = np.average(y[grupo], weights=w[grupo]), np.average(y[~grupo], weights=w[~grupo])
    expl_v = (xa - xb) * bp
    return {"brecha": float(ya - yb), "explicada": float(expl_v.sum()), "no_explicada": float(ya - yb - expl_v.sum()),
            "por_variable": expl_v}


def dfl(y, X, grupo, w=None, cuantiles=(0.1, 0.25, 0.5, 0.75, 0.9)):
    """Reponderación DFL: distribución contrafactual de B (grupo False) con la composición de A (grupo True), logit.
    Devuelve, para la media y los cuantiles: brecha total A-B, composición (contrafactual - B) y resto (A - contrafactual)."""
    import statsmodels.api as sm
    y, X, grupo = np.asarray(y, float), np.asarray(X, float), np.asarray(grupo, bool)
    w = _w(len(y), w)
    m = sm.GLM(grupo.astype(float), np.column_stack([np.ones(len(y)), X]), family=sm.families.Binomial(), freq_weights=w).fit()
    p = np.clip(m.predict(), 1e-6, 1 - 1e-6)
    pa = np.average(grupo, weights=w)
    psi = (p / (1 - p)) * ((1 - pa) / pa)
    wb = w[~grupo] * psi[~grupo]
    from comun import cuantil_pond
    out = {}
    for q in ("media",) + tuple(cuantiles):
        if q == "media":
            A, B, C = (np.average(y[grupo], weights=w[grupo]), np.average(y[~grupo], weights=w[~grupo]),
                       np.average(y[~grupo], weights=wb))
        else:
            A, B, C = cuantil_pond(y[grupo], w[grupo], q), cuantil_pond(y[~grupo], w[~grupo], q), cuantil_pond(y[~grupo], wb, q)
        out[q] = {"brecha": A - B, "composicion": C - B, "resto": A - C}
    return out


def akm0(y, x, S, g, W, w=None, beta0=0.0, rejilla=None, alfa=0.05):
    """Inferencia AKM0 (Adão, Kolesár y Morales 2019) para el MC2E shift-share: t² con residuos impuestos bajo H0 al nivel del
    shock (validada por Monte Carlo en docs/montecarlo.md, a diferencia del Wald de bhj). Devuelve el p de H0: beta = beta0 y
    el intervalo al (1-alfa) por inversión del test en una rejilla."""
    from scipy import stats
    y, x, S, g, W = (np.asarray(a, float) for a in (y, x, S, g, W))
    w = _w(len(y), w)
    yr, xr = _resid(y, W, w), _resid(x, W, w)
    so = (w[:, None] * S).sum(0)
    k = so > 0
    Sk, gk, so = S[:, k], g[k], so[k]
    gd = gk - (so * gk).sum() / so.sum()
    yo = (w[:, None] * Sk * yr[:, None]).sum(0) / so
    xo = (w[:, None] * Sk * xr[:, None]).sum(0) / so

    def t2(b0):
        e0 = yo - b0 * xo
        return float((so * gd * e0).sum() ** 2 / ((so * gd * e0) ** 2).sum())
    crit = stats.chi2.ppf(1 - alfa, 1)
    b = bhj(y, x, S, g, W, w)
    if rejilla is None:
        rejilla = np.linspace(b["b"] - 15 * b["se"], b["b"] + 15 * b["se"], 3001)
    acc = np.array([t2(r) <= crit for r in rejilla])
    idx = np.where(acc)[0]
    if len(idx) == 0:
        inf = sup = np.nan
    else:
        inf = -np.inf if acc[0] else float(rejilla[idx[0]])
        sup = np.inf if acc[-1] else float(rejilla[idx[-1]])
    return {"b": b["b"], "p": float(1 - stats.chi2.cdf(t2(beta0), 1)), "ic_inf": inf, "ic_sup": sup, "O": b["O"],
            "hhi_inv": b["hhi_inv"], "F_shock": b["F_shock"]}
