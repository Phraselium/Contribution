"""Tests rápidos de src/m1/econ.py con datos simulados pequeños (nunca datos reales).

- ols coincide con statsmodels OLS con errores agrupados CR1 (G/(G-1)·(n-1)/(n-k), la corrección por defecto de statsmodels).
- iv2sls coincide con linearmodels IV2SLS en coeficientes y EE agrupado. Corrección de pequeña muestra: econ aplica
  G/(G-1)·(n-1)/(n-k) (como Stata ivregress con small); linearmodels 7.1 la aplica entera con debiased=True (coincidencia
  exacta). Con debiased=False (su opción por defecto) linearmodels 7.1 no aplica ninguna corrección, aunque su docstring
  menciona G/(G-1): V_econ = V_lm·G/(G-1)·(n-1)/(n-k).
- Identidades contables de oaxaca y dfl.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "m1"))
import econ  # noqa: E402


def _datos(seed=20261019, G=30, n=600, w=False):
    rg = np.random.default_rng(seed)
    cl = rg.integers(0, G, n)
    a = rg.normal(0, 1, G)[cl]
    z = rg.normal(0, 1, n) + 0.5 * rg.normal(0, 1, G)[cl]
    c = rg.normal(0, 1, n)
    v = rg.normal(0, 1, n) + 0.5 * a
    x = 0.8 * z + 0.3 * c + v
    y = 1 + 0.5 * x - 0.2 * c + a + 0.7 * v + rg.normal(0, 1, n)
    pesos = rg.uniform(0.5, 2, n) if w else None
    return y, x, z, c, cl, pesos


@pytest.mark.parametrize("pond", [False, True])
def test_ols_igual_statsmodels_cr1(pond):
    import statsmodels.api as sm
    y, x, z, c, cl, w = _datos(w=pond)
    X = np.column_stack([x, np.ones(len(y)), c])
    o = econ.ols(y, X, cl, w)
    m = (sm.WLS(y, X, weights=w) if pond else sm.OLS(y, X)).fit(cov_type="cluster", cov_kwds={"groups": cl})
    np.testing.assert_allclose(o["b"], m.params, rtol=1e-10)
    np.testing.assert_allclose(o["se"], m.bse, rtol=1e-8)


def test_ols_hc1_statsmodels():
    import statsmodels.api as sm
    y, x, z, c, cl, _ = _datos()
    X = np.column_stack([x, np.ones(len(y)), c])
    np.testing.assert_allclose(econ.ols(y, X)["se"], sm.OLS(y, X).fit(cov_type="HC1").bse, rtol=1e-8)


@pytest.mark.parametrize("pond", [False, True])
def test_iv2sls_igual_linearmodels(pond):
    from linearmodels.iv import IV2SLS
    y, x, z, c, cl, w = _datos(w=pond)
    n = len(y)
    W = np.column_stack([np.ones(n), c])
    o = econ.iv2sls(y, x, z, W, cl, w)
    kw = {"weights": w} if pond else {}
    lm = IV2SLS(y, W, x[:, None], z[:, None], **kw)
    r_deb = lm.fit(cov_type="clustered", clusters=cl, debiased=True)
    r_def = lm.fit(cov_type="clustered", clusters=cl, debiased=False)
    # linearmodels ordena [exógenas, endógena]; econ pone la endógena primero
    b_lm = np.r_[r_deb.params.values[-1], r_deb.params.values[:-1]]
    se_deb = np.r_[r_deb.std_errors.values[-1], r_deb.std_errors.values[:-1]]
    se_def = np.r_[r_def.std_errors.values[-1], r_def.std_errors.values[:-1]]
    np.testing.assert_allclose(o["b"], b_lm, rtol=1e-9)
    np.testing.assert_allclose(o["se"], se_deb, rtol=1e-8)
    k, G = 3, len(np.unique(cl))
    np.testing.assert_allclose(o["se"], se_def * np.sqrt(G / (G - 1) * (n - 1) / (n - k)), rtol=1e-8)


def test_f_efectivo_igual_F_primera():
    y, x, z, c, cl, _ = _datos()
    W = np.column_stack([np.ones(len(y)), c])
    assert econ.f_efectivo(x, z, W, cl) == pytest.approx(econ.iv2sls(y, x, z, W, cl)["F_primera"], rel=1e-10)


def test_ar_contiene_valor_y_es_coherente():
    y, x, z, c, cl, _ = _datos()
    W = np.column_stack([np.ones(len(y)), c])
    s = econ.ar_conjunto(y, x, z, W, cl)
    iv = econ.iv2sls(y, x, z, W, cl)
    assert s["acotado"] and s["inf"] < iv["b"][0] < s["sup"]


def test_bhj_coincide_con_mc2e_de_ubicacion():
    rg = np.random.default_rng(1)
    L, O = 52, 25
    e = rg.uniform(0.05, 0.25, L)
    S = e[:, None] * rg.dirichlet(np.ones(O), L)
    g = rg.normal(0, 1, O)
    z = S @ g
    x = 3 * z + rg.normal(0, 0.1, L)
    y = 0.5 * x + rg.normal(0, 0.1, L)
    W = np.column_stack([np.ones(L), e])
    o = econ.bhj(y, x, S, g, W)
    assert o["b"] == pytest.approx(econ.iv2sls(y, x, z, W)["b"][0], rel=1e-9)
    assert o["se"] > 0 and o["O"] == O


def _oaxaca_datos(seed=3, n=3000):
    rg = np.random.default_rng(seed)
    A = rg.random(n) < 0.3
    educ = np.where(A, rg.choice(3, n, p=[0.5, 0.3, 0.2]), rg.choice(3, n, p=[0.2, 0.4, 0.4]))
    edad = rg.choice(3, n)
    X = np.column_stack([educ == 1, educ == 2, edad == 1, edad == 2]).astype(float)
    b = np.array([0.3, 0.7, 0.2, 0.35])
    return X, A, b, rg


def test_oaxaca_identidades_y_caso_exacto():
    X, A, b, rg = _oaxaca_datos()
    y = 2 + X @ b - 0.1 * A                                   # sin ruido: descomposición exacta
    o = econ.oaxaca(y, X, A)
    dx = X[A].mean(0) - X[~A].mean(0)
    assert o["brecha"] == pytest.approx(y[A].mean() - y[~A].mean(), abs=1e-12)
    assert o["explicada"] + o["no_explicada"] == pytest.approx(o["brecha"], abs=1e-12)
    assert o["por_variable"].sum() == pytest.approx(o["explicada"], abs=1e-12)
    assert o["explicada"] == pytest.approx(dx @ b, abs=1e-9)
    assert o["no_explicada"] == pytest.approx(-0.1, abs=1e-9)
    y2 = y + rg.normal(0, 0.3, len(y))
    w = rg.uniform(0.5, 2, len(y))
    o1 = econ.oaxaca(y2, X, A, w)                             # sin constante (econ la añade)
    o2 = econ.oaxaca(y2, np.column_stack([np.ones(len(y)), X]), A, w)
    assert o1["explicada"] == pytest.approx(o2["explicada"], abs=1e-10)


def test_dfl_identidades_y_saturado():
    X, A, b, rg = _oaxaca_datos()
    y = 2 + X @ b - 0.1 * A + rg.normal(0, 0.3, len(A))
    w = rg.uniform(0.5, 2, len(A))
    f = econ.dfl(y, X, A, w)
    for v in f.values():
        assert v["composicion"] + v["resto"] == pytest.approx(v["brecha"], abs=1e-12)
    assert f["media"]["brecha"] == pytest.approx(np.average(y[A], weights=w[A]) - np.average(y[~A], weights=w[~A]), abs=1e-12)
    # Con covariables independientes dentro de grupo... aquí educ y edad son independientes de A salvo educ: el logit con
    # efectos principales es correcto y la composición en la media ≈ dx·b (error de muestreo pequeño).
    dx = np.average(X[A], 0, w[A]) - np.average(X[~A], 0, w[~A])
    assert f["media"]["composicion"] == pytest.approx(dx @ b, abs=0.03)


def test_akm0_coincide_con_referencia_mc():
    """econ.akm0 reproduce el estadístico AKM0 validado en src/m1/montecarlo/bhj.py (akm0_t2)."""
    import importlib.util
    from scipy import stats
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src/m1/montecarlo"))
    spec = importlib.util.spec_from_file_location("mc_bhj", Path(__file__).resolve().parents[1] / "src/m1/montecarlo/bhj.py")
    mc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mc)
    rng = np.random.default_rng(1)
    n, O = 52, 15
    S = rng.dirichlet(np.ones(O) * 0.3, n) * rng.uniform(0.05, 0.2, (n, 1))
    g = rng.normal(size=O)
    W = np.column_stack([np.ones(n), S.sum(1)])
    x = S @ g * 2 + rng.normal(size=n)
    y = 0.3 * x + rng.normal(size=n)
    r = econ.akm0(y, x, S, g, W, beta0=0.0)
    assert abs(r["p"] - (1 - stats.chi2.cdf(mc.akm0_t2(y, x, S, g, W, 0.0), 1))) < 1e-10
    assert r["ic_inf"] < r["b"] < r["ic_sup"]
