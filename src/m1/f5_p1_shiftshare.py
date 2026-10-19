"""M1-F5 · P1 y P2: impacto de la inmigración sobre el empleo y las ocupaciones de los nacidos en España por provincia
(shift-share de Card 2001). SOLO con la puerta prereg-m1 abierta (docs/preregistro.md y docs/preregistro_adenda.md).

Especificación principal (adenda A1): 50 provincias; periodos apilados A 2005→2009, B 2009→2015, C 2015→2022; tratamiento =
Δ nacidos fuera de 15-64 (ECP) / población 15-64 inicial (ECP); instrumento z = Σ_o s̃_lo · ΔM_o,p con s̃_lo = cuota de la
provincia en los nacidos en o con nacionalidad extranjera en 1998 / población 15-64 inicial y ΔM_o,p la variación nacional de
nacidos en o (padrón 03006); controles: efectos de periodo, suma de cuotas × periodo, paro inicial de nativos, construcción 2005
× periodo y Bartik sectorial de nativos; pesos: población 15-64 inicial. Inferencia: AKM0 agrupado por origen (APTO), con BHJ,
F al nivel del shock y F efectivo agrupado por provincia como diagnósticos. Pruebas y reglas de clasificación de la adenda A3-A6.
Salidas: output/f5/p1/ y output/f5/p2/ (resultado.json con el campo prereg), Registry en output/f5/registro.csv.
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
from comun import OUT, PROC, SEED, Cifras, Registry, bh, escribir_resultado, holm  # noqa: E402

O = OUT / "f5"
PERIODOS = {"P0": (1998, 2005), "A": (2005, 2009), "B": (2009, 2015), "C": (2015, 2022)}
PRINCIPAL = dict(base=1998, solo_extranjera=True, pesos=True, controles="completo", muestra=50, diseno="apilado",
                 suelo=False, excluir_ue14=False, tratamiento="15-64", loo=False, control_cuotas="bhj")
# control de cuotas incompletas (BHJ): suma de las exposiciones del instrumento, Σ_o s̃_lo = Σ_o cuota_lo / población 15-64 inicial,
# por periodo. La primera versión del código usaba Σ_o cuota_lo sin dividir (error corregido en la cuarta revisión; desviación 13);
# «original» la reproduce y «cuota_1998» usa la lectura literal del pre-registro (nacidos fuera en 1998 / población 1998).
UE14 = ["Alemania", "Austria", "Bélgica", "Dinamarca", "Finlandia", "Francia", "Grecia", "Irlanda", "Italia", "Luxemburgo",
        "Países Bajos", "Portugal", "Suecia", "Reino Unido"]


# ── datos ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def padron() -> pd.DataFrame:
    p = pd.read_csv(PROC / "padron_nacimiento.csv.gz", dtype={"prov": str})
    return p[(p.sexo == "total") & (p.grupo != "España")]


def ecp() -> pd.DataFrame:
    return pd.read_csv(PROC / "ecp_15_64.csv.gz", dtype={"prov": str}).pivot_table(
        index=["prov", "anio"], columns="nacimiento", values="valor")


def epa_nativos() -> pd.DataFrame:
    c = pd.read_csv(PROC / "epa_celdas.csv.gz", dtype={"prov": str})
    c = c[(c.origen_def == "nacimiento") & (c.grupo == "España")]
    return c


def resultados_nativos(c: pd.DataFrame) -> pd.DataFrame:
    a = c[c.edad6 != "65+"]
    g = a.groupby(["prov", "anio"])
    r = pd.DataFrame({"tasa_empleo": g.ocu.sum() / g.pob.sum(), "tasa_paro": g.par.sum() / g.act.sum(),
                      "tasa_actividad": g.act.sum() / g.pob.sum(), "log_ocupados": np.log(g.ocu.sum()),
                      "cuota_nomanual": g.ocu_nomanual.sum() / g.ocu.sum(), "cuota_alta_cualif": g.ocu_alta.sum() / g.ocu.sum()})
    for e in ("baja", "media", "alta"):
        ge = a[a.educ == e].groupby(["prov", "anio"])
        r[f"tasa_empleo_educ_{e}"] = ge.ocu.sum() / ge.pob.sum()
    return r


def controles(c: pd.DataFrame) -> pd.DataFrame:
    s = pd.read_csv(PROC / "epa_sectores.csv.gz", dtype={"prov": str, "sector": str})
    s = s[s.grupo == "España"]
    s05 = s[s.anio == 2005].pivot_table(index="prov", columns="sector", values="ocu", aggfunc="sum").fillna(0)
    cuota = s05.div(s05.sum(1), axis=0)
    out = {"construccion_2005": cuota.get("4", pd.Series(0, index=cuota.index))}
    nat = s.groupby(["anio", "sector"]).ocu.sum().unstack().fillna(0)
    bart = {}
    for k, (a0, a1) in PERIODOS.items():
        if a0 < 2005:
            continue
        crec = (nat.loc[a1] - nat.loc[a0]) / nat.loc[a0].where(nat.loc[a0] > 0)
        bart[k] = (cuota * crec.reindex(cuota.columns).fillna(0)).sum(1)
    a = c[c.edad6 != "65+"]
    g = a.groupby(["prov", "anio"])
    paro = (g.par.sum() / g.act.sum())
    return pd.DataFrame(out), pd.DataFrame(bart), paro


def panel(spec: dict, P: pd.DataFrame, E: pd.DataFrame, Y: pd.DataFrame, ctrl, paro) -> tuple:
    """Filas (provincia, periodo); devuelve el DataFrame y las matrices S̃ (bloques origen × periodo) y g."""
    base = spec["base"]
    nac = "extranjera" if spec["solo_extranjera"] else "total"
    sh = P[(P.anio == base) & (P.nacionalidad == nac)].pivot_table(index="prov", columns="pais", values="valor", aggfunc="sum").fillna(0)
    tot = P[P.nacionalidad == "total"].pivot_table(index=["anio", "prov"], columns="pais", values="valor", aggfunc="sum").fillna(0)
    if spec["suelo"]:
        peq = sh.columns[sh.sum() < 1000]
        sh["resto_suelo"] = sh[peq].sum(1)
        sh = sh.drop(columns=peq)
        for a in tot.index.get_level_values(0).unique():
            pass
        tot["resto_suelo"] = tot[[c for c in peq if c in tot]].sum(1)
        tot = tot.drop(columns=[c for c in peq if c in tot])
    if spec["excluir_ue14"]:
        sh = sh.drop(columns=[c for c in UE14 if c in sh])
    paises = list(sh.columns)
    cuota = sh.div(sh.sum(0).where(sh.sum(0) > 0), axis=1).fillna(0)
    provs = sorted(p for p in cuota.index if spec["muestra"] == 52 or p not in ("51", "52"))
    periodos = ["A", "B", "C"] if spec["diseno"] == "apilado" else ["L"]
    per = dict(PERIODOS, L=(2005, 2022))
    filas, bloques, gs = [], [], []
    for k in periodos:
        a0, a1 = per[k]
        nac_tot = tot.groupby(level=0).sum()
        dM = (nac_tot.loc[a1] - nac_tot.loc[a0]).reindex(paises).fillna(0)
        pob0 = E.loc[(provs, a0), "Total"].droplevel(1) if a0 >= 2002 else None
        for l in provs:
            if spec["tratamiento"] == "15-64":
                x = (E.loc[(l, a1), "Extranjero"] - E.loc[(l, a0), "Extranjero"]) / E.loc[(l, a0), "Total"]
            else:
                f0 = tot.loc[(a0, l)].sum() if (a0, l) in tot.index else np.nan
                f1 = tot.loc[(a1, l)].sum() if (a1, l) in tot.index else np.nan
                x = (f1 - f0) / E.loc[(l, a0), "Total"]
            suma = {"bhj": cuota.loc[l].sum() / pob0.loc[l], "original": cuota.loc[l].sum(),
                    "cuota_1998": sh.loc[l].sum() / E.loc[(l, 2002), "Total"] if (l, 2002) in E.index else np.nan}[spec.get("control_cuotas", "bhj")]
            fila = {"prov": l, "periodo": k, "x": x, "pob0": pob0.loc[l], "suma_cuotas": suma,
                    "paro0": paro.get((l, a0), np.nan), "construccion": ctrl[0]["construccion_2005"].get(l, np.nan),
                    "bartik": ctrl[1][k].get(l, np.nan) if k in ctrl[1] else ctrl[1].sum(1).get(l, np.nan)}
            if spec["loo"]:
                dloo = dM - (tot.loc[(a1, l)].reindex(paises).fillna(0) - tot.loc[(a0, l)].reindex(paises).fillna(0))
                fila["z_loo"] = float((cuota.loc[l] * dloo).sum() / pob0.loc[l])
            for v in Y.columns:
                fila[f"d_{v}"] = Y.loc[(l, a1), v] - Y.loc[(l, a0), v] if (l, a1) in Y.index and (l, a0) in Y.index else np.nan
            filas.append(fila)
        bloques.append(cuota.loc[provs].to_numpy() / pob0.loc[provs].to_numpy()[:, None])
        gs.append(dM.to_numpy())
    d = pd.DataFrame(filas)
    n, Ob = d.shape[0], len(paises)
    S = np.zeros((n, Ob * len(periodos)))
    for i, k in enumerate(periodos):
        m = (d.periodo == k).to_numpy()
        S[m, i * Ob:(i + 1) * Ob] = bloques[i]
    g = np.concatenate(gs)
    grupos = np.tile(np.arange(Ob), len(periodos))
    d["z"] = S @ g
    return d, S, g, grupos, paises, periodos


def W_de(d: pd.DataFrame, spec: dict) -> np.ndarray:
    cols = [np.ones(len(d))]
    per = sorted(d.periodo.unique())
    for k in per[1:]:
        cols.append((d.periodo == k).astype(float).to_numpy())
    for k in per:
        cols.append(((d.periodo == k) * d.suma_cuotas).to_numpy(float))
    cols.append(d.paro0.fillna(d.paro0.mean()).to_numpy(float))
    if spec["controles"] == "completo":
        for k in per:
            cols.append(((d.periodo == k) * d.construccion.fillna(0)).to_numpy(float))
        cols.append(d.bartik.fillna(0).to_numpy(float))
    return np.column_stack(cols)


def estimar(d, S, g, grupos, spec, y: str, ligero: bool = False) -> dict:
    m = d[f"d_{y}"].notna().to_numpy() & d.x.notna().to_numpy()
    dd, SS = d[m], S[m]
    W = W_de(dd, spec)
    w = dd.pob0.to_numpy(float) if spec["pesos"] else None
    yv, xv = dd[f"d_{y}"].to_numpy(float), dd.x.to_numpy(float)
    z = dd.z_loo.to_numpy(float) if spec.get("loo") else dd.z.to_numpy(float)
    iv = econ.iv2sls(yv, xv, z, W, dd.prov.to_numpy(), w)
    if ligero:      # permutaciones: solo el t con el error BHJ
        return {"b": float(iv["b"][0]), "se_bhj": econ.bhj(yv, xv, SS, g, W, w)["se"]}
    fe = econ.f_efectivo(xv, z, W, dd.prov.to_numpy(), w)
    bh_ = econ.bhj(yv, xv, SS, g, W, w)
    ak = econ.akm0(yv, xv, SS, g, W, w, grupos=grupos)
    rf = econ.ols(yv, np.column_stack([z, W]), dd.prov.to_numpy(), w)
    return {"b": float(iv["b"][0]), "se_cluster_prov": float(iv["se"][0]), "F_efectivo": fe, "F_shock": bh_["F_shock"],
            "se_bhj": bh_["se"], "akm0_p": ak["p"], "akm0_inf": ak["ic_inf"], "akm0_sup": ak["ic_sup"], "akm0_acotado": ak["acotado"],
            "akm0_convexo": ak["convexo"], "akm0_conjunto": ak["conjunto"], "orig_efectivos": bh_["hhi_inv"], "n": int(m.sum()), "forma_reducida": float(rf["b"][0])}


def wcb_ccaa(d, spec, y: str) -> dict:
    """Wild cluster bootstrap restringido (Webb, B = 9.999) de la forma reducida agrupando por comunidad autónoma (preregistro §2 y
    adenda A6: control de dependencia espacial; p ≤ 0,05 estricto)."""
    from territorio import PROV
    m = d[f"d_{y}"].notna().to_numpy()
    dd = d[m]
    W = W_de(dd, spec)
    X = np.column_stack([dd.z.to_numpy(float), W])
    cl = dd.prov.map(lambda p: PROV[p][1]).to_numpy()
    r = econ.wcr_boot(dd[f"d_{y}"].to_numpy(float), X, 0, cl, B=9999, w=dd.pob0.to_numpy(float) if spec["pesos"] else None)
    return {"p_wcb_ccaa": r["p"], "t": r["t"], "G": r["G"]}


# ── pruebas ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def rotemberg_top(d, S, g, spec, y, paises, periodos, k=5) -> pd.DataFrame:
    m = d[f"d_{y}"].notna().to_numpy()
    W = W_de(d[m], spec)
    w = d[m].pob0.to_numpy(float) if spec["pesos"] else None
    alfa, beta_o = econ.rotemberg(d[m][f"d_{y}"].to_numpy(float), d[m].x.to_numpy(float), S[m], g, W, w)
    etiquetas_ = [f"{p}|{per}" for per in periodos for p in paises]
    r = pd.DataFrame({"origen_periodo": etiquetas_, "alfa": alfa, "beta_o": beta_o})
    r["origen"] = r.origen_periodo.str.split("|").str[0]
    return r.reindex(r.alfa.abs().sort_values(ascending=False).index).head(k * 3)


def permutaciones(d, S, g, grupos, spec, y, n=500) -> dict:
    rng = np.random.default_rng(SEED)
    base = estimar(d, S, g, grupos, spec, y)
    t0 = base["b"] / base["se_bhj"]
    ts = []
    Ob = len(g) // len(set(d.periodo))
    for _ in range(n):
        gp = g.copy()
        for i in range(len(set(d.periodo))):
            seg = gp[i * Ob:(i + 1) * Ob]
            gp[i * Ob:(i + 1) * Ob] = seg[rng.permutation(Ob)]
        dd = d.copy()
        dd["z"] = S @ gp
        r = estimar(dd, S, gp, grupos, spec, y, ligero=True)
        ts.append(r["b"] / r["se_bhj"])
    ts = np.array(ts)
    med = float(np.median(ts))
    lo, hi = float(np.quantile(ts, 0.025)), float(np.quantile(ts, 0.975))
    return {"t_principal": float(t0), "p_permutacion": float(np.mean(np.abs(ts) >= abs(t0))),
            "p_recentrado": float(np.mean(np.abs(ts - med) >= abs(t0 - med))), "mediana_t": med, "cuantiles_t": [lo, hi],
            "fuera_95_central": bool(t0 < lo or t0 > hi)}


def pretendencia(P, E, spec, ctrl, paro) -> dict:
    """Δ log afiliados 1999→2001 sobre z_A controlando z_P0 (adenda A3)."""
    af = pd.read_csv(PROC / "afiliacion_hist.csv.gz", dtype={"prov": str}).pivot(index="prov", columns="anio", values="afiliados_dic")
    s1 = dict(spec, diseno="apilado")
    d, S, g, grupos, paises, periodos = panel(s1, P, E, pd.DataFrame(index=pd.MultiIndex.from_tuples([], names=["prov", "anio"])),
                                              ctrl, paro)
    dA = d[d.periodo == "A"].set_index("prov")
    # z_P0 con las mismas cuotas y shocks 1998→2005
    tot = P[P.nacionalidad == "total"].pivot_table(index=["anio", "prov"], columns="pais", values="valor", aggfunc="sum").fillna(0)
    nt = tot.groupby(level=0).sum()
    sh = P[(P.anio == spec["base"]) & (P.nacionalidad == ("extranjera" if spec["solo_extranjera"] else "total"))].pivot_table(
        index="prov", columns="pais", values="valor", aggfunc="sum").fillna(0)
    cuota = sh.div(sh.sum(0).where(sh.sum(0) > 0), axis=1).fillna(0)
    dM0 = (nt.loc[2005] - nt.loc[1998]).reindex(cuota.columns).fillna(0)
    z0 = (cuota * dM0).sum(1) / dA.pob0.reindex(cuota.index)
    r = pd.DataFrame({"y": np.log(af[2001] / af[1999]), "zA": dA.z, "z0": z0, "suma": dA.suma_cuotas,
                      "w": dA.pob0}).dropna()
    X = np.column_stack([np.ones(len(r)), r.zA, r.z0, r.suma])
    o = econ.ols(r.y.to_numpy(), X, None, r.w.to_numpy())
    from scipy import stats
    t = o["b"][1] / o["se"][1]
    p = 2 * (1 - stats.norm.cdf(abs(t)))
    corr = float(np.corrcoef(r.zA, r.z0)[0, 1])
    return {"coef_zA": float(o["b"][1]), "ee": float(o["se"][1]), "p": float(p), "n": len(r), "corr_zA_zP0": corr}


def clasificar(r: dict, prueba: dict) -> str:
    fuerte = r["F_shock"] >= 10 and r["F_efectivo"] >= 10
    akm = r["akm0_acotado"] and r["akm0_convexo"]
    if not (fuerte and akm):
        return "ASOCIACIÓN"
    ok_pre = prueba["pretendencia"]["p"] > 0.10
    ok_exc = prueba["exclusion_signo"] and prueba["exclusion_solapa"]
    ok_nac = prueba["nacionalidad_signo"] and prueba["nacionalidad_solapa"]
    ok_perm = (r["akm0_p"] > 0.05) or prueba["permutacion"]["fuera_95_central"]   # A6: t fuera del 95 % central
    if ok_pre and ok_exc and ok_nac and ok_perm:
        return "IDENTIFICADO (pendiente de replicador-ciego y abogado-del-diablo)"
    if prueba["pretendencia"]["p"] > 0.05 and (ok_exc or ok_nac):
        return "SUGESTIVO"
    return "ASOCIACIÓN"


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    O.mkdir(parents=True, exist_ok=True)
    reg = Registry(O / "registro.csv")
    cf = Cifras("f5_p1", "src/m1/f5_p1_shiftshare.py")
    P, E, c = padron(), ecp(), epa_nativos()
    Y = resultados_nativos(c)
    # P1-E6 (adenda A3): movilidad interna de los nativos, Δ log población nacida en España de 15-64 (ECP)
    Y["log_pob_nativos"] = np.log((E["Total"] - E["Extranjero"]).reindex(Y.index))
    ctrl0, bart, paro = controles(c)
    ctrl = (ctrl0, bart)
    d, S, g, grupos, paises, periodos = panel(PRINCIPAL, P, E, Y, ctrl, paro)
    hip = {"P1-H1": "tasa_empleo", "P1-H2": "tasa_paro", "P1-E1": "tasa_actividad", "P1-E2": "log_ocupados",
           "P1-E3a": "tasa_empleo_educ_baja", "P1-E3b": "tasa_empleo_educ_media", "P1-E3c": "tasa_empleo_educ_alta",
           "P1-E6": "log_pob_nativos", "P2-E1": "cuota_nomanual", "P2-E2": "cuota_alta_cualif"}
    res = {}
    for h, y in hip.items():
        r = estimar(d, S, g, grupos, PRINCIPAL, y)
        res[h] = r
        reg.log("F5", h, "principal", json.dumps(PRINCIPAL), "50 prov × A-C", r["n"], r["b"], r["se_bhj"], r["akm0_p"])
    for h, y in hip.items():
        res[h].update(wcb_ccaa(d, PRINCIPAL, y))
    # pruebas para las confirmatorias
    pre = pretendencia(P, E, PRINCIPAL, ctrl, paro)
    salidas = {}
    for h in hip:      # la batería completa también para las exploratorias (revisión del árbitro, segunda ronda)
        y = hip[h]
        rot = rotemberg_top(d, S, g, PRINCIPAL, y, paises, periodos)
        top3 = list(dict.fromkeys(rot.origen))[:3]
        Pex = P[~P.pais.isin(top3)]
        dx, Sx, gx, grx, _, _ = panel(PRINCIPAL, Pex, E, Y, ctrl, paro)
        rex = estimar(dx, Sx, gx, grx, PRINCIPAL, y)
        perm = permutaciones(d, S, g, grupos, PRINCIPAL, y)
        base = res[h]
        solapa = lambda a, b: not (a["akm0_sup"] < b["akm0_inf"] or b["akm0_sup"] < a["akm0_inf"])  # noqa: E731
        nacv = nacionalidad(PRINCIPAL, E, Y, ctrl, paro, y)
        prueba = {"pretendencia": pre, "rotemberg_top": rot.to_dict("records"), "excluidos": top3, "sin_top3": rex,
                  "exclusion_signo": np.sign(rex["b"]) == np.sign(base["b"]), "exclusion_solapa": solapa(rex, base),
                  "nacionalidad": nacv, "nacionalidad_signo": np.sign(nacv["b"]) == np.sign(base["b"]),
                  "nacionalidad_solapa": solapa(nacv, base), "permutacion": perm, "F_shock_sin_top3": rex["F_shock"],
                  "F_shock_nacionalidad": nacv["F_shock"]}
        salidas[h] = prueba
    p_holm = holm({h: res[h]["akm0_p"] for h in ("P1-H1", "P1-H2")})
    p_bh = bh({h: res[h]["akm0_p"] for h in hip if h.startswith("P1-E")})
    p_bh.update(bh({h: res[h]["akm0_p"] for h in hip if h.startswith("P2")}))
    # multiverso
    mult = []
    for comb in itertools.product([1998, 2002], [True, False], ["basico", "completo"], [50, 52], ["apilado", "larga"]):
        s = dict(PRINCIPAL, base=comb[0], pesos=comb[1], controles=comb[2], muestra=comb[3], diseno=comb[4])
        dm, Sm, gm, grm, _, _ = panel(s, P, E, Y, ctrl, paro)
        for h in hip:
            r = estimar(dm, Sm, gm, grm, s, hip[h])
            mult.append({**s, "hipotesis": h, **r})
            reg.log("F5", h, "multiverso", json.dumps(s), "", r["n"], r["b"], r["se_bhj"], r["akm0_p"])
    for extra in ({"solo_extranjera": False}, {"suelo": True}, {"excluir_ue14": True}, {"tratamiento": "todas"},
                  {"controles": "basico"}, {"loo": True}):
        s = dict(PRINCIPAL, **extra)
        dm, Sm, gm, grm, _, _ = panel(s, P, E, Y, ctrl, paro)
        for h in hip:
            r = estimar(dm, Sm, gm, grm, s, hip[h])
            mult.append({**s, "hipotesis": h, "variante": json.dumps(extra), **r})
    mv = pd.DataFrame(mult)
    mv.to_csv(O / "multiverso_p1.csv", index=False)
    # JRS (secundaria): dos endógenas con el retardo
    jrs = dinamico(P, E, Y, ctrl, paro, hip)
    for parte, hs in (("p1", [h for h in hip if h.startswith("P1")]), ("p2", [h for h in hip if h.startswith("P2")])):
        for h in hs:
            r = res[h]
            clas = clasificar(r, salidas[h])
            escribir_resultado(O / parte / h / "resultado.json", pregunta=f"{h}: Δ {hip[h]} de los nacidos en España (16-64) por "
                               "punto de aumento de la población nacida fuera de 15-64 sobre la población 15-64",
                               capa="C3" if clas.startswith("IDENTIFICADO") else "C4", clasificacion=clas,
                               datos="padrón 1998-2022 (INE), ECP, EPA microdatos, afiliación TGSS", N=r["n"],
                               metodo="MC2E shift-share (Card), AKM0 agrupado por origen", estimacion=r["b"],
                               ic95=r["akm0_conjunto"], p_ajustado=p_holm.get(h, p_bh.get(h)),
                               diagnosticos={**r, **salidas[h]},
                               notas="pre-registro interno sin sello externo", prereg=f"prereg-m1 {commit}",
                               dinamico=jrs.get(h))
            gk = "nacidos en España con educación " + {"a": "baja", "b": "media", "c": "alta"}[h[-1]] if h.startswith("P1-E3") else "nacidos en España"
            cf.add(f"F5_{h.replace('-', '_')}_beta", round(r["b"], 3), "log por pp" if hip[h].startswith("log") else "pp por pp",
                   f"{h}: asociación con {hip[h]} (MC2E, especificación "
                   "principal; IC: envolvente del conjunto AKM0)",
                   "C3" if clas.startswith("IDENTIFICADO") else "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias",
                   gk, clasificacion="IDENTIFICADO" if clas.startswith("IDENTIFICADO") else
                   ("SUGESTIVO" if clas.startswith("SUGESTIVO") else "ASOCIACIÓN"),
                   ic_inf=round(r["akm0_inf"], 3) if np.isfinite(r["akm0_inf"]) else np.nan,
                   ic_sup=round(r["akm0_sup"], 3) if np.isfinite(r["akm0_sup"]) else np.nan)
    for h in ("P1-H1", "P1-H2"):
        x = mv[(mv.hipotesis == h) & mv.get("variante", pd.Series(index=mv.index, dtype=object)).isna()]
        k = h.replace("-", "_")
        cf.add(f"F5_{k}_MULT_MED", round(float(x.b.median()), 3), "pp por pp", f"{h}: mediana de β en el multiverso pre-registrado "
               f"({len(x)} especificaciones; intervalo: mínimo y máximo)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias",
               "nacidos en España", clasificacion="ASOCIACIÓN", ic_inf=round(float(x.b.min()), 3), ic_sup=round(float(x.b.max()), 3))
        cf.add(f"F5_{k}_MULT_NEG", int((x.b < 0).sum()), "especificaciones", f"{h}: especificaciones del multiverso con β negativo "
               f"(de {len(x)})", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España")
        cf.add(f"F5_{k}_MULT_RECHAZA", int((x.akm0_p < 0.05).sum()), "especificaciones", f"{h}: especificaciones del multiverso cuyo "
               f"AKM0 rechaza β = 0 al 5 % sin ajuste (de {len(x)})", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias",
               "nacidos en España")
        nv = salidas[h]["nacionalidad"]
        cf.add(f"F5_{k}_NACIONALIDAD", round(nv["b"], 3), "pp por pp", f"{h}: variante con instrumento y tratamiento por nacionalidad "
               f"(F al nivel del shock = {nv['F_shock']:.1f}; IC: conjunto AKM0, acotado = {nv['akm0_acotado']})", "C4",
               "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España", clasificacion="ASOCIACIÓN",
               ic_inf=round(nv["akm0_inf"], 3) if np.isfinite(nv["akm0_inf"]) else np.nan,
               ic_sup=round(nv["akm0_sup"], 3) if np.isfinite(nv["akm0_sup"]) else np.nan)
    nv = salidas["P1-E3a"]["nacionalidad"]
    cf.add("F5_P1_E3a_NACIONALIDAD", round(nv["b"], 3), "pp por pp", "P1-E3a: variante con instrumento y tratamiento por nacionalidad "
           f"(F al nivel del shock = {nv['F_shock']:.1f}; IC: conjunto AKM0, acotado = {nv['akm0_acotado']}, convexo = {nv['akm0_convexo']})",
           "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España con educación baja", clasificacion="ASOCIACIÓN",
           ic_inf=round(nv["akm0_inf"], 3) if np.isfinite(nv["akm0_inf"]) else np.nan,
           ic_sup=round(nv["akm0_sup"], 3) if np.isfinite(nv["akm0_sup"]) else np.nan)
    cf.add("F5_P1_E3a_PERM_p", round(salidas["P1-E3a"]["permutacion"]["p_recentrado"], 3), "p", "P1-E3a: p del placebo de "
           "permutación de shocks (500 permutaciones), recentrado en la mediana de la distribución permutada", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias",
           "nacidos en España con educación baja")
    for h in ("P1-H1", "P1-H2", "P1-E3a"):
        cf.add(f"F5_{h.replace('-', '_')}_WCB_p", round(res[h]["p_wcb_ccaa"], 3), "p", f"{h}: p del wild cluster bootstrap de la forma "
               "reducida agrupando por comunidad autónoma (Webb, 17 grupos; pre-registrado)", "C4", "padrón, ECP, EPA (INE)", "2005-2022",
               "50 provincias", "nacidos en España")
        pm = salidas[h]["permutacion"]
        cf.add(f"F5_{h.replace('-', '_')}_PERM_MED", round(pm["mediana_t"], 2), "t", f"{h}: mediana del t de las 500 permutaciones de los "
               "shocks (intervalo: 95 % central)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España",
               ic_inf=round(pm["cuantiles_t"][0], 2), ic_sup=round(pm["cuantiles_t"][1], 2))
        cf.add(f"F5_{h.replace('-', '_')}_T", round(pm["t_principal"], 2), "t", f"{h}: t de la especificación principal con el error BHJ",
               "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España")
    cf.add("F5_P1_PRETEND_CORR", round(pre["corr_zA_zP0"], 2), "correlación", "Correlación entre el instrumento del periodo A y el del "
           "periodo previo 1998-2005 (pretendencia)", "C4", "padrón (INE)", "1998-2009", "50 provincias", "todos")
    cf.add("F5_P1_PRETEND_p", round(pre["p"], 3), "p", "p de la pretendencia (Δ log afiliación 1999-2001 sobre z_A, controlando z_P0)",
           "C4", "TGSS y padrón", "1999-2001", "50 provincias", "todos")
    for h in ("P1-H1", "P1-H2", "P1-E3a"):
        x = mv[(mv.hipotesis == h) & mv.get("variante", pd.Series(index=mv.index, dtype=object)).isna()]
        fu = x[x.F_shock >= 10]
        k = h.replace("-", "_")
        cf.add(f"F5_{k}_MULT_FUERTE_MED", round(float(fu.b.median()), 3) if len(fu) else np.nan, "pp por pp", f"{h}: mediana de β en las "
               f"especificaciones del multiverso con F al nivel del shock ≥ 10 ({len(fu)} de {len(x)}; intervalo: mínimo y máximo)", "C4",
               "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España", clasificacion="ASOCIACIÓN",
               ic_inf=round(float(fu.b.min()), 3) if len(fu) else np.nan, ic_sup=round(float(fu.b.max()), 3) if len(fu) else np.nan)
        cf.add(f"F5_{k}_MULT_FUERTE_N", int(len(fu)), "especificaciones", f"{h}: especificaciones del multiverso con F al nivel del shock ≥ 10",
               "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España")
        if h == "P1-E3a":
            cf.add("F5_P1_E3a_MULT_MED", round(float(x.b.median()), 3), "pp por pp", f"P1-E3a: mediana de β en el multiverso ({len(x)} "
                   "especificaciones; intervalo: mínimo y máximo)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias",
                   "nacidos en España con educación baja", clasificacion="ASOCIACIÓN", ic_inf=round(float(x.b.min()), 3),
                   ic_sup=round(float(x.b.max()), 3))
            cf.add("F5_P1_E3a_MULT_NEG", int((x.b < 0).sum()), "especificaciones", "P1-E3a: especificaciones del multiverso con β negativo",
                   "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España con educación baja")
            cf.add("F5_P1_E3a_MULT_RECHAZA", int((x.akm0_p < 0.05).sum()), "especificaciones", "P1-E3a: especificaciones del multiverso cuyo "
                   "AKM0 rechaza β = 0 al 5 % sin ajuste", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias",
                   "nacidos en España con educación baja")
    cf.add("F5_P1_F_NACIONALIDAD", round(salidas["P1-H1"]["F_shock_nacionalidad"], 1), "F", "F de primera etapa al nivel del shock en la "
           "variante por nacionalidad", "C4", "padrón (INE)", "2005-2022", "50 provincias", "todos")
    cf.add("F5_P1_F_SIN_TOP3", round(salidas["P1-H1"]["F_shock_sin_top3"], 2), "F", "F de primera etapa al nivel del shock al excluir "
           "los tres orígenes de mayor peso de Rotemberg (prueba no informativa si es < 10)", "C4", "padrón (INE)", "2005-2022",
           "50 provincias", "todos")
    conj = res["P1-E3a"]["akm0_conjunto"]
    if len(conj) == 2 and conj[0][0] == -np.inf and conj[1][1] == np.inf:
        cf.add("F5_P1_E3a_CONJ_A", round(conj[0][1], 2), "pp por pp", "P1-E3a: el conjunto AKM0 es (−∞, a] ∪ [b, ∞); este es a", "C4",
               "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España con educación baja")
        cf.add("F5_P1_E3a_CONJ_B", round(conj[1][0], 2), "pp por pp", "P1-E3a: el conjunto AKM0 es (−∞, a] ∪ [b, ∞); este es b", "C4",
               "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España con educación baja")
    for h in hip:
        cf.add(f"F5_{h.replace('-', '_')}_p", round(float(p_holm.get(h, p_bh.get(h))), 3), "p ajustado",
               f"{h}: p de AKM0 frente a β = 0 ajustado ({'Holm' if h in p_holm else 'BH'}); el conjunto AKM0 puede no estar acotado aunque "
               "el p sea pequeño (primera etapa débil al nivel del shock)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias",
               "nacidos en España")
    cf.add("F5_P1_F_SHOCK", round(res["P1-H1"]["F_shock"], 1), "F", "F de primera etapa al nivel del shock (BHJ), especificación "
           "principal de P1 (umbral pre-registrado: 10)", "C4", "padrón, ECP (INE)", "2005-2022", "50 provincias", "todos")
    cf.add("F5_P1_F_EFECTIVO", round(res["P1-H1"]["F_efectivo"], 1), "F", "F efectivo de primera etapa agrupado por provincia, "
           "especificación principal de P1", "C4", "padrón, ECP (INE)", "2005-2022", "50 provincias", "todos")
    reg.flush()
    cf.escribir()
    print(json.dumps({h: {k: res[h][k] for k in ("b", "akm0_inf", "akm0_sup", "F_shock", "F_efectivo")} for h in hip}, indent=1,
                     default=float))
    return 0


def nacionalidad(spec, E, Y, ctrl, paro, y) -> dict:
    """Instrumento y shocks por nacionalidad (padrón 03005); tratamiento: Δ población de nacionalidad extranjera / población."""
    x = pd.read_csv(PROC / "padron_nacionalidad.csv.gz", dtype={"prov": str})
    x = x[(x.sexo == "total")].assign(nacionalidad="total")
    x2 = x.assign(nacionalidad="extranjera")
    d, S, g, grupos, _, _ = panel(dict(spec, tratamiento="todas"), pd.concat([x, x2]), E, Y, ctrl, paro)
    return estimar(d, S, g, grupos, spec, y)


def dinamico(P, E, Y, ctrl, paro, hip) -> dict:
    """JRS: dos endógenas (x_p, x_p−1) e instrumentos (z_p, z_p−1); P0 = 1998→2005 como retardo de A."""
    d, S, g, grupos, paises, periodos = panel(PRINCIPAL, P, E, Y, ctrl, paro)
    tot = P[P.nacionalidad == "total"].pivot_table(index=["anio", "prov"], columns="pais", values="valor", aggfunc="sum").fillna(0)
    sh = P[(P.anio == 1998) & (P.nacionalidad == "extranjera")].pivot_table(index="prov", columns="pais", values="valor",
                                                                             aggfunc="sum").fillna(0)
    cuota = sh.div(sh.sum(0).where(sh.sum(0) > 0), axis=1).fillna(0)
    nt = tot.groupby(level=0).sum()
    prev = {"A": "P0", "B": "A", "C": "B"}
    zl, xl = [], []
    for _, r in d.iterrows():
        a0, a1 = PERIODOS[prev[r.periodo]]
        dM = (nt.loc[a1] - nt.loc[a0]).reindex(cuota.columns).fillna(0)
        zl.append(float((cuota.loc[r.prov] * dM).sum() / r.pob0))
        f0 = tot.loc[(a0, r.prov)].sum()
        f1 = tot.loc[(a1, r.prov)].sum()
        xl.append((f1 - f0) / r.pob0)
    d["z_l"], d["x_l"] = zl, xl
    pares = {k: float(np.corrcoef(d[d.periodo == k].z, d[d.periodo == k].z_l)[0, 1]) for k in ("A", "B", "C")}
    out = {"corr_z_zlag": float(np.corrcoef(d.z, d.z_l)[0, 1]), "corr_por_periodo": pares,
           "separable": all(abs(v) <= 0.8 for v in pares.values())}
    for h, y in hip.items():
        m = d[f"d_{y}"].notna()
        dd = d[m]
        r = econ.iv2sls_k(dd[f"d_{y}"], np.column_stack([dd.x, dd.x_l]), np.column_stack([dd.z, dd.z_l]), W_de(dd, PRINCIPAL),
                          dd.prov.to_numpy(), dd.pob0.to_numpy(float))
        out[h] = {"corto": float(r["b"][0]), "ee_corto": float(r["se"][0]), "largo": float(r["b"][0] + r["b"][1]),
                  "ee_largo": float(np.sqrt(r["V"][0, 0] + r["V"][1, 1] + 2 * r["V"][0, 1])), "F_SW": r["F_sw"],
                  "separable": out["separable"], "inferencia": "errores agrupados por provincia (convencional; no válida como "
                  "inferencia del shift-share, solo descriptiva)"}
    return out


if __name__ == "__main__":
    sys.exit(main())
