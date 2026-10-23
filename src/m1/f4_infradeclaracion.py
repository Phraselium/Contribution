"""M1-F4 · A POSTERIORI (congelación): cobertura de las encuestas frente a la contabilidad nacional antes de escalar, e
infradeclaración diferencial de rentas de los nacidos fuera. Sin red. No cambia ninguna clasificación.

1. Cobertura (output/f4/cobertura_2024.csv): total ponderado de cada partida en la encuesta, antes de escalar, frente a su total de
   las cuentas de las AAPP de 2024 (Eurostat). Cómo se escala: las partidas «calibradas» (impuestos sobre la renta y cotizaciones,
   prestaciones monetarias) se multiplican por un factor único CN / encuesta, igual para todas las personas y grupos (no hay factor
   por grupo de origen); las «repartidas» (IVA, especiales, vivienda, sociedades y capital, gasto en especie) toman de la encuesta solo
   la distribución y el total es siempre el de las cuentas. El IVA de la EPF se compara también directamente con el D211.
2. Infradeclaración diferencial (output/f4/infradeclaracion_rejilla.csv y _resumen.csv): las rentas declaradas por los nacidos fuera
   en la ECV se elevan por 1 / (1 − d), con d = 0, 10 y 20 % (rejilla explícita: no se ha localizado una estimación publicada y
   verificada de la infradeclaración por origen en la ECV), antes de calibrar o repartir las partidas de ingresos ligadas a la renta.
   Los totales siguen siendo los de las cuentas: es una reasignación de impuestos de los nativos a los nacidos fuera. Las prestaciones
   no se tocan. Se recalculan las 64 combinaciones de supuestos y el nivel «edad y sexo».
3. Otras direcciones (a posteriori, corrección de neutralidad): (a) renta informal no gravada: la renta no declarada no está en la
   recaudación de las cuentas, así que no se reasignan IRPF, cotizaciones ni rentas del capital; solo cambia el consumo (IVA y
   especiales); (b) dirección contraria en transferencias: los nacidos fuera declaran de menos, un d = 10 o 20 % más que los nativos,
   las prestaciones de enfermedad e incapacidad, familia, desempleo, vivienda y exclusión social, que se calibran al total de las
   cuentas; (c) IVA con remesas: la base de consumo de cada grupo de nacidos fuera se reduce por las remesas de trabajadores pagadas al
   exterior en 2024 (D752W, débitos, balanza de pagos del Banco de España vía Eurostat bop_rem6), las de socios UE-27 atribuidas a los
   nacidos en el resto de la UE y las de fuera de la UE a los nacidos fuera de la UE (supuesto explícito), en proporción a su renta.
   Supuesto y sesgo: el país de destino de la remesa se usa como indicador del origen de quien la envía porque no hay una fuente
   pública de remesas por país de nacimiento del emisor. Es una aproximación: (i) atribuye a los nacidos fuera todas las remesas,
   aunque parte las envían nacidos en España (descendientes de emigrantes, hogares mixtos, transferencias familiares a residentes en
   el extranjero), lo que sobrestima sus remesas y subestima su consumo y su IVA (sesgo desfavorable a los nacidos fuera); (ii) un
   nacido fuera de la UE que envía dinero a familia en otro país de la UE (o al revés) se asigna al grupo equivocado, con un efecto
   pequeño porque las remesas a la UE son el 6 % del total; (iii) el reparto proporcional a la renta dentro de cada grupo ignora que la
   propensión a remitir suele ser mayor en los recién llegados de renta baja. La variante es, por tanto, una cota del lado
   desfavorable para los nacidos fuera, no una estimación central.
   Tabla única: output/f4/infradeclaracion_direcciones.csv.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import f4_fiscal as ff  # noqa: E402
from comun import PROC, Cifras  # noqa: E402

O = ff.O
SUP = ["calibrar", "sanidad", "bienes", "educ_hijos", "indirectos", "capital"]
D = (0.0, 0.1, 0.2)


def cobertura(d: pd.DataFrame, ctas: dict) -> pd.DataFrame:
    t, d62 = ctas["t"], ctas["d62"]
    w = d.w
    rb = d.PY010G + d.PY050G.clip(lower=0) + d.PY100G + d.PY110G + d.PY130G + d.PY090G + d.PY120G
    rb_h = rb.groupby(d.hid).transform("sum")
    cuota = np.where(rb_h > 0, rb / rb_h.where(rb_h > 0, 1), (d.edad >= 16) / d.groupby("hid").edad.transform(lambda e: max((e >= 16).sum(), 1)))
    filas = [("IRPF y cotizaciones del trabajador (HY140G)", float((w * d.HY140G * cuota).sum()), t["D51A_C1"] + t["D613"], "ECV", "calibrada"),
             ("Cotizaciones empresariales (PY030G)", float((w * d.PY030G).sum()), t["D611"], "ECV", "calibrada")]
    for nombre, (f, vs) in ff.BEN.items():
        x = sum(d[v] for v in vs)
        if vs[0].startswith("HY"):
            x = x / d.n_hogar
        filas.append((f"Prestación: {nombre} ({'+'.join(vs)})", float((w * x).sum()), d62.get(f, 0.0), "ECV", "calibrada"))
    filas.append(("Becas y prestaciones de educación (PY140G)", float((w * d.PY140G).sum()), d62.get("GF09", 0.0), "ECV", "calibrada"))
    e = pd.read_csv(PROC / "epf_hogares.csv.gz")
    for a in (2022, 2023):
        x = e[e.anio == a]
        c = ff.cuentas(a)
        filas.append((f"IVA imputado en la EPF {a} (COICOP × tipos)", float((x.FACTOR * x.iva).sum()), c["t"]["D211"], f"EPF {a}", "repartida"))
    r = pd.DataFrame(filas, columns=["partida", "total_encuesta", "total_cn", "fuente", "tratamiento"])
    r["total_encuesta"], r["total_cn"] = r.total_encuesta / 1e6, r.total_cn / 1e6
    r["cobertura_pct"] = 100 * r.total_encuesta / r.total_cn
    r["escalado"] = np.where(r.tratamiento == "calibrada", "factor único CN/encuesta, igual para todos los grupos",
                             "solo distribución; el total es el de las cuentas")
    return r


# escenarios (a posteriori): base; renta gravada infradeclarada (la rejilla original); renta informal no gravada (solo cambia el
# consumo); prestaciones infradeclaradas por los nacidos fuera (dirección contraria); IVA con la base de consumo neta de remesas
ESCENARIOS = [("base", 0.0, {}), ("gravada", 0.1, {"infra": 0.1}), ("gravada", 0.2, {"infra": 0.2}),
              ("informal", 0.1, {"infra": 0.1, "infra_modo": "informal"}), ("informal", 0.2, {"infra": 0.2, "infra_modo": "informal"}),
              ("prestaciones", 0.1, {"infra_prest": 0.1}), ("prestaciones", 0.2, {"infra_prest": 0.2}), ("remesas", 0.0, {"remesas": True})]
NOMBRE_ESC = {"base": "base", "gravada": "renta gravada infradeclarada", "informal": "renta informal no gravada",
              "prestaciones": "prestaciones infradeclaradas", "remesas": "IVA con remesas"}
MEDIDAS = [("dif_fuera", "nacidos fuera", "Diferencia con los nativos, conjunto de nacidos fuera", "C2"),
           ("dif_nat", "Resto UE", "Diferencia con los nativos, resto de la UE", "C2"),
           ("dif_nat", "Resto del mundo", "Diferencia con los nativos, resto del mundo", "C2"),
           ("neta_fuera", "nacidos fuera", "Contribución neta, conjunto de nacidos fuera", "C2"),
           ("neta_pc", "Resto UE", "Contribución neta, resto de la UE", "C2"),
           ("neta_pc", "Resto del mundo", "Contribución neta, resto del mundo", "C2"),
           ("neta_pc", "España", "Contribución neta, nacidos en España", "C2"),
           ("dif_nat_est", "Resto UE", "Diferencia con los nativos a igual edad y sexo, resto de la UE", "C4"),
           ("dif_nat_est", "Resto del mundo", "Diferencia con los nativos a igual edad y sexo, resto del mundo", "C4"),
           ("neta_pc_est", "Resto UE", "Contribución a igual edad y sexo, resto de la UE", "C4"),
           ("neta_pc_est", "Resto del mundo", "Contribución a igual edad y sexo, resto del mundo", "C4")]


def direcciones(xa: pd.DataFrame, cf) -> pd.DataFrame:
    """Tabla única (a posteriori): para cada comparación, rango en todas las direcciones y escenarios (8 × 64 combinaciones), cuota de
    combinaciones con signo positivo y negativo, y cuántos de los 8 intervalos de escenario son positivos, negativos o contienen el cero."""
    filas = []
    for var, g, nom, capa in MEDIDAS:
        y = xa[xa.grupo == ("Resto UE" if g == "nacidos fuera" else g)]
        v = y[var]
        sig = y.groupby(["escenario", "infra"])[var].agg(lambda s: 1 if s.min() > 0 else (-1 if s.max() < 0 else 0))
        por = {f"{e}_{int(round(100 * dd))}": (float(z[var].min()), float(z[var].max())) for (e, dd), z in y.groupby(["escenario", "infra"])}
        filas.append({"medida": var, "grupo": g, "comparacion": nom, "capa": capa, "min": float(v.min()), "max": float(v.max()),
                      "pct_positivas": 100 * float((v > 0).mean()), "pct_negativas": 100 * float((v < 0).mean()),
                      "esc_positivos": int((sig == 1).sum()), "esc_negativos": int((sig == -1).sum()), "esc_contienen_cero": int((sig == 0).sum()),
                      **{f"rango_{k}": f"[{a:.0f}, {b:.0f}]" for k, (a, b) in por.items()}})
    t = pd.DataFrame(filas)
    t.to_csv(O / "infradeclaracion_direcciones.csv", index=False)
    for r in t.itertuples():
        k = f"F4_DIRS_{r.medida.upper()}_{r.grupo.replace(' ', '_')}"
        cf.add(k, round(r.pct_positivas, 0), "% de las combinaciones", f"{r.comparacion}: porcentaje de las 512 combinaciones (8 escenarios de "
               "infradeclaración y remesas × 64 de supuestos) con signo positivo; intervalo: mínimo y máximo en euros por persona (a posteriori)",
               r.capa, "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", r.grupo, ic_inf=round(r.min, 0), ic_sup=round(r.max, 0))
        cf.add(k + "_NEG", round(r.pct_negativas, 0), "% de las combinaciones", f"{r.comparacion}: porcentaje de las 512 combinaciones con signo "
               "negativo (a posteriori)", r.capa, "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", r.grupo)
        cf.add(k + "_ESCPOS", int(r.esc_positivos), "escenarios", f"{r.comparacion}: escenarios (de 8) cuyo intervalo de 64 combinaciones es "
               "positivo (a posteriori)", r.capa, "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", r.grupo)
        cf.add(k + "_ESCNEG", int(r.esc_negativos), "escenarios", f"{r.comparacion}: escenarios (de 8) cuyo intervalo de 64 combinaciones es "
               "negativo (a posteriori)", r.capa, "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", r.grupo)
        cf.add(k + "_ESC0", int(r.esc_contienen_cero), "escenarios", f"{r.comparacion}: escenarios (de 8) cuyo intervalo de 64 combinaciones "
               f"contiene el cero ({int(r.esc_positivos)} positivos, {int(r.esc_negativos)} negativos; a posteriori)", r.capa,
               "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", r.grupo)
    for (e, dd), z in xa[xa.escenario.isin(["informal", "prestaciones", "remesas"])].groupby(["escenario", "infra"]):
        for var, g, nom, capa in MEDIDAS:
            y = z[z.grupo == ("Resto UE" if g == "nacidos fuera" else g)]
            p = y[np.logical_and.reduce([y[k] == v for k, v in ff.PRINCIPAL.items()])].iloc[0]
            k = f"F4_DIR_{e.upper()}{int(round(100 * dd)) if e != 'remesas' else ''}_{var.upper()}_{g.replace(' ', '_')}"
            cf.add(k, round(float(p[var]), 0), "€ por persona y año", f"{nom}, escenario «{NOMBRE_ESC[e]}»"
                   f"{f' del {100 * dd:.0f} %' if e != 'remesas' else ''}: principal e intervalo de las 64 combinaciones (a posteriori)", capa,
                   "ECV, EPF, ENSE, cuentas de las AAPP y balanza de pagos", "2024", "España", g,
                   ic_inf=round(float(y[var].min()), 0), ic_sup=round(float(y[var].max()), 0))
    return t


def main() -> int:
    cf = Cifras("f4_infradeclaracion", "src/m1/f4_infradeclaracion.py")
    ctas = ff.cuentas(2024)
    d = ff.personas(2025)
    perf, rat = ff.perfil_sanitario(), ff.ratios_epf()
    cob = cobertura(d, ctas)
    cob.to_csv(O / "cobertura_2024.csv", index=False)
    for i, r in cob.iterrows():
        cf.add(f"F4_COB_{i:02d}", round(float(r.cobertura_pct), 1), "% del total de las cuentas", f"Cobertura antes de escalar: {r.partida} "
               f"({r.fuente}) frente a la contabilidad nacional; {r.escalado} (a posteriori)", "C2", f"{r.fuente} y Eurostat", "2024", "España", "todos")
    filas = []
    desde = "--desde-rejilla" in sys.argv and (O / "infradeclaracion_rejilla.csv").exists()   # resúmenes sin recalcular la rejilla
    for esc, dd, extra in ([] if desde else ESCENARIOS):
        for comb in itertools.product([True, False], ["edad_sexo", "observado"], ["medio", "marginal"], ["hijo", "padres"],
                                      ["epf", "uniforme"], ["rentas", "persona"]):
            s = {**dict(zip(SUP, comb)), **extra}
            c = ff.contribuciones(d, ctas, perf, rat, s)
            rr = ff.resumen(c, ctas["pib"]).set_index("grupo")
            est = ff.estandarizar(c)
            fu = [g for g in ff.GR if g != "España"]
            neta_fuera = float(np.average(rr.loc[fu, "neta"], weights=rr.loc[fu, "poblacion"]))
            for g in ff.GR:
                filas.append({**dict(zip(SUP, comb)), "escenario": esc, "infra": dd, "grupo": g, "neta_pc": rr.loc[g, "neta"], "neta_pc_est": est.loc[g, "neta_est"],
                              "dif_nat": rr.loc[g, "neta"] - rr.loc["España", "neta"],
                              "dif_nat_est": est.loc[g, "neta_est"] - est.loc[g, "nat_neta_mismas"], "neta_fuera": neta_fuera,
                              "dif_fuera": neta_fuera - rr.loc["España", "neta"]})
    if desde:
        xa = pd.read_csv(O / "infradeclaracion_rejilla.csv")
    else:
        xa = pd.DataFrame(filas)
        xa.to_csv(O / "infradeclaracion_rejilla.csv", index=False)
    direcciones(xa, cf)
    x = xa[xa.escenario.isin(["base", "gravada"])].copy()      # la rejilla original (renta gravada) conserva sus cifras
    princ = np.logical_and.reduce([x[k] == v for k, v in ff.PRINCIPAL.items()])
    res = []
    for (dd, g), y in x.groupby(["infra", "grupo"]):
        p = y[princ[y.index]].iloc[0]
        for var in ("neta_pc", "dif_nat", "neta_pc_est", "dif_nat_est", "neta_fuera", "dif_fuera"):
            if g == "España" and var.startswith("dif"):
                continue
            if var in ("neta_fuera", "dif_fuera") and g != "Resto UE":
                continue      # el conjunto de nacidos fuera se guarda una sola vez
            lo, hi = float(y[var].min()), float(y[var].max())
            res.append({"infra": dd, "grupo": "nacidos fuera" if var.endswith("fuera") else g, "medida": var, "principal": float(p[var]),
                        "min": lo, "max": hi, "signo": 1 if lo > 0 else (-1 if hi < 0 else 0), "positivas": int((y[var] > 0).sum())})
    rs = pd.DataFrame(res)
    base = rs[rs.infra == 0].set_index(["grupo", "medida"]).signo
    rs["cambia_signo_vs_0"] = [int(r.signo != base[(r.grupo, r.medida)]) for r in rs.itertuples()]
    rs.to_csv(O / "infradeclaracion_resumen.csv", index=False)
    nombres = {"neta_pc": "contribución neta por persona", "dif_nat": "diferencia con los nativos", "neta_pc_est": "contribución a igual edad y sexo",
               "dif_nat_est": "diferencia con los nativos a igual edad y sexo", "neta_fuera": "contribución neta por persona",
               "dif_fuera": "diferencia con los nativos"}
    for r in rs.itertuples():
        k = f"F4_INFRA{int(round(100 * r.infra))}_{r.medida.upper()}_{r.grupo.replace(' ', '_')}"
        cf.add(k, round(r.principal, 0), "€ por persona y año", f"{nombres[r.medida].capitalize()}, {r.grupo}, con infradeclaración diferencial de "
               f"las rentas de los nacidos fuera del {100 * r.infra:.0f} %: principal e intervalo de las 64 combinaciones (positiva en {r.positivas}; "
               "a posteriori)", "C4" if "est" in r.medida else "C2", "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", r.grupo,
               ic_inf=round(r.min, 0), ic_sup=round(r.max, 0))
    # resto del mundo a igual edad y sexo, convención a convención (una cada vez) y con cada d
    conv = {"principal": {}, "bienes marginal": {"bienes": "marginal"}, "capital por persona": {"capital": "persona"},
            "sanidad observada": {"sanidad": "observado"}, "indirectos uniformes": {"indirectos": "uniforme"},
            "hijos a los padres": {"educ_hijos": "padres"}, "sin calibrar": {"calibrar": False}}
    filas = []
    for dd in D:
        y = x[(x.infra == dd) & (x.grupo == "Resto del mundo")]
        for nom, cambio in conv.items():
            spec = {**ff.PRINCIPAL, **cambio}
            z = y[np.logical_and.reduce([y[k] == v for k, v in spec.items()])].iloc[0]
            filas.append({"infra": dd, "convencion": nom, "neta_pc_est": z.neta_pc_est, "dif_nat_est": z.dif_nat_est})
        filas.append({"infra": dd, "convencion": "rango de las 64", "neta_pc_est_min": y.neta_pc_est.min(), "neta_pc_est_max": y.neta_pc_est.max()})
    rc = pd.DataFrame(filas)
    rc.to_csv(O / "infradeclaracion_rdm_est.csv", index=False)
    for r in rc[rc.convencion != "rango de las 64"].itertuples():
        cf.add(f"F4_INFRA{int(round(100 * r.infra))}_EST_RDM_{r.convencion.upper().replace(' ', '_')}", round(float(r.neta_pc_est), 0),
               "€ por persona y año", f"Contribución neta a igual edad y sexo, nacidos fuera de la UE, convención «{r.convencion}» (las demás como en "
               f"el principal), infradeclaración diferencial del {100 * r.infra:.0f} % (a posteriori)", "C4", "ECV, EPF, ENSE y cuentas de las AAPP",
               "2024", "España", "Resto del mundo")
    cf.escribir()
    print(rc.round(0).to_string())
    pd.set_option("display.width", 220)
    print(cob.round(1).to_string())
    print(rs.round(0).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
