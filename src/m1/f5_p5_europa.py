"""M1-F5 · P5: empleo de los nativos y llegada de inmigrantes en las regiones NUTS2 de la UE-27. SOLO con la puerta prereg-m1
abierta (docs/preregistro.md §7 y adenda A8; techo SUGESTIVO).

Unidad: regiones NUTS2 de la UE-27. Resultado: Δ tasa de empleo 20-64 de los nativos 2021→2024 (EU-LFS, lfst_r_lfe2emprc, en
puntos). Tratamiento: Δ población nacida fuera de 20-64 2021→2024 / población 20-64 de 2021 (EU-LFS, lfst_r_lfsd2pwc).
Instrumento: z_r = Σ_o N_o,r,2021 · g_o,−k / población_r,2021, con N el censo de 2021 por país de nacimiento (cens_21cob_r3,
nivel NUTS2), sin el propio país de la región, y g_o,−k = inmigración desde o en 2021-2024 hacia el resto de la UE-27 excluido el
país k de la región / stock de nacidos en o en el resto de la UE-27 (migr_imm3ctb; leave-one-country-out). Es la forma de tasa de
crecimiento del shock de la adenda A8: equivale a cuotas s_o,r = N_o,r / N_o,UE−k. Efectos fijos de país, pesos por población
20-64 de 2021, celdas con bandera de baja fiabilidad («u») excluidas.
Inferencia: wild cluster bootstrap restringido de la forma reducida agrupando por país (Webb); AKM0 y F al nivel del shock en la
variante con shocks comunes a toda la UE (z = S·g exacto, como en la adenda A1); F efectivo agrupado por país. Variantes: sin los
flujos desde Ucrania; shocks comunes; heterogeneidad por grupos institucionales de países fijados en el pre-registro.
Clasificación: techo SUGESTIVO; SUGESTIVO solo si F al nivel del shock y F efectivo ≥ 10 y conjunto AKM0 acotado y convexo; si no,
ASOCIACIÓN. Salidas: output/f5/p5/P5/resultado.json y output/f5/p5_regiones.csv.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import etiquetas  # noqa: E402
from comun import OUT, RAW, Cifras, Registry, escribir_resultado  # noqa: E402

O = OUT / "f5"
EU = RAW / "eurostat"
UE27 = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR", "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT",
        "NL", "PL", "PT", "RO", "SE", "SI", "SK"]
GRUPOS = {"mediterráneos": ["ES", "IT", "PT", "EL", "CY", "MT"], "continentales": ["DE", "FR", "AT", "BE", "NL", "LU"],
          "nórdicos": ["DK", "FI", "SE"], "anglosajón": ["IE"]}


def censo() -> pd.DataFrame:
    trozos = []
    for ch in pd.read_csv(EU / "grandes" / "cens_21cob_r3.csv.gz", usecols=["c_birth", "sex", "age", "geo", "OBS_VALUE"],
                          chunksize=2_000_000):
        ch = ch[(ch.sex == "T") & (ch.age == "TOTAL") & (ch.geo.str.len() == 4)]
        trozos.append(ch)
    c = pd.concat(trozos)
    c["pais"] = c.geo.str[:2]
    c = c[c.pais.isin(UE27)]
    pob = c[c.c_birth == "TOTAL"].set_index("geo").OBS_VALUE
    c = c[(c.c_birth.str.len() == 2) & (c.c_birth != c.pais) & ~c.c_birth.isin(["NR", "UN"])]
    return c.pivot_table(index="geo", columns="c_birth", values="OBS_VALUE", aggfunc="sum").fillna(0), pob


def shocks(N: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    m = pd.read_csv(EU / "migr_imm3ctb.csv.gz", usecols=["age", "c_birth", "sex", "geo", "TIME_PERIOD", "OBS_VALUE"], low_memory=False)
    m = m[(m.age == "TOTAL") & (m.sex == "T") & m.geo.isin(UE27) & m.TIME_PERIOD.between(2021, 2024)]
    flujo = m.pivot_table(index="geo", columns="c_birth", values="OBS_VALUE", aggfunc="sum").reindex(columns=N.columns).fillna(0)
    stock_pais = N.groupby(N.index.str[:2]).sum()
    loo = {}
    for k in UE27:
        f = flujo.drop(index=k, errors="ignore").sum()
        s = stock_pais.drop(index=k, errors="ignore").sum()
        loo[k] = (f / s.where(s > 0)).fillna(0)
    comun = (flujo.sum() / stock_pais.sum().where(stock_pais.sum() > 0)).fillna(0)
    return pd.DataFrame(loo).T, comun


def lfs() -> pd.DataFrame:
    e = pd.read_csv(EU / "lfst_r_lfe2emprc.csv.gz", usecols=["c_birth", "isced11", "age", "sex", "geo", "TIME_PERIOD", "OBS_VALUE",
                                                             "OBS_FLAG"])
    e = e[(e.c_birth == "NAT") & (e.isced11 == "TOTAL") & (e.age == "Y20-64") & (e.sex == "T") & (e.geo.str.len() == 4)]
    e = e[~e.OBS_FLAG.fillna("").str.contains("u")]
    tasa = e.pivot_table(index="geo", columns="TIME_PERIOD", values="OBS_VALUE")
    p = pd.read_csv(EU / "lfst_r_lfsd2pwc.csv.gz", usecols=["wstatus", "c_birth", "sex", "age", "geo", "TIME_PERIOD", "OBS_VALUE",
                                                            "OBS_FLAG"])
    p = p[(p.wstatus == "POP") & (p.sex == "T") & (p.age == "Y20-64") & (p.geo.str.len() == 4) & p.c_birth.isin(["FOR", "TOTAL"])]
    p = p[~p.OBS_FLAG.fillna("").str.contains("u")]
    pp = p.pivot_table(index="geo", columns=["c_birth", "TIME_PERIOD"], values="OBS_VALUE")
    d = pd.DataFrame({"dy": tasa[2024] - tasa[2021],
                      "x": 100 * (pp[("FOR", 2024)] - pp[("FOR", 2021)]) / pp[("TOTAL", 2021)],  # en puntos
                      "pob2064": pp[("TOTAL", 2021)]})
    return d


def estimar(d: pd.DataFrame, S: np.ndarray, g: np.ndarray, zcol: str) -> dict:
    paises = sorted(d.pais.unique())
    W = np.column_stack([np.ones(len(d))] + [(d.pais == p).astype(float).to_numpy() for p in paises[1:]])
    y, x, z, cl, w = (d.dy.to_numpy(float), d.x.to_numpy(float), d[zcol].to_numpy(float), d.pais.to_numpy(),
                      d.pob2064.to_numpy(float))
    iv = econ.iv2sls(y, x, z, W, cl, w)
    fe = econ.f_efectivo(x, z, W, cl, w)
    Xrf = np.column_stack([z, W])
    rf = econ.ols(y, Xrf, cl, w)
    wb = econ.wcr_boot(y, Xrf, 0, cl, B=9999, w=w)
    out = {"b": float(iv["b"][0]), "ee_cluster_pais": float(iv["se"][0]), "F_efectivo": fe, "forma_reducida": float(rf["b"][0]),
           "p_wcb_forma_reducida": wb["p"], "G": wb["G"], "n": int(len(d))}
    if S is not None:
        bh_ = econ.bhj(y, x, S, g, W, w)
        ak = econ.akm0(y, x, S, g, W, w)
        out.update({"F_shock": bh_["F_shock"], "se_bhj": bh_["se"], "akm0_p": ak["p"], "akm0_conjunto": ak["conjunto"],
                    "akm0_inf": ak["ic_inf"],
                    "akm0_sup": ak["ic_sup"], "akm0_acotado": ak["acotado"], "akm0_convexo": ak["convexo"]})
    return out


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    reg = Registry(O / "registro_p5.csv")
    cf = Cifras("f5_p5", "src/m1/f5_p5_europa.py")
    N, pob = censo()
    g_loo, g_com = shocks(N)
    d = lfs().join(pob.rename("pob_censo"), how="inner").dropna()
    d = d[d.index.isin(N.index)]
    d["pais"] = d.index.str[:2]
    Nd = N.loc[d.index]
    d["z_loo"] = [(Nd.loc[r] * g_loo.loc[r[:2]].reindex(Nd.columns).fillna(0)).sum() / d.loc[r, "pob_censo"] for r in d.index]
    S = Nd.to_numpy() / d.pob_censo.to_numpy()[:, None]
    gc = g_com.reindex(Nd.columns).fillna(0).to_numpy()
    d["z_comun"] = S @ gc
    sin_ua = [c for c in Nd.columns if c != "UA"]
    d["z_loo_sin_ua"] = [(Nd.loc[r, sin_ua] * g_loo.loc[r[:2]].reindex(sin_ua).fillna(0)).sum() / d.loc[r, "pob_censo"] for r in d.index]
    d.reset_index(names="geo").to_csv(O / "p5_regiones.csv", index=False)
    pr = estimar(d, None, None, "z_loo")
    com = estimar(d, S, gc, "z_comun")
    sua = estimar(d, None, None, "z_loo_sin_ua")
    het = {}
    for k, ps in list(GRUPOS.items()) + [("centro y este", [p for p in UE27 if not any(p in v for v in GRUPOS.values())])]:
        x = d[d.pais.isin(ps)]
        if x.pais.nunique() >= 2 and len(x) >= 15:
            het[k] = estimar(x, None, None, "z_loo")
        else:
            het[k] = {"no_estimable": f"{x.pais.nunique()} país(es) y {len(x)} regiones: no hay variación suficiente con efectos de país"}
    for k, r in (("principal_loo", pr), ("shocks_comunes", com), ("sin_ucrania", sua)):
        reg.log("F5", "P5", k, "NUTS2 UE-27, efectos de país", "2021-2024", r["n"], r["b"], r["ee_cluster_pais"], r["p_wcb_forma_reducida"])
    fuerte = com["F_shock"] >= 10 and pr["F_efectivo"] >= 10 and com["akm0_acotado"] and com["akm0_convexo"]
    clas = "SUGESTIVO" if fuerte and pr["p_wcb_forma_reducida"] <= 0.05 else "ASOCIACIÓN"
    ic = [pr["b"] - 1.96 * pr["ee_cluster_pais"], pr["b"] + 1.96 * pr["ee_cluster_pais"]]   # orientativo; la inferencia es el WCB
    escribir_resultado(O / "p5" / "P5" / "resultado.json",
                       pregunta="P5: Δ tasa de empleo 20-64 de los nativos 2021→2024 por punto de aumento de la población nacida fuera "
                                "de 20-64 sobre la población 20-64, regiones NUTS2 de la UE-27",
                       capa="C4", clasificacion=clas, datos="Eurostat: cens_21cob_r3, migr_imm3ctb, lfst_r_lfe2emprc, lfst_r_lfsd2pwc",
                       N=pr["n"], metodo="MC2E shift-share leave-one-country-out con efectos de país; wild cluster bootstrap de la "
                       "forma reducida por país (Webb); AKM0 en la variante con shocks comunes", estimacion=pr["b"], ic95=ic,
                       p_ajustado=pr["p_wcb_forma_reducida"], diagnosticos={"principal": pr, "shocks_comunes": com, "sin_ucrania": sua,
                                                                           "heterogeneidad": het},
                       notas="Techo SUGESTIVO (A8): periodo corto y cuotas de un censo posterior a la COVID. El IC es orientativo "
                             "(errores agrupados por país); la inferencia es el p del wild bootstrap. El conjunto AKM0 corresponde a otra "
                             "especificación (shocks comunes) y se guarda aparte en diagnosticos. La regla adicional para SUGESTIVO (F al "
                             "nivel del shock ≥ 10 y AKM0 acotado) se fijó al programar el script, sin poder acreditar que fuera antes de "
                             "ver estimaciones (docs/desviaciones.md).", prereg=f"prereg-m1 {commit}")
    cf.add("F5_P5_beta", round(pr["b"], 3), "pp por pp", "P5: asociación entre la llegada de población nacida fuera y la tasa de "
           f"empleo de los nativos, NUTS2 de la UE-27, 2021-2024 (MC2E leave-one-country-out; p wild bootstrap por país = "
           f"{pr['p_wcb_forma_reducida']:.2f}; IC orientativo por errores agrupados por país)", "C4", "Eurostat (censo 2021, migr_imm3ctb, EU-LFS)",
           "2021-2024", "NUTS2 UE-27", "nativos", clasificacion=clas,
           ic_inf=round(ic[0], 3) if np.isfinite(ic[0]) else np.nan, ic_sup=round(ic[1], 3) if np.isfinite(ic[1]) else np.nan)
    for k, r in het.items():
        if "b" in r:
            cf.add(f"F5_P5_HET_{k.replace(' ', '_')}", round(r["b"], 3), "pp por pp", f"P5, países {k}: β leave-one-country-out "
                   f"({r['n']} regiones; p wild bootstrap = {r['p_wcb_forma_reducida']:.2f})", "C4", "Eurostat", "2021-2024", f"NUTS2, {k}",
                   "nativos", clasificacion="ASOCIACIÓN")
    reg.flush()
    cf.escribir()
    print({"principal": pr, "comunes": com, "sin_ua": sua})
    print({k: (round(v["b"], 3), round(v["p_wcb_forma_reducida"], 3), v["n"]) if "b" in v else v for k, v in het.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
