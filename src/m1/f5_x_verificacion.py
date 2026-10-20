"""M1-F5 · VERIFICACIÓN A POSTERIORI (tras el cierre; no pre-registrada). No cambia ninguna clasificación. SOLO con la puerta prereg-m1.

1. Efecto mínimo detectable (EMD) al 80 % de potencia y 5 % bilateral: EMD = (z_0,975 + z_0,80) · EE = 2,80 · EE, con el error
   típico de la inferencia de cada hipótesis (P1 y P2: BHJ al nivel del shock y, como contraste, agrupado por provincia; P1-E4: por
   celda; P3: por comunidad; P5: por país). Es una aproximación normal: con pocos grupos y primera etapa débil la potencia real es
   menor (docs/montecarlo.md), así que el EMD es una cota inferior de lo detectable.
2. Intervalos de Anderson-Rubin (robustos a instrumento débil; test agrupado por provincia, comunidad o país de la forma reducida
   con β impuesto) junto al conjunto AKM0 (al nivel del shock). P1-E4 no tiene instrumento: AR no aplica.
3. F efectivo de Montiel Olea y Pflueger (2013): con un instrumento es el F de Wald robusto (agrupado) de la primera etapa; valor
   crítico para un sesgo de Nagar del 10 % del peor caso al 5 %: 23,1 (K = 1; con τ = 20 %, 15,1). Se compara con el F agrupado por
   provincia y con el F al nivel del shock (BHJ).
4. Curva de especificaciones: las 32 especificaciones del multiverso de P1 con cada una de las tres lecturas del control de cuotas
   incompletas («bhj», principal; «original», el error; «cuota_1998», la lectura literal del texto original).
5. Quitar una comunidad autónoma (todas las hipótesis de P1 y P2 y P3-educación); en P5, quitar un país (análogo europeo). P1-E4
   usa celdas nacionales sin dimensión geográfica: no aplica.
Salidas: output/f5/x_verificacion/resultado.json, output/f5/x_verificacion_{emd,curva,sin_ccaa}.csv; cifras F5V_* (capa C4).
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import etiquetas  # noqa: E402
import f5_p1_shiftshare as p1  # noqa: E402
from comun import OUT, Cifras, escribir_resultado  # noqa: E402
from territorio import PROV  # noqa: E402

O = OUT / "f5"
K_EMD = 1.959964 + 0.841621
CRIT_MOP = {"tau_10": 23.109, "tau_20": 15.062}
HIP = {"P1-H1": "tasa_empleo", "P1-H2": "tasa_paro", "P1-E1": "tasa_actividad", "P1-E2": "log_ocupados",
       "P1-E3a": "tasa_empleo_educ_baja", "P1-E3b": "tasa_empleo_educ_media", "P1-E3c": "tasa_empleo_educ_alta",
       "P1-E6": "log_pob_nativos", "P2-E1": "cuota_nomanual", "P2-E2": "cuota_alta_cualif"}
CURVA = ("P1-H1", "P1-H2", "P1-E3a")


def _fin(v):
    return None if v is None or pd.isna(v) or not np.isfinite(v) else float(v)


def ar_p1(d, spec, y):
    m = d[f"d_{y}"].notna().to_numpy() & d.x.notna().to_numpy()
    dd = d[m]
    W = p1.W_de(dd, spec)
    w = dd.pob0.to_numpy(float) if spec["pesos"] else None
    yv, xv, z = dd[f"d_{y}"].to_numpy(float), dd.x.to_numpy(float), dd.z.to_numpy(float)
    iv = econ.iv2sls(yv, xv, z, W, dd.prov.to_numpy(), w)
    b, s = iv["b"][0], iv["se"][0]
    return econ.ar_conjunto(yv, xv, z, W, dd.prov.to_numpy(), w, rejilla=np.linspace(b - 40 * s, b + 40 * s, 4001))


def datos_p1():
    P, E, c = p1.padron(), p1.ecp(), p1.epa_nativos()
    Y = p1.resultados_nativos(c)
    Y["log_pob_nativos"] = np.log((E["Total"] - E["Extranjero"]).reindex(Y.index))
    ctrl0, bart, paro = p1.controles(c)
    return P, E, Y, (ctrl0, bart), paro


def datos_p3():
    import f5_p3_servicios as p3
    r, pob, z = p3.ratios(), p3.poblacion_5_19(), p3.instrumento()
    d = r.merge(pob, on=["ccaa", "anio"]).sort_values(["ccaa", "anio"])
    d = d[~d.ccaa.isin(["18", "19"])]
    d["pob0"] = d.groupby("ccaa").Total.shift(1)
    d["x"] = d.groupby("ccaa").Extranjero.diff() / d.pob0
    d["dy"] = d.groupby("ccaa").alumnos_profesor.diff()
    d = d.merge(z, on=["ccaa", "anio"], how="left")
    d["z"] = d.shift_share / d.pob0
    return d.dropna(subset=["x", "dy", "z"]).reset_index(drop=True)


def est_simple(d, cl_col, fe_col, w_col, zcol="z", B=9999):
    """MC2E con un instrumento y efectos fijos: β, EE agrupado, F efectivo (MOP, K = 1), AR y p del wild bootstrap de la forma reducida."""
    niv = sorted(d[fe_col].unique())
    W = np.column_stack([np.ones(len(d))] + [(d[fe_col] == a).astype(float).to_numpy() for a in niv[1:]])
    y, x, z, cl, w = (d.dy.to_numpy(float), d.x.to_numpy(float), d[zcol].to_numpy(float), d[cl_col].to_numpy(),
                      d[w_col].to_numpy(float))
    iv = econ.iv2sls(y, x, z, W, cl, w)
    b, s = float(iv["b"][0]), float(iv["se"][0])
    ar = econ.ar_conjunto(y, x, z, W, cl, w, rejilla=np.linspace(b - 40 * s, b + 40 * s, 4001))
    out = {"b": b, "se": s, "F_efectivo": econ.f_efectivo(x, z, W, cl, w), "ar": ar, "n": len(d), "G": int(d[cl_col].nunique())}
    if B:
        out["p_wcb"] = econ.wcr_boot(y, np.column_stack([z, W]), 0, cl, B=B, w=w)["p"]
    return out


def datos_p5():
    import f5_p5_europa as p5
    N, pob = p5.censo()
    g_loo, _ = p5.shocks(N)
    d = p5.lfs().join(pob.rename("pob_censo"), how="inner").dropna()
    d = d[d.index.isin(N.index)]
    d["pais"] = d.index.str[:2]
    Nd = N.loc[d.index]
    d["z"] = [(Nd.loc[r] * g_loo.loc[r[:2]].reindex(Nd.columns).fillna(0)).sum() / d.loc[r, "pob_censo"] for r in d.index]
    return d.reset_index(drop=True)


def frase(lo, hi, unidad):
    """Lectura del intervalo como «se descartan / no se pueden descartar» (sin lenguaje causal: β es una asociación)."""
    if lo is None and hi is None:
        return "el conjunto de confianza es toda la recta: no se descarta ningún valor de β"
    if lo is None:
        return f"se descartan valores de β mayores que {hi:.2f} {unidad}; no se pueden descartar valores negativos de cualquier tamaño"
    if hi is None:
        return f"se descartan valores de β menores que {lo:.2f} {unidad}; no se pueden descartar valores positivos de cualquier tamaño"
    return (f"con inferencia agrupada quedarían fuera los valores de β menores que {lo:.2f} o mayores que {hi:.2f} {unidad}; no se pueden "
            f"descartar los valores entre {lo:.2f} y {hi:.2f}")


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    cf = Cifras("f5_x_verificacion", "src/m1/f5_x_verificacion.py")
    P, E, Y, ctrl, paro = datos_p1()
    spec = p1.PRINCIPAL
    d, S, g, grupos, _, _ = p1.panel(spec, P, E, Y, ctrl, paro)
    filas = []
    # ── 1-3: EMD, AR, F efectivo ─────────────────────────────────────────────────────────────────────────────────────────
    for h, y in HIP.items():
        r = p1.estimar(d, S, g, grupos, spec, y)
        ar = ar_p1(d, spec, y)
        conj = r["akm0_conjunto"]
        filas.append({"hipotesis": h, "b": r["b"], "se_inferencia": r["se_bhj"], "tipo_se": "BHJ (shock)", "se_alternativo": r["se_cluster_prov"],
                      "emd": K_EMD * r["se_bhj"], "emd_alternativo": K_EMD * r["se_cluster_prov"],
                      "ar_inf": _fin(ar["inf"]), "ar_sup": _fin(ar["sup"]), "ar_acotado": ar["acotado"], "ar_convexo": ar.get("convexo"),
                      "akm0_conjunto": json.dumps(conj), "akm0_acotado": r["akm0_acotado"], "F_efectivo_MOP": r["F_efectivo"],
                      "F_shock": r["F_shock"], "unidad": "pp por pp" if not y.startswith("log") else "log por pp"})
    p3d = datos_p3()
    r3 = est_simple(p3d, "ccaa", "anio", "pob0")
    pp = lambda v: None if _fin(v) is None else v / 100  # noqa: E731   tratamiento en tasa: se expresa por punto porcentual
    filas.append({"hipotesis": "P3-educacion", "b": r3["b"] / 100, "se_inferencia": r3["se"] / 100, "tipo_se": "agrupado por comunidad (17)",
                  "emd": K_EMD * r3["se"] / 100, "ar_inf": pp(r3["ar"]["inf"]), "ar_sup": pp(r3["ar"]["sup"]), "ar_acotado": r3["ar"]["acotado"],
                  "ar_convexo": r3["ar"].get("convexo"), "F_efectivo_MOP": r3["F_efectivo"], "unidad": "alumnos por profesor por pp"})
    p5d = datos_p5()
    r5 = est_simple(p5d, "pais", "pais", "pob2064")
    filas.append({"hipotesis": "P5", "b": r5["b"], "se_inferencia": r5["se"], "tipo_se": f"agrupado por país ({r5['G']})", "emd": K_EMD * r5["se"],
                  "ar_inf": _fin(r5["ar"]["inf"]), "ar_sup": _fin(r5["ar"]["sup"]), "ar_acotado": r5["ar"]["acotado"],
                  "ar_convexo": r5["ar"].get("convexo"), "F_efectivo_MOP": r5["F_efectivo"], "unidad": "pp por pp"})
    import f5_p1e4_borjas as e4
    de = e4.salarios().merge(e4.cuotas(), on=["anio", "educ", "edad_t"], how="inner")
    de["celda"] = de.educ + "|" + de.edad_t
    de = de[(de.n_ees >= 50) & (de.n_act >= 50)]
    r4 = e4.regresion(de, "cuota_fuera")
    filas.append({"hipotesis": "P1-E4", "b": r4["b"], "se_inferencia": r4["se_cluster"], "tipo_se": "agrupado por celda (15)",
                  "emd": K_EMD * r4["se_cluster"], "ar_inf": r4["b"] - 1.96 * r4["se_cluster"], "ar_sup": r4["b"] + 1.96 * r4["se_cluster"],
                  "ar_acotado": True, "nota": "sin instrumento: AR no aplica; intervalo MCO agrupado (orientativo, 15 celdas)",
                  "unidad": "Δ log salario por unidad de cuota"})
    emd = pd.DataFrame(filas)
    emd["supera_mop_10"] = emd.F_efectivo_MOP >= CRIT_MOP["tau_10"]
    emd["lectura"] = [frase(_fin(r.ar_inf), _fin(r.ar_sup), r.unidad) for r in emd.itertuples()]
    emd.to_csv(O / "x_verificacion_emd.csv", index=False)
    for r in emd.itertuples():
        k = r.hipotesis.replace("-", "_")
        cf.add(f"F5V_EMD_{k}", round(r.emd, 3), r.unidad, f"{r.hipotesis}: efecto mínimo detectable al 80 % de potencia y 5 % bilateral "
               f"(2,80 × EE {r.tipo_se}; aproximación normal, cota inferior de lo detectable; verificación a posteriori)", "C4",
               "M1 fase 5", "—", "—", "—")
        if r.hipotesis != "P1-E4":
            cf.add(f"F5V_AR_{k}", round(r.b, 4), r.unidad, f"{r.hipotesis}: estimación e intervalo de Anderson-Rubin al 95 % (test agrupado de la "
                   "forma reducida; vacío en un extremo = no acotado; verificación a posteriori)", "C4", "M1 fase 5", "—", "—", "—",
                   ic_inf=round(r.ar_inf, 4) if r.ar_inf is not None and np.isfinite(r.ar_inf) else np.nan,
                   ic_sup=round(r.ar_sup, 4) if r.ar_sup is not None and np.isfinite(r.ar_sup) else np.nan)
            cf.add(f"F5V_FMOP_{k}", round(r.F_efectivo_MOP, 1), "F", f"{r.hipotesis}: F efectivo de Montiel Olea-Pflueger (un instrumento: F de "
                   "Wald agrupado de la primera etapa); valor crítico 23,1 para un sesgo del 10 % del peor caso al 5 %", "C4", "M1 fase 5",
                   "—", "—", "—")
    cf.add("F5V_MOP_CRIT_10", CRIT_MOP["tau_10"], "F", "Valor crítico del F efectivo de Montiel Olea-Pflueger con un instrumento (τ = 10 %, "
           "5 %)", "C4", "Montiel Olea y Pflueger (2013)", "—", "—", "—")
    # ── 4: curva de especificaciones con las tres lecturas del control ────────────────────────────────────────────────────
    ejes = {"base": [1998, 2002], "solo_extranjera": [True, False], "pesos": [True, False], "controles": ["completo", "basico"],
            "muestra": [50, 52]}
    curva = []
    for cc in ("bhj", "original", "cuota_1998"):
        for comb in itertools.product(*ejes.values()):
            sp = {**spec, **dict(zip(ejes, comb)), "control_cuotas": cc}
            dd, SS, gg, gr, _, _ = p1.panel(sp, P, E, Y, ctrl, paro)
            for h in CURVA:
                r = p1.estimar(dd, SS, gg, gr, sp, HIP[h])
                curva.append({**{k: sp[k] for k in ejes}, "control_cuotas": cc, "hipotesis": h, "b": r["b"], "akm0_p": r["akm0_p"],
                              "akm0_acotado": r["akm0_acotado"], "F_shock": r["F_shock"], "F_efectivo": r["F_efectivo"]})
    cu = pd.DataFrame(curva)
    cu.to_csv(O / "x_verificacion_curva.csv", index=False)
    rc = cu.groupby(["hipotesis", "control_cuotas"]).agg(b_med=("b", "median"), b_min=("b", "min"), b_max=("b", "max"),
                                                       neg=("b", lambda s: int((s < 0).sum())), rechaza=("akm0_p", lambda s: int((s < 0.05).sum())),
                                                       n=("b", "size"), F_med=("F_shock", "median"))
    for (h, cc), r in rc.iterrows():
        cf.add(f"F5V_CURVA_{h.replace('-', '_')}_{cc.upper()}", round(float(r.b_med), 2), "pp por pp", f"{h}, control de cuotas «{cc}»: mediana "
               f"de β en {int(r.n)} especificaciones (intervalo: mínimo y máximo; {int(r.neg)} negativas; AKM0 rechaza al 5 % sin ajuste en "
               f"{int(r.rechaza)}; verificación a posteriori)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España",
               clasificacion="ASOCIACIÓN", ic_inf=round(float(r.b_min), 2), ic_sup=round(float(r.b_max), 2))
    # ── 5: quitar una comunidad autónoma (P1, P2, P3) y un país (P5) ──────────────────────────────────────────────────────
    ccaa = d.prov.map(lambda p: PROV[p][1])
    sin = []
    for k in sorted(ccaa.unique()):
        m = (ccaa != k).to_numpy()
        for h, y in HIP.items():
            r = p1.estimar(d[m].reset_index(drop=True), S[m], g, grupos, spec, y)
            sin.append({"excluida": k, "hipotesis": h, "b": r["b"], "akm0_p": r["akm0_p"], "acotado": r["akm0_acotado"],
                        "F_shock": r["F_shock"]})
    for k in sorted(p3d.ccaa.unique()):
        r = est_simple(p3d[p3d.ccaa != k].reset_index(drop=True), "ccaa", "anio", "pob0", B=1999)
        sin.append({"excluida": k, "hipotesis": "P3-educacion", "b": r["b"] / 100, "p_wcb": r["p_wcb"], "F_shock": np.nan,
                    "F_efectivo": r["F_efectivo"]})
    for k in sorted(p5d.pais.unique()):
        x = p5d[p5d.pais != k].reset_index(drop=True)
        r = est_simple(x, "pais", "pais", "pob2064", B=1999)
        sin.append({"excluida": k, "hipotesis": "P5", "b": r["b"], "p_wcb": r["p_wcb"], "F_efectivo": r["F_efectivo"]})
    sc = pd.DataFrame(sin)
    sc.to_csv(O / "x_verificacion_sin_ccaa.csv", index=False)
    base = emd.set_index("hipotesis").b
    sc["cambia_signo"] = (np.sign(sc.b) != np.sign(sc.hipotesis.map(base))).astype(int)
    rs = sc.groupby("hipotesis").agg(b_min=("b", "min"), b_max=("b", "max"), n=("b", "size"), cambia_signo=("cambia_signo", "sum"),
                                     rechaza=("akm0_p", lambda s: int((s < 0.05).sum())),
                                     rechaza_wcb=("p_wcb", lambda s: int((s < 0.05).sum())))
    for h, r in rs.iterrows():
        cf.add(f"F5V_SINCCAA_{h.replace('-', '_')}", round(float(base[h]), 3), "pp por pp" if h != "P3-educacion" else "alumnos por profesor por pp",
               f"{h}: estimación principal e intervalo entre mínimo y máximo al excluir {'un país' if h == 'P5' else 'una comunidad autónoma'} "
               f"cada vez ({int(r.n)} exclusiones; cambia de signo en {int(r.cambia_signo)}; verificación a posteriori)", "C4", "M1 fase 5",
               "—", "—", "—", clasificacion="ASOCIACIÓN", ic_inf=round(float(r.b_min), 3), ic_sup=round(float(r.b_max), 3))
    escribir_resultado(O / "x_verificacion" / "resultado.json", pregunta="Verificación a posteriori: EMD, Anderson-Rubin, F de Montiel "
                       "Olea-Pflueger, curva de especificaciones y quitar una comunidad", capa="C4", clasificacion="ASOCIACIÓN",
                       datos="los de la fase 5", N=int(len(d)), metodo="ver docstring de src/m1/f5_x_verificacion.py", estimacion=None,
                       ic95=[None, None], p_ajustado=None, diagnosticos={"emd": emd.to_dict("records"), "curva": rc.reset_index().to_dict("records"),
                                                                        "sin_ccaa": rs.reset_index().to_dict("records")},
                       notas="No pre-registrado; no cambia ninguna clasificación.", prereg=f"prereg-m1 {commit}")
    cf.escribir()
    pd.set_option("display.width", 220)
    print(emd.drop(columns=["akm0_conjunto", "lectura"]).round(3).to_string())
    print(rc.round(3).to_string())
    print(rs.round(3).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
