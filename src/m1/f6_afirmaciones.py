"""M1-F6 · Síntesis crítica: fichas de las afirmaciones más repetidas del debate público sobre inmigración y economía, en los dos
sentidos, sin atribuirlas a nadie. Cada ficha: qué dice la contabilidad (A), qué dice la evidencia causal (B), qué depende de
supuestos y veredicto («se sostiene», «se sostiene con matices», «engañosa», «incorrecta», «no se puede saber») con su confianza.
Las cifras se citan con marcadores {{id}} de output/cifras_clave.csv y se sustituyen con render(). Mismas reglas para las
afirmaciones favorables y desfavorables. La evidencia causal propia de M1 (fase 5) está pendiente de la puerta prereg-m1: donde
se cita, es la literatura verificada (docs/literatura), no una estimación de M1.
Salidas: output/f6/afirmaciones.md y output/f6/afirmaciones.csv.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, Cifras, tabla_md  # noqa: E402

O = OUT / "f6"
CAUSAL_M1 = ("La estimación propia de M1 (fase 5) no se ha ejecutado: la puerta del pre-registro interno sigue cerrada porque la "
             "etiqueta prereg-m1 no está en un repositorio remoto. Lo que sigue es la literatura verificada, no M1.")

FICHAS = [
    {"id": "A1", "sentido": "desfavorable", "afirmacion": "Los inmigrantes viven de las ayudas: reciben más prestaciones que los nacidos en España.",
     "contabilidad": "Por persona, las prestaciones monetarias que reciben los nacidos fuera son menores en total: {{F6_PREST_MONETARIAS_PC_Resto_del_mundo}} € "
                     "(resto del mundo) y {{F6_PREST_MONETARIAS_PC_Resto_UE}} € (resto de la UE) frente a {{F6_PREST_MONETARIAS_PC_España}} € de los nacidos en "
                     "España (2024), sobre todo porque reciben pocas pensiones contributivas (perciben jubilación el {{F3_PRE_jubilacion_Resto_del_mundo}} % de los "
                     "mayores de 65 nacidos en el resto del mundo frente al {{F3_PRE_jubilacion_España}} %). En prestaciones no contributivas la relación se invierte: "
                     "viven en hogares que perciben rentas mínimas o IMV el {{F3_PRE_rentas_minimas_IMV_Resto_del_mundo}} % frente al {{F3_PRE_rentas_minimas_IMV_España}} %, "
                     "y ayudas a la vivienda el {{F3_PRE_ayuda_vivienda_Resto_del_mundo}} % frente al {{F3_PRE_ayuda_vivienda_España}} %; la diferencia en rentas mínimas "
                     "se mantiene a igual edad, sexo, educación y región ({{F3_PRE_BRECHA_perceptor_rentas_minimas_IMV_Resto_del_mundo_completo}} pp).",
     "causal": "No es una pregunta causal: es contabilidad.", "supuestos": "Prestaciones de la ECV calibradas a las cuentas públicas (COFOG); las del hogar se reparten por persona.",
     "veredicto": "engañosa", "confianza": "alta",
     "razon": "En el total por persona es falsa; es cierta solo para las prestaciones no contributivas, que son una parte pequeña del gasto."},
    {"id": "A2", "sentido": "desfavorable", "afirmacion": "La inmigración quita empleo a los españoles.",
     "contabilidad": "Entre 2014 y 2025 la ocupación media aumentó en {{F3_EMP_AUMENTO_OCUPADOS_2014_2025}} millones; el {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del "
                     "aumento corresponde a nacidos fuera y el resto a nacidos en España, cuya ocupación también creció. La tasa de empleo 16-64 de los nacidos en "
                     "España es del {{F3_EMP_TASA_España_2025}} % (2025).",
     "causal": CAUSAL_M1 + " En España, los trabajos con datos de provincias y celdas (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Banco de "
               "España, Informe Anual 2025) no encuentran efectos negativos significativos sobre el empleo de los nativos.",
     "supuestos": "La contabilidad no dice qué habría pasado sin inmigración.", "veredicto": "engañosa", "confianza": "media",
     "razon": "La contabilidad no la apoya y la literatura española no encuentra desplazamiento; falta la estimación propia de M1."},
    {"id": "A3", "sentido": "desfavorable", "afirmacion": "La inmigración hunde los salarios de los españoles.",
     "contabilidad": "Los extranjeros cobran por hora un {{F3_SAL_BRECHA_bruto_2022}} % menos que los españoles (bruto, 2022); a igual edad, sexo, estudios y "
                     "región la diferencia es {{F3_SAL_BRECHA_completo_2022}} %. Es una brecha entre grupos, no un efecto sobre los salarios de los nativos.",
     "causal": CAUSAL_M1 + " La literatura internacional verificada da efectos medios pequeños sobre los salarios nativos (Dustmann, Schönberg y Stuhler 2016) y "
               "la española no documenta caídas generalizadas; con datos públicos no hay salarios provinciales por nacionalidad (la AEAT no fue accesible).",
     "supuestos": "—", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Con datos públicos y sin la fase 5 no se puede estimar el efecto en España; la versión fuerte («hunde») no tiene apoyo en la literatura."},
    {"id": "A4", "sentido": "desfavorable", "afirmacion": "Los inmigrantes colapsan la sanidad pública.",
     "contabilidad": "A igual edad (25-54), los nacidos fuera declaran menos consultas de especialista, menos días de hospital y menos fármacos recetados, y algo "
                     "más de urgencias (ENSE 2017). Su estructura por edad es más joven: el {{F3_POB_65MAS_nacidos fuera_2025}} % tiene 65 o más años frente al "
                     "{{F3_POB_65MAS_España_2025}} % de los nacidos en España.",
     "causal": "P3 (listas de espera) no es estimable con datos públicos procesables (SISLE solo en PDF por CCAA) y la congestión local no se observa. "
               "Giuntella, Nicodemo y Vargas-Silva (2018) no encuentran más espera en el NHS inglés.",
     "supuestos": "Uso declarado en encuesta (2017).", "veredicto": "engañosa", "confianza": "media",
     "razon": "El uso por persona no es mayor; la congestión local en zonas concretas no se puede medir con datos públicos."},
    {"id": "A5", "sentido": "desfavorable", "afirmacion": "Los inmigrantes suponen un coste fiscal neto para España.",
     "contabilidad": "Contribución neta estática por persona en 2024 (todas las partidas, incluido el déficit): nacidos en España {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024}} € "
                     "(intervalo de supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}}]); resto de la UE "
                     "[{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}}] €; resto del mundo "
                     "[{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}] €.",
     "causal": "No es causal: contabilidad (capa C2).",
     "supuestos": "En el resto del mundo el signo depende del reparto de los bienes públicos (coste medio o marginal) y de a quién se asignan los hijos nacidos en "
                  "España (decisión D11: solo intervalos).",
     "veredicto": "no se puede saber", "confianza": "alta",
     "razon": "Para los nacidos en la UE es incorrecta en todos los supuestos; para los nacidos fuera de la UE el signo depende de supuestos defendibles."},
    {"id": "A6", "sentido": "desfavorable", "afirmacion": "La inmigración es la causa de la subida del precio de la vivienda.",
     "contabilidad": "Entre 2015 y 2022 el aumento de la población nacida fuera implica unos {{F3_VIV_DEMANDA_FUERA_2015_2022}} mil hogares a tasa de jefatura "
                     "constante, frente a {{F3_VIV_DEMANDA_ESPANA_2015_2022}} mil de los nacidos en España (cuya población se redujo); la formación de hogares por "
                     "envejecimiento no está incluida. Los nacidos fuera viven sobre todo de alquiler.",
     "causal": "P4 no se duplica en M1: el estudio de vivienda de Econometr-a no encuentra efectos que sobrevivan a la inferencia con pocos grupos; González y "
               "Ortega (2013) atribuyen a la inmigración una parte de la subida de 2000-2010.",
     "supuestos": "Tasa de jefatura constante por grupo y región.", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Es cierto que la población nacida fuera explica la mayor parte del aumento demográfico de la demanda de hogares; que sea «la causa» de los "
              "precios es una afirmación contrafactual no identificada con datos públicos recientes (mismo estándar que F2)."},
    {"id": "F1", "sentido": "favorable", "afirmacion": "Los inmigrantes pagan nuestras pensiones.",
     "contabilidad": "En la contabilidad de 2024 los nacidos fuera pagan cotizaciones e impuestos y reciben pocas pensiones; en la regla demográfica mecánica, sin "
                     "migración el gasto en pensiones de 2050 sería {{F4_PEN_EFECTO_SIN_MIGRACION_2050}} puntos de PIB mayor que en la proyección base "
                     "(Ageing Report 2024: {{F4_PEN_AR2024_MAS_MIGRACION_2050}} % con un tercio más de migración frente a {{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % "
                     "con un tercio menos).",
     "causal": "No es causal: contabilidad y proyección.",
     "supuestos": "Las cotizaciones de hoy generan derechos de pensión futuros: en el ciclo vital el valor actual de los nacidos fuera depende del retorno, la "
                  "convergencia y los bienes públicos (intervalos que contienen el cero).",
     "veredicto": "se sostiene con matices", "confianza": "media",
     "razon": "Alivian la financiación corriente y la tasa de dependencia, pero también acumulan derechos; no resuelven por sí solos la sostenibilidad."},
    {"id": "F2", "sentido": "favorable", "afirmacion": "Sin inmigrantes no habría crecido el empleo.",
     "contabilidad": "El {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del aumento de la ocupación de 2014-2025 y el {{F3_EMP_CONTRIB_HORAS_FUERA_2014_2025}} % del de las horas "
                     "corresponden a nacidos fuera.",
     "causal": "El contrafactual (qué empleo habría sin inmigración) no está identificado en M1; la contabilidad no lo dice.",
     "supuestos": "—", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Es cierto que la mayor parte del aumento del empleo corresponde a nacidos fuera, pero la afirmación es contrafactual («no habría crecido») y no "
              "está identificada (mismo estándar que A6)."},
    {"id": "F3", "sentido": "favorable", "afirmacion": "Los inmigrantes aportan más de lo que reciben.",
     "contabilidad": "Véase A5: positiva en todos los supuestos para los nacidos en la UE; intervalo que contiene el cero para los nacidos fuera de la UE.",
     "causal": "No es causal.", "supuestos": "Bienes públicos e hijos nacidos en España.", "veredicto": "no se puede saber", "confianza": "alta",
     "razon": "Generalizada a todos los inmigrantes no se sostiene con el mismo estándar que A5."},
    {"id": "F4", "sentido": "favorable", "afirmacion": "Los inmigrantes trabajan tanto como los españoles.",
     "contabilidad": "Tasa de empleo 16-64 de 2025: nacidos fuera {{F3_EMP_TASA_FUERA_2025}} % frente a {{F3_EMP_TASA_España_2025}} %; con variación interna amplia "
                     "(África {{F3_EMP_TASA_África_2025}} %, América Latina {{F3_EMP_TASA_América Latina_2025}} %). Tasa de paro de nacidos fuera "
                     "{{F3_EMP_PARO_FUERA_2025}} % frente a {{F3_EMP_PARO_España_2025}} %.",
     "causal": "No es causal.", "supuestos": "EPA; agrupación aproximada de los ocho grupos (D6).", "veredicto": "se sostiene con matices", "confianza": "alta",
     "razon": "En la media de la tasa de empleo sí; el paro es mayor y hay grupos con tasas de empleo muy inferiores."},
    {"id": "F5", "sentido": "favorable", "afirmacion": "A los inmigrantes se les paga menos por el mismo trabajo.",
     "contabilidad": "Brecha de salario por hora: {{F3_SAL_BRECHA_bruto_2022}} % bruta, {{F3_SAL_BRECHA_completo_2022}} % a igual edad, sexo, estudios y región y "
                     "{{F3_SAL_BRECHA_completo_inf_2022}} % si además se iguala ocupación, sector, contrato y jornada; alrededor de dos tercios es composición.",
     "causal": "Un resto no explicado no es por sí solo discriminación: faltan años de residencia, idioma, homologación de títulos y calidad del empleo.",
     "supuestos": "EES solo distingue nacionalidad.", "veredicto": "se sostiene con matices", "confianza": "media",
     "razon": "Queda una diferencia pequeña a igualdad de características observables; su causa no se puede saber con datos públicos."},
    {"id": "F6", "sentido": "favorable", "afirmacion": "Los inmigrantes hacen los trabajos que los españoles no quieren.",
     "contabilidad": "Los nacidos fuera están sobrerrepresentados en ocupaciones elementales y tienen más sobrecualificación (output/f3/empleo_nacional.csv).",
     "causal": CAUSAL_M1 + " Peri y Sparber (2009) y Amuedo-Dorantes y De la Rica documentan especialización de tareas entre nativos e inmigrantes.",
     "supuestos": "—", "veredicto": "se sostiene con matices", "confianza": "baja",
     "razon": "Hay especialización por ocupaciones; «que no quieren» es una afirmación sobre preferencias que los datos no miden."},
]


def render(texto: str, cifras: pd.DataFrame) -> str:
    c = cifras.set_index("id")

    def fmt(v):
        if pd.isna(v):
            return "n. d."
        v = float(v)
        s = f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.1f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")

    def rep(m):
        k, parte = m.group(1), m.group(2)
        if k not in c.index:
            return f"[FALTA CIFRA: {k}]"
        col = {"inf": "ic_inf", "sup": "ic_sup"}.get(parte, "valor")
        return fmt(c.loc[k, col])
    return re.sub(r"\{\{([^}:]+)(?::(inf|sup))?\}\}", rep, texto)


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f6_afirmaciones", "src/m1/f6_afirmaciones.py")
    r = pd.read_csv(OUT / "f4" / "neta_por_grupo_2024.csv").set_index("grupo")
    monet = ["gas_desempleo", "gas_vejez", "gas_supervivencia", "gas_enfermedad_incapacidad", "gas_familia", "gas_exclusion_social", "gas_vivienda"]
    for g in r.index:
        cf.add(f"F6_PREST_MONETARIAS_PC_{g.replace(' ', '_')}", round(float(r.loc[g, monet].sum()), 0), "€ por persona y año",
               f"Prestaciones monetarias por persona (calibradas a COFOG), nacidos en {g}", "C2", "ECV (INE) y Eurostat COFOG", "2024", "España", g)
    cf.escribir()
    import cifras as cmod
    todas = cmod.consolidar()
    filas, md = [], ["# Afirmaciones del debate y su veredicto (fase 6)", "",
                     "Se evalúan afirmaciones, no personas ni grupos. Las favorables y las desfavorables a la inmigración siguen las mismas reglas.", ""]
    for f in FICHAS:
        md += [f"## {f['id']} · «{f['afirmacion']}»", f"- Sentido: {f['sentido']}.",
               f"- Contabilidad: {render(f['contabilidad'], todas)}", f"- Evidencia causal: {render(f['causal'], todas)}",
               f"- Depende de supuestos: {render(f['supuestos'], todas)}",
               f"- **Veredicto: {f['veredicto']}** (confianza {f['confianza']}). {f['razon']}", ""]
        filas.append({k: f[k] for k in ("id", "sentido", "afirmacion", "veredicto", "confianza", "razon")})
    t = pd.DataFrame(filas)
    t.to_csv(O / "afirmaciones.csv", index=False)
    bal = t.groupby(["sentido", "veredicto"]).size().unstack(fill_value=0)
    md += ["## Balance por sentido", "", tabla_md(bal), ""]
    (O / "afirmaciones.md").write_text("\n".join(md), encoding="utf-8")
    print(bal)
    print("faltan cifras:", sum("[FALTA CIFRA" in x for x in md))
    return 0 if np.all(["[FALTA CIFRA" not in x for x in md]) else 1


if __name__ == "__main__":
    sys.exit(main())
