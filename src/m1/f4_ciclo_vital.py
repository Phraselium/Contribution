"""M1-F4 · Contribución fiscal neta a lo largo del ciclo vital (valor actual) por grupo y edad de llegada (C2: contabilidad con
supuestos explícitos; no identifica efectos). Sin red.

Perfiles por edad (tramos de 5 años) de la contabilidad estática de 2024 (output/f4/perfil_edad_2024.csv, escenario principal):
impuestos y cotizaciones, prestaciones no contributivas y de desempleo, pensiones (vejez y supervivencia), sanidad, educación y
bienes públicos. Para una persona que llega a la edad a0 en 2024 se proyecta cada año de vida hasta los 100 con:
- supervivencia de la tabla de mortalidad de España (Eurostat demo_mlifetable, último año);
- probabilidad anual de retorno o reemigración r (0 %, la tasa observada 2021-2024 en la Estadística de Migraciones y el doble);
- convergencia de impuestos y prestaciones no contributivas hacia el perfil de los nacidos en España de la misma edad: una fracción
  c (0, 0,5 o 1) de la brecha se cierra linealmente en 20 años de residencia;
- pensión futura = pensión media de los nacidos en España a esa edad × (contribución relativa acumulada en la vida laboral) ×
  min(1, años cotizables / 37), con suelo de pensión no contributiva (7.250 € al año, 2024) si residió al menos 10 años;
- crecimiento real de la productividad del 1 % anual y tasas reales de descuento del 2, 3 y 4 %;
- bienes públicos con coste medio o con coste marginal cero;
- gasto en especie ligado a la edad (sanidad, educación, protección social en especie, resto de servicios): perfil de los nacidos en
  España para todos (el perfil transversal de los nacidos fuera mayores de 65 tiene pocas observaciones).
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


def perfiles() -> dict[str, pd.DataFrame]:
    p = pd.read_csv(O / "perfil_edad_2024.csv")
    out = {}
    for g, x in p.groupby("grupo"):
        x = x.set_index("e").sort_index().drop(columns=["grupo"], errors="ignore").select_dtypes("number")
        idx = pd.DataFrame(index=range(0, 101))
        idx["e"] = (idx.index.to_series().clip(upper=85) // 5) * 5
        out[g] = idx.join(x, on="e").drop(columns=["e"]).interpolate(limit_direction="both")
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
    f = pd.read_csv(OUT / "f3" / "poblacion_flujos.csv")
    e = f[f.prov.isna() & (f.nacimiento == "Extranjero")].emigraciones.sum() / 4
    stock = pd.read_csv(OUT / "f3" / "poblacion_padron_nacional.csv")
    s = stock[(stock.origen_def == "nacimiento") & (stock.anio == stock.anio.max()) & (stock.grupo != "España")].valor.sum()
    return float(e / s)


def vida(a0: int, g: str, P: dict, q: pd.Series, r: float, c: float, dto: float, bienes: str, crec=0.01) -> dict:
    nat, imm = P["España"], P[g]
    sobrev, va_joven, va_mayor, contrib_rel_acum, anos_trab = 1.0, 0.0, 0.0, [], 0
    for x in range(a0, 101):
        y = x - a0
        k = min(1.0, y / 20) * c if g != "España" else 0.0
        mezcla = lambda cols: sum(imm.loc[x, v] + k * (nat.loc[x, v] - imm.loc[x, v]) for v in cols)  # noqa: E731
        imp = mezcla(TAX) if g != "España" else sum(nat.loc[x, v] for v in TAX)
        conv = mezcla(CONV) if g != "España" else sum(nat.loc[x, v] for v in CONV)
        if x < 65:
            rel = imp / max(sum(nat.loc[x, v] for v in TAX), 1.0)
            contrib_rel_acum.append(rel)
            anos_trab += 1 if x >= 18 else 0
            pens = sum((imm if g != "España" else nat).loc[x, v] for v in PENS)
        else:
            if g == "España":
                pens = sum(nat.loc[x, v] for v in PENS)
            else:
                fr = (np.mean(contrib_rel_acum) if contrib_rel_acum else 0.0) * min(1.0, anos_trab / 37)
                pens = max(sum(nat.loc[x, v] for v in PENS) * min(fr, 1.2), PNC if (65 - a0) >= 10 or y >= 10 else 0.0)
        edad_g = sum(nat.loc[x, v] for v in EDAD)   # gasto en especie por edad: mismo perfil para todos (criterio OCDE)
        bp = nat.loc[x, BP] if (bienes == "medio" or g == "España") else 0.0
        neta = imp - conv - pens - edad_g - bp
        fac = sobrev * ((1 + crec) / (1 + dto)) ** y
        if x < 65:
            va_joven += fac * neta
        else:
            va_mayor += fac * neta
        sobrev *= (1 - q.loc[x]) * (1 - (r if g != "España" else 0.0))
    return {"va_total": va_joven + va_mayor, "va_hasta_64": va_joven, "va_65_mas": va_mayor}


def main() -> int:
    cf = Cifras("f4_ciclo_vital", "src/m1/f4_ciclo_vital.py")
    P, q = perfiles(), supervivencia()
    r_obs = tasa_retorno()
    filas = []
    for g, a0, r, c, dto, bienes in itertools.product(["España", "Resto UE", "Resto del mundo"], [0, 20, 30, 40, 50],
                                                      [0.0, r_obs, 2 * r_obs], [0.0, 0.5, 1.0], [0.02, 0.03, 0.04],
                                                      ["medio", "marginal"]):
        if g == "España" and (r > 0 or c > 0):
            continue
        filas.append({"grupo": g, "edad_llegada": a0, "retorno": r, "convergencia": c, "descuento": dto, "bienes": bienes,
                      **vida(a0, g, P, q, r, c, dto, bienes)})
    v = pd.DataFrame(filas)
    v.to_csv(O / "ciclo_vital.csv", index=False)
    princ = v[(v.descuento == 0.03) & (v.bienes == "medio") & ((v.retorno == r_obs) | (v.grupo == "España")) &
              ((v.convergencia == 0.5) | (v.grupo == "España"))]
    princ.to_csv(O / "ciclo_vital_principal.csv", index=False)
    for g in ("Resto UE", "Resto del mundo"):
        for a0 in (20, 30, 40):
            x = v[(v.grupo == g) & (v.edad_llegada == a0)]
            p = princ[(princ.grupo == g) & (princ.edad_llegada == a0)].iloc[0]
            cf.add(f"F4_VA_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_total / 1e3, 0), "miles de € (VA en 2024)",
                   f"Valor actual de la contribución neta de por vida de una persona nacida en {g} que llega a los {a0} años "
                   f"(principal: descuento 3 %, convergencia 50 %, retorno observado {100 * r_obs:.1f} %, bienes públicos a coste medio; "
                   "intervalo: todas las combinaciones)", "C2", "Perfiles M1 (ECV, EPF, ENSE, cuentas AAPP) y Eurostat", "2024",
                   "España", g, ic_inf=round(x.va_total.min() / 1e3, 0), ic_sup=round(x.va_total.max() / 1e3, 0))
            cf.add(f"F4_VA_HASTA64_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_hasta_64 / 1e3, 0), "miles de € (VA)",
                   f"Parte del valor actual hasta los 64 años («población joven hoy»), llegada a los {a0}", "C2", "Perfiles M1", "2024",
                   "España", g)
            cf.add(f"F4_VA_65MAS_{g.replace(' ', '_')}_LLEGADA_{a0}", round(p.va_65_mas / 1e3, 0), "miles de € (VA)",
                   f"Parte del valor actual de 65 y más años (pensiones y sanidad futuras), llegada a los {a0}", "C2", "Perfiles M1", "2024",
                   "España", g)
    for a0 in (0, 20, 30, 40):
        p = princ[(princ.grupo == "España") & (princ.edad_llegada == a0)].iloc[0]
        cf.add(f"F4_VA_España_EDAD_{a0}", round(p.va_total / 1e3, 0), "miles de € (VA)",
               f"Valor actual de la contribución neta de la vida restante de una persona nacida en España de {a0} años (comparador)",
               "C2", "Perfiles M1", "2024", "España", "España")
    cf.add("F4_RETORNO_OBSERVADO", round(100 * r_obs, 2), "% anual", "Emigraciones anuales de nacidos fuera / población nacida fuera",
           "C1", "Estadística de Migraciones y padrón (INE)", "2021-2024", "España", "nacidos fuera")
    # qué supuestos cambian el signo
    s = []
    for g in ("Resto UE", "Resto del mundo"):
        for a0 in (20, 30, 40):
            x = v[(v.grupo == g) & (v.edad_llegada == a0)]
            for sup in ("retorno", "convergencia", "descuento", "bienes"):
                m = x.groupby(sup).va_total.mean()
                s.append({"grupo": g, "edad_llegada": a0, "supuesto": sup, **{f"va_medio_{k}": val for k, val in m.items()},
                          "signo_cambia_con_supuesto": bool((m > 0).any() and (m < 0).any())})
            s.append({"grupo": g, "edad_llegada": a0, "supuesto": "todos", "min": x.va_total.min(), "max": x.va_total.max(),
                      "signo_cambia_con_supuesto": bool(x.va_total.min() < 0 < x.va_total.max())})
    pd.DataFrame(s).to_csv(O / "ciclo_vital_signos.csv", index=False)
    cf.escribir()
    print(princ[["grupo", "edad_llegada", "va_total", "va_hasta_64", "va_65_mas"]].round(0).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
