"""M1-F4 · Contribución fiscal neta estática anual por grupo de origen (contribución A: contabilidad con supuestos, capa C2).
Método de la OCDE (2021, cap. 4) adaptado a datos públicos españoles. Sin red. NO identifica efectos causales.

Unidad: persona residente en hogares privados (ECV). Año principal: ECV 2025 (renta y prestaciones de 2024) con las cuentas de
las AAPP de 2024 (Eurostat gov_10a_taxag y gov_10a_exp, COFOG); robustez con ECV 2023 y 2024 (cuentas de 2022 y 2023).
Grupos: nacimiento (España / resto UE / resto del mundo; la ECV no permite más) y nacionalidad como sensibilidad.

INGRESOS (cada partida se calibra al total de las cuentas públicas de su año; «observado» = importe de la ECV, «imputado» = reparto)
- IRPF y cotizaciones del trabajador (D51A + D613): HY140G del hogar (observado en la ECV), repartido entre sus miembros según su
  renta bruta individual (trabajo, actividad, pensiones, desempleo).
- Cotizaciones empresariales (D611): PY030G individual (observado).
- IVA (D211) e impuestos especiales (D214): imputados con la EPF: cociente IVA / renta neta e impuestos especiales / renta por
  origen del sustentador y quintil de renta equivalente, aplicado a la renta disponible del hogar de la ECV.
- Impuestos sobre la vivienda (D29A + D59, IBI y otros): imputados a los hogares propietarios (HH021 = 1, 2) a partes iguales.
- Sociedades, otros impuestos sobre la producción y capital (D51B + D29 − D29A + D91): imputados según rentas del capital y de la
  actividad (HY040G + HY090G + PY050G).
- Resto de ingresos públicos (ventas, rentas de la propiedad, transferencias recibidas, cotizaciones imputadas): por persona, para
  que la suma de las contribuciones netas sea igual al saldo de las AAPP (como Dustmann y Frattini 2014).
GASTOS
- Prestaciones monetarias (D62 por función COFOG): importes de la ECV (observado) calibrados al total de su función: desempleo
  (GF1005 ↔ PY090G), vejez (GF1002 ↔ PY100G), supervivencia (GF1003 ↔ PY110G), enfermedad e incapacidad (GF1001 ↔ PY120G+PY130G),
  familia (GF1004 ↔ HY050G), exclusión social (GF1007 ↔ HY060G), vivienda (GF1006 ↔ HY070G).
- Sanidad en especie (GF07 sin D62): perfil de uso por edad y sexo de la ENSE 2017 por tipo de servicio (fármacos ↔ GF0701,
  consultas ↔ GF0702, hospital y urgencias ↔ GF0703; el resto por persona).
- Educación en especie (GF09 sin D62): 3-11 años ↔ GF0901; 12-15 años y estudiantes de secundaria ↔ GF0902; estudiantes
  universitarios ↔ GF0904; el resto por estudiante.
- Protección social en especie (GF10 sin D62): vejez ↔ 65+; familia ↔ menores de 18; desempleo ↔ parados; resto por persona.
- Bienes públicos puros (GF01 servicios generales e intereses, GF02 defensa): coste medio por persona o coste marginal cero para
  los nacidos fuera.
- Resto (GF03-GF06, GF08): por persona (servicios congestionables).
SUPUESTOS (rejilla; output/f4/rejilla.csv): calibración (sí/no), uso sanitario por origen (mismo uso a igual edad y sexo / uso
observado en la ENSE por origen), bienes públicos (medio / marginal), educación de los hijos de inmigrantes nacidos en España
(al hijo / a los padres), impuestos indirectos (EPF por origen y quintil / tasa uniforme), capital (rentas / por persona).
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, PROC, RAW, SEED, Cifras  # noqa: E402

O = OUT / "f4"
GR = ["España", "Resto UE", "Resto del mundo"]
PRINCIPAL = dict(calibrar=True, sanidad="edad_sexo", bienes="medio", educ_hijos="hijo", indirectos="epf", capital="rentas")
BEN = {"desempleo": ("GF1005", ["PY090G"]), "vejez": ("GF1002", ["PY100G"]), "supervivencia": ("GF1003", ["PY110G"]),
       "enfermedad_incapacidad": ("GF1001", ["PY120G", "PY130G"]), "familia": ("GF1004", ["HY050G"]),
       "exclusion_social": ("GF1007", ["HY060G"]), "vivienda": ("GF1006", ["HY070G"])}


# ── cuentas públicas ───────────────────────────────────────────────────────────────────────────────────────────────────────
def cuentas(a: int) -> dict:
    t = pd.read_csv(RAW / "eurostat" / "gov_10a_taxag.csv.gz", low_memory=False)
    t = t[(t.geo == "ES") & (t.unit == "MIO_EUR") & (t.sector == "S13") & (t.TIME_PERIOD == a)].set_index("na_item").OBS_VALUE * 1e6
    e = pd.read_csv(RAW / "eurostat" / "grandes" / "gov_10a_exp.csv.gz", usecols=["geo", "sector", "unit", "na_item", "cofog99",
                                                                                   "TIME_PERIOD", "OBS_VALUE"])
    e = e[(e.geo == "ES") & (e.sector == "S13") & (e.unit == "MIO_EUR") & (e.TIME_PERIOD == a)]
    te = e[e.na_item == "TE"].set_index("cofog99").OBS_VALUE * 1e6
    d62 = e[e.na_item == "D62"].set_index("cofog99").OBS_VALUE * 1e6
    g = pd.read_csv(RAW / "eurostat" / "nama_10_gdp.csv.gz", low_memory=False)
    pib = g[(g.geo == "ES") & (g.unit == "CP_MEUR") & (g.na_item == "B1GQ") & (g.TIME_PERIOD == a)].OBS_VALUE.iloc[0] * 1e6
    m = pd.read_csv(RAW / "eurostat" / "gov_10a_main.csv.gz", low_memory=False)
    tr = m[(m.geo == "ES") & (m.unit == "MIO_EUR") & (m.sector == "S13") & (m.na_item == "TR") & (m.TIME_PERIOD == a)]
    return {"t": t, "te": te, "d62": d62, "pib": pib, "tr": tr.OBS_VALUE.iloc[0] * 1e6}


# ── perfiles externos ──────────────────────────────────────────────────────────────────────────────────────────────────────
def perfil_sanitario() -> pd.DataFrame:
    """Uso relativo por edad (tramos de 5 años), sexo y origen (ENSE 2017). Para los menores sin dato de fármacos ni urgencias se
    toma el uso del tramo 15-24 (supuesto). Las razones por origen se estiman por tramos amplios para reducir ruido."""
    s = pd.read_csv(PROC / "ense_uso.csv.gz")
    s["e5"] = (s.edad.clip(upper=90) // 5) * 5
    s["consultas"] = s.consultas_ap.fillna(0) + s.consultas_esp.fillna(0)
    s["hosp"] = s.dias_hosp.fillna(0)
    s["urg"] = s.urgencias
    s["far"] = s.med_receta
    m = s.groupby(["e5", "sexo"]).apply(lambda g: pd.Series({v: np.average(g[v].fillna(g[v].mean() if g[v].notna().any() else 0),
                                                                             weights=g.factor) for v in ("consultas", "hosp", "urg", "far")}),
                                        include_groups=False).reset_index()
    joven = m[m.e5.isin([15, 20])].groupby("sexo")[["urg", "far"]].mean()
    for v in ("urg", "far"):
        m.loc[m.e5 < 15, v] = m.loc[m.e5 < 15, "sexo"].map(joven[v])
    s["amplio"] = pd.cut(s.edad, [-1, 14, 34, 54, 74, 200], labels=["0-14", "15-34", "35-54", "55-74", "75+"]).astype(str)
    r = []
    for amp, g in s.groupby("amplio"):
        fila = {"amplio": amp}
        for v in ("consultas", "hosp", "urg", "far"):
            gg = g.dropna(subset=[v])
            if (~gg.nacido_fuera).sum() == 0 or gg.nacido_fuera.sum() < 30:
                fila[f"razon_{v}"] = 1.0
                continue
            a = np.average(gg.loc[gg.nacido_fuera, v], weights=gg.loc[gg.nacido_fuera, "factor"]) if gg.nacido_fuera.any() else np.nan
            b = np.average(gg.loc[~gg.nacido_fuera, v], weights=gg.loc[~gg.nacido_fuera, "factor"])
            fila[f"razon_{v}"] = a / b if b > 0 else 1.0
        fila["n_nacidos_fuera"] = int(g.nacido_fuera.sum())
        r.append(fila)
    razones = pd.DataFrame(r).fillna(1.0)
    m.attrs["razones"] = razones
    return m


def ratios_epf() -> pd.DataFrame:
    e = pd.read_csv(PROC / "epf_hogares.csv.gz")
    e = e[(e.ingreso_anual_neto > 0) & e.origen_sp.notna() & e.anio.isin([2022, 2023])]
    e["eq"] = e.ingreso_anual_neto / e.UC2.where(e.UC2 > 0, 1)
    e["q"] = e.groupby("anio").eq.transform(lambda s: pd.qcut(s.rank(method="first"), 5, labels=False)) + 1
    r = e.groupby(["origen_sp", "q"]).apply(lambda g: pd.Series({
        "iva_renta": np.average(g.iva, weights=g.FACTOR) / np.average(g.ingreso_anual_neto, weights=g.FACTOR),
        "esp_renta": np.average(g.base_especiales, weights=g.FACTOR) / np.average(g.ingreso_anual_neto, weights=g.FACTOR),
        "n": len(g)}), include_groups=False).reset_index()
    return r


# ── datos de personas ──────────────────────────────────────────────────────────────────────────────────────────────────────
def personas(anio: int) -> pd.DataFrame:
    cols = ["anio", "RB030", "hid", "RB050", "RB090", "edad", "nacimiento3", "nacionalidad3", "segunda_gen", "PE010", "PE021", "PL032",
            "DB040", "HH021", "HY020", "HY040G", "HY050G", "HY060G", "HY070G", "HY090G", "HY140G", "PY010G", "PY030G", "PY050G",
            "PY090G", "PY100G", "PY110G", "PY120G", "PY130G", "PY140G"]
    d = pd.read_csv(PROC / "ecv_personas.csv.gz", usecols=cols, low_memory=False)
    d = d[(d.anio == anio) & d.nacimiento3.notna()].copy()
    for c in cols[13:]:
        if c not in ("PL032",):
            d[c] = d[c].fillna(0.0)
    d["sexo"] = d.RB090.map({1: "hombre", 2: "mujer"})
    d["w"] = d.RB050
    d["n_hogar"] = d.groupby("hid").RB030.transform("size")
    adultos = d.edad >= 14
    d["uc"] = d.groupby("hid").edad.transform(lambda e: 1 + 0.5 * ((e >= 14).sum() - 1) + 0.3 * (e < 14).sum())
    del adultos
    # origen del hogar (persona de referencia ≈ menor identificador entre los adultos) para los impuestos indirectos
    ref = d[d.edad >= 16].sort_values("RB030").groupby("hid").nacimiento3.first()
    d["origen_hogar"] = d.hid.map(ref).fillna(d.nacimiento3)
    # grupo de los padres (para la sensibilidad de la educación de los hijos nacidos en España)
    fuera = d[(d.edad >= 18) & d.nacimiento3.isin(["Resto UE", "Resto del mundo"])].groupby("hid").nacimiento3.agg(
        lambda s: s.mode().iloc[0])
    d["grupo_padres"] = np.where((d.edad < 18) & d.segunda_gen.fillna(False).astype(bool), d.hid.map(fuera), None)
    return d


def contribuciones(d: pd.DataFrame, ctas: dict, perf: pd.DataFrame, rat: pd.DataFrame, s: dict) -> pd.DataFrame:
    t, te, d62 = ctas["t"], ctas["te"], ctas["d62"]
    w = d.w.to_numpy()
    out = pd.DataFrame(index=d.index)

    def cal(x: pd.Series, total: float) -> pd.Series:
        tot = float((x * w).sum())
        return x * (total / tot) if (s["calibrar"] and tot > 0) else x

    def reparto(indice: pd.Series, total: float) -> pd.Series:
        """Reparto de un total de las cuentas según un índice (siempre al total: es gasto en especie o impuesto imputado)."""
        tot = float((indice * w).sum())
        return indice * (total / tot) if tot > 0 else indice * 0
    # ingresos
    rb = d.PY010G + d.PY050G.clip(lower=0) + d.PY100G + d.PY110G + d.PY130G + d.PY090G + d.PY120G
    rb_h = rb.groupby(d.hid).transform("sum")
    cuota = np.where(rb_h > 0, rb / rb_h.where(rb_h > 0, 1), (d.edad >= 16) / d.groupby("hid").edad.transform(lambda e: max((e >= 16).sum(), 1)))
    out["ing_irpf_cotiz_trab"] = cal(d.HY140G * cuota, t["D51A_C1"] + t["D613"])
    out["ing_cotiz_empresa"] = cal(d.PY030G, t["D611"])
    eq = d.HY020 / d.uc
    q = pd.qcut(eq.rank(method="first"), 5, labels=False) + 1
    if s["indirectos"] == "epf":
        m = rat.set_index(["origen_sp", "q"])
        k = pd.MultiIndex.from_arrays([d.origen_hogar, q])
        iva_r = pd.Series(m["iva_renta"].reindex(k).to_numpy(), index=d.index)
        esp_r = pd.Series(m["esp_renta"].reindex(k).to_numpy(), index=d.index)
    else:
        iva_r = pd.Series(1.0, index=d.index)
        esp_r = pd.Series(1.0, index=d.index)
    renta_pc = d.HY020.clip(lower=0) / d.n_hogar
    out["ing_iva"] = reparto(renta_pc * iva_r, t["D211"])
    out["ing_especiales"] = reparto(renta_pc * esp_r, t["D214"])
    prop = d.HH021.isin([1, 2]).astype(float) / d.n_hogar
    out["ing_vivienda_ibi"] = reparto(prop, t["D29A"] + t["D59"])
    cap = ((d.HY040G + d.HY090G).clip(lower=0) / d.n_hogar + d.PY050G.clip(lower=0)) if s["capital"] == "rentas" else pd.Series(1.0, index=d.index)
    out["ing_sociedades_capital"] = reparto(cap, t["D51B_C2"] + t["D29"] - t["D29A"] + t["D91"])
    impuestos = (t["D51A_C1"] + t["D613"] + t["D611"] + t["D211"] + t["D214"] + t["D59"] + t["D51B_C2"] + t["D29"] + t["D91"])
    # resto de ingresos (ventas, rentas de la propiedad, transferencias, cotizaciones imputadas D612): por persona, para que la suma
    # de las contribuciones netas cuadre con el saldo de las AAPP
    out["ing_otros_ingresos"] = reparto(pd.Series(1.0, index=d.index), ctas["tr"] - impuestos)
    # gastos: prestaciones monetarias
    for nombre, (f, vs) in BEN.items():
        x = sum(d[v] for v in vs)
        if vs[0].startswith("HY"):
            x = x / d.n_hogar
        out[f"gas_{nombre}"] = cal(x, d62.get(f, 0.0))
    otras = d62.get("GF10", 0) - sum(d62.get(f, 0) for f, _ in BEN.values())
    out["gas_otras_prestaciones"] = reparto(pd.Series(1.0, index=d.index), max(otras, 0))
    # sanidad en especie
    p = perf.set_index(["e5", "sexo"])
    e5 = (d.edad.clip(upper=90) // 5) * 5
    k = pd.MultiIndex.from_arrays([e5, d.sexo])
    idx = {v: pd.Series(p[v].reindex(k).to_numpy(), index=d.index).fillna(0) for v in ("consultas", "hosp", "urg", "far")}
    if s["sanidad"] == "observado":
        raz = perf.attrs["razones"].set_index("amplio")
        amp = pd.cut(d.edad, [-1, 14, 34, 54, 74, 200], labels=["0-14", "15-34", "35-54", "55-74", "75+"]).astype(str)
        fuera = d.nacimiento3 != "España"
        for v in idx:
            idx[v] = idx[v] * np.where(fuera, amp.map(raz[f"razon_{v}"]).astype(float), 1.0)
    sanidad_te = te["GF07"] - d62.get("GF07", 0)
    out["gas_sanidad"] = (reparto(idx["far"], te["GF0701"] - d62.get("GF0701", 0)) +
                          reparto(idx["consultas"], te["GF0702"] - d62.get("GF0702", 0)) +
                          reparto(0.8 * idx["hosp"] / max(idx["hosp"].mean(), 1e-9) + 0.2 * idx["urg"] / max(idx["urg"].mean(), 1e-9),
                                  te["GF0703"] - d62.get("GF0703", 0)) +
                          reparto(pd.Series(1.0, index=d.index), sanidad_te - sum(te[f] - d62.get(f, 0) for f in ("GF0701", "GF0702", "GF0703"))))
    # educación en especie
    est = d.PE010 == 1
    prim = d.edad.between(3, 11).astype(float)
    sec = (d.edad.between(12, 15) | (est & d.PE021.between(20, 45))).astype(float)
    uni = (est & (d.PE021 == 50)).astype(float)
    todos = ((prim + sec + uni) > 0).astype(float)
    ed = (reparto(prim, te["GF0901"] - d62.get("GF0901", 0)) + reparto(sec, te["GF0902"] - d62.get("GF0902", 0)) +
          reparto(uni, te["GF0904"] - d62.get("GF0904", 0)) +
          reparto(todos, (te["GF09"] - d62.get("GF09", 0)) - sum(te[f] - d62.get(f, 0) for f in ("GF0901", "GF0902", "GF0904"))))
    out["gas_educacion"] = ed + cal(d.PY140G, d62.get("GF09", 0))
    # protección social en especie
    out["gas_prot_social_especie"] = (reparto((d.edad >= 65).astype(float), te["GF1002"] - d62.get("GF1002", 0)) +
                                      reparto((d.edad < 18).astype(float), te["GF1004"] - d62.get("GF1004", 0)) +
                                      reparto(((d.PL032 == 2) | (d.PY090G > 0)).astype(float), te["GF1005"] - d62.get("GF1005", 0)) +
                                      reparto(pd.Series(1.0, index=d.index), (te["GF10"] - d62.get("GF10", 0)) -
                                              sum(te[f] - d62.get(f, 0) for f in ("GF1002", "GF1004", "GF1005"))))
    # bienes públicos puros y resto
    puros = te["GF01"] + te["GF02"]
    base = pd.Series(1.0, index=d.index) if s["bienes"] == "medio" else (d.nacimiento3 == "España").astype(float)
    out["gas_bienes_publicos_puros"] = reparto(base, puros)
    out["gas_resto_servicios"] = reparto(pd.Series(1.0, index=d.index), sum(te[f] for f in ("GF03", "GF04", "GF05", "GF06", "GF08")))
    ing = [c for c in out if c.startswith("ing_")]
    gas = [c for c in out if c.startswith("gas_")]
    out["ingresos"], out["gastos"] = out[ing].sum(1), out[gas].sum(1)
    out["neta"] = out.ingresos - out.gastos
    out["grupo"] = d.nacimiento3
    if s["educ_hijos"] == "padres":
        out.loc[d.grupo_padres.notna(), "grupo"] = d.grupo_padres[d.grupo_padres.notna()]
    out["nacionalidad3"], out["edad"], out["w"], out["hid"], out["DB040"] = d.nacionalidad3, d.edad, d.w, d.hid, d.DB040
    return out


def resumen(c: pd.DataFrame, pib: float, por="grupo") -> pd.DataFrame:
    cols = [x for x in c.columns if x.startswith(("ing_", "gas_"))] + ["ingresos", "gastos", "neta"]
    r = c.groupby(por).apply(lambda g: pd.Series({**{k: np.average(g[k], weights=g.w) for k in cols},
                                                  "poblacion": g.w.sum(), "n_muestral": len(g)}), include_groups=False)
    r["neta_total_pct_pib"] = 100 * r.neta * r.poblacion / pib
    return r.reset_index()


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f4_fiscal", "src/m1/f4_fiscal.py")
    perf, rat = perfil_sanitario(), ratios_epf()
    perf.attrs["razones"].to_csv(O / "razones_uso_sanitario_ense.csv", index=False)
    rat.to_csv(O / "ratios_indirectos_epf.csv", index=False)
    res_anios, rej = [], []
    for anio_ecv in (2023, 2024, 2025):
        ctas = cuentas(anio_ecv - 1)
        d = personas(anio_ecv)
        c = contribuciones(d, ctas, perf, rat, PRINCIPAL)
        r = resumen(c, ctas["pib"])
        r["anio_cuentas"] = anio_ecv - 1
        res_anios.append(r)
        if anio_ecv == 2025:
            principal, ctas25 = c, ctas
            rn = resumen(c, ctas["pib"], "nacionalidad3")
            rn.to_csv(O / "neta_por_nacionalidad_2024.csv", index=False)
            # rejilla de supuestos (64 combinaciones)
            for comb in itertools.product([True, False], ["edad_sexo", "observado"], ["medio", "marginal"], ["hijo", "padres"],
                                          ["epf", "uniforme"], ["rentas", "persona"]):
                s = dict(zip(["calibrar", "sanidad", "bienes", "educ_hijos", "indirectos", "capital"], comb))
                rr = resumen(contribuciones(d, ctas, perf, rat, s), ctas["pib"])
                for _, x in rr.iterrows():
                    rej.append({**s, "grupo": x.grupo, "neta_pc": x.neta, "neta_total_pct_pib": x.neta_total_pct_pib,
                                "poblacion": x.poblacion})
    todos = pd.concat(res_anios)
    todos.to_csv(O / "neta_por_grupo_anios.csv", index=False)
    rej = pd.DataFrame(rej)
    # presupuesto equilibrado (OCDE): el saldo de las AAPP se reparte por igual por persona, de modo que la suma de las contribuciones
    # netas es cero; y diferencia con los nacidos en España en cada combinación (la comparación de Fiorio et al. 2023)
    sup_cols = ["calibrar", "sanidad", "bienes", "educ_hijos", "indirectos", "capital"]
    saldo_pc = rej.groupby(sup_cols).apply(lambda x: np.average(x.neta_pc, weights=x.poblacion), include_groups=False)
    rej["neta_pc_equilibrada"] = rej.neta_pc - rej.set_index(sup_cols).index.map(saldo_pc).values
    nat = rej[rej.grupo == "España"].set_index(sup_cols).neta_pc
    rej["dif_nativos"] = rej.neta_pc - rej.set_index(sup_cols).index.map(nat).values
    rej.to_csv(O / "rejilla.csv", index=False)
    # bootstrap por hogares del escenario principal (muestreo)
    rng = np.random.default_rng(SEED)
    hogares = principal.hid.unique()
    bs = []
    for _ in range(200):
        hh = rng.choice(hogares, len(hogares), replace=True)
        cnt = pd.Series(hh).value_counts()
        m = principal.hid.map(cnt).fillna(0)
        x = principal.assign(w=principal.w * m)
        bs.append(x.groupby("grupo").apply(lambda g: np.average(g.neta, weights=g.w), include_groups=False))
    bs = pd.DataFrame(bs)
    r25 = todos[todos.anio_cuentas == 2024].set_index("grupo")
    r25.to_csv(O / "neta_por_grupo_2024.csv")
    perfil_edad(principal).to_csv(O / "perfil_edad_2024.csv", index=False)
    regiones(principal, ctas25["pib"]).to_csv(O / "neta_por_region_2024.csv", index=False)
    signos = []
    for g in GR:
        x = rej[rej.grupo == g]
        lo, hi = x.neta_pc.min(), x.neta_pc.max()
        b_lo, b_hi = np.percentile(bs[g], [2.5, 97.5])
        cf.add(f"F4_NETA_PC_{g.replace(' ', '_')}_2024", round(r25.loc[g, "neta"], 0), "€ por persona y año",
               f"Contribución fiscal neta estática por persona, nacidos en {g} (escenario principal; IC por muestreo)", "C2",
               "ECV, EPF, ENSE (INE) y cuentas de las AAPP (Eurostat)", "2024", "España", g, ic_inf=round(b_lo, 0), ic_sup=round(b_hi, 0))
        cf.add(f"F4_NETA_PC_RANGO_SUPUESTOS_{g.replace(' ', '_')}_2024", round(r25.loc[g, "neta"], 0), "€ por persona y año",
               f"Contribución neta por persona, nacidos en {g}: intervalo entre las 64 combinaciones de supuestos", "C2",
               "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", g, ic_inf=round(lo, 0), ic_sup=round(hi, 0))
        cf.add(f"F4_NETA_TOTAL_PIB_{g.replace(' ', '_')}_2024", round(r25.loc[g, "neta_total_pct_pib"], 2), "% del PIB",
               f"Contribución neta total del grupo nacidos en {g} (escenario principal)", "C2", "ECV y cuentas de las AAPP", "2024",
               "España", g, ic_inf=round(x.neta_total_pct_pib.min(), 2), ic_sup=round(x.neta_total_pct_pib.max(), 2))
        es_p = np.logical_and.reduce([x[k] == v for k, v in PRINCIPAL.items()])
        pe = x[es_p].iloc[0]
        cf.add(f"F4_NETA_EQUILIBRADA_PC_{g.replace(' ', '_')}_2024", round(pe.neta_pc_equilibrada, 0), "€ por persona y año",
               f"Contribución neta por persona con presupuesto equilibrado (saldo de las AAPP repartido por igual), nacidos en {g}: "
               "principal e intervalo de las 64 combinaciones", "C2", "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", g,
               ic_inf=round(x.neta_pc_equilibrada.min(), 0), ic_sup=round(x.neta_pc_equilibrada.max(), 0))
        if g != "España":
            cf.add(f"F4_NETA_DIF_NAT_{g.replace(' ', '_')}_2024", round(pe.dif_nativos, 0), "€ por persona y año",
                   f"Contribución neta por persona de los nacidos en {g} menos la de los nacidos en España: principal e intervalo de las "
                   "64 combinaciones", "C2", "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", g,
                   ic_inf=round(x.dif_nativos.min(), 0), ic_sup=round(x.dif_nativos.max(), 0))
        signos.append({"grupo": g, "principal": pe.neta_pc, "min": lo, "max": hi, "cuota_positivas": float((x.neta_pc > 0).mean()),
                       "cambia_signo": bool(lo < 0 < hi), "equilibrada_principal": pe.neta_pc_equilibrada,
                       "equilibrada_min": x.neta_pc_equilibrada.min(), "equilibrada_max": x.neta_pc_equilibrada.max(),
                       "dif_nativos_principal": pe.dif_nativos, "dif_nativos_min": x.dif_nativos.min(),
                       "dif_nativos_max": x.dif_nativos.max()})
    bm = rej.set_index(sup_cols + ["grupo"]).neta_pc.unstack("bienes")
    tras = (bm["marginal"] - bm["medio"]).groupby("grupo").mean()
    cf.add("F4_BIENES_MARGINAL_TRASLADO_España_2024", round(float(tras["España"]), 0), "€ por persona y año",
           "Cambio en la contribución neta por persona de los nacidos en España al pasar los bienes públicos puros de coste medio a "
           "coste marginal cero para los nacidos fuera (media de las combinaciones)", "C2", "ECV y cuentas de las AAPP", "2024",
           "España", "España")
    sg = pd.DataFrame(signos)
    sg.to_csv(O / "signo_por_supuestos.csv", index=False)
    sensibilidad(rej).to_csv(O / "sensibilidad_supuestos.csv", index=False)
    cf.escribir()
    print(r25[["neta", "ingresos", "gastos", "neta_total_pct_pib", "poblacion"]].round(1))
    print(sg)
    return 0


def perfil_edad(c: pd.DataFrame) -> pd.DataFrame:
    c = c.assign(e=(c.edad.clip(upper=85) // 5) * 5)
    cols = ["ingresos", "gastos", "neta"] + [x for x in c.columns if x.startswith(("ing_", "gas_"))]
    r = c.groupby(["grupo", "e"]).apply(lambda g: pd.Series({**{k: np.average(g[k], weights=g.w) for k in cols}, "n_muestral": len(g)}),
                                        include_groups=False).reset_index()
    r.loc[r.n_muestral < 50, cols] = np.nan
    return r


def regiones(c: pd.DataFrame, pib: float) -> pd.DataFrame:
    """Por NUTS2 (C4): los gastos en especie y los bienes públicos se reparten con reglas nacionales, así que la variación
    regional procede de rentas, impuestos y prestaciones observadas; no es un saldo fiscal regional."""
    r = c.groupby(["DB040", "grupo"]).apply(lambda g: pd.Series({"neta_pc": np.average(g.neta, weights=g.w),
                                                                 "ingresos_pc": np.average(g.ingresos, weights=g.w),
                                                                 "gastos_pc": np.average(g.gastos, weights=g.w),
                                                                 "n_muestral": len(g)}), include_groups=False).reset_index()
    r.loc[r.n_muestral < 50, ["neta_pc", "ingresos_pc", "gastos_pc"]] = np.nan
    return r


def sensibilidad(rej: pd.DataFrame) -> pd.DataFrame:
    """Efecto medio de cambiar cada supuesto (manteniendo los demás) sobre la contribución neta por persona de cada grupo."""
    filas = []
    for sup, (a, b) in {"calibrar": (True, False), "sanidad": ("edad_sexo", "observado"), "bienes": ("medio", "marginal"),
                        "educ_hijos": ("hijo", "padres"), "indirectos": ("epf", "uniforme"), "capital": ("rentas", "persona")}.items():
        for g in GR:
            x = rej[rej.grupo == g]
            filas.append({"supuesto": sup, "de": a, "a": b, "grupo": g,
                          "efecto_medio_eur_pc": x[x[sup] == b].neta_pc.mean() - x[x[sup] == a].neta_pc.mean()})
    return pd.DataFrame(filas)


if __name__ == "__main__":
    sys.exit(main())
