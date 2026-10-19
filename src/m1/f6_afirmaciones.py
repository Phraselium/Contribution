"""M1-F6 · Síntesis crítica: fichas de las afirmaciones más repetidas del debate público sobre inmigración y economía, en los dos
sentidos, sin atribuirlas a nadie. Cada ficha: qué dice la contabilidad (A), qué dice la evidencia causal (B), qué depende de
supuestos y veredicto («se sostiene», «se sostiene con matices», «engañosa», «incorrecta», «no se puede saber») con su confianza.
Las cifras se citan con marcadores {{id}} de output/cifras_clave.csv y se sustituyen con render(). Mismas reglas para las
afirmaciones favorables y desfavorables. La evidencia causal propia de M1 es la de la fase 5 pre-registrada (output/f5); la
literatura verificada (docs/literatura) se cita aparte.
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
CAUSAL_M1 = ("Estimación propia de M1 (fase 5, pre-registrada; corregido un error de código en el control de cuotas que cambió los signos): "
             "la primera etapa del shift-share provincial es fuerte al nivel del shock (F = {{F5_P1_F_SHOCK}}), pero los conjuntos AKM0 no están "
             "acotados, de modo que todas las preguntas causales quedan en ASOCIACIÓN y ninguna rechaza el cero con la corrección por multiplicidad.")

FICHAS = [
    {"id": "A1", "sentido": "desfavorable", "afirmacion": "Los inmigrantes viven de las ayudas: reciben más prestaciones que los nacidos en España.",
     "contabilidad": "Por persona, las prestaciones monetarias que reciben los nacidos fuera son menores en total: {{F6_PREST_MONETARIAS_PC_Resto_del_mundo}} € "
                     "(resto del mundo) y {{F6_PREST_MONETARIAS_PC_Resto_UE}} € (resto de la UE) frente a {{F6_PREST_MONETARIAS_PC_España}} € de los nacidos en "
                     "España (2024), sobre todo porque reciben pocas pensiones contributivas (perciben jubilación o viven en un hogar que la "
                     "percibe el {{F3_PRE_jubilacion_Resto_del_mundo}} % de los mayores de 65 nacidos en el resto del mundo frente al {{F3_PRE_jubilacion_España}} %). A"
                     " igual edad y sexo siguen recibiendo menos: "
                     "{{F4_PREST_MONET_EST_DIF_Resto_del_mundo_2024}} € (resto del mundo) y {{F4_PREST_MONET_EST_DIF_Resto_UE_2024}} € (resto de la UE) por persona. En"
                     " prestaciones no contributivas la relación se invierte: "
                     "viven en hogares que perciben rentas mínimas o IMV el {{F3_PRE_rentas_minimas_IMV_Resto_del_mundo}} % frente al {{F3_PRE_rentas_minimas_IMV_España}} %, "
                     "y ayudas a la vivienda el {{F3_PRE_ayuda_vivienda_Resto_del_mundo}} % frente al {{F3_PRE_ayuda_vivienda_España}} %; la diferencia en rentas mínimas "
                     "se mantiene a igual edad, sexo, educación y región ({{F3_PRE_BRECHA_perceptor_rentas_minimas_IMV_Resto_del_mundo_completo}} pp).",
     "causal": "No es una pregunta causal: es contabilidad.",
     "supuestos": "Prestaciones de la ECV calibradas a las cuentas públicas (COFOG); las del hogar se reparten por persona.",
     "veredicto": "engañosa", "confianza": "media",
     "razon": "En el total por persona es falsa, en bruto y a igual edad y sexo; es cierta para las prestaciones no contributivas, también a igualdad "
              "de características, que son el {{F6_PREST_NO_CONTRIB_CUOTA}} % de las prestaciones monetarias (2024, calibradas a COFOG). Las tasas se "
              "refieren a personas que viven en hogares perceptores, no a hogares."},
    {"id": "A2", "sentido": "desfavorable", "afirmacion": "La inmigración quita empleo a los españoles.",
     "contabilidad": "Entre 2014 y 2025 la ocupación media aumentó en {{F3_EMP_AUMENTO_OCUPADOS_2014_2025}} millones; el {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del "
                     "aumento corresponde a nacidos fuera y el resto a nacidos en España, cuya ocupación también creció. La tasa de empleo 16-64 de los nacidos en "
                     "España es del {{F3_EMP_TASA_España_2025}} % (2025).",
     "causal": CAUSAL_M1 + " Para la tasa de empleo de los nacidos en España, la estimación puntual es {{F5_P1_H1_beta}} puntos por punto de "
               "aumento de la población nacida fuera (p de Holm = {{F5_P1_H1_p}}), y para la de paro {{F5_P1_H2_beta}}. El indicio más consistente es "
               "desfavorable y exploratorio: los nacidos en España con educación baja, {{F5_P1_E3a_beta}} (p ajustado por BH = {{F5_P1_E3a_p}}; "
               "conjunto AKM0 sin cota inferior; en la variante por nacionalidad, [{{F5_P1_E3a_NACIONALIDAD:inf}}, {{F5_P1_E3a_NACIONALIDAD:sup}}]). "
               "En España, los trabajos con datos de provincias y celdas (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Banco de "
               "España 2026, Informe Anual 2025) no encuentran en general efectos negativos significativos sobre el empleo de los nativos, aunque Carrasco, Jimeno y "
               "Ortega (2008) obtienen una elasticidad negativa (−0,17; ficha en docs/literatura/trabajo.md) cuando solo cuentan a los inmigrantes con permiso de"
               " trabajo, y la ficha del Banco de España no "
               "informa de inferencia adecuada para shift-share.",
     "supuestos": "La contabilidad no dice qué habría pasado sin inmigración.", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "La contabilidad no responde a una pregunta contrafactual. La estimación propia queda en ASOCIACIÓN, con un indicio desfavorable para los "
              "nacidos en España con educación baja; la literatura española no encuentra en general efectos negativos. El efecto no está identificado "
              "(mismo estándar que A3 y F2)."},
    {"id": "A3", "sentido": "desfavorable", "afirmacion": "La inmigración hunde los salarios de los españoles.",
     "contabilidad": "Los extranjeros cobran por hora un {{F3_SAL_BRECHA_bruto_2022:abs}} % menos que los españoles (bruto, 2022); a igual edad, sexo, estudios y "
                     "región la diferencia es un {{F3_SAL_BRECHA_completo_2022:abs}} % menos. Es una brecha entre grupos, no un efecto sobre los salarios de los nativos.",
     "causal": CAUSAL_M1 + " Para salarios, el diseño de celdas educación × edad (Borjas) da {{F5_P1_E4_beta}} en log por punto de cuota, "
               "sin significación (ASOCIACIÓN por diseño, sin instrumento). "
               "La literatura internacional verificada da efectos medios pequeños sobre los salarios nativos (Dustmann, Schönberg y Stuhler 2016) y "
               "la española no documenta caídas generalizadas; con datos públicos no hay salarios provinciales por nacionalidad (la AEAT no fue accesible).",
     "supuestos": "—", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Con datos públicos el efecto en España no queda identificado (fase 5: ASOCIACIÓN, sin significación en salarios); la literatura verificada no documenta caídas "
              "generalizadas, pero eso no basta para afirmar ni descartar la versión fuerte («hunde»)."},
    {"id": "A4", "sentido": "desfavorable", "afirmacion": "Los inmigrantes colapsan la sanidad pública.",
     "contabilidad": "Uso declarado por persona, nacidos fuera / nacidos en España del mismo tramo de edad (ENSE 2017; 1 = igual). 15-34 años: consultas "
                     "{{F6_ENSE_RAZON_CONSULTAS_15_34}}, días de hospital {{F6_ENSE_RAZON_HOSP_15_34}}, urgencias {{F6_ENSE_RAZON_URG_15_34}}, fármacos "
                     "{{F6_ENSE_RAZON_FAR_15_34}}. 35-54: consultas "
                     "{{F6_ENSE_RAZON_CONSULTAS_35_54}}, hospital {{F6_ENSE_RAZON_HOSP_35_54}}, urgencias {{F6_ENSE_RAZON_URG_35_54}}, fármacos "
                     "{{F6_ENSE_RAZON_FAR_35_54}}. 55-74: consultas {{F6_ENSE_RAZON_CONSULTAS_55_74}}, hospital {{F6_ENSE_RAZON_HOSP_55_74}} (pocas observaciones), "
                     "urgencias {{F6_ENSE_RAZON_URG_55_74}}, fármacos {{F6_ENSE_RAZON_FAR_55_74}}. Su estructura por edad es más joven: el {{F3_POB_65MAS_nacidos"
                     " fuera_2025}} % tiene 65 o más años "
                     "frente al {{F3_POB_65MAS_España_2025}} % de los nacidos en España, lo que reduce el uso por persona del grupo, pero no el uso agregado, "
                     "que crece con el tamaño de la población.",
     "causal": "P3 (listas de espera) NO ESTIMABLE con datos públicos procesables (SISLE solo en PDF por CCAA) y la congestión local no se observa. "
               "Giuntella, Nicodemo y Vargas-Silva (2018) no encuentran más espera en el NHS inglés.",
     "supuestos": "Uso declarado en encuesta (2017); razones por tramo con muestras pequeñas en los mayores.", "veredicto": "no se puede saber",
     "confianza": "media",
     "razon": "El uso por persona a igual edad no es mayor en la mayoría de los tramos y partidas, pero la afirmación es agregada y contrafactual (congestión) y "
              "no hay datos públicos procesables para medirla (mismo estándar que A6)."},
    {"id": "A5", "sentido": "desfavorable", "afirmacion": "Los inmigrantes suponen un coste fiscal neto para España.",
     "contabilidad": "Contribución neta estática por persona en 2024 (todas las partidas, incluido el déficit): nacidos en España {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024}} € "
                     "(intervalo de supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}}]); resto de la UE "
                     "[{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}}] €; resto del mundo "
                     "[{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}] €; conjunto de "
                     "nacidos fuera {{F4_NETA_PC_FUERA_2024}} € [{{F4_NETA_PC_FUERA_2024:inf}}, {{F4_NETA_PC_FUERA_2024:sup}}], positiva en "
                     "{{F4_NETA_PC_FUERA_POSITIVAS}} de 64 combinaciones, según el reparto de los bienes públicos y la asignación de los hijos. A igual "
                     "edad y sexo, frente a los nativos, la ventaja del resto de la UE se reduce mucho (positiva en las 64 combinaciones, pero no "
                     "distinguible de cero por muestreo) y la del resto del mundo es negativa en el principal pero positiva con bienes públicos a "
                     "coste marginal cero. En el ciclo vital, "
                     "las llegadas entre 20 y 50 años tienen intervalos que contienen el cero para los dos grupos; frente a un nativo de la misma edad, "
                     "quien llega de fuera de la UE a los 20 años aporta menos y quien llega del resto de la UE a los 50 aporta más en todas las "
                     "combinaciones sin convergencia adicional.",
     "causal": "No es causal: contabilidad (capa C2).",
     "supuestos": "En el resto del mundo el signo depende del reparto de los bienes públicos (coste medio o marginal) y de a quién se asignan los hijos nacidos en "
                  "España (decisión D11: solo intervalos).",
     "veredicto": "no se puede saber", "confianza": "alta",
     "razon": "Para el conjunto de los inmigrantes el signo de la contabilidad estática depende de dos supuestos defendibles: es un coste neto con "
              "bienes públicos a coste medio e hijos asignados a sus padres, y no lo es en las demás celdas; para los nacidos en la UE es incorrecta en "
              "las 64 combinaciones; en el ciclo vital el saldo depende de supuestos para todas las edades de llegada entre 20 y 50 años."},
    {"id": "A6", "sentido": "desfavorable", "afirmacion": "La inmigración es la causa de la subida del precio de la vivienda.",
     "contabilidad": "Entre 2015 y 2022 el aumento de la población nacida fuera implica unos {{F3_VIV_DEMANDA_FUERA_2015_2022}} mil hogares a tasa de jefatura "
                     "constante, frente a {{F3_VIV_DEMANDA_ESPANA_2015_2022}} mil de los nacidos en España (cuya población se redujo); la formación de hogares por "
                     "envejecimiento no está incluida. Los nacidos fuera viven sobre todo de alquiler.",
     "causal": "P4 no se duplica en M1. El estudio de vivienda del repositorio de referencia Econometr-a (trabajo no publicado ni revisado, sin ficha "
               "verificada) no encuentra efectos que sobrevivan a la inferencia con pocos grupos; González y "
               "Ortega (2013) atribuyen a la inmigración una parte de la subida de 2000-2010.",
     "supuestos": "Tasa de jefatura constante por grupo y región.", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Es cierto que la población nacida fuera explica la mayor parte del aumento demográfico de la demanda de hogares; que sea «la causa» de los "
              "precios es una afirmación contrafactual no identificada con datos públicos recientes (mismo estándar que F2)."},
    {"id": "F1", "sentido": "favorable", "afirmacion": "Los inmigrantes pagan nuestras pensiones.",
     "contabilidad": "En la contabilidad de 2024 los nacidos fuera aportan el {{F6_TRABAJO_CUOTA_FUERA}} % de los impuestos sobre el trabajo y las cotizaciones "
                     "(son el {{F6_POB_CUOTA_FUERA_ECV}} % de la población de la ECV) y reciben pocas pensiones; con la regla demográfica mecánica "
                     "aplicada a EUROPOP2023, el gasto en pensiones de 2050 de la variante sin migración es {{F4_PEN_DIF_SIN_MIGRACION_2050}} puntos de "
                     "PIB mayor que el de la variante base, y la diferencia entre menos y más migración es de {{F4_PEN_MEC_DIF_LMIGR_HMIGR_2050}} puntos. "
                     "En el Ageing Report 2024 (referencia NO VERIFICADA), {{F4_PEN_AR2024_MAS_MIGRACION_2050}} % con un tercio más de migración frente a "
                     "{{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % con un tercio menos.",
     "causal": "La comparación «sin migración» es una regla mecánica (empleo, cobertura y pensión relativa constantes), no un contrafactual identificado.",
     "supuestos": "Las cotizaciones de hoy generan derechos de pensión futuros: en el ciclo vital el valor actual de los nacidos fuera depende de la salida, el "
                  "descuento y los bienes públicos: para las llegadas entre 20 y 50 años el intervalo contiene el cero, y frente a un nativo de "
                  "la misma edad quien llega de fuera de la UE a los 20 años aporta menos y quien llega del resto de la UE a los 50, más, en todas "
                  "las combinaciones sin convergencia.",
     "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Es cierto que sus cotizaciones financian una parte de las pensiones corrientes; que sostengan el sistema es una afirmación contrafactual y de "
              "largo plazo que no está identificada (mismo estándar que A6)."},
    {"id": "F2", "sentido": "favorable", "afirmacion": "Sin inmigrantes no habría crecido el empleo.",
     "contabilidad": "El {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del aumento de la ocupación de 2014-2025 y el {{F3_EMP_CONTRIB_HORAS_FUERA_2014_2025}} % del de las horas "
                     "corresponden a nacidos fuera.",
     "causal": "El contrafactual (qué empleo habría sin inmigración) no está identificado: en la fase 5 la primera etapa del shift-share es "
               "fuerte al nivel del shock, pero los conjuntos AKM0 no están acotados y todas las estimaciones quedan en ASOCIACIÓN; la contabilidad no lo dice.",
     "supuestos": "—", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "Es cierto que la mayor parte del aumento del empleo corresponde a nacidos fuera, pero la afirmación es contrafactual («no habría crecido») y no "
              "está identificada (mismo estándar que A6)."},
    {"id": "F3", "sentido": "favorable", "afirmacion": "Los inmigrantes aportan más de lo que reciben.",
     "contabilidad": "Véase A5: en la contabilidad estática, positiva en las 64 combinaciones para los nacidos en la UE, intervalo que contiene el cero para los "
                     "nacidos fuera de la UE y, para el conjunto, negativa solo con bienes públicos a coste medio e hijos asignados a sus padres; en el "
                     "ciclo vital, las llegadas entre 20 y 50 años tienen intervalos que contienen el cero para los dos grupos, las llegadas a los 0 años "
                     "son negativas, y frente a un nativo de la misma edad quien llega de fuera de la UE a los 20 años aporta menos y quien llega "
                     "del resto de la UE a los 50, más, en todas las combinaciones sin convergencia.",
     "causal": "No es causal.", "supuestos": "Bienes públicos e hijos nacidos en España.", "veredicto": "no se puede saber", "confianza": "alta",
     "razon": "En la contabilidad estática se sostiene para los nacidos en la UE; para el conjunto de inmigrantes y en el ciclo vital depende de "
              "supuestos (mismo estándar que A5)."},
    {"id": "F4", "sentido": "favorable", "afirmacion": "Los inmigrantes trabajan tanto como los españoles.",
     "contabilidad": "Tasa de empleo 16-64 de 2025: nacidos fuera {{F3_EMP_TASA_FUERA_2025}} % frente a {{F3_EMP_TASA_España_2025}} %; con variación interna amplia "
                     "(África {{F3_EMP_TASA_África_2025}} %, América Latina {{F3_EMP_TASA_América Latina_2025}} %). Tasa de paro de nacidos fuera "
                     "{{F3_EMP_PARO_FUERA_2025}} % frente a {{F3_EMP_PARO_España_2025}} %. En los tres niveles, la brecha de empleo del conjunto de nacidos fuera es "
                     "{{F3_EMP_BRECHA_FUERA_bruto_2025}} pp en bruto, {{F3_EMP_BRECHA_FUERA_edad_y_sexo_2025}} pp a igual edad y sexo y "
                     "{{F3_EMP_BRECHA_FUERA_completo_2025}} pp al añadir educación, residencia y región; la de paro, {{F3_PARO_BRECHA_FUERA_bruto_2025}}, "
                     "{{F3_PARO_BRECHA_FUERA_edad_y_sexo_2025}} y {{F3_PARO_BRECHA_FUERA_completo_2025}} pp. En bruto a 25-54 años, la tasa de empleo es "
                     "{{F3_EMP_TASA_FUERA_25_54_2025}} % frente a {{F3_EMP_TASA_España_25_54_2025}} %, y a 25-64, {{F3_EMP_TASA_FUERA_25_64_2025}} % frente a "
                     "{{F3_EMP_TASA_España_25_64_2025}} %.",
     "causal": "No es causal.", "supuestos": "EPA; agrupación aproximada de los ocho grupos (D6).", "veredicto": "engañosa", "confianza": "media",
     "razon": "La igualdad solo aparece en la tasa 16-64, que incluye a los menores de 25; en las edades centrales y a igual "
              "edad y sexo los nacidos fuera trabajan menos, y el paro es mayor en los tres niveles (mismo criterio que A1: la cantidad principal "
              "contradice la afirmación). Hay grupos con tasas de empleo iguales o mayores que las de los nativos."},
    {"id": "F5", "sentido": "favorable", "afirmacion": "A los inmigrantes se les paga menos por el mismo trabajo.",
     "contabilidad": "Brecha de salario por hora: {{F3_SAL_BRECHA_bruto_2022}} % bruta, {{F3_SAL_BRECHA_completo_2022}} % a igual edad, sexo, estudios y región y "
                     "{{F3_SAL_BRECHA_completo_inf_2022}} % si además se iguala ocupación, sector, contrato y jornada; alrededor de dos tercios es composición.",
     "causal": "Un resto no explicado no es por sí solo discriminación: faltan años de residencia, idioma, homologación de títulos y calidad del empleo.",
     "supuestos": "EES solo distingue nacionalidad.", "veredicto": "se sostiene con matices", "confianza": "media",
     "razon": "Queda una diferencia pequeña a igualdad de características observables; su causa no se puede saber con datos públicos."},
    {"id": "F6", "sentido": "favorable", "afirmacion": "Los inmigrantes hacen los trabajos que los españoles no quieren.",
     "contabilidad": "Ocupados en ocupaciones elementales: {{F3_EMP_OCUP_ELEMENTALES_FUERA_2025}} % de los nacidos fuera frente al "
                     "{{F3_EMP_OCUP_ELEMENTALES_España_2025}} % de los nacidos en España (2025); titulados superiores en ocupaciones que no lo requieren: "
                     "{{F3_EMP_SOBRECUALIFICACION_FUERA_2025}} % frente al {{F3_EMP_SOBRECUALIFICACION_España_2025}} %.",
     "causal": CAUSAL_M1 + " Peri y Sparber (2009) y Amuedo-Dorantes y De la Rica (2011) documentan especialización de tareas entre nativos e inmigrantes. "
               "En M1, la cuota de nativos en ocupaciones no manuales (P2-E1, {{F5_P2_E1_beta}}) y de alta cualificación (P2-E2, {{F5_P2_E2_beta}}) "
               "no se asocia de forma significativa con la inmigración (ASOCIACIÓN).",
     "supuestos": "—", "veredicto": "no se puede saber", "confianza": "media",
     "razon": "La especialización por ocupaciones se observa; el núcleo de la afirmación («que no quieren») es sobre preferencias, que los datos no miden."},
]


def render(texto: str, cifras: pd.DataFrame) -> str:
    """Sustituye {{id}}, {{id:inf}}, {{id:sup}} y {{id:abs}} (valor absoluto, para «un 18 % menos»). Recuentos y posiciones sin
    decimales; euros y miles de euros sin decimales; el resto con un decimal si |v| < 100."""
    c = cifras.set_index("id")

    def fmt(v, unidad: str):
        if pd.isna(v):
            return "n. d."
        v = float(v)
        u = str(unidad)
        entero = any(k in u for k in ("posición", "provincias", "€", "miles de hogares", "especificaciones", "combinaciones")) or abs(v) >= 100
        if entero:
            s = f"{v:,.0f}"
        elif u in ("p", "p ajustado"):
            s = f"{v:,.3f}"
        elif "por p" in u or u.startswith(("razón", "elasticidad", "correlación", "t")):
            s = f"{v:,.2f}"
        else:
            s = f"{v:,.1f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")

    def rep(m):
        k, parte = m.group(1), m.group(2)
        if k not in c.index:
            return f"[FALTA CIFRA: {k}]"
        col = {"inf": "ic_inf", "sup": "ic_sup"}.get(parte, "valor")
        v = c.loc[k, col]
        if parte == "abs" and pd.notna(v):
            v = abs(float(v))
        return fmt(v, c.loc[k, "unidad"])
    return re.sub(r"\{\{([^}:]+)(?::(inf|sup|abs))?\}\}", rep, texto)


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f6_afirmaciones", "src/m1/f6_afirmaciones.py")
    r = pd.read_csv(OUT / "f4" / "neta_por_grupo_2024.csv").set_index("grupo")
    monet = ["gas_desempleo", "gas_vejez", "gas_supervivencia", "gas_enfermedad_incapacidad", "gas_familia", "gas_exclusion_social", "gas_vivienda"]
    for g in r.index:
        cf.add(f"F6_PREST_MONETARIAS_PC_{g.replace(' ', '_')}", round(float(r.loc[g, monet].sum()), 0), "€ por persona y año",
               f"Prestaciones monetarias por persona (calibradas a COFOG), nacidos en {g}", "C2", "ECV (INE) y Eurostat COFOG", "2024", "España", g)
    rz = pd.read_csv(OUT / "f4" / "razones_uso_sanitario_ense.csv").set_index("amplio")
    for tramo in ("15-34", "35-54", "55-74"):
        for v, dsc in (("consultas", "consultas de primaria y especialista"), ("hosp", "días de hospital"), ("urg", "urgencias"),
                       ("far", "uso de medicamentos recetados")):
            cf.add(f"F6_ENSE_RAZON_{v.upper()}_{tramo.replace('-', '_')}", round(float(rz.loc[tramo, f"razon_{v}"]), 2), "razón (nativos = 1)",
                   f"Uso relativo de {dsc}: nacidos fuera / nacidos en España, {tramo} años (n nacidos fuera = "
                   f"{int(rz.loc[tramo, 'n_nacidos_fuera'])})", "C4", "ENSE 2017 (INE)", "2017", "España", "nacidos fuera")
    trab = r[["ing_irpf_cotiz_trab", "ing_cotiz_empresa"]].sum(axis=1) * r.poblacion
    fuera = [g for g in r.index if g != "España"]
    cf.add("F6_TRABAJO_CUOTA_FUERA", round(100 * float(trab[fuera].sum() / trab.sum()), 1), "% del total",
           "Cuota de los nacidos fuera en IRPF del trabajo y cotizaciones sociales (calibradas a las cuentas de las AAPP)", "C2",
           "ECV (INE) y Eurostat", "2024", "España", "nacidos fuera")
    cf.add("F6_POB_CUOTA_FUERA_ECV", round(100 * float(r.poblacion[fuera].sum() / r.poblacion.sum()), 1), "% de la población",
           "Cuota de los nacidos fuera en la población de la ECV (hogares privados)", "C2", "ECV (INE)", "2024", "España", "nacidos fuera")
    tot = r.loc[:, monet].mul(r.poblacion, axis=0).sum()
    nc = tot[["gas_exclusion_social", "gas_vivienda"]].sum() / tot.sum()
    cf.add("F6_PREST_NO_CONTRIB_CUOTA", round(100 * float(nc), 1), "% de las prestaciones monetarias",
           "Rentas mínimas, IMV y ayudas a la vivienda sobre el total de prestaciones monetarias (calibradas a COFOG)", "C2",
           "ECV (INE) y Eurostat COFOG", "2024", "España", "todos")
    cf.escribir()
    import cifras as cmod
    todas = cmod.consolidar()
    filas, md = [], ["# Afirmaciones del debate y su veredicto (fase 6)", "",
                     "Se evalúan afirmaciones, no personas ni grupos. Las favorables y las desfavorables a la inmigración siguen las mismas reglas.", ""]
    for f in FICHAS:
        md += [f"## {f['id']} · «{f['afirmacion']}»", f"- Sentido: {f['sentido']}.",
               f"- Contabilidad: {render(f['contabilidad'], todas)}", f"- Evidencia causal: {render(f['causal'], todas)}",
               f"- Depende de supuestos: {render(f['supuestos'], todas)}",
               f"- **Veredicto: {f['veredicto']}** (confianza {f['confianza']}). {render(f['razon'], todas)}", ""]
        filas.append({**{k: f[k] for k in ("id", "sentido", "afirmacion", "veredicto", "confianza")}, "razon": render(f["razon"], todas)})
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
