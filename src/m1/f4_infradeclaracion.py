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
    for dd in D:
        for comb in itertools.product([True, False], ["edad_sexo", "observado"], ["medio", "marginal"], ["hijo", "padres"],
                                      ["epf", "uniforme"], ["rentas", "persona"]):
            s = dict(zip(SUP, comb), infra=dd)
            c = ff.contribuciones(d, ctas, perf, rat, s)
            rr = ff.resumen(c, ctas["pib"]).set_index("grupo")
            est = ff.estandarizar(c)
            fu = [g for g in ff.GR if g != "España"]
            neta_fuera = float(np.average(rr.loc[fu, "neta"], weights=rr.loc[fu, "poblacion"]))
            for g in ff.GR:
                filas.append({**s, "grupo": g, "neta_pc": rr.loc[g, "neta"], "neta_pc_est": est.loc[g, "neta_est"],
                              "dif_nat": rr.loc[g, "neta"] - rr.loc["España", "neta"],
                              "dif_nat_est": est.loc[g, "neta_est"] - est.loc[g, "nat_neta_mismas"], "neta_fuera": neta_fuera,
                              "dif_fuera": neta_fuera - rr.loc["España", "neta"]})
    x = pd.DataFrame(filas)
    x.to_csv(O / "infradeclaracion_rejilla.csv", index=False)
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
