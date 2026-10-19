"""M1 · Monte Carlo de econ.conley (MCO con varianza de Conley, núcleo uniforme, radio 200 km) frente a HC1.

DGP (declarado antes de simular):
- 52 puntos FIJOS (dibujados una vez) uniformes en el rectángulo lat 36-43,8, lon -9,3 a 3,3 (escala de las provincias).
- Regresor y error: campos gaussianos independientes con covarianza exp(-d/lambda) (d en km, gran círculo) más un 20 % de ruido
  propio (pepita): x = 0,9·F1 + 0,45·N(0,1), e = 0,9·F2 + 0,45·N(0,1). lambda ∈ {50, 100, 200} km.
- y = 1 + beta·x + e; beta = 0 (tamaño) y beta = 0,5 (potencia). IC95 normal b ± 1,96·EE.
"""

from __future__ import annotations

import time

import numpy as np

import _mc
import econ

R, N, RADIO = 500, 52, 200
LAMBDAS = (50, 100, 200)
BETAS = (0.0, 0.5)


def distancias(lat, lon):
    la, lo = np.radians(lat), np.radians(lon)
    return (
        6371
        * 2
        * np.arcsin(
            np.sqrt(
                np.sin((la[:, None] - la[None]) / 2) ** 2
                + np.cos(la[:, None]) * np.cos(la[None]) * np.sin((lo[:, None] - lo[None]) / 2) ** 2
            )
        )
    )


def main():
    t0 = time.time()
    rp = _mc.rng(5, 0)
    lat, lon = rp.uniform(36, 43.8, N), rp.uniform(-9.3, 3.3, N)
    D = distancias(lat, lon)
    vecinos = float(((D <= RADIO).sum(1) - 1).mean())
    res = []
    X1 = np.ones((N, 1))
    for i, lam in enumerate(LAMBDAS):
        Lc = np.linalg.cholesky(np.exp(-D / lam) + 1e-10 * np.eye(N))
        for j, beta in enumerate(BETAS):
            rr = _mc.rng(5, 1, i, j)
            b, cc, ch, rc, rh, neg, vc, vh = ([] for _ in range(8))
            for _ in range(R):
                x = 0.9 * Lc @ rr.normal(0, 1, N) + 0.45 * rr.normal(0, 1, N)
                e = 0.9 * Lc @ rr.normal(0, 1, N) + 0.45 * rr.normal(0, 1, N)
                y = 1 + beta * x + e
                X = np.column_stack([x, X1])
                with np.errstate(invalid="ignore"):
                    c = econ.conley(y, X, lat, lon, RADIO)  # el núcleo uniforme puede dar varianza negativa → EE NaN (no cubre)
                neg.append(c["V"][0, 0] < 0)
                vc.append(c["V"][0, 0])
                h = econ.ols(y, X)
                b.append(c["b"][0])
                vh.append(h["V"][0, 0])
                cc.append(abs(c["b"][0] - beta) <= 1.96 * c["se"][0])
                ch.append(abs(h["b"][0] - beta) <= 1.96 * h["se"][0])
                rc.append(abs(c["b"][0]) > 1.96 * c["se"][0])
                rh.append(abs(h["b"][0]) > 1.96 * h["se"][0])
            nulo = beta == 0
            clave = "tamano" if nulo else "potencia"
            fila = {
                "diseno": f"lambda_{lam}km",
                "lambda_km": lam,
                "beta": beta,
                "conley": _mc.resumen(b, beta, cc, rc, nulo),
                "hc1": {**_mc.cobertura(ch), clave: float(np.mean(rh))},
                "frac_var_conley_negativa": float(np.mean(neg)),
                "var_conley_media/var_mc_b": float(np.mean(vc) / np.var(b, ddof=1)),
                "var_hc1_media/var_mc_b": float(np.mean(vh) / np.var(b, ddof=1)),
            }
            fila["conley_apto"] = _mc.apto(fila["conley"]["cobertura95"], fila["conley"].get("tamano"))
            res.append(fila)
            print(fila["diseno"], beta, fila["conley"]["cobertura95"], fila["hc1"]["cobertura95"], flush=True)
    ok = [f["lambda_km"] for f in res if f["conley_apto"]]
    cumple = sorted({lam for lam in LAMBDAS if all(f["conley_apto"] for f in res if f["lambda_km"] == lam)})
    veredicto = "APTO" if len(cumple) == len(LAMBDAS) else ("APTO CON CONDICIÓN" if cumple else "NO APTO")
    condicion = "; ".join(
        f"lambda={f['lambda_km']} km, beta={f['beta']}: cobertura Conley {f['conley']['cobertura95']:.3f} "
        f"(HC1 {f['hc1']['cobertura95']:.3f})"
        for f in res
    ) + (
        f". Cumple con lambda ∈ {cumple} km."
        if cumple and ok
        else f". Con {N} puntos y ~{vecinos:.0f} vecinos por radio el estimador infraestima la varianza (residuos estimados y "
        "núcleo truncado): no cumple en ningún diseño."
    )
    dgp = {
        "N": N,
        "radio_km": RADIO,
        "lambdas_km": LAMBDAS,
        "betas": BETAS,
        "R": R,
        "vecinos_medios_en_radio": vecinos,
        "descripcion": __doc__,
    }
    print(_mc.guardar("conley", dgp, res, veredicto, condicion, t0))


if __name__ == "__main__":
    main()
