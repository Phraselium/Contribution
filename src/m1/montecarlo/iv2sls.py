"""M1 · Monte Carlo de econ.iv2sls + econ.f_efectivo + econ.ar_conjunto con instrumento fuerte y débil y 52 clusters.

DGP (declarado antes de simular; todo se redibuja en cada réplica):
- G = 52 clusters (provincias) con N_g ~ U{10, …, 60} observaciones.
- Instrumento z_ig = z_g + 0,5·N(0,1), z_g ~ N(0,1); control c_ig ~ N(0,1).
- Errores con componente de cluster y endogeneidad fuerte: (u, v) = (a_g, b_g) + (e_ig, f_ig), cada par N(0, [[1, 0,8], [0,8, 1]]).
- x = pi·z + 0,3·c + v; y = beta·x + 0,3·c + u; beta = 1 (cobertura y tamaño en el valor verdadero; potencia contra beta = 0).
- pi calibrado para un F efectivo (= F de Wald agrupado de la primera etapa) mediano ≈ 3, 10 y 50.
- Wald: IC b ± t(G-1)·EE CR1. AR: conjunto de econ.ar_conjunto (test agrupado con t(G-1)²); cobertura = el valor verdadero
  no se rechaza (rejilla de un punto); forma del conjunto (acotado/convexo/longitud) con una rejilla de 201 puntos en beta ± 5.
"""

from __future__ import annotations

import time

import numpy as np
from scipy import stats

import _mc
import econ

R, G, BETA = 500, 52, 1.0
OBJETIVO_F = (3, 10, 50)


def una(rg, pi, beta=BETA):
    Ng = rg.integers(10, 61, G)
    cl = np.repeat(np.arange(G), Ng)
    n = Ng.sum()
    C = np.array([[1, 0.8], [0.8, 1]])
    ab = rg.multivariate_normal([0, 0], C, G)[cl]
    ef = rg.multivariate_normal([0, 0], C, n)
    u, v = ab[:, 0] + ef[:, 0], ab[:, 1] + ef[:, 1]
    z = rg.normal(0, 1, G)[cl] + 0.5 * rg.normal(0, 1, n)
    c = rg.normal(0, 1, n)
    x = pi * z + 0.3 * c + v
    y = beta * x + 0.3 * c + u
    return y, x, z, np.column_stack([np.ones(n), c]), cl


def calibrar(objetivo):
    """pi tal que el F efectivo mediano ≈ objetivo (F ∝ pi²), con 200 réplicas piloto."""
    rp = _mc.rng(4, 0)
    F0 = np.median([econ.f_efectivo(x, z, W, cl) for y, x, z, W, cl in (una(rp, 0.2) for _ in range(200))])
    return 0.2 * np.sqrt(objetivo / F0)


def main():
    t0 = time.time()
    tcrit = stats.t.ppf(0.975, G - 1)
    res = []
    for d, objetivo in enumerate(OBJETIVO_F):
        pi = calibrar(objetivo)
        rr = _mc.rng(4, 1, d)
        b, Fe, difF, cw, rw0, ca, ra0, acot, conv, lon, vac = ([] for _ in range(11))
        rej = BETA + np.linspace(-5, 5, 201)
        for _ in range(R):
            y, x, z, W, cl = una(rr, pi)
            iv = econ.iv2sls(y, x, z, W, cl)
            F = econ.f_efectivo(x, z, W, cl)
            b.append(iv["b"][0])
            Fe.append(F)
            difF.append(abs(F - iv["F_primera"]))
            cw.append(abs(iv["b"][0] - BETA) <= tcrit * iv["se"][0])
            rw0.append(abs(iv["b"][0]) > tcrit * iv["se"][0])
            ca.append(not econ.ar_conjunto(y, x, z, W, cl, rejilla=np.array([BETA]))["vacio"])
            ra0.append(econ.ar_conjunto(y, x, z, W, cl, rejilla=np.array([0.0]))["vacio"])
            s = econ.ar_conjunto(y, x, z, W, cl, rejilla=rej)
            vac.append(s["vacio"])
            acot.append(s["acotado"] and not s["vacio"])
            conv.append(bool(s.get("convexo", True)))
            lon.append(s["sup"] - s["inf"] if acot[-1] else np.inf)
        fila = {
            "diseno": f"F_objetivo_{objetivo}",
            "pi": float(pi),
            "G": G,
            "beta": BETA,
            "F_efectivo_mediana": float(np.median(Fe)),
            "F_efectivo_p10_p90": [float(np.quantile(Fe, 0.1)), float(np.quantile(Fe, 0.9))],
            "max_dif_f_efectivo_vs_F_primera": float(np.max(difF)),
            "wald_iv2sls_CR1": {**_mc.resumen(b, BETA, cw, None), "tamano": float(1 - np.mean(cw)), "potencia_vs_0": float(np.mean(rw0))},
            "ar_conjunto": {
                **_mc.cobertura(ca),
                "tamano": float(1 - np.mean(ca)),
                "potencia_vs_0": float(np.mean(ra0)),
                "frac_acotado_en_beta±5": float(np.mean(acot)),
                "frac_convexo": float(np.mean(conv)),
                "frac_vacio": float(np.mean(vac)),
                "longitud_mediana_acotados": float(np.median([v for v in lon if np.isfinite(v)])) if np.isfinite(lon).any() else None,
            },
        }
        fila["wald_apto"] = _mc.apto(fila["wald_iv2sls_CR1"]["cobertura95"], fila["wald_iv2sls_CR1"]["tamano"])
        fila["ar_apto"] = _mc.apto(fila["ar_conjunto"]["cobertura95"], fila["ar_conjunto"]["tamano"])
        res.append(fila)
        print(
            fila["diseno"],
            fila["F_efectivo_mediana"],
            fila["wald_iv2sls_CR1"]["cobertura95"],
            fila["ar_conjunto"]["cobertura95"],
            round(time.time() - t0, 1),
            flush=True,
        )
    # El test AR en el valor verdadero no depende de pi (y - beta·x = u + 0,3·c): se agrega su cobertura de los tres diseños.
    ar_all = np.mean([f["ar_conjunto"]["cobertura95"] for f in res])
    ar_ee = float(np.sqrt(ar_all * (1 - ar_all) / (R * len(res))))
    ok_w = [f["F_efectivo_mediana"] for f in res if f["wald_apto"]]
    # AR se juzga con la cobertura agregada (misma distribución en los tres diseños); Wald, diseño a diseño.
    ar_ok = _mc.apto(ar_all, 1 - ar_all)
    veredicto = (
        "APTO"
        if all(f["wald_apto"] for f in res) and ar_ok
        else ("APTO CON CONDICIÓN" if ar_ok and ok_w else "NO APTO")
    )
    condicion = (
        "Wald (iv2sls CR1): "
        + "; ".join(f"F≈{f['F_efectivo_mediana']:.1f} cobertura {f['wald_iv2sls_CR1']['cobertura95']:.3f}" for f in res)
        + ". AR (ar_conjunto): "
        + "; ".join(f"F≈{f['F_efectivo_mediana']:.1f} cobertura {f['ar_conjunto']['cobertura95']:.3f}" for f in res)
        + f" (agregada {ar_all:.3f} ± {ar_ee:.3f}, idéntica en distribución en los tres diseños)"
        + (
            f". Wald solo cumple con F efectivo ≥ {min(ok_w):.0f}; con F menor, usar el conjunto AR."
            if ok_w and len(ok_w) < len(res)
            else ""
        )
    )
    dgp = {
        "ar_cobertura_agregada": float(ar_all),
        "ar_cobertura_agregada_ee": ar_ee,
        "G": G,
        "beta": BETA,
        "F_objetivo": OBJETIVO_F,
        "rho_endogeneidad": 0.8,
        "R": R,
        "descripcion": __doc__,
    }
    print(_mc.guardar("iv2sls", dgp, res, veredicto, condicion, t0))


if __name__ == "__main__":
    main()
