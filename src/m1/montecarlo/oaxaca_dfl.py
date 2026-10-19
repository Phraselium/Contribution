"""M1 · Monte Carlo de econ.oaxaca y econ.dfl: identidades contables exactas e insesgadez de la parte explicada (composición).

DGP (declarado antes de simular; composición conocida, todo se redibuja en cada réplica):
- n = 4000 con 30 % del grupo A y 70 % del grupo B (grupos genéricos; sin atribuir rasgos a ningún colectivo real).
- Covariables discretas independientes dentro de cada grupo: educación (3 niveles), edad (3 tramos), sexo.
  P(educ | A) = (0,45; 0,35; 0,20), P(educ | B) = (0,25; 0,45; 0,30); P(edad | A) = (0,50; 0,35; 0,15), P(edad | B) = (0,30; 0,40; 0,30);
  P(mujer | A) = 0,45, P(mujer | B) = 0,50. Con esta estructura el logit con efectos principales de DFL está bien especificado.
- «lineal»: y = 2 + 0,3·e2 + 0,7·e3 + 0,2·a2 + 0,35·a3 − 0,15·mujer − 0,10·A + error, error ~ N(0, (0,4 + 0,2·e3)²).
  Verdad: explicada = (E[x|A] − E[x|B])·b (poblacional); no explicada = −0,10.
- «lineal_pesos»: igual, pero la muestra sobrerrepresenta educación alta (probabilidad ×2) y se usan pesos 1/probabilidad.
- «heterogeneo»: A tiene la mitad de rendimiento educativo (0,15; 0,35). Verdad de composición con estructura de B:
  (E[x|A] − E[x|B])·b_B. DFL debe ser insesgado; Oaxaca con coeficientes agrupados estima otra cantidad (se informa, no se exige).
- Cuantiles de DFL: verdad por simulación grande (2·10⁶) de la distribución contrafactual (composición de A, estructura de B).
- Criterio (las herramientas no dan EE, así que no hay cobertura): identidades con error < 1e-10 y |sesgo| < max(3·EE_MC; 2 % de |verdad|).
"""

from __future__ import annotations

import time

import numpy as np

import _mc
import econ
from comun import cuantil_pond

R, N, PA = 500, 4000, 0.30
P = {
    "A": {"educ": (0.45, 0.35, 0.20), "edad": (0.50, 0.35, 0.15), "mujer": 0.45},
    "B": {"educ": (0.25, 0.45, 0.30), "edad": (0.30, 0.40, 0.30), "mujer": 0.50},
}
B_COEF = np.array([0.3, 0.7, 0.2, 0.35, -0.15])
DELTA = -0.10
QS = (0.1, 0.25, 0.5, 0.75, 0.9)
DISENOS = ("lineal", "lineal_pesos", "heterogeneo")


def covariables(rg, g, n):
    e = rg.choice(3, n, p=P[g]["educ"])
    a = rg.choice(3, n, p=P[g]["edad"])
    m = rg.random(n) < P[g]["mujer"]
    return np.column_stack([e == 1, e == 2, a == 1, a == 2, m]).astype(float)


def resultado(rg, X, A, diseno):
    b = np.tile(B_COEF, (len(A), 1))
    if diseno == "heterogeneo":
        b[A, 0:2] *= 0.5
    sd = 0.4 + 0.2 * X[:, 1]
    return 2 + (X * b).sum(1) + DELTA * A + sd * rg.normal(0, 1, len(A))


def media_x(g):
    p = P[g]
    return np.array([p["educ"][1], p["educ"][2], p["edad"][1], p["edad"][2], p["mujer"]])


def muestra(rg, diseno):
    if diseno != "lineal_pesos":
        nA = rg.binomial(N, PA)
        XA, XB = covariables(rg, "A", nA), covariables(rg, "B", N - nA)
        X = np.vstack([XA, XB])
        A = np.r_[np.ones(nA, bool), np.zeros(N - nA, bool)]
        return X, A, None
    # muestreo desigual: se genera una población de 3N y se retiene con probabilidad 0,25 (×2 si educación alta)
    M = 3 * N
    nA = rg.binomial(M, PA)
    X = np.vstack([covariables(rg, "A", nA), covariables(rg, "B", M - nA)])
    A = np.r_[np.ones(nA, bool), np.zeros(M - nA, bool)]
    pr = np.where(X[:, 1] == 1, 0.5, 0.25)
    k = rg.random(M) < pr
    return X[k], A[k], 1 / pr[k]


def verdad_cuantiles(diseno):
    rg = _mc.rng(6, 9, DISENOS.index(diseno))
    M = 2_000_000
    XB, XC = covariables(rg, "B", M), covariables(rg, "A", M)
    yB = resultado(rg, XB, np.zeros(M, bool), diseno)
    yC = resultado(rg, XC, np.zeros(M, bool), diseno)  # composición de A, estructura de B
    return {q: float(np.quantile(yC, q) - np.quantile(yB, q)) for q in QS}


def main():
    t0 = time.time()
    dx = media_x("A") - media_x("B")
    out = {"oaxaca": [], "dfl": []}
    for d, diseno in enumerate(DISENOS):
        verdad_expl = float(dx @ B_COEF)
        bA = B_COEF.copy()
        if diseno == "heterogeneo":
            bA[0:2] *= 0.5
        verdad_brecha = float(media_x("A") @ bA - media_x("B") @ B_COEF + DELTA)
        vq = verdad_cuantiles(diseno)
        rr = _mc.rng(6, d)
        ox_e, ox_u, ox_sc, df_m, id_ox, id_df, dq = [], [], [], [], [], [], {q: [] for q in QS}
        for _ in range(R):
            X, A, w = muestra(rr, diseno)
            y = resultado(rr, X, A, diseno)
            o = econ.oaxaca(y, X, A, w)
            o2 = econ.oaxaca(y, np.column_stack([np.ones(len(y)), X]), A, w)
            ox_e.append(o["explicada"])
            ox_u.append(o["no_explicada"])
            ox_sc.append(abs(o["explicada"] - o2["explicada"]))
            ww = np.ones(len(y)) if w is None else w
            brecha = np.average(y[A], weights=ww[A]) - np.average(y[~A], weights=ww[~A])
            id_ox.append(
                max(
                    abs(o["explicada"] + o["no_explicada"] - o["brecha"]),
                    abs(o["por_variable"].sum() - o["explicada"]),
                    abs(o["brecha"] - brecha),
                )
            )
            f = econ.dfl(y, X, A, w, cuantiles=QS)
            df_m.append(f["media"]["composicion"])
            id_df.append(max(abs(v["composicion"] + v["resto"] - v["brecha"]) for v in f.values()))
            for q in QS:
                dq[q].append(f[q]["composicion"])
                id_df[-1] = max(id_df[-1], abs(f[q]["brecha"] - (cuantil_pond(y[A], ww[A], q) - cuantil_pond(y[~A], ww[~A], q))))
        fo = {
            "diseno": diseno,
            "verdad_brecha": verdad_brecha,
            "explicada": _mc.resumen(ox_e, verdad_expl),
            "no_explicada": _mc.resumen(ox_u, verdad_brecha - verdad_expl),
            "max_error_identidades": float(np.max(id_ox)),
            "max_dif_sin_vs_con_constante": float(np.max(ox_sc)),
        }
        fd = {
            "diseno": diseno,
            "composicion_media": _mc.resumen(df_m, verdad_expl),
            "max_error_identidades": float(np.max(id_df)),
            "composicion_cuantiles": {str(q): _mc.resumen(dq[q], vq[q]) for q in QS},
        }
        out["oaxaca"].append(fo)
        out["dfl"].append(fd)
        print(
            diseno,
            fo["explicada"]["sesgo"],
            fd["composicion_media"]["sesgo"],
            fo["max_error_identidades"],
            fd["max_error_identidades"],
            round(time.time() - t0, 1),
            flush=True,
        )

    def insesgado(s):
        return abs(s["sesgo"]) < max(3 * s["de_mc"] / np.sqrt(s["R_validas"]), 0.02 * abs(s["verdad"]))

    for f in out["oaxaca"]:
        f["identidades_ok"] = f["max_error_identidades"] < 1e-10
        f["explicada_insesgada"] = bool(insesgado(f["explicada"]))
    for f in out["dfl"]:
        f["identidades_ok"] = f["max_error_identidades"] < 1e-10
        f["media_insesgada"] = bool(insesgado(f["composicion_media"]))
        f["cuantiles_insesgados"] = {q: bool(insesgado(s)) for q, s in f["composicion_cuantiles"].items()}
    exig = [f for f in out["oaxaca"] if f["diseno"] != "heterogeneo"]
    ok_o = all(f["identidades_ok"] for f in out["oaxaca"]) and all(f["explicada_insesgada"] for f in exig)
    het = next(f for f in out["oaxaca"] if f["diseno"] == "heterogeneo")
    cond_o = (
        "identidades exactas (error máx. "
        + f"{max(f['max_error_identidades'] for f in out['oaxaca']):.1e}); parte explicada "
        + "; ".join(f"{f['diseno']}: sesgo {f['explicada']['sesgo']:+.4f} (verdad {f['explicada']['verdad']:.4f})" for f in out["oaxaca"])
        + ". Con rendimientos heterogéneos la referencia agrupada no coincide con la de B (sesgo frente a b_B "
        + f"{het['explicada']['sesgo']:+.4f}): no es error, es otra referencia; declararla. Sin constante en X ya no hay sesgo "
        + f"(corrección en econ.oaxaca; dif. máx. con/sin constante {max(f['max_dif_sin_vs_con_constante'] for f in out['oaxaca']):.1e})."
    )
    ok_d = all(f["identidades_ok"] and f["media_insesgada"] and all(f["cuantiles_insesgados"].values()) for f in out["dfl"])
    malq = [f"{f['diseno']} q={q}" for f in out["dfl"] for q, v in f["cuantiles_insesgados"].items() if not v]
    cond_d = (
        "identidades exactas (error máx. "
        + f"{max(f['max_error_identidades'] for f in out['dfl']):.1e}); composición en la media "
        + "; ".join(f"{f['diseno']}: sesgo {f['composicion_media']['sesgo']:+.4f}" for f in out["dfl"])
        + (f"; cuantiles con sesgo apreciable: {', '.join(malq)}" if malq else "; cuantiles insesgados en todos los diseños")
        + ". Logit bien especificado por construcción; con covariables continuas o interacciones omitidas hay que validar el logit."
    )
    dgp = {
        "N": N,
        "proporcion_A": PA,
        "probabilidades": P,
        "coeficientes_B": B_COEF,
        "delta": DELTA,
        "disenos": DISENOS,
        "R": R,
        "cuantiles": QS,
        "descripcion": __doc__,
    }
    print(_mc.guardar("oaxaca", dgp, out["oaxaca"], "APTO" if ok_o else "NO APTO", cond_o, t0))
    print(_mc.guardar("dfl", dgp, out["dfl"], "APTO" if ok_d else "NO APTO", cond_d, t0))


if __name__ == "__main__":
    main()
