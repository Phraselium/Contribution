# Afirmaciones del debate y su veredicto (fase 6)

Se evalúan afirmaciones, no personas ni grupos. Las favorables y las desfavorables a la inmigración siguen las mismas reglas.

## A1 · «Los inmigrantes viven de las ayudas: reciben más prestaciones que los nacidos en España.»
- Sentido: desfavorable.
- Contabilidad: Por persona, las prestaciones monetarias que reciben los nacidos fuera son menores en total: 1.927 € (resto del mundo) y 2.813 € (resto de la UE) frente a 6.252 € de los nacidos en España (2024), sobre todo porque reciben pocas pensiones contributivas (perciben jubilación o viven en un hogar que la percibe el 44,1 % de los mayores de 65 nacidos en el resto del mundo frente al 72,5 %). A igual edad y sexo siguen recibiendo menos: -3.637 € (resto del mundo) y -3.312 € (resto de la UE) por persona. En prestaciones no contributivas la relación se invierte: viven en hogares que perciben rentas mínimas o IMV el 11,9 % frente al 5,5 %, y ayudas a la vivienda el 4,9 % frente al 1,8 %; la diferencia en rentas mínimas se mantiene a igual edad, sexo, educación y región (6,0 pp).
- Evidencia causal: No es una pregunta causal: es contabilidad.
- Depende de supuestos: Prestaciones de la ECV calibradas a las cuentas públicas (COFOG); las del hogar se reparten por persona.
- **Veredicto: engañosa** (confianza media). En el total por persona es falsa, en bruto y a igual edad y sexo; es cierta para las prestaciones no contributivas, también a igualdad de características, que son el 2,5 % de las prestaciones monetarias (2024, calibradas a COFOG). Las tasas se refieren a personas que viven en hogares perceptores, no a hogares.

## A2 · «La inmigración quita empleo a los españoles.»
- Sentido: desfavorable.
- Contabilidad: Entre 2014 y 2025 la ocupación media aumentó en 4,9 millones; el 55,6 % del aumento corresponde a nacidos fuera y el resto a nacidos en España, cuya ocupación también creció. La tasa de empleo 16-64 de los nacidos en España es del 68,4 % (2025).
- Evidencia causal: Estimación propia de M1 (fase 5, pre-registrada; corregido un error de código en el control de cuotas que cambió los signos): la primera etapa del shift-share provincial es fuerte al nivel del shock (F = 13,5), pero los conjuntos AKM0 no están acotados, de modo que todas las preguntas causales quedan en ASOCIACIÓN y ninguna rechaza el cero con la corrección por multiplicidad. Para la tasa de empleo de los nacidos en España, la estimación puntual es 0,06 puntos por punto de aumento de la población nacida fuera (p de Holm = 0,892), y para la de paro -0,55. El indicio más consistente es desfavorable y exploratorio: los nacidos en España con educación baja, -0,61 (p ajustado por BH = 0,245; conjunto AKM0 sin cota inferior; en la variante por nacionalidad, [-0,46, -0,04]). En España, los trabajos con datos de provincias y celdas (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Banco de España 2026, Informe Anual 2025) no encuentran en general efectos negativos significativos sobre el empleo de los nativos, aunque Carrasco, Jimeno y Ortega (2008) obtienen una elasticidad negativa (−0,17; ficha en docs/literatura/trabajo.md) cuando solo cuentan a los inmigrantes con permiso de trabajo, y la ficha del Banco de España no informa de inferencia adecuada para shift-share.
- Depende de supuestos: La contabilidad no dice qué habría pasado sin inmigración.
- **Veredicto: no se puede saber** (confianza media). La contabilidad no responde a una pregunta contrafactual. La estimación propia queda en ASOCIACIÓN, con un indicio desfavorable para los nacidos en España con educación baja; la literatura española no encuentra en general efectos negativos. El efecto no está identificado (mismo estándar que A3 y F2).

## A3 · «La inmigración hunde los salarios de los españoles.»
- Sentido: desfavorable.
- Contabilidad: Los extranjeros cobran por hora un 18,1 % menos que los españoles (bruto, 2022); a igual edad, sexo, estudios y región la diferencia es un 6,2 % menos. Es una brecha entre grupos, no un efecto sobre los salarios de los nativos.
- Evidencia causal: Estimación propia de M1 (fase 5, pre-registrada; corregido un error de código en el control de cuotas que cambió los signos): la primera etapa del shift-share provincial es fuerte al nivel del shock (F = 13,5), pero los conjuntos AKM0 no están acotados, de modo que todas las preguntas causales quedan en ASOCIACIÓN y ninguna rechaza el cero con la corrección por multiplicidad. Para salarios, el diseño de celdas educación × edad (Borjas) da -0,10 en log por punto de cuota, sin significación (ASOCIACIÓN por diseño, sin instrumento). La literatura internacional verificada da efectos medios pequeños sobre los salarios nativos (Dustmann, Schönberg y Stuhler 2016) y la española no documenta caídas generalizadas; con datos públicos no hay salarios provinciales por nacionalidad (la AEAT no fue accesible).
- Depende de supuestos: —
- **Veredicto: no se puede saber** (confianza media). Con datos públicos el efecto en España no queda identificado (fase 5: ASOCIACIÓN, sin significación en salarios); la literatura verificada no documenta caídas generalizadas, pero eso no basta para afirmar ni descartar la versión fuerte («hunde»).

## A4 · «Los inmigrantes colapsan la sanidad pública.»
- Sentido: desfavorable.
- Contabilidad: Uso declarado por persona, nacidos fuera / nacidos en España del mismo tramo de edad (ENSE 2017; 1 = igual). 15-34 años: consultas 1,02, días de hospital 0,60, urgencias 0,90, fármacos 0,90. 35-54: consultas 0,84, hospital 0,82, urgencias 1,16, fármacos 0,89. 55-74: consultas 0,96, hospital 2,58 (pocas observaciones), urgencias 1,00, fármacos 0,85. Su estructura por edad es más joven: el 9,2 % tiene 65 o más años frente al 23,5 % de los nacidos en España, lo que reduce el uso por persona del grupo, pero no el uso agregado, que crece con el tamaño de la población.
- Evidencia causal: P3 (listas de espera) NO ESTIMABLE con datos públicos procesables (SISLE solo en PDF por CCAA) y la congestión local no se observa. Giuntella, Nicodemo y Vargas-Silva (2018) no encuentran más espera en el NHS inglés.
- Depende de supuestos: Uso declarado en encuesta (2017); razones por tramo con muestras pequeñas en los mayores.
- **Veredicto: no se puede saber** (confianza media). El uso por persona a igual edad no es mayor en la mayoría de los tramos y partidas, pero la afirmación es agregada y contrafactual (congestión) y no hay datos públicos procesables para medirla (mismo estándar que A6).

## A5 · «Los inmigrantes suponen un coste fiscal neto para España.»
- Sentido: desfavorable.
- Contabilidad: Contribución neta estática por persona en 2024 (todas las partidas, incluido el déficit): nacidos en España -1.367 € (intervalo de supuestos [-1.953, -636]); resto de la UE [761, 5.949] €; resto del mundo [-2.087, 2.823] €; conjunto de nacidos fuera 525 € [-1.515, 3.339], positiva en 48 de 64 combinaciones, según el reparto de los bienes públicos y la asignación de los hijos. A igual edad y sexo, frente a los nativos, la ventaja del resto de la UE se reduce mucho (positiva en las 64 combinaciones, pero no distinguible de cero por muestreo) y el intervalo del resto del mundo contiene el cero. En el ciclo vital, las llegadas entre 20 y 50 años tienen intervalos que contienen el cero para los dos grupos; frente a un nativo de la misma edad, quienes llegan de fuera de la UE a los 20 o a los 30 años aportan menos en todas las combinaciones sin convergencia adicional.
- Evidencia causal: No es causal: contabilidad (capa C2).
- Depende de supuestos: En el resto del mundo el signo depende del reparto de los bienes públicos (coste medio o marginal) y de a quién se asignan los hijos nacidos en España (decisión D11: solo intervalos).
- **Veredicto: no se puede saber** (confianza alta). Para el conjunto de los inmigrantes el signo de la contabilidad estática depende de dos supuestos defendibles: es un coste neto con bienes públicos a coste medio e hijos asignados a sus padres, y no lo es en las demás celdas; para los nacidos en la UE es incorrecta en las 64 combinaciones; en el ciclo vital el saldo depende de supuestos para todas las edades de llegada entre 20 y 50 años.

## A6 · «La inmigración es la causa de la subida del precio de la vivienda.»
- Sentido: desfavorable.
- Contabilidad: Entre 2015 y 2022 el aumento de la población nacida fuera implica unos 477 mil hogares a tasa de jefatura constante, frente a -225 mil de los nacidos en España (cuya población se redujo); la formación de hogares por envejecimiento no está incluida. Los nacidos fuera viven sobre todo de alquiler.
- Evidencia causal: P4 no se duplica en M1. El estudio de vivienda del repositorio de referencia Econometr-a (trabajo no publicado ni revisado, sin ficha verificada) no encuentra efectos que sobrevivan a la inferencia con pocos grupos; González y Ortega (2013) atribuyen a la inmigración una parte de la subida de 2000-2010.
- Depende de supuestos: Tasa de jefatura constante por grupo y región.
- **Veredicto: no se puede saber** (confianza media). Es cierto que la población nacida fuera explica la mayor parte del aumento demográfico de la demanda de hogares; que sea «la causa» de los precios es una afirmación contrafactual no identificada con datos públicos recientes (mismo estándar que F2).

## F1 · «Los inmigrantes pagan nuestras pensiones.»
- Sentido: favorable.
- Contabilidad: En la contabilidad de 2024 los nacidos fuera aportan el 15,5 % de los impuestos sobre el trabajo y las cotizaciones (son el 18,5 % de la población de la ECV) y reciben pocas pensiones; con la regla demográfica mecánica aplicada a EUROPOP2023, el gasto en pensiones de 2050 de la variante sin migración es 4,4 puntos de PIB mayor que el de la variante base, y la diferencia entre menos y más migración es de 3,1 puntos. En el Ageing Report 2024 (referencia NO VERIFICADA), 16,1 % con un tercio más de migración frente a 18,7 % con un tercio menos.
- Evidencia causal: La comparación «sin migración» es una regla mecánica (empleo, cobertura y pensión relativa constantes), no un contrafactual identificado.
- Depende de supuestos: Las cotizaciones de hoy generan derechos de pensión futuros: en el ciclo vital el valor actual de los nacidos fuera depende del retorno, la convergencia y los bienes públicos: para las llegadas entre 20 y 50 años el intervalo contiene el cero, y frente a un nativo de la misma edad quienes llegan de fuera de la UE a los 20 o 30 años aportan menos en todas las combinaciones.
- **Veredicto: no se puede saber** (confianza media). Es cierto que sus cotizaciones financian una parte de las pensiones corrientes; que sostengan el sistema es una afirmación contrafactual y de largo plazo que no está identificada (mismo estándar que A6).

## F2 · «Sin inmigrantes no habría crecido el empleo.»
- Sentido: favorable.
- Contabilidad: El 55,6 % del aumento de la ocupación de 2014-2025 y el 71,8 % del de las horas corresponden a nacidos fuera.
- Evidencia causal: El contrafactual (qué empleo habría sin inmigración) no está identificado: en la fase 5 la primera etapa del shift-share es fuerte al nivel del shock, pero los conjuntos AKM0 no están acotados y todas las estimaciones quedan en ASOCIACIÓN; la contabilidad no lo dice.
- Depende de supuestos: —
- **Veredicto: no se puede saber** (confianza media). Es cierto que la mayor parte del aumento del empleo corresponde a nacidos fuera, pero la afirmación es contrafactual («no habría crecido») y no está identificada (mismo estándar que A6).

## F3 · «Los inmigrantes aportan más de lo que reciben.»
- Sentido: favorable.
- Contabilidad: Véase A5: en la contabilidad estática, positiva en las 64 combinaciones para los nacidos en la UE, intervalo que contiene el cero para los nacidos fuera de la UE y, para el conjunto, negativa solo con bienes públicos a coste medio e hijos asignados a sus padres; en el ciclo vital, las llegadas entre 20 y 50 años tienen intervalos que contienen el cero para los dos grupos, las llegadas a los 0 años son negativas, y frente a un nativo de la misma edad quienes llegan de fuera de la UE a los 20 o 30 años aportan menos en todas las combinaciones.
- Evidencia causal: No es causal.
- Depende de supuestos: Bienes públicos e hijos nacidos en España.
- **Veredicto: no se puede saber** (confianza alta). En la contabilidad estática se sostiene para los nacidos en la UE; para el conjunto de inmigrantes y en el ciclo vital depende de supuestos (mismo estándar que A5).

## F4 · «Los inmigrantes trabajan tanto como los españoles.»
- Sentido: favorable.
- Contabilidad: Tasa de empleo 16-64 de 2025: nacidos fuera 67,3 % frente a 68,4 %; con variación interna amplia (África 50,8 %, América Latina 71,7 %). Tasa de paro de nacidos fuera 14,0 % frente a 9,4 %. En los tres niveles, la brecha de empleo del conjunto de nacidos fuera es -1,2 pp en bruto, -5,3 pp a igual edad y sexo y -2,0 pp al añadir educación, residencia y región; la de paro, 4,5, 4,6 y 3,4 pp. En bruto a 25-54 años, la tasa de empleo es 73,2 % frente a 82,3 %, y a 25-64, 71,1 % frente a 76,6 %.
- Evidencia causal: No es causal.
- Depende de supuestos: EPA; agrupación aproximada de los ocho grupos (D6).
- **Veredicto: engañosa** (confianza media). La igualdad solo aparece en la tasa 16-64, porque entre los nativos hay más jóvenes de 16-24 años que estudian; en las edades centrales y a igual edad y sexo los nacidos fuera trabajan menos, y el paro es mayor en los tres niveles (mismo criterio que A1: la cantidad principal contradice la afirmación). Hay grupos con tasas de empleo iguales o mayores que las de los nativos.

## F5 · «A los inmigrantes se les paga menos por el mismo trabajo.»
- Sentido: favorable.
- Contabilidad: Brecha de salario por hora: -18,1 % bruta, -6,2 % a igual edad, sexo, estudios y región y -3,0 % si además se iguala ocupación, sector, contrato y jornada; alrededor de dos tercios es composición.
- Evidencia causal: Un resto no explicado no es por sí solo discriminación: faltan años de residencia, idioma, homologación de títulos y calidad del empleo.
- Depende de supuestos: EES solo distingue nacionalidad.
- **Veredicto: se sostiene con matices** (confianza media). Queda una diferencia pequeña a igualdad de características observables; su causa no se puede saber con datos públicos.

## F6 · «Los inmigrantes hacen los trabajos que los españoles no quieren.»
- Sentido: favorable.
- Contabilidad: Ocupados en ocupaciones elementales: 23,8 % de los nacidos fuera frente al 8,4 % de los nacidos en España (2025); titulados superiores en ocupaciones que no lo requieren: 44,6 % frente al 32,2 %.
- Evidencia causal: Estimación propia de M1 (fase 5, pre-registrada; corregido un error de código en el control de cuotas que cambió los signos): la primera etapa del shift-share provincial es fuerte al nivel del shock (F = 13,5), pero los conjuntos AKM0 no están acotados, de modo que todas las preguntas causales quedan en ASOCIACIÓN y ninguna rechaza el cero con la corrección por multiplicidad. Peri y Sparber (2009) y Amuedo-Dorantes y De la Rica (2011) documentan especialización de tareas entre nativos e inmigrantes. En M1, la cuota de nativos en ocupaciones no manuales (P2-E1, 0,14) y de alta cualificación (P2-E2, 0,74) no se asocia de forma significativa con la inmigración (ASOCIACIÓN).
- Depende de supuestos: —
- **Veredicto: no se puede saber** (confianza media). La especialización por ocupaciones se observa; el núcleo de la afirmación («que no quieren») es sobre preferencias, que los datos no miden.

## Balance por sentido

| sentido | engañosa | no se puede saber | se sostiene con matices |
|---|---|---|---|
| desfavorable | 1 | 5 | 0 |
| favorable | 1 | 4 | 1 |
