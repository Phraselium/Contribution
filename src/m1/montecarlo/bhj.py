"""M1 · Monte Carlo de econ.bhj (MC2E shift-share con EE robustos a la exposición, BHJ 2022) frente a EE convencionales.

DGP (declarado antes de simular; cuotas FIJAS entre réplicas, como en el enfoque de diseño de BHJ/AKM; se redibujan shocks y errores):
- 52 provincias agrupadas en 17 «CCAA» contiguas; cada CCAA tiene uno de K=5 patrones de asentamiento (provincias de patrones
  iguales tienen cuotas parecidas aunque estén en CCAA distintas).
- O orígenes con mezcla nacional m ~ Dirichlet(a·1) (a pequeño: pocos orígenes dominantes); patrón k: m_k ~ Dirichlet(5·O·m);
  provincia l: pi_l ~ Dirichlet(60·m_k); exposición total e_l ~ U(0,04; 0,25); cuotas S_lo = e_l·pi_lo (suman e_l < 1).
- Shocks nacionales g_o ~ N(0, 1)/sigma_S i.i.d. (sigma_S² = media_l sum_o S_lo²: el instrumento z = S·g tiene DE ≈ 1).
- Problema de AKM: errores con componente de origen no observado nu_o: eps_l = sum_o S_lo nu_o + eta_l (provincias con cuotas
  parecidas tienen errores correlacionados); endogeneidad: mu_o = rho·nu_o + ..., v_l = rho·eta_l + ..., rho = 0,5.
- x_l = 2·z_l + sum_o S_lo mu_o + v_l (primera etapa fuerte); y_l = beta·x_l + eps_l (+ constante y e_l, que entran en los
  controles W = [1, e_l]).
- Apilado: 3 periodos con las mismas cuotas, shocks g_ot y nu_ot i.i.d. por (origen, periodo); W = efectos de periodo y periodo × e_l.
- beta = 0 (nulo) y beta = 0,5 (no nulo). Referencia adicional: test AKM0 (residuos con el nulo impuesto, al nivel del shock).
  Se compara el IC95 normal de bhj con MC2E de ubicación (econ.iv2sls) con EE robustos HC1 (normal) y agrupados CR1 por CCAA
  (corte) o por provincia (apilado), con t(G-1).
"""

from __future__ import annotations

import time

import numpy as np
from scipy import stats

import _mc
import econ

R = 500
L, NCCAA, K = 52, 17, 5
BETAS = (0.0, 0.5)
DISENOS = [  # nombre, O, a (concentración nacional), T
    ("corte_O40", 40, 1.0, 1),
    ("corte_O20_10efectivos", 20, 1.0, 1),
    ("apilado_3periodos_O40", 40, 1.0, 3),
]


def cuotas(rg, O, a):
    m = np.sort(rg.dirichlet(np.full(O, a)))[::-1]
    m = np.maximum(m, 1e-4)
    m /= m.sum()
    patrones = np.array([rg.dirichlet(5 * O * m) for _ in range(K)])
    ccaa = np.sort(np.concatenate([np.arange(NCCAA), rg.integers(0, NCCAA, L - NCCAA)]))  # cada CCAA ≥ 1 provincia
    tipo_ccaa = rg.integers(0, K, NCCAA)
    pi = np.array([rg.dirichlet(60 * np.maximum(patrones[tipo_ccaa[c]], 1e-6)) for c in ccaa])
    e = rg.uniform(0.04, 0.25, L)
    return e[:, None] * pi, e, ccaa


def apilar(S, e, ccaa, T):
    n, O = S.shape
    Sb = np.zeros((n * T, O * T))
    W = np.zeros((n * T, 2 * T))
    for t in range(T):
        Sb[t * n : (t + 1) * n, t * O : (t + 1) * O] = S
        W[t * n : (t + 1) * n, t] = 1
        W[t * n : (t + 1) * n, T + t] = e
    prov = np.tile(np.arange(n), T)
    return Sb, W, np.tile(ccaa, T), prov


def una(rg, Sb, W, beta, rho=0.5):
    n, O = Sb.shape
    sig = np.sqrt(np.mean((Sb**2).sum(1)))
    g = rg.normal(0, 1, O) / sig
    nu = rg.normal(0, 1, O) / sig
    mu = rho * nu + np.sqrt(1 - rho**2) * rg.normal(0, 1, O) / sig
    eta = rg.normal(0, 0.5, n)
    v = rho * eta + np.sqrt(1 - rho**2) * rg.normal(0, 0.5, n)
    z = Sb @ g
    x = 2 * z + Sb @ mu + v
    y = beta * x + Sb @ nu + eta + W @ np.linspace(0.2, 1.0, W.shape[1])
    return y, x, z, g


def akm0_t2(y, x, S, g, W, beta0):
    """Estadístico AKM0 (Adão, Kolesár y Morales 2019): t² con residuos impuestos bajo H0: beta = beta0, al nivel del shock.
    Variante candidata calculada aquí solo como referencia (no está en econ.py)."""
    yr, xr = econ._resid(y, W, None), econ._resid(x, W, None)
    so = S.sum(0)
    k = so > 0
    S, g, so = S[:, k], g[k], so[k]
    e0 = (S * (yr - beta0 * xr)[:, None]).sum(0) / so
    gd = g - (so * g).sum() / so.sum()
    return float((so * gd * e0).sum() ** 2 / ((so * gd * e0) ** 2).sum())


def main():
    t0 = time.time()
    res = []
    for d, (nombre, O, a, T) in enumerate(DISENOS):
        rs = _mc.rng(1, d)
        S, e, ccaa = cuotas(rs, O, a)
        Sb, W, cl_ccaa, prov = apilar(S, e, ccaa, T)
        cl = cl_ccaa if T == 1 else prov
        G = len(np.unique(cl))
        tcrit = stats.t.ppf(0.975, G - 1)
        for j, beta in enumerate(BETAS):
            rr = _mc.rng(2, d, j)
            b, se, cb, cr, cc, ca, r0b, r0r, r0c, r0a, hhi, Fs, dif = ([] for _ in range(13))
            for _ in range(R):
                y, x, z, g = una(rr, Sb, W, beta)
                o = econ.bhj(y, x, Sb, g, W)
                hc = econ.iv2sls(y, x, z, W, None)
                cr1 = econ.iv2sls(y, x, z, W, cl)
                b.append(o["b"])
                dif.append(abs(o["b"] - hc["b"][0]))
                hhi.append(o["hhi_inv"])
                Fs.append(o["F_shock"])
                cb.append(abs(o["b"] - beta) <= 1.96 * o["se"])
                cr.append(abs(hc["b"][0] - beta) <= 1.96 * hc["se"][0])
                cc.append(abs(cr1["b"][0] - beta) <= tcrit * cr1["se"][0])
                r0b.append(abs(o["b"]) > 1.96 * o["se"])
                r0r.append(abs(hc["b"][0]) > 1.96 * hc["se"][0])
                r0c.append(abs(cr1["b"][0]) > tcrit * cr1["se"][0])
                se.append(o["se"])
                ca.append(akm0_t2(y, x, Sb, g, W, beta) <= 1.96**2)
                r0a.append(akm0_t2(y, x, Sb, g, W, 0.0) > 1.96**2)
            nulo = beta == 0
            fila = {
                "diseno": nombre,
                "O": O,
                "T": T,
                "n": int(Sb.shape[0]),
                "beta": beta,
                "orígenes_efectivos_1/HHI": float(np.mean(hhi)),
                "F_shock_mediana": float(np.median(Fs)),
                "max_dif_b_bhj_vs_iv2sls": float(np.max(dif)),
                "bhj": {
                    **_mc.resumen(b, beta, cb, r0b, nulo),
                    "ee_medio": float(np.mean(se)),
                    "ee_rms": float(np.sqrt(np.mean(np.square(se)))),
                },
                "akm0_referencia": {**_mc.cobertura(ca), ("tamano" if nulo else "potencia"): float(np.mean(r0a))},
                "iv2sls_HC1": {**_mc.cobertura(cr), ("tamano" if nulo else "potencia"): float(np.mean(r0r))},
                f"iv2sls_CR1_{'ccaa' if T == 1 else 'provincia'}_G{G}": {
                    **_mc.cobertura(cc),
                    ("tamano" if nulo else "potencia"): float(np.mean(r0c)),
                },
            }
            res.append(fila)
            print(
                nombre,
                beta,
                round(fila["orígenes_efectivos_1/HHI"], 1),
                fila["bhj"].get("cobertura95"),
                fila["iv2sls_HC1"]["cobertura95"],
                round(time.time() - t0, 1),
                flush=True,
            )
    for f in res:
        f["bhj_apto"] = _mc.apto(f["bhj"]["cobertura95"], f["bhj"].get("tamano"))
        f["akm0_apto"] = _mc.apto(f["akm0_referencia"]["cobertura95"], f["akm0_referencia"].get("tamano"))
    ok = all(f["bhj_apto"] for f in res)
    partes = []
    for nombre, *_ in DISENOS:
        fs = [f for f in res if f["diseno"] == nombre]
        partes.append(
            f"{nombre} (1/HHI≈{fs[0]['orígenes_efectivos_1/HHI']:.0f}): cobertura bhj "
            + "/".join(f"{f['bhj']['cobertura95']:.3f}" for f in fs)
            + f", tamaño {fs[0]['bhj']['tamano']:.3f}"
            + (" → cumple" if all(f["bhj_apto"] for f in fs) else " → falla")
        )
    conv_mal = all(f["iv2sls_HC1"]["cobertura95"] < 0.92 for f in res)
    akm0_ok = all(f["akm0_apto"] for f in res)
    veredicto = "APTO" if ok else "NO APTO"
    condicion = (
        "; ".join(partes) + ". El EE de bhj (tipo HC0 al nivel del shock) infra-cubre cuando pocos orígenes concentran la "
        "exposición (apalancamiento alto); solo se acerca al umbral con ~70 orígenes efectivos. EE convencionales HC1/CR1 "
        + ("sobre-rechazan en todos los diseños" if conv_mal else "no siempre sobre-rechazan")
        + ". AKM0 (nulo impuesto, "
        "referencia calculada en el MC) "
        + ("cumple en todos" if akm0_ok else "cumple en: " + ", ".join(f"{f['diseno']} β={f['beta']}" for f in res if f["akm0_apto"]))
        + "."
    )
    dgp = {
        "provincias": L,
        "ccaa": NCCAA,
        "patrones_asentamiento": K,
        "disenos": [dict(zip(["nombre", "O", "a_dirichlet", "T"], x)) for x in DISENOS],
        "betas": BETAS,
        "rho_endogeneidad": 0.5,
        "R": R,
        "cuotas": "fijas entre réplicas; shocks y errores redibujados",
        "descripcion": __doc__,
    }
    print(_mc.guardar("bhj", dgp, res, veredicto, condicion, t0))


if __name__ == "__main__":
    main()
