"""M1-F3 · Empleo por grupo de origen (contribución A, descriptivo: capa C1/C4, sin causalidad). Sin red.

Fuentes: EPA (celdas de data/processed/epa_celdas.csv.gz) y Eurostat (lfsa_ergacob, lfsa_urgacob, lfst_r_lfe2emprc).
Salidas en output/f3/: empleo_nacional.csv (series), empleo_tres_niveles.csv, empleo_oaxaca.csv, empleo_contribucion.csv,
empleo_provincias.csv, empleo_residencia.csv, empleo_cohortes.csv, empleo_generaciones.csv, empleo_europa.csv; y cifras en
output/cifras/f3_empleo.csv. Celdas con < 50 observaciones muestrales, suprimidas.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
from comun import OUT, PROC, RAW, UMBRAL_CELDA, Cifras  # noqa: E402
from niveles import oaxaca_celdas, tres_niveles  # noqa: E402

O = OUT / "f3"
EPA = "EPA (INE, microdatos trimestrales)"
GRUPOS_EPA = ["España", "UE-14", "UE-13 y otros de Europa", "América Latina", "África", "Asia", "Resto"]


def cargar() -> pd.DataFrame:
    c = pd.read_csv(PROC / "epa_celdas.csv.gz", dtype={"prov": str})
    c["edad1664"] = ~c["edad6"].isin(["65+"])
    return c


def tasas(g: pd.DataFrame) -> pd.Series:
    a = g[g.edad1664]
    s = {"pob_16_64": a.pob.sum(), "tasa_actividad": a.act.sum() / a.pob.sum(), "tasa_empleo": a.ocu.sum() / a.pob.sum(),
         "tasa_paro": g.par.sum() / g.act.sum(), "temporalidad": g.temp.sum() / g.asal.sum(),
         "parcialidad": g.parc.sum() / g.ocu.sum(), "horas_semana": g.horas.sum() / g.ocu.sum(),
         "ocup_alta_cualif": g.ocu_alta.sum() / g.ocu.sum(), "ocup_elementales": g.ocu_elem.sum() / g.ocu.sum(),
         "ocupados": g.ocu.sum(), "horas_totales": g.horas.sum(), "n_muestral": g.n_obs.sum()}
    ed = g[g.educ == "alta"]
    s["sobrecualificacion"] = ed.sobrecual.sum() / ed.ocu.sum() if ed.ocu.sum() > 0 else np.nan
    return pd.Series(s)


def _sup(df: pd.DataFrame, n="n_muestral") -> pd.DataFrame:
    cols = [c for c in df.columns if c not in (n,) and pd.api.types.is_float_dtype(df[c])]
    df.loc[df[n] < UMBRAL_CELDA, cols] = np.nan
    return df


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f3_empleo", "src/m1/f3_empleo.py")
    c = cargar()
    ult = 2025
    # 1. series nacionales
    nac = c.groupby(["origen_def", "anio", "grupo"]).apply(tasas, include_groups=False).reset_index()
    nac = _sup(nac)
    nac.to_csv(O / "empleo_nacional.csv", index=False)
    x = nac[(nac.origen_def == "nacimiento") & (nac.anio == ult)].set_index("grupo")
    for g in GRUPOS_EPA:
        if g in x.index:
            cf.add(f"F3_EMP_TASA_{g}_{ult}", round(100 * x.loc[g, "tasa_empleo"], 1), "% (16-64)",
                   f"Tasa de empleo 16-64, nacidos en {g if g != 'España' else 'España'}", "C1", EPA, str(ult), "España", g)
            cf.add(f"F3_EMP_PARO_{g}_{ult}", round(100 * x.loc[g, "tasa_paro"], 1), "%", f"Tasa de paro, grupo {g}", "C1", EPA,
                   str(ult), "España", g)
    # total nacidos fuera
    fuera = c[(c.origen_def == "nacimiento") & (c.grupo != "España")]
    tf = fuera.groupby("anio").apply(tasas, include_groups=False)
    tf.reset_index().assign(grupo="Nacidos fuera (total)").to_csv(O / "empleo_nacidos_fuera.csv", index=False)
    cf.add(f"F3_EMP_TASA_FUERA_{ult}", round(100 * tf.loc[ult, "tasa_empleo"], 1), "% (16-64)",
           "Tasa de empleo 16-64, nacidos fuera de España", "C1", EPA, str(ult), "España", "nacidos fuera")
    cf.add(f"F3_EMP_PARO_FUERA_{ult}", round(100 * tf.loc[ult, "tasa_paro"], 1), "%", "Tasa de paro, nacidos fuera de España",
           "C1", EPA, str(ult), "España", "nacidos fuera")

    for etq, fila in (("España", x.loc["España"] if "España" in x.index else None), ("FUERA", tf.loc[ult])):
        grp = "España" if etq == "España" else "nacidos fuera"
        for v, u, dsc in (("temporalidad", "% de asalariados", "Asalariados con contrato temporal"),
                          ("ocup_elementales", "% de ocupados", "Ocupados en ocupaciones elementales (CNO 9)"),
                          ("ocup_alta_cualif", "% de ocupados", "Ocupados en ocupaciones de alta cualificación (CNO 1-3)"),
                          ("sobrecualificacion", "% de ocupados con estudios superiores", "Titulados superiores en ocupaciones CNO 4-9")):
            cf.add(f"F3_EMP_{v.upper()}_{etq}_{ult}", round(100 * fila[v], 1), u, f"{dsc}, {grp}", "C1", EPA, str(ult), "España", grp)

    # 2. tres niveles (16-64) en años seleccionados
    filas = []
    for a in (2008, 2013, 2019, ult):
        b = c[(c.anio == a) & (c.origen_def == "nacimiento") & c.edad1664].copy()
        b["tasa_empleo"] = b.ocu / b.pob
        t = tres_niveles(b, "tasa_empleo", "pob")
        t["anio"], t["variable"] = a, "tasa_empleo_16_64"
        filas.append(t)
        ba = b[b.act > 0].copy()
        ba["tasa_paro"] = ba.par / ba.act
        t = tres_niveles(ba, "tasa_paro", "act")
        t["anio"], t["variable"] = a, "tasa_paro"
        filas.append(t)
        bs = c[(c.anio == a) & (c.origen_def == "nacimiento") & (c.asal > 0)].copy()
        bs["temporalidad"] = bs.temp / bs.asal
        t = tres_niveles(bs, "temporalidad", "asal")
        t["anio"], t["variable"] = a, "temporalidad"
        filas.append(t)
        # sensibilidad: nacionalidad
        bn = c[(c.anio == a) & (c.origen_def == "nacionalidad") & c.edad1664].copy()
        bn["tasa_empleo"] = bn.ocu / bn.pob
        t = tres_niveles(bn, "tasa_empleo", "pob", resid=None)
        t["anio"], t["variable"] = a, "tasa_empleo_16_64 (nacionalidad)"
        filas.append(t)
    tn = pd.concat(filas)
    tn.to_csv(O / "empleo_tres_niveles.csv", index=False)
    # conjunto de nacidos fuera (cantidad de la afirmación F4): tres niveles con los grupos agrupados
    for v, dfv, yv, pw in (("EMP", c[(c.anio == ult) & (c.origen_def == "nacimiento") & c.edad1664].assign(tasa=lambda x: x.ocu / x.pob),
                            "tasa", "pob"),
                           ("PARO", c[(c.anio == ult) & (c.origen_def == "nacimiento") & c.edad1664 & (c.act > 0)].assign(
                               tasa=lambda x: x.par / x.act), "tasa", "act")):
        dfv = dfv.assign(grupo=np.where(dfv.grupo == "España", "España", "FUERA"))
        tf = tres_niveles(dfv, yv, pw)
        for _, r in tf.iterrows():
            cf.add(f"F3_{v}_BRECHA_FUERA_{r.nivel_ajuste.replace(' ', '_')}_{ult}", round(100 * r.brecha, 1), "pp",
                   f"Brecha de tasa de {'empleo 16-64' if v == 'EMP' else 'paro'} del conjunto de nacidos fuera frente a nacidos en España "
                   f"({r.nivel_ajuste})", "C1" if r.nivel_ajuste == "bruto" else "C4", EPA, str(ult), "España", "nacidos fuera",
                   nivel_ajuste=r.nivel_ajuste, ic_inf=round(100 * (r.brecha - 1.96 * r.ee), 1), ic_sup=round(100 * (r.brecha + 1.96 * r.ee), 1))
    k = tn[(tn.anio == ult) & (tn.variable == "tasa_empleo_16_64")]
    for _, r in k.iterrows():
        cf.add(f"F3_EMP_BRECHA_{r.grupo}_{r.nivel_ajuste.replace(' ', '_')}_{ult}", round(100 * r.brecha, 1), "pp",
               f"Brecha de tasa de empleo 16-64 frente a nacidos en España ({r.nivel_ajuste})", "C1" if r.nivel_ajuste == "bruto"
               else "C4", EPA, str(ult), "España", r.grupo, nivel_ajuste=r.nivel_ajuste, ic_inf=round(100 * (r.brecha - 1.96 * r.ee), 1),
               ic_sup=round(100 * (r.brecha + 1.96 * r.ee), 1))

    # 3. Oaxaca de la brecha de empleo
    b = c[(c.anio == ult) & (c.origen_def == "nacimiento") & c.edad1664].copy()
    b["tasa_empleo"] = b.ocu / b.pob
    ox = []
    for g in GRUPOS_EPA[1:]:
        r = oaxaca_celdas(b, "tasa_empleo", "pob", g)
        ox.append({"grupo": g, "anio": ult, "variable": "tasa_empleo_16_64", **r,
                   "n_muestral": b.loc[b.grupo == g, "n_obs"].sum()})
    ox = _sup(pd.DataFrame(ox))
    ox.to_csv(O / "empleo_oaxaca.csv", index=False)

    # 4. contribución al crecimiento del empleo y de las horas
    contr = []
    for a0, a1 in ((2014, ult), (2019, ult), (2008, 2013)):
        e0 = nac[(nac.origen_def == "nacimiento") & (nac.anio == a0)].set_index("grupo")
        e1 = nac[(nac.origen_def == "nacimiento") & (nac.anio == a1)].set_index("grupo")
        for v in ("ocupados", "horas_totales"):
            d = e1[v] - e0[v]
            for g in d.index:
                contr.append({"periodo": f"{a0}-{a1}", "variable": v, "grupo": g, "variacion": d[g], "cuota_variacion": d[g] / d.sum(),
                              "n_muestral": min(e0.loc[g, "n_muestral"], e1.loc[g, "n_muestral"])})
    contr = pd.DataFrame(contr)
    contr.to_csv(O / "empleo_contribucion.csv", index=False)
    cc = contr[(contr.periodo == f"2014-{ult}") & (contr.variable == "ocupados")].set_index("grupo")
    cf.add(f"F3_EMP_CONTRIB_FUERA_2014_{ult}", round(100 * (1 - cc.loc["España", "cuota_variacion"]), 1), "% del aumento",
           "Parte del aumento de la ocupación 2014-2025 que corresponde a nacidos fuera de España (contabilidad, no causal)",
           "C1", EPA, f"2014-{ult}", "España", "nacidos fuera")
    cf.add(f"F3_EMP_AUMENTO_OCUPADOS_2014_{ult}", round(cc["variacion"].sum() / 1e6, 2), "millones",
           "Aumento de la ocupación media anual 2014-2025", "C1", EPA, f"2014-{ult}", "España", "todos")
    ch = contr[(contr.periodo == f"2014-{ult}") & (contr.variable == "horas_totales")].set_index("grupo")
    cf.add(f"F3_EMP_CONTRIB_HORAS_FUERA_2014_{ult}", round(100 * (1 - ch.loc["España", "cuota_variacion"]), 1), "% del aumento",
           "Parte del aumento de las horas efectivas semanales 2014-2025 de nacidos fuera", "C1", EPA, f"2014-{ult}", "España",
           "nacidos fuera")

    # 5. provincias: nacidos en España frente a nacidos fuera
    p = c[(c.origen_def == "nacimiento") & c.anio.isin([2014, 2019, ult])].copy()
    p["origen2"] = np.where(p.grupo == "España", "España", "Nacidos fuera")
    pr = p.groupby(["anio", "prov", "origen2"]).apply(tasas, include_groups=False).reset_index()
    pr = _sup(pr)
    pr.to_csv(O / "empleo_provincias.csv", index=False)
    w = pr[pr.anio == ult].pivot(index="prov", columns="origen2", values="tasa_empleo")
    gap = (w["Nacidos fuera"] - w["España"]) * 100
    cf.add(f"F3_EMP_BRECHA_PROV_MIN_{ult}", round(gap.min(), 1), "pp", f"Brecha provincial mínima de tasa de empleo 16-64 "
           f"(nacidos fuera menos nacidos en España), provincia {gap.idxmin()}", "C4", EPA, str(ult), f"provincia {gap.idxmin()}",
           "nacidos fuera")
    cf.add(f"F3_EMP_BRECHA_PROV_MAX_{ult}", round(gap.max(), 1), "pp", f"Brecha provincial máxima, provincia {gap.idxmax()}",
           "C4", EPA, str(ult), f"provincia {gap.idxmax()}", "nacidos fuera")
    cf.add(f"F3_EMP_BRECHA_PROV_POSITIVAS_{ult}", int((gap > 0).sum()), "provincias",
           "Provincias donde la tasa de empleo 16-64 de los nacidos fuera supera a la de los nacidos en España", "C4", EPA, str(ult),
           "provincias", "nacidos fuera")

    # 6. años de residencia y cohortes de llegada (pseudo-panel; supuesto: efectos de periodo comunes con los nativos)
    r = c[(c.origen_def == "nacimiento") & (c.grupo != "España") & c.edad1664 & ~c.resid.isin(["no consta"])]
    rr = r.groupby(["anio", "resid"]).apply(tasas, include_groups=False).reset_index()
    _sup(rr).to_csv(O / "empleo_residencia.csv", index=False)
    coh = cohortes(c)
    coh.to_csv(O / "empleo_cohortes.csv", index=False)
    k15 = coh.set_index("termino").loc["cohorte_2015+"]
    cf.add("F3_EMP_COHORTE_2015_REL", round(100 * k15.coef, 1), "pp", "Tasa de empleo 25-54 relativa a los nativos de la cohorte llegada "
           "en 2015 o después frente a la de 1995-2001, a igual tramo de residencia (pseudopanel; supuesto: efectos de periodo comunes)",
           "C4", EPA, "2005-2025", "España", "nacidos fuera", ic_inf=round(100 * (k15.coef - 1.96 * k15.ee), 1),
           ic_sup=round(100 * (k15.coef + 1.96 * k15.ee), 1))

    # 7. nacionalizados y segunda generación
    gen = []
    x = c[(c.origen_def == "nacimiento") & c.edad1664 & (c.anio == ult)]
    cats = [("nacidos fuera, nacionalizados", (x.grupo != "España") & x.nacionalizado, None),
            ("nacidos fuera, sin nacionalidad española", (x.grupo != "España") & ~x.nacionalizado, None)]
    for tramo in ("16-24", "25-34"):   # segunda generación: comparación entre quienes conviven con sus padres, por tramo de edad
        cats += [(f"nacidos en España que conviven con un progenitor nacido fuera ({tramo})", (x.grupo == "España") & x.sg &
                  (x.edad6 == tramo), tramo),
                 (f"nacidos en España que conviven con progenitores nacidos en España ({tramo})", (x.grupo == "España") & ~x.sg &
                  x.con_padres & (x.edad6 == tramo), tramo)]
    for etiqueta, m, _ in cats:
        t = tasas(x[m])
        t["categoria"] = etiqueta
        gen.append(t)
    gdf = _sup(pd.DataFrame(gen)).set_index("categoria")
    gdf.reset_index().to_csv(O / "empleo_generaciones.csv", index=False)
    for tramo in ("16-24", "25-34"):
        a_ = gdf.loc[f"nacidos en España que conviven con un progenitor nacido fuera ({tramo})", "tasa_empleo"]
        b_ = gdf.loc[f"nacidos en España que conviven con progenitores nacidos en España ({tramo})", "tasa_empleo"]
        cf.add(f"F3_EMP_SEGUNDA_GEN_{tramo.replace('-', '_')}", round(100 * (a_ - b_), 1), "pp",
               f"Tasa de empleo de nacidos en España que conviven con un progenitor nacido fuera menos la de quienes conviven con progenitores "
               f"nacidos en España, {tramo} años", "C4", EPA, str(ult), "España", "segunda generación")

    # 8. Europa (Eurostat, EU-LFS): tasas de empleo 20-64 por país de nacimiento
    eu = europa()
    eu.to_csv(O / "empleo_europa.csv", index=False)
    es = eu[(eu.geo == "ES") & (eu.anio == eu.anio.max())].set_index("c_birth")
    if "NAT" in es.index and "FOR" in es.index:
        cf.add(f"F3_EMP_EU_ES_BRECHA_{int(eu.anio.max())}", round(es.loc["FOR", "valor"] - es.loc["NAT", "valor"], 1), "pp",
               "Brecha de tasa de empleo 20-64 nacidos fuera menos nativos en España (Eurostat, segunda fuente)", "C1",
               "Eurostat lfsa_ergacob", str(int(eu.anio.max())), "España", "nacidos fuera")
        e27 = eu[(eu.geo == "EU27_2020") & (eu.anio == eu.anio.max())].set_index("c_birth")
        cf.add(f"F3_EMP_EU_UE27_BRECHA_{int(eu.anio.max())}", round(e27.loc["FOR", "valor"] - e27.loc["NAT", "valor"], 1), "pp",
               "Brecha de tasa de empleo 20-64 nacidos fuera menos nativos en la UE-27", "C1", "Eurostat lfsa_ergacob",
               str(int(eu.anio.max())), "UE-27", "nacidos fuera")
    nuts = europa_nuts2()
    nuts.to_csv(O / "empleo_europa_nuts2.csv", index=False)
    cf.escribir()
    print("f3_empleo: hecho;", len(cf.filas), "cifras")
    return 0


def cohortes(c: pd.DataFrame) -> pd.DataFrame:
    """Separación de cohorte de llegada y años de residencia (Borjas 1985) en la tasa de empleo de los nacidos fuera, 25-54.
    Celdas por año × años de residencia (residencia exacta no disponible: tramos) → cohorte = año − tramo; efectos de periodo
    tomados de los nativos (supuesto de identificación). Resultado C4."""
    x = c[(c.origen_def == "nacimiento") & c.edad6.isin(["25-34", "35-44", "45-54"])].copy()
    nat = x[x.grupo == "España"].groupby("anio").apply(lambda g: g.ocu.sum() / g.pob.sum(), include_groups=False)
    f = x[(x.grupo != "España") & x.resid.isin(["0-4", "5-9", "10-19", "20+"])]
    t = f.groupby(["anio", "resid"]).apply(lambda g: pd.Series({"tasa": g.ocu.sum() / g.pob.sum(), "pob": g.pob.sum(),
                                                               "n_muestral": g.n_obs.sum()}), include_groups=False).reset_index()
    medio = {"0-4": 2, "5-9": 7, "10-19": 14.5, "20+": 25}
    t["llegada"] = t.anio - t.resid.map(medio)
    t["cohorte"] = pd.cut(t.llegada, [1900, 1994, 2001, 2008, 2014, 2030], labels=["≤1994", "1995-2001", "2002-2008",
                                                                                   "2009-2014", "2015+"]).astype(str)
    t["tasa_rel_nativos"] = t.tasa - t.anio.map(nat)
    X = pd.get_dummies(t[["resid", "cohorte"]], drop_first=True, dtype=float)
    r = econ.ols(t.tasa_rel_nativos.to_numpy(), np.column_stack([np.ones(len(t)), X.to_numpy()]), None, t.pob.to_numpy())
    coef = pd.DataFrame({"termino": ["constante"] + list(X.columns), "coef": r["b"], "ee": r["se"]})
    coef["n_muestral"] = int(t.n_muestral.sum())
    return coef


def _eurostat(nombre: str) -> pd.DataFrame:
    p = RAW / "eurostat" / f"{nombre}.csv.gz"
    if not p.exists():
        p = RAW / "eurostat" / "grandes" / f"{nombre}.csv.gz"
    return pd.read_csv(p, low_memory=False)


def europa() -> pd.DataFrame:
    d = _eurostat("lfsa_ergacob")
    d = d[(d.sex == "T") & (d.age == "Y20-64") & (d.c_birth.isin(["NAT", "FOR", "EU27_2020_FOR", "NEU27_2020_FOR"]))]
    return d.rename(columns={"TIME_PERIOD": "anio", "OBS_VALUE": "valor"})[["geo", "anio", "c_birth", "valor"]]


def europa_nuts2() -> pd.DataFrame:
    d = _eurostat("lfst_r_lfe2emprc")
    d = d[(d.sex == "T") & (d.age == "Y20-64") & (d.isced11 == "TOTAL") & (d.geo.str.len() == 4)]
    d = d[d.TIME_PERIOD >= 2019]
    return d.rename(columns={"TIME_PERIOD": "anio", "OBS_VALUE": "valor"})[["geo", "anio", "c_birth", "valor", "OBS_FLAG"]]


if __name__ == "__main__":
    sys.exit(main())
