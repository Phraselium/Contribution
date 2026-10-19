"""M1-F4 · Contribución fiscal neta a lo largo del ciclo vital (valor actual) por grupo y edad de llegada (C2: contabilidad con
supuestos explícitos; no identifica efectos). Sin red.

Perfiles por edad (tramos de 5 años) de la contabilidad estática de 2024 (output/f4/perfil_edad_2024.csv, escenario principal):
impuestos y cotizaciones, prestaciones no contributivas y de desempleo, pensiones (vejez y supervivencia), sanidad, educación y
bienes públicos. Los tramos con menos de 50 observaciones (suprimidos) NO se interpolan: se usa el perfil de los nacidos en España de
esa edad escalado por la razón grupo/nativos del tramo observado más próximo, bloque a bloque (impuestos, prestaciones, pensiones).
Para una persona que llega a la edad a0 en 2024 se proyecta cada año de vida hasta los 100 con:
- supervivencia de la tabla de mortalidad de España (Eurostat demo_mlifetable, último año);
- salida (retorno o reemigración) con riesgo que decrece con la duración de la residencia: riesgos relativos 1; 0,5; 0,25; 0,1 en
  0-4, 5-9, 10-19 y 20+ años (supuesto), calibrados para que el riesgo medio sobre el stock por años de residencia (EPA) iguale la
  tasa observada: emigraciones de nacidos fuera 2021-2024 (Estadística de Migraciones) / stock medio de nacidos fuera del mismo
  periodo (ECP). La tasa observada incluye bajas por caducidad de inscripciones de extranjeros no comunitarios sin residencia
  permanente, que no siempre son salidas reales: es una cota superior de las salidas. Variantes: sin salida, la mitad del riesgo y
  riesgo constante (el supuesto anterior);
- quien sale conserva la pensión contributiva devengada (exportable) y la cobra desde los 65 con la misma mortalidad, sin más flujos;
- convergencia de impuestos y prestaciones no contributivas hacia el perfil de los nacidos en España de la misma edad: una fracción
  c (0, 0,5 o 1) de la brecha se cierra linealmente en 20 años. El perfil transversal por edad de los nacidos fuera ya mezcla
  duraciones de residencia (contiene convergencia), por lo que c > 0 la contaría dos veces: el principal es c = 0;
- pensión contributiva = pensión media de los nacidos en España a esa edad × (contribución relativa media en la vida laboral) ×
  min(1, años cotizables / 37), solo con al menos 15 años cotizables; suelo de pensión no contributiva (7.250 € al año, 2024) para
  quien reside y residió al menos 10 años;
- crecimiento real de la productividad del 1 % anual y tasas reales de descuento del 2, 3 y 4 %;
- bienes públicos con coste medio o con coste marginal cero (el cero traslada su coste a los demás residentes);
- gasto en especie ligado a la edad (sanidad, educación, protección social en especie, resto de servicios): perfil de los nacidos en
  España para todos (D12).
No se incluyen los descendientes (sus impuestos y su educación), que en la contabilidad estática son el componente que más pesa.
Comparadores: un nacido en España de la misma edad a0 (vida restante) y un recién nacido en España.
Descomposición: valor actual de los años hasta los 64 («población joven hoy») frente al de 65 y más (pensiones y sanidad futuras).
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, RAW, Cifras  # noqa: E402

O = OUT / "f4"
PNC = 7250.0
TAX = ["ing_irpf_cotiz_trab", "ing_cotiz_empresa", "ing_iva", "ing_especiales", "ing_vivienda_ibi", "ing_sociedades_capital"]
CONV = ["gas_desempleo", "gas_exclusion_social", "gas_vivienda", "gas_familia", "gas_enfermedad_incapacidad"]
PENS = ["gas_vejez", "gas_supervivencia"]
EDAD = ["gas_sanidad", "gas_educacion", "gas_prot_social_especie", "gas_otras_prestaciones", "gas_resto_servicios"]
BP = "gas_bienes_publicos_puros"


OTROS = ["ing_otros_ingresos"]   # ingresos no tributarios repartidos por persona (contrapartida de gas_resto_servicios); faltaban en la
#                                  primera versión del ciclo vital, lo que añadía su cuantía al déficit cada año (corregido en la ronda 3)
BLOQUES = {"tax": TAX, "conv": CONV, "pens": PENS}   # OTROS no se escala: es igual por persona para todos
DUR = [(0, 5, 1.0), (5, 10, 0.5), (10, 20, 0.25), (20, 200, 0.1)]   # riesgos relativos de salida por años de residencia


def perfiles(escalar: bool = True) -> dict[str, pd.DataFrame]:
    p = pd.read_csv(O / "perfil_edad_2024.csv")
    p = p[p.e >= 0]
    num = [c for c in p.columns if c not in ("grupo", "e", "n_muestral") and pd.api.types.is_numeric_dtype(p[c])]
    nat = p[p.grupo == "España"].set_index("e")[num].sort_index()
    out = {}
    for g, x in p.groupby("grupo"):
        x = x.set_index("e").sort_index()
        x = x[num].where(x.n_muestral >= 50).reindex(nat.index)
        obs = x.dropna(how="all").index
        for e in x.index[x.isna().all(axis=1)]:          # tramo suprimido: perfil nativo escalado por el tramo observado más próximo
            e0 = min(obs, key=lambda o: (abs(o - e), o))
            for cols in BLOQUES.values():
                den = nat.loc[e0, cols].sum()
                x.loc[e, cols] = nat.loc[e, cols] * (x.loc[e0, cols].sum() / den if (den > 0 and escalar) else 1.0)
            otros = [c for c in num if not any(c in b for b in BLOQUES.values())]
            x.loc[e, otros] = nat.loc[e, otros]
        idx = pd.DataFrame(index=range(0, 101))
        idx["e"] = (idx.index.to_series().clip(upper=85) // 5) * 5
        out[g] = idx.join(x, on="e").drop(columns=["e"])
    return out


def supervivencia() -> pd.Series:
    t = pd.read_csv(RAW / "eurostat" / "demo_mlifetable_ES.csv.gz")
    t = t[t.TIME_PERIOD == t.TIME_PERIOD.max()].copy()
    t["e"] = pd.to_numeric(t.age.str.replace("Y_LT1", "Y0").str.replace("Y_GE85", "Y85").str.replace("Y_OPEN", "Y100")
                           .str.extract(r"(\d+)")[0], errors="coerce")
    q = t.dropna(subset=["e"]).groupby("e").OBS_VALUE.mean().reindex(range(0, 101)).ffill().clip(0, 1)
    q.iloc[-1] = 1.0
    return q


def tasa_retorno() -> float:
    """Emigraciones anuales de nacidos fuera / stock medio de nacidos fuera en el mismo año (ECP a 1 de enero de t y t+1)."""
    f = pd.read_csv(OUT / "f3" / "poblacion_flujos.csv")
    e = f[f.prov.isna() & (f.nacimiento == "Extranjero")].set_index("anio").emigraciones
    s = pd.read_csv(OUT / "f3" / "poblacion_ecp_nacional.csv").set_index("anio").Extranjero
    return float(np.mean([e[a] / ((s[a] + s[a + 1]) / 2) for a in e.index]))


def riesgo_inicial(r_obs: float) -> float:
    """h0 tal que la media del riesgo por duración, ponderada por el stock según años de residencia (EPA), iguale r_obs."""
    res = pd.read_csv(OUT / "f3" / "poblacion_residencia.csv").groupby("resid").pob.sum()
    w = res / res.sum()
    rel = {"0-4": 1.0, "5-9": 0.5, "10-19": 0.25, "20+": 0.1}
    return float(r_obs / sum(w[k] * v for k, v in rel.items()))


def riesgo(y: int, modo: str, r_obs: float, h0: float) -> float:
    if modo == "ninguno":
        return 0.0
    if modo == "constante":
        return r_obs
    h = h0 * next(v for a, b, v in DUR if a <= y < b)
    return h / 2 if modo == "decreciente_mitad" else h


def vida(a0: int, g: str, P: dict, q: pd.Series, modo: str, c: float, dto: float, bienes: str, r_obs: float, h0: float,
         crec=0.01, ajuste_pc=0.0, anos_min=15, suelo=True) -> dict:
    """ajuste_pc: cantidad por persona y año sumada a la contribución neta de quien reside (presupuesto equilibrado: menos el saldo
    medio por persona); anos_min: años cotizables mínimos para la pensión contributiva; suelo: pensión no contributiva."""
    nat, imm = P["España"], P[g]
    nativo = g == "España"
    sobrev, va_joven, va_mayor, contrib_rel_acum, anos_trab = 1.0, 0.0, 0.0, [], 0
    derechos_fuera = 0.0     # masa superviviente de quienes salieron × fracción de pensión devengada
    for x in range(a0, 101):
        y = x - a0
        k = 0.0 if nativo else min(1.0, y / 20) * c
        mezcla = lambda cols: sum(imm.loc[x, v] + k * (nat.loc[x, v] - imm.loc[x, v]) for v in cols)  # noqa: E731
        imp = sum(nat.loc[x, v] for v in TAX) if nativo else mezcla(TAX)
        otros = sum((nat if nativo else imm).loc[x, v] for v in OTROS)
        conv = sum(nat.loc[x, v] for v in CONV) if nativo else mezcla(CONV)
        fr = (np.mean(contrib_rel_acum) if contrib_rel_acum else 0.0) * min(1.0, anos_trab / 37) if anos_trab >= anos_min else 0.0
        fr = min(fr, 1.2)
        pens_nat = sum(nat.loc[x, v] for v in PENS)
        if x < 65:
            contrib_rel_acum.append(imp / max(sum(nat.loc[x, v] for v in TAX), 1.0))
            anos_trab += 1 if x >= 18 else 0
            pens = sum((nat if nativo else imm).loc[x, v] for v in PENS)
        else:
            pens = pens_nat if nativo else max(pens_nat * fr, PNC if (y >= 10 and suelo) else 0.0)
        edad_g = sum(nat.loc[x, v] for v in EDAD)   # gasto en especie por edad: mismo perfil para todos (criterio OCDE)
        # con coste marginal cero para los nacidos fuera, el nativo asume su parte (traslado medido en la contabilidad estática)
        bp = nat.loc[x, BP] if bienes == "medio" else (nat.loc[x, BP] + TRASLADO_BP["valor"] if nativo else 0.0)
        neta = sobrev * (imp + otros - conv - pens - edad_g - bp + ajuste_pc) - (derechos_fuera * pens_nat if x >= 65 else 0.0)
        fac = ((1 + crec) / (1 + dto)) ** y
        if x < 65:
            va_joven += fac * neta
        else:
            va_mayor += fac * neta
        h = 0.0 if nativo else riesgo(y, modo, r_obs, h0)
        derechos_fuera = derechos_fuera * (1 - q.loc[x]) + sobrev * (1 - q.loc[x]) * h * fr
        sobrev *= (1 - q.loc[x]) * (1 - h)
    return {"va_total": va_joven + va_mayor, "va_hasta_64": va_joven, "va_65_mas": va_mayor}


MODOS = ["ninguno", "decreciente_mitad", "decreciente", "constante"]
TRASLADO_BP = {"valor": 0.0}


def traslado_bienes() -> float:
    """Gasto adicional en bienes públicos puros por nativo y año cuando a los nacidos fuera se les imputa coste marginal cero (media de
    la rejilla de la contabilidad estática)."""
    r = pd.read_csv(O / "rejilla.csv")
    x = r[r.grupo == "España"].copy()
    cols = ["calibrar", "sanidad", "educ_hijos", "indirectos", "capital"]
    m = x.pivot_table(index=cols, columns="bienes", values="neta_pc")
    return float(-(m["marginal"] - m["medio"]).mean())


def main() -> int:
    cf = Cifras("f4_ciclo_vital", "src/m1/f4_ciclo_vital.py")
    P, q = perfiles(), supervivencia()
    r_obs = tasa_retorno()
    h0 = riesgo_inicial(r_obs)
    TRASLADO_BP["valor"] = traslado_bienes()
    pe = pd.read_csv(O / "perfil_edad_2024.csv")
    pe = pe[pe.grupo == "España"]
    cf.add("F4_OTROS_INGRESOS_PC", round(float(np.average(pe.ing_otros_ingresos, weights=pe.n_muestral)), 0), "€ por persona y año",
           "Ingresos no tributarios repartidos por persona en la contabilidad estática (ventas, rentas de la propiedad y otros)", "C2",
           "Eurostat gov_10a_main", "2024", "España", "todos")
    cf.add("F4_TRASLADO_BIENES_NAT", round(TRASLADO_BP["valor"], 0), "€ por persona y año", "Gasto adicional en bienes públicos puros por "
           "nativo y año cuando a los nacidos fuera se les imputa coste marginal cero (aplicado al comparador nativo del ciclo vital)", "C2",
           "ECV y cuentas de las AAPP", "2024", "España", "España")
    filas = []
    for g, a0, modo, c, dto, bienes in itertools.product(["España", "Resto UE", "Resto del mundo"], [0, 20, 30, 40, 50], MODOS,
                                                         [0.0, 0.5, 1.0], [0.02, 0.03, 0.04], ["medio", "marginal"]):
        if g == "España" and (modo != "ninguno" or c > 0):
            continue
        filas.append({"grupo": g, "edad_llegada": a0, "retorno": modo, "convergencia": c, "descuento": dto, "bienes": bienes,
                      **vida(a0, g, P, q, modo, c, dto, bienes, r_obs, h0)})
    v = pd.DataFrame(filas)
    v.to_csv(O / "ciclo_vital.csv", index=False)
    nat = v.grupo == "España"
    princ = v[(v.descuento == 0.03) & (v.bienes == "medio") & ((v.retorno == "decreciente") | nat) & (v.convergencia == 0.0)]
    princ.to_csv(O / "ciclo_vital_principal.csv", index=False)
    txt = (f"principal: descuento 3 %, sin convergencia adicional, salida con riesgo decreciente calibrado a {100 * r_obs:.1f} % anual, "
           "pensiones devengadas exportables, bienes públicos a coste medio; intervalo: las 24 combinaciones sin convergencia adicional, "
           "porque el perfil transversal ya la contiene)")
    for g in ("Resto UE", "Resto del mundo"):
        for a0 in (0, 20, 30, 40, 50):
            xc = v[(v.grupo == g) & (v.edad_llegada == a0)]
            x = xc[xc.convergencia == 0]
            p = princ[(princ.grupo == g) & (princ.edad_llegada == a0)].iloc[0]
            cf.add(f"F4_VA_CONVERG_{g.replace(' ', '_')}_LLEGADA_{a0}", round(xc[xc.convergencia > 0].va_total.median() / 1e3, 0),
                   "miles de € (VA)", f"Sensibilidad: combinaciones con convergencia de 0,5 o 1 (cuentan dos veces la convergencia), llegada a "
                   f"los {a0}: mediana e intervalo", "C2", "Perfiles M1", "2024", "España", g,
                   ic_inf=round(xc[xc.convergencia > 0].va_total.min() / 1e3, 0), ic_sup=round(xc[xc.convergencia > 0].va_total.max() / 1e3, 0))
            cf.add(f"F4_VA_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_total / 1e3, 0), "miles de € (VA en 2024)",
                   f"Valor actual de la contribución neta de por vida de una persona nacida en {g} que llega a los {a0} años ({txt})",
                   "C2", "Perfiles M1 (ECV, EPF, ENSE, cuentas AAPP) y Eurostat", "2024", "España", g,
                   ic_inf=round(x.va_total.min() / 1e3, 0), ic_sup=round(x.va_total.max() / 1e3, 0))
            if a0 == 0:
                continue
            cf.add(f"F4_VA_HASTA64_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_hasta_64 / 1e3, 0), "miles de € (VA)",
                   f"Parte del valor actual hasta los 64 años («población joven hoy»), llegada a los {a0}", "C2", "Perfiles M1", "2024",
                   "España", g)
            cf.add(f"F4_VA_65MAS_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_65_mas / 1e3, 0), "miles de € (VA)",
                   f"Parte del valor actual de 65 y más años (pensiones y sanidad futuras, también las exportadas), llegada a los {a0}",
                   "C2", "Perfiles M1", "2024", "España", g)
            nat_a = princ[nat & (princ.edad_llegada == a0)].iloc[0]
            dif = x.merge(v[nat & (v.edad_llegada == a0)][["descuento", "bienes", "va_total"]], on=["descuento", "bienes"],
                          suffixes=("", "_nat"))
            dif = dif.va_total - dif.va_total_nat
            cf.add(f"F4_VA_DIF_NAT_{g.replace(' ', '_')}_LLEGADA_{a0}", round((p.va_total - nat_a.va_total) / 1e3, 0),
                   "miles de € (VA)", f"Diferencia con un nacido en España de la misma edad (vida restante), llegada a los {a0}",
                   "C2", "Perfiles M1", "2024", "España", g, ic_inf=round(dif.min() / 1e3, 0), ic_sup=round(dif.max() / 1e3, 0))
            difc = xc[xc.convergencia > 0].merge(v[nat & (v.edad_llegada == a0)][["descuento", "bienes", "va_total"]],
                                                 on=["descuento", "bienes"], suffixes=("", "_nat"))
            difc = difc.va_total - difc.va_total_nat
            cf.add(f"F4_VA_DIF_NAT_CONV_{g.replace(' ', '_')}_LLEGADA_{a0}", round(float(difc.median()) / 1e3, 0), "miles de € (VA)",
                   f"Diferencia con un nacido en España de la misma edad en las combinaciones con convergencia de 0,5 o 1 (sensibilidad), llegada a "
                   f"los {a0}: mediana e intervalo", "C2", "Perfiles M1", "2024", "España", g,
                   ic_inf=round(difc.min() / 1e3, 0), ic_sup=round(difc.max() / 1e3, 0))
            if a0 == 50:
                continue
            mit = x[(x.retorno == "decreciente_mitad") & (x.convergencia == 0) & (x.descuento == 0.03) & (x.bienes == "medio")].iloc[0]
            cf.add(f"F4_VA_MITAD_SALIDA_{g.replace(' ', '_')}_LLEGADA_{a0}", round(mit.va_total / 1e3, 0), "miles de € (VA)",
                   f"Como el principal pero con la mitad del riesgo de salida (por si las bajas por caducidad no son salidas reales), "
                   f"llegada a los {a0}", "C2", "Perfiles M1", "2024", "España", g)
            ret0 = x[(x.retorno == "ninguno") & (x.convergencia == 0) & (x.descuento == 0.03) & (x.bienes == "medio")].iloc[0]
            cf.add(f"F4_VA_SIN_SALIDA_{g.replace(' ', '_')}_LLEGADA_{a0}", round(ret0.va_total / 1e3, 0), "miles de € (VA)",
                   f"Como el principal pero sin salidas (toda la vida en España), llegada a los {a0}", "C2", "Perfiles M1", "2024",
                   "España", g)
    for a0 in (0, 20, 30, 40):
        p = princ[nat & (princ.edad_llegada == a0)].iloc[0]
        x = v[nat & (v.edad_llegada == a0)]
        cf.add(f"F4_VA_España_EDAD_{a0}", round(p.va_total / 1e3, 0), "miles de € (VA)",
               f"Valor actual de la contribución neta de la vida restante de una persona nacida en España de {a0} años (comparador; "
               "intervalo: descuento y bienes públicos)", "C2", "Perfiles M1", "2024", "España", "España",
               ic_inf=round(x.va_total.min() / 1e3, 0), ic_sup=round(x.va_total.max() / 1e3, 0))
    cf.add("F4_RETORNO_OBSERVADO", round(100 * r_obs, 2), "% anual", "Emigraciones anuales de nacidos fuera / stock medio de nacidos "
           "fuera del mismo año (incluye bajas por caducidad: cota superior de las salidas)", "C1",
           "Estadística de Migraciones y ECP (INE)", "2021-2024", "España", "nacidos fuera")
    cf.add("F4_RIESGO_SALIDA_0_4", round(100 * h0, 1), "% anual", "Riesgo anual de salida en los primeros 5 años de residencia "
           "(calibrado; supuesto de riesgos relativos 1; 0,5; 0,25; 0,1)", "C2", "Estadística de Migraciones, ECP y EPA (INE)",
           "2021-2024", "España", "nacidos fuera")
    # qué supuestos cambian el signo (D11)
    s = []
    for g in ("Resto UE", "Resto del mundo"):
        for a0 in (0, 20, 30, 40, 50):
            xc = v[(v.grupo == g) & (v.edad_llegada == a0)]
            x = xc[xc.convergencia == 0]
            for sup in ("retorno", "descuento", "bienes"):
                m = x.groupby(sup).va_total.mean()
                s.append({"grupo": g, "edad_llegada": a0, "supuesto": sup, **{f"va_medio_{k}": val for k, val in m.items()},
                          "signo_cambia_con_supuesto": bool((m > 0).any() and (m < 0).any())})
            s.append({"grupo": g, "edad_llegada": a0, "supuesto": "todos", "min": x.va_total.min(), "max": x.va_total.max(),
                      "cuota_positivas": float((x.va_total > 0).mean()),
                      "signo_cambia_con_supuesto": bool(x.va_total.min() < 0 < x.va_total.max())})
            s.append({"grupo": g, "edad_llegada": a0, "supuesto": "todos, con convergencia (sensibilidad)", "min": xc.va_total.min(),
                      "max": xc.va_total.max(), "cuota_positivas": float((xc.va_total > 0).mean()),
                      "signo_cambia_con_supuesto": bool(xc.va_total.min() < 0 < xc.va_total.max())})
    pd.DataFrame(s).to_csv(O / "ciclo_vital_signos.csv", index=False)
    sensibilidad_principal(cf, P, q, r_obs, h0)
    cf.escribir()
    print(f"r_obs={r_obs:.4f} h0={h0:.4f}")
    print(princ[["grupo", "edad_llegada", "va_total", "va_hasta_64", "va_65_mas"]].round(0).to_string())
    return 0


def sensibilidad_principal(cf, P, q, r_obs, h0) -> None:
    """Variantes del escenario principal fuera de la rejilla D11: presupuesto equilibrado, imputación de los tramos suprimidos de
    la UE y reglas de pensiones."""
    r = pd.read_csv(O / "neta_por_grupo_2024.csv")
    saldo = float(np.average(r.neta, weights=r.poblacion))
    P1 = perfiles(escalar=False)
    base = dict(modo="decreciente", c=0.0, dto=0.03, bienes="medio", r_obs=r_obs, h0=h0)
    filas = []
    for g in ("España", "Resto UE", "Resto del mundo"):
        for a0 in (0, 20, 30, 40):
            b = dict(base, modo="ninguno") if g == "España" else base
            filas.append({"grupo": g, "edad_llegada": a0, "variante": "principal", "va_total": vida(a0, g, P, q, **b)["va_total"]})
            filas.append({"grupo": g, "edad_llegada": a0, "variante": "presupuesto equilibrado",
                          "va_total": vida(a0, g, P, q, **b, ajuste_pc=-saldo)["va_total"]})
            if g != "España":
                filas.append({"grupo": g, "edad_llegada": a0, "variante": "tramos suprimidos con perfil nativo sin escalar",
                              "va_total": vida(a0, g, P1, q, **b)["va_total"]})
                filas.append({"grupo": g, "edad_llegada": a0, "variante": "pensión contributiva sin mínimo de 15 años",
                              "va_total": vida(a0, g, P, q, **b, anos_min=0)["va_total"]})
                filas.append({"grupo": g, "edad_llegada": a0, "variante": "sin suelo de pensión no contributiva",
                              "va_total": vida(a0, g, P, q, **b, suelo=False)["va_total"]})
                filas.append({"grupo": g, "edad_llegada": a0, "variante": "mitad de salidas y sin mínimo de 15 años",
                              "va_total": vida(a0, g, P, q, **dict(b, modo="decreciente_mitad"), anos_min=0)["va_total"]})
    s = pd.DataFrame(filas)
    s.to_csv(O / "ciclo_vital_sensibilidad.csv", index=False)
    k = s.set_index(["grupo", "edad_llegada", "variante"]).va_total
    for g in ("España", "Resto UE", "Resto del mundo"):
        for a0 in (0, 30):
            cf.add(f"F4_VA_EQUILIBRADO_{g.replace(' ', '_')}_{a0}", round(k[(g, a0, "presupuesto equilibrado")] / 1e3, 0),
                   "miles de € (VA)", f"Valor actual del escenario principal con presupuesto equilibrado (se suma cada año el saldo medio "
                   f"por persona de 2024, {f'{-saldo:,.0f}'.replace(',', '.')} €), {g}, {'nacimiento' if a0 == 0 else f'llegada o edad {a0}'}",
                   "C2", "Perfiles M1", "2024", "España", g)
    for g in ("Resto UE", "Resto del mundo"):
        v = k.xs((g, 30), level=("grupo", "edad_llegada"))
        cf.add(f"F4_VA_IMPUT_UE_{g.replace(' ', '_')}_30", round(v["tramos suprimidos con perfil nativo sin escalar"] / 1e3, 0),
               "miles de € (VA)", f"Principal con los tramos de edad suprimidos (< 50 observaciones) rellenados con el perfil nativo sin "
               f"escalar, {g}, llegada a los 30", "C2", "Perfiles M1", "2024", "España", g)
        cf.add(f"F4_VA_SIN_MIN15_{g.replace(' ', '_')}_30", round(v["pensión contributiva sin mínimo de 15 años"] / 1e3, 0),
               "miles de € (VA)", f"Principal sin el mínimo de 15 años cotizados para la pensión contributiva, {g}, llegada a los 30",
               "C2", "Perfiles M1", "2024", "España", g)
        cf.add(f"F4_VA_CONJUNTA_{g.replace(' ', '_')}_30", round(v["mitad de salidas y sin mínimo de 15 años"] / 1e3, 0), "miles de € (VA)",
               f"Principal con la mitad del riesgo de salida y sin el mínimo de 15 años cotizados a la vez, {g}, llegada a los 30", "C2",
               "Perfiles M1", "2024", "España", g)
        cf.add(f"F4_VA_SIN_SUELO_{g.replace(' ', '_')}_30", round(v["sin suelo de pensión no contributiva"] / 1e3, 0),
               "miles de € (VA)", f"Principal sin el suelo de pensión no contributiva, {g}, llegada a los 30", "C2", "Perfiles M1", "2024",
               "España", g)


if __name__ == "__main__":
    sys.exit(main())
