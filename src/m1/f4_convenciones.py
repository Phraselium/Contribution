"""M1-F4 · A POSTERIORI (verificación tras el cierre): sensibilidad de C2 por convención, presentada igual para los tres grupos, y
tratamiento de la diferencia de pensiones de la regla mecánica. Sin red; lee salidas de f4_fiscal y f4_pensiones.

1. Tabla de convenciones (output/f4/sensibilidad_convenciones.csv): contribución neta por persona de cada grupo en el escenario
   principal y al cambiar UNA convención cada vez (el resto como en el principal): déficit (presupuesto equilibrado: el saldo de las
   AAPP se reparte por igual por persona), bienes públicos puros (coste marginal cero para los nacidos fuera), sociedades y capital
   (por persona en lugar de según rentas del capital), sanidad (uso observado por origen en la ENSE), indirectos (tasa uniforme),
   educación de los hijos nacidos en España (a los padres) y pensiones de los jubilados nacidos en el resto de la UE (cota: todas las
   pensiones de vejez y supervivencia que declaran en la ECV las pagaría otro Estado; el gasto D62 de España se repartiría entonces
   entre los demás en proporción a sus pensiones). La ECV pública no distingue el país pagador de la pensión: la cota es extrema
   (incluye pensiones españolas de quienes cotizaron en España).
2. Pensiones (output/f4/pensiones_kappa.csv): la regla mecánica hace el PIB proporcional a la población de 20-64 años (PIB endógeno
   con empleo y productividad medios). Variante con κ = empleo relativo × productividad relativa de la población adicional que aporta
   la migración (diferencia entre la variante base y la sin migración de EUROPOP2023), aplicada a sus trabajadores y a sus pensiones:
   κ ∈ {1; 0,89 (empleo 25-54 relativo); 0,73 (además salario bruto relativo)}. Sigue siendo contabilidad demográfica, no un efecto.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, Cifras  # noqa: E402
from f4_fiscal import GR, PRINCIPAL  # noqa: E402

O = OUT / "f4"
CAMBIOS = {"bienes": ("marginal", "bienes públicos a coste marginal cero para los nacidos fuera"),
           "capital": ("persona", "sociedades y capital por persona"), "sanidad": ("observado", "sanidad con uso observado por origen"),
           "indirectos": ("uniforme", "impuestos indirectos con tasa uniforme"),
           "educ_hijos": ("padres", "educación de los hijos nacidos en España asignada a los padres")}


def tabla() -> pd.DataFrame:
    rej = pd.read_csv(O / "rejilla.csv")
    sup = list(PRINCIPAL)
    es_p = np.logical_and.reduce([rej[k] == v for k, v in PRINCIPAL.items()])
    pr = rej[es_p].set_index("grupo")
    filas = [{"convencion": "principal", **{g: pr.loc[g, "neta_pc"] for g in GR}}]
    filas.append({"convencion": "presupuesto equilibrado (déficit repartido por igual)", **{g: pr.loc[g, "neta_pc_equilibrada"] for g in GR}})
    for k, (v, nombre) in CAMBIOS.items():
        m = np.logical_and.reduce([rej[s] == (v if s == k else PRINCIPAL[s]) for s in sup])
        x = rej[m].set_index("grupo")
        filas.append({"convencion": nombre, **{g: x.loc[g, "neta_pc"] for g in GR}})
    n = pd.read_csv(O / "neta_por_grupo_2024.csv").set_index("grupo")
    pens = (n.gas_vejez + n.gas_supervivencia) * n.poblacion
    t_ue = pens["Resto UE"]
    otros = pens.drop("Resto UE")
    alt = {"Resto UE": n.loc["Resto UE", "neta"] + t_ue / n.loc["Resto UE", "poblacion"]}
    for g in otros.index:
        alt[g] = n.loc[g, "neta"] - t_ue * otros[g] / otros.sum() / n.loc[g, "poblacion"]
    filas.append({"convencion": "cota: pensiones de los nacidos en el resto de la UE pagadas por otro Estado", **alt})
    t = pd.DataFrame(filas)
    pob = n.poblacion
    fuera = [g for g in GR if g != "España"]
    t["nacidos fuera"] = (t[fuera] * pob[fuera].to_numpy()).sum(axis=1) / pob[fuera].sum()
    for g in fuera + ["nacidos fuera"]:
        t[f"dif_nativos_{g}"] = t[g] - t["España"]
    return t


def pensiones_kappa() -> pd.DataFrame:
    import f4_pensiones as fp
    from f4_fiscal import cuentas
    c = cuentas(2024)
    gasto = (c["d62"]["GF1002"] + c["d62"]["GF1003"]) / c["pib"]
    d = fp.dependencia("ES").set_index(["projection", "TIME_PERIOD"])
    base = d.loc[("BSL", 2025), "tasa_dependencia"]
    filas = []
    for a in (2050, 2070):
        n0, b = d.loc[("NMIGR", a)], d.loc[("BSL", a)]
        for k, nom in ((1.0, "empleo y productividad medios (la regla mecánica)"), (0.89, "empleo relativo 25-54 (73,2/82,3)"),
                       (0.73, "empleo relativo × salario bruto relativo (0,89 × 0,82)")):
            pob = n0.pob_20_64 + k * (b.pob_20_64 - n0.pob_20_64)
            may = n0.pob_65_mas + k * (b.pob_65_mas - n0.pob_65_mas)
            g_bsl = 100 * gasto * (may / pob) / base
            g_sin = 100 * gasto * n0.tasa_dependencia / base
            filas.append({"anio": a, "kappa": k, "supuesto": nom, "gasto_base_kappa": g_bsl, "gasto_sin_migracion": g_sin,
                          "dif_sin_migracion_pp": g_sin - g_bsl})
    return pd.DataFrame(filas)


def main() -> int:
    cf = Cifras("f4_convenciones", "src/m1/f4_convenciones.py")
    t = tabla()
    t.to_csv(O / "sensibilidad_convenciones.csv", index=False)
    for g in GR + ["nacidos fuera"]:
        col = t[g]
        cf.add(f"F4_CONV_{g.replace(' ', '_')}", round(float(col.iloc[0]), 0), "€ por persona y año", f"Contribución neta por persona, nacidos "
               f"{'en ' + g if g != 'nacidos fuera' else 'fuera (conjunto)'}: principal e intervalo al cambiar una convención cada vez "
               f"({len(t) - 1} convenciones, incluida la cota de pensiones pagadas fuera; a posteriori)", "C2", "ECV, EPF, ENSE y cuentas de las AAPP",
               "2024", "España", g, ic_inf=round(float(col.min()), 0), ic_sup=round(float(col.max()), 0))
    claves = ["PRINCIPAL", "EQUILIBRADO", "BIENES_MARGINAL", "CAPITAL_PERSONA", "SANIDAD_OBSERVADA", "INDIRECTOS_UNIFORME",
              "HIJOS_PADRES", "PENS_UE_FUERA"]
    for clave, (_, r) in zip(claves, t.iterrows()):
        for g in GR + ["nacidos fuera"]:
            cf.add(f"F4_CONV_{clave}_{g.replace(' ', '_')}", round(float(r[g]), 0), "€ por persona y año", f"Contribución neta por persona, "
                   f"{g}, con la convención «{r.convencion}» (las demás como en el principal; a posteriori)", "C2",
                   "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", g)
            if g != "España":
                cf.add(f"F4_CONV_DIF_{clave}_{g.replace(' ', '_')}", round(float(r[f"dif_nativos_{g}"]), 0), "€ por persona y año",
                       f"Diferencia con los nacidos en España, {g}, convención «{r.convencion}» (a posteriori)", "C2",
                       "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", g)
    ue = t.set_index("convencion")["Resto UE"]
    cf.add("F4_CONV_PENS_UE", round(float(ue.iloc[-1]), 0), "€ por persona y año", "Cota: contribución neta por persona de los nacidos en el "
           "resto de la UE si todas las pensiones que declaran las pagara otro Estado (a posteriori)", "C2", "ECV y cuentas de las AAPP", "2024",
           "España", "Resto UE")
    x = pd.read_csv(O / "neta_nacimiento_x_nacionalidad_2024.csv")
    for r in x.dropna(subset=["neta_pc"]).itertuples():
        if r.nacimiento == "España" and r.nacionalidad3 != "España":
            continue      # nacidos en España con nacionalidad extranjera: casi todos menores (edad media < 13); se publican en el CSV
        cf.add(f"F4_CRUCE_{r.nacimiento.replace(' ', '_')}_NAC_{r.nacionalidad3.replace(' ', '_')}", round(float(r.neta_pc), 0),
               "€ por persona y año", f"Contribución neta por persona, nacidos en {r.nacimiento} con nacionalidad {r.nacionalidad3} (escenario "
               f"principal; edad media {r.edad_media:.0f} años; {int(r.n_muestral)} observaciones; a posteriori)", "C2",
               "ECV, EPF, ENSE y cuentas de las AAPP", "2024", "España", r.nacimiento)
    k = pensiones_kappa()
    k.to_csv(O / "pensiones_kappa.csv", index=False)
    x = k[k.anio == 2050].set_index("kappa").dif_sin_migracion_pp
    cf.add("F4_PEN_DIF_SIN_MIGRACION_KAPPA_2050", round(float(x[1.0]), 1), "pp del PIB", "Diferencia de gasto en pensiones / PIB en 2050 "
           "entre la variante sin migración y la base, con la población adicional ponderada por κ = empleo × productividad relativos "
           "(valor: κ = 1, la regla mecánica; intervalo: κ entre 0,73 y 1; contabilidad demográfica, a posteriori)", "C2",
           "Eurostat proj_23np y gov_10a_exp; EPA", "2050", "España", "todos", ic_inf=round(float(x.min()), 1), ic_sup=round(float(x.max()), 1))
    cf.escribir()
    pd.set_option("display.width", 250)
    print(t.round(0).to_string())
    print(k.round(2).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
