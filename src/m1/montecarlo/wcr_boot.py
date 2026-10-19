"""M1 · Monte Carlo de econ.wcr_boot (wild cluster bootstrap restringido, pesos de Webb) frente a CR1 con t(G-1).

DGP (declarado antes de simular; se redibuja todo en cada réplica salvo el número de clusters):
- G ∈ {17, 52} clusters (CCAA, provincias) de tamaños muy heterogéneos: N_g = redondeo(exp(N(log 40, 1))) acotado a [5, 400].
- Tratamiento al nivel del cluster: «asimetrico» (pocos clusters de alto apalancamiento) x_g = (exp(N(0,1)) - e^{1/2}) / DE, o
  «normal» x_g ~ N(0,1); x_ig = x_g + 0,3·N(0,1); un control individual c_ig ~ N(0,1).
- Error u_ig = a_g + e_ig con a_g ~ N(0, 1)·(0,5 + |x_g|) (heterocedasticidad ligada al apalancamiento) y e_ig ~ N(0, 1).
- y_ig = 1 + beta·x_ig + 0,5·c_ig + u_ig; beta = 0 (tamaño) y beta = 0,5 (potencia). H0: beta = 0 al 5 %.
- wcr_boot con B = 399 dentro del MC (con B = 9999 en la aplicación) y semilla distinta por réplica (SEED + r).
"""

from __future__ import annotations

import time

import numpy as np
from scipy import stats

import _mc
import econ

R, B = 500, 399
DISENOS = ((17, "asimetrico"), (17, "normal"), (52, "asimetrico"), (52, "normal"))  # (G, distribución de x_g)
BETAS = (0.0, 0.5)


def una(rg, G, beta, dist="asimetrico"):
    Ng = np.clip(np.round(np.exp(rg.normal(np.log(40), 1.0, G))), 5, 400).astype(int)
    cl = np.repeat(np.arange(G), Ng)
    if dist == "asimetrico":
        xg = (np.exp(rg.normal(0, 1, G)) - np.exp(0.5)) / np.sqrt((np.e - 1) * np.e)
    else:
        xg = rg.normal(0, 1, G)
    ag = rg.normal(0, 1, G) * (0.5 + np.abs(xg))
    n = Ng.sum()
    x = xg[cl] + 0.3 * rg.normal(0, 1, n)
    c = rg.normal(0, 1, n)
    y = 1 + beta * x + 0.5 * c + ag[cl] + rg.normal(0, 1, n)
    return y, np.column_stack([x, np.ones(n), c]), cl


def main():
    t0 = time.time()
    res = []
    for i, (G, dist) in enumerate(DISENOS):
        tcrit = stats.t.ppf(0.975, G - 1)
        for j, beta in enumerate(BETAS):
            rr = _mc.rng(3, i, j)
            b, rej_w, rej_c, cub_c = [], [], [], []
            for r in range(R):
                y, X, cl = una(rr, G, beta, dist)
                o = econ.ols(y, X, cl)
                wb = econ.wcr_boot(y, X, 0, cl, B=B, seed=_mc.SEED + 1000 * (2 * i + j) + r)
                b.append(o["b"][0])
                rej_w.append(wb["p"] <= 0.05)
                rej_c.append(abs(o["b"][0] / o["se"][0]) > tcrit)
                cub_c.append(abs(o["b"][0] - beta) <= tcrit * o["se"][0])
            nulo = beta == 0
            clave = "tamano" if nulo else "potencia"
            fila = {
                "diseno": f"G{G}_{dist}",
                "G": G,
                "x_g": dist,
                "beta": beta,
                "B": B,
                "mco": _mc.resumen(b, beta, cub_c, None),
                "wcr_webb": {clave: float(np.mean(rej_w)), "ee_mc": float(np.sqrt(np.mean(rej_w) * (1 - np.mean(rej_w)) / R))},
                "cr1_t(G-1)": {clave: float(np.mean(rej_c)), "ee_mc": float(np.sqrt(np.mean(rej_c) * (1 - np.mean(rej_c)) / R))},
            }
            res.append(fila)
            print(fila["diseno"], beta, fila["wcr_webb"], fila["cr1_t(G-1)"], round(time.time() - t0, 1), flush=True)
    tam = {f["diseno"]: f["wcr_webb"]["tamano"] for f in res if f["beta"] == 0}
    tam_c = {f["diseno"]: f["cr1_t(G-1)"]["tamano"] for f in res if f["beta"] == 0}
    # El WCR no da IC directamente (se obtendría invirtiendo el test); el criterio aplicable es el tamaño
    # (cobertura implícita = 1 - tamaño del test en el valor verdadero).
    ok = {G: _mc.apto(1 - t, t) for G, t in tam.items()}
    veredicto = "APTO" if all(ok.values()) else ("APTO CON CONDICIÓN" if any(ok.values()) else "NO APTO")
    condicion = "; ".join(f"{k}: tamaño WCR {tam[k]:.3f} (CR1 t(G-1) {tam_c[k]:.3f}) → {'cumple' if ok[k] else 'falla'}" for k in tam)
    dgp = {"disenos_G_xg": DISENOS, "betas": BETAS, "R": R, "B": B, "descripcion": __doc__}
    print(_mc.guardar("wcr_boot", dgp, res, veredicto, condicion, t0))


if __name__ == "__main__":
    main()
