"""M1 · Monte Carlo de la adenda A5 del pre-registro (antes de estimar). Solo datos simulados, SEED=20261019, R = 500.

1. AKM0 en el apilado de 3 periodos con shocks PERSISTENTES entre periodos (g_o,t = ρ·g_o,t−1 + ruido, ρ ∈ {0,6; −0,5}) y
   componente no observado de origen también persistente (ν_o,t con el mismo ρ), O = 40 orígenes muy concentrados (≈ 15
   efectivos) y cuotas comunes a los periodos. Se compara AKM0 sin agrupar con AKM0 agrupando por origen entre periodos.
2. MC2E con dos endógenas (x_p, x_p−1) y dos instrumentos (z_p, z_p−1) de econ.iv2sls_k, con corr(z_p, z_p−1) ≈ 0,5 y ≈ 0,8,
   52 provincias × 2 periodos, CR1 por provincia: sesgo y cobertura del efecto de corto plazo (β1) y de largo plazo (β1 + β2).
Veredicto: APTO si cobertura ∈ [0,92; 0,98] y tamaño ≤ 0,08.
"""
from __future__ import annotations

import json

import numpy as np
from scipy import stats

import _mc
import econ
from bhj import apilar, cuotas

R = 500


def akm0_persistente(rho: float, beta: float, agrupar: bool, rs) -> dict:
    S, e, ccaa = cuotas(_mc.rng(7, 1), 40, 0.6)
    T = 3
    Sb, W, _, _ = apilar(S, e, ccaa, T)
    O = S.shape[1]
    grupos = np.tile(np.arange(O), T)
    sig = np.sqrt(np.mean((Sb ** 2).sum(1)))
    cubre, rech, hhi = [], [], []
    for _ in range(R):
        g = np.zeros((T, O))
        nu = np.zeros((T, O))
        g[0], nu[0] = rs.normal(size=O), rs.normal(size=O)
        for t in range(1, T):
            g[t] = rho * g[t - 1] + np.sqrt(1 - rho ** 2) * rs.normal(size=O)
            nu[t] = rho * nu[t - 1] + np.sqrt(1 - rho ** 2) * rs.normal(size=O)
        g, nu = g.ravel() / sig, nu.ravel() / sig
        mu = 0.5 * nu + np.sqrt(0.75) * rs.normal(size=g.size) / sig
        n = Sb.shape[0]
        eta = rs.normal(0, 0.5, n)
        v = 0.5 * eta + np.sqrt(0.75) * rs.normal(0, 0.5, n)
        z = Sb @ g
        x = 2 * z + Sb @ mu + v
        y = beta * x + Sb @ nu + eta + W @ np.linspace(0.2, 1.0, W.shape[1])
        a = econ.akm0(y, x, Sb, g, W, beta0=beta, grupos=grupos if agrupar else None)
        a0 = econ.akm0(y, x, Sb, g, W, beta0=0.0, grupos=grupos if agrupar else None) if beta != 0 else a
        cubre.append(a["p"] > 0.05)
        rech.append(a0["p"] <= 0.05)
        hhi.append(a["hhi_inv"])
    return {"rho": rho, "beta": beta, "agrupado_por_origen": agrupar, "cobertura": float(np.mean(cubre)),
            "rechazo_beta0": float(np.mean(rech)), "orig_efectivos_1_hhi": float(np.mean(hhi)), "R": R}


def dos_endogenas(corr: float, rs) -> dict:
    L = 52
    b1, b2 = 0.3, 0.4   # corto plazo y ajuste del periodo previo; largo plazo = 0,7
    est1, est_lp, cub1, cub_lp, f1 = [], [], [], [], []
    for _ in range(R):
        z_prev = rs.normal(size=(L, 1))
        z_now = corr * z_prev + np.sqrt(1 - corr ** 2) * rs.normal(size=(L, 1))
        Z = np.hstack([z_now, z_prev])
        Zs = np.vstack([Z, rs.normal(size=(L, 2))])          # segundo periodo con instrumentos nuevos
        Zs[L:, 1] = Z[:, 0]                                   # el retardo del 2.º periodo es el instrumento del 1.º
        n = 2 * L
        u = rs.normal(size=n)
        v1 = 0.5 * u + rs.normal(size=n)
        v2 = 0.5 * u + rs.normal(size=n)
        x1 = Zs[:, 0] + v1
        x2 = Zs[:, 1] + v2
        y = b1 * x1 + b2 * x2 + u
        W = np.column_stack([np.r_[np.ones(L), np.zeros(L)], np.r_[np.zeros(L), np.ones(L)]])
        prov = np.tile(np.arange(L), 2)
        r = econ.iv2sls_k(y, np.column_stack([x1, x2]), Zs, W, prov)
        tcrit = stats.t.ppf(0.975, L - 1)
        est1.append(r["b"][0])
        cub1.append(abs(r["b"][0] - b1) <= tcrit * r["se"][0])
        lp = r["b"][0] + r["b"][1]
        se_lp = np.sqrt(r["V"][0, 0] + r["V"][1, 1] + 2 * r["V"][0, 1])
        est_lp.append(lp)
        cub_lp.append(abs(lp - (b1 + b2)) <= tcrit * se_lp)
        f1.append(min(r["F_sw"]))
    return {"corr_instrumentos": corr, "sesgo_corto": float(np.mean(est1) - b1), "cobertura_corto": float(np.mean(cub1)),
            "sesgo_largo": float(np.mean(est_lp) - (b1 + b2)), "cobertura_largo": float(np.mean(cub_lp)),
            "F_SW_min_medio": float(np.mean(f1)), "R": R}


def main() -> int:
    filas = []
    for i, (rho, beta, agr) in enumerate([(r, b, a) for r in (0.6, -0.5) for b in (0.0, 0.5) for a in (False, True)]):
        filas.append(akm0_persistente(rho, beta, agr, _mc.rng(71, i)))
    dos = [dos_endogenas(c, _mc.rng(72, i)) for i, c in enumerate((0.5, 0.8))]
    ok = lambda c: _mc.COB_MIN <= c <= _mc.COB_MAX  # noqa: E731
    v_akm0 = "APTO" if all(ok(f["cobertura"]) for f in filas if f["agrupado_por_origen"]) else "NO APTO"
    v_dos = {d["corr_instrumentos"]: ("APTO" if ok(d["cobertura_corto"]) and ok(d["cobertura_largo"]) else "NO APTO") for d in dos}
    res = {"akm0_persistente": filas, "veredicto_akm0_agrupado": v_akm0, "iv_dos_endogenas": dos, "veredicto_iv_dos": v_dos}
    o = _mc.OUT_MC / "adenda_a5"
    o.mkdir(parents=True, exist_ok=True)
    (o / "resultado.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
