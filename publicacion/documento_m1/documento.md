---
titulo: "Contribución e impacto económico de la población según su origen: España por provincia y Europa por país y región (solo información pública)"
serie: "Documento de trabajo M1 (formato de la serie Documentos de Trabajo del Banco de España; no es una publicación del Banco de España)"
fecha: "octubre de 2026"
---

# Contribución e impacto económico de la población según su origen

*España por provincia y Europa por país y región, solo con información pública*

Documento de trabajo M1 · octubre de 2026 · Formato de la serie Documentos de Trabajo del Banco de España; no es una publicación del Banco de España ni ha pasado por su revisión.

## Resumen ejecutivo

**Pregunta.** El estudio separa dos preguntas que no se mezclan. La primera es la **contribución**, una pregunta de contabilidad: cuánto aporta y recibe cada grupo de origen en empleo, salarios, vivienda y cuentas públicas. La segunda es el **impacto**, una pregunta de identificación: qué efecto tiene la inmigración sobre la población local. Solo se usan datos públicos descargables sin solicitud.

**Población.** La población nacida fuera de España era el 15,9 % en el padrón de 2022 y el 19,3 % en la Estadística Continua de Población de 2025. En 1998 era el 2,9 %. En la UE-27 la cifra es del 14,4 % (Eurostat, que para España se basa en la misma estadística del INE). Es una población más joven: el 9,2 % tiene 65 o más años, frente al 23,5 % de los nacidos en España.

**Empleo.** En 2025 la tasa de empleo de 16 a 64 años es del 67,3 % entre los nacidos fuera y del 68,4 % entre los nacidos en España. La variación interna es amplia: África 50,8 %, UE-14 73,3 %. El paro es mayor entre los nacidos fuera: 14,0 % frente a 9,4 %. Al aumento de la ocupación entre 2014 y 2025, de 4,9 millones, los nacidos fuera aportan el 55,6 %. Es contabilidad: no dice qué habría ocurrido sin inmigración.

**Salarios.** Los extranjeros cobran por hora un 18,1 % menos que los españoles (Encuesta de Estructura Salarial, EES, 2022). A igual edad, sexo, estudios y región la diferencia baja al 6,2 % menos (exploratorio, C4). En la descomposición de Oaxaca-Blinder, alrededor del 68,0 % de la brecha media corresponde a diferencias de composición observables.

**Vivienda.** Vive en vivienda en propiedad el 81,9 % de los nacidos en España, frente al 32,9 % de los nacidos fuera de la UE. La sobrecarga del gasto en vivienda afecta al 26,1 % de los segundos y al 4,9 % de los primeros.

**Cuentas públicas.** Contribución neta estática en 2024, en euros por persona: escenario principal de referencia e intervalo de las 64 combinaciones de supuestos (capa C2):
- nacidos en España: -1.367 [-1.953, -636];
- nacidos en el resto de la UE: 3.432 [761, 5.949];
- nacidos fuera de la UE: -160 [-2.087, 2.823].

Las cifras incluyen el déficit de las administraciones, que se reparte entre todos; con presupuesto equilibrado (criterio de la OCDE) las cifras suben para todos (sección 4). Para el conjunto de nacidos fuera, el signo depende de dos supuestos: con bienes públicos a coste medio y los hijos nacidos en España asignados a sus padres es negativo en todas las combinaciones de los demás supuestos ([-1.515, -670] €), y en las otras tres celdas, positivo. Estas comparaciones son brutas. A igual edad y sexo, la diferencia con los nativos es 737 € para el resto de la UE (positiva en las 64 combinaciones, aunque su intervalo de muestreo contiene el cero) y -1.627 € para el resto del mundo, cuyo intervalo de supuestos contiene el cero (positiva en 32 de 64). En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España: el principal es solo una referencia y lo que se afirma es el intervalo (decisión del autor, D11; tablas de signo en output/f4/signo_por_supuestos.csv y output/f4/ciclo_vital_signos.csv). En el ciclo vital (valor actual de por vida, sin convergencia adicional), para los dos grupos de nacidos fuera todas las llegadas entre 20 y 50 años dependen de supuestos; las llegadas a los 0 años son negativas en todos los supuestos, como el valor de un recién nacido en España. Frente a un nacido en España de la misma edad, quienes llegan de fuera de la UE a los 20 o a los 30 años aportan menos en las 24 combinaciones; para el resto de la UE y para las demás edades, depende de supuestos. Todos los valores incluyen el déficit de 2024 y excluyen a los descendientes.

**Pensiones.** Con una regla demográfica mecánica, el gasto en pensiones de 2050 de la variante de EUROPOP2023 sin migración es 4,4 puntos de PIB mayor que el de la variante base, y entre las variantes con menos y con más migración la diferencia es de 3,1 puntos. Es una comparación de escenarios con supuestos, no una proyección del sistema ni un efecto estimado. En el Ageing Report 2024, que modeliza empleo y reformas, la diferencia entre un tercio menos y un tercio más de migración es de 2,6 puntos (18,7 % frente a 16,1 %; referencia NO VERIFICADA, sin DOI).

**Impacto sobre la población local.** La estimación causal se hizo con el diseño pre-registrado (shift-share provincial con cuotas de 1998). Tras corregir un error de código en el control de cuotas incompletas detectado en la revisión (que cambió los signos de las confirmatorias; las tres lecturas del control se publican), la primera etapa es fuerte al nivel del shock (F = 13,5), pero los conjuntos de confianza AKM0 no están acotados. Por las reglas fijadas antes de estimar, **ningún efecto queda IDENTIFICADO ni SUGESTIVO**: todas las preguntas causales son ASOCIACIÓN o NO ESTIMABLE, y ninguna rechaza el cero con la corrección por multiplicidad. Los datos públicos no permiten afirmar ni descartar un efecto de la inmigración sobre el empleo, los salarios o los servicios de la población local. El indicio más consistente es desfavorable y exploratorio: la tasa de empleo de los nacidos en España con educación baja tiene una estimación de -0,61 puntos por punto, con un conjunto de confianza sin cota inferior, que no supera la corrección por multiplicidad ni el wild bootstrap; estandarizada por edad baja a -0,30 y pierde las señales que la apoyaban, y depende de una sola comunidad. Hay también indicios favorables más débiles, apoyados solo en el placebo de permutación, en el paro y en el empleo de los nativos con educación alta; la variante por nacionalidad y el multiverso no los acompañan (sección 5).

**Afirmaciones del debate.** Se evalúan doce afirmaciones: de las seis desfavorables a la inmigración, cinco con veredicto «no se puede saber» y una con veredicto «engañosa»; de las seis favorables a la inmigración, cuatro con veredicto «no se puede saber» y una con veredicto «engañosa» y una con veredicto «se sostiene con matices» (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. En conjunto trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales, y con grandes diferencias entre grupos. Cobran menos por hora; unos dos tercios de esa diferencia se corresponden con diferencias de edad, sexo, estudios y región, y el resto no se explica con esas variables. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas de un año (2024), los nacidos en otros países de la UE aportan más de lo que reciben en todas las combinaciones de supuestos estudiadas. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos. Buena parte de esa ventaja corresponde a una estructura por edad más joven: comparados con nativos de la misma edad y sexo, la ventaja de los nacidos en otros países de la UE se reduce mucho, y para los nacidos fuera de la UE el resultado depende de supuestos. Cuando se mira toda la vida (impuestos de hoy y pensiones de mañana), el saldo de quien llega depende de supuestos; pero quien llega de fuera de la UE joven (a los 20 o 30 años) aporta, a lo largo de su vida, menos que un nacido en España de su misma edad en todos los supuestos estudiados.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. Con los datos públicos y el diseño fijado de antemano, la respuesta es que no se puede saber: las estimaciones son demasiado imprecisas para afirmar un efecto en cualquier sentido. Hay un indicio, no concluyente, de menor tasa de empleo de los nativos con estudios bajos en las provincias con más llegadas, y otros más débiles en sentido favorable (menos paro y más empleo de los nativos con estudios altos).

## 1. Introducción

Este documento mide la contribución de cada grupo de origen al empleo, a los salarios, a la vivienda y a las cuentas públicas en España (nacional, comunidad y provincia) y en Europa (país y NUTS2). Además prepara, con un pre-registro interno, la estimación del impacto de la inmigración sobre la población local (pregunta B).

Las dos preguntas se responden por separado. La contribución (A) es contabilidad. El impacto (B) exige identificación y solo se describe con lenguaje causal si queda IDENTIFICADO según reglas fijadas antes de estimar. Cada cifra lleva una capa:
- **C1, hechos:** dato oficial o dos fuentes independientes;
- **C2, cotas con supuestos explícitos:** contabilidad fiscal, proyecciones y demanda de hogares;
- **C3, efectos identificados:** ninguno en esta versión (sección 5);
- **C4, exploratorio:** brechas ajustadas por regresión, descomposiciones y pseudopaneles. Describen diferencias condicionales, no efectos.

Reglas comunes a todo el documento:
- Las comparaciones se dan en tres niveles: bruto; ajustado por edad y sexo; ajustado además por educación, años de residencia (cuando la fuente los tiene) y región. En la EPA el nivel completo se evalúa en el tramo de 10 a 19 años de residencia; con otro tramo de referencia las cifras cambian.
- Las diferencias brutas se descomponen en composición y resto.
- Se describen agregados y su variación interna; nunca se atribuyen rasgos a un grupo.
- Las afirmaciones favorables y desfavorables se evalúan con el mismo estándar.

## 2. Datos públicos y definiciones

**Origen.** El criterio principal es el país de nacimiento; la nacionalidad es la sensibilidad. Hay ocho grupos: nacidos en España; UE-14; UE-13 y otros de Europa; América Latina; Magreb; resto de África; Asia; resto.

**Qué permite cada fuente:**
- Padrón (1998-2022): ofrece los ocho grupos completos.
- EPA: los aproxima por región de nacimiento, sin separar Magreb y resto de África (decisión D6).
- Encuesta de Condiciones de Vida (ECV) y Eurostat: solo distinguen España, resto de la UE y resto del mundo.
- EES: solo nacionalidad.

Los nacionalizados son el 33,4 % de los nacidos fuera. La segunda generación solo se identifica si convive con sus padres (EPA, ECV).

El inventario de fuentes, con URL, licencia, fecha y sha256, está en el anexo D y en `data/fuentes.csv`. Lo que no es público, y qué pregunta afecta, está en la sección 8.

**Protección de datos.** Solo se publican agregados y se suprimen las celdas con menos de 50 observaciones muestrales. Las encuestas públicas no traen estratos ni conglomerados, salvo la EES (establecimiento), y los errores se agrupan en consecuencia (D7).

## 3. Hechos: población, empleo, salarios, vivienda y prestaciones

### 3.1 Población

La población nacida fuera pasó del 2,9 % en 1998 al 15,9 % en 2022. Por grupos, en 2022: América Latina 7,0 %, UE-13 y otros de Europa 2,4 %, UE-14 2,3 %, Magreb 2,3 %, Asia 1,1 % y resto de África 0,6 %.

Por provincias va del 3,9 % al 24,7 % (mapa 1).

Entre 2021 y 2024 el saldo migratorio exterior de los nacidos fuera fue de 2,3 millones, y el de los nacidos en España de -0,1 millones.

El 35,2 % de los nacidos fuera de 16 o más años lleva 20 años o más en España, y el 23,7 % menos de 5.

En Europa, España ocupa el puesto 12 por cuota de nacidos fuera (19,3 % según Eurostat, que procede de la misma estadística del INE y no es una fuente independiente).

![Mapa 1](figuras/mapa1_provincias_nacidos_fuera.png)

### 3.2 Empleo

Tasas de empleo de 16 a 64 años en 2025 (gráfico 1):
- nacidos en España: 68,4 %;
- UE-14: 73,3 %;
- UE-13 y otros de Europa: 69,4 %;
- América Latina: 71,7 %;
- África: 50,8 %;
- Asia: 68,4 %.

**Tres niveles** (los ajustados son C4). La brecha de África con los nacidos en España es de -17,6 pp en bruto, -22,2 pp a igual edad y sexo, y -13,5 pp al añadir educación, residencia (10 a 19 años) y región. La de América Latina es de 3,3 pp en bruto, -0,4 pp a igual edad y sexo y 4,9 pp en el nivel completo: el nivel intermedio cambia el signo.

**Calidad del empleo** (2025): contrato temporal, 17,9 % de los asalariados nacidos fuera frente al 14,5 %; ocupaciones elementales, 23,8 % frente al 8,4 %; ocupaciones de alta cualificación, 21,5 % frente al 41,1 %; titulados superiores en ocupaciones que no lo requieren, 44,6 % frente al 32,2 %.

**Por provincias**, la brecha de empleo entre nacidos fuera y nacidos en España va de -16,6 a 3,0 pp. En 9 provincias los nacidos fuera tienen una tasa mayor (mapa 2).

**Crecimiento del empleo.** En 2014-2025 los nacidos fuera aportan el 55,6 % del aumento de la ocupación y el 71,8 % del de las horas.

**Europa.** La brecha de empleo de 20 a 64 años entre nacidos fuera y nativos es de -3,7 pp en España y de -6,4 pp en la UE-27 (mapa 3).

**Cohortes y generaciones** (C4). En el pseudopanel de cohortes de llegada (EPA 2005-2025, 25-54 años), la tasa de empleo relativa a los nativos de la cohorte llegada en 2015 o después es -8,1 pp distinta de la de la cohorte de 1995-2001 a igual tramo de residencia (IC 95 % [-12,4, -3,9]). Supuestos: efectos de periodo comunes a todas las cohortes y cohorte de referencia 1995-2001; la composición de cada cohorte cambia con las salidas. Los nacidos en España que conviven con un progenitor nacido fuera tienen una tasa de empleo -3,9 pp distinta (16-24 años) y -7,4 pp distinta (25-34) de la de quienes conviven con progenitores nacidos en España; solo se observa a quien convive con sus padres (output/f3/empleo_generaciones.csv).

![Gráfico 1](figuras/fig1_empleo.png)

![Mapa 2](figuras/mapa2_provincias_brecha_empleo.png)

![Mapa 3](figuras/mapa3_europa_nuts2.png)

### 3.3 Salarios

**Brecha de salario por hora** entre extranjeros y españoles (EES 2022, errores agrupados por establecimiento):
- bruta: -18,1 %;
- a igual edad y sexo: -15,5 %;
- además a igual estudios y región: -6,2 %;
- además a igual ocupación, sector, contrato y jornada: -3,0 % (informativo).

**Por percentiles**, la brecha es de -4,5 % en el 10, -19,4 % en la mediana y -26,5 % en el 90. La reponderación DFL atribuye a la composición el 64,0 %, el 62,0 % y el 66,0 % de la brecha en esos percentiles (gráfico 2; C4). Las cuotas de composición no llevan intervalo de confianza, y la de Oaxaca-Blinder usa como referencia la regresión agrupada; con otra referencia cambian.

**Segunda fuente.** Con la ECV, la mediana de los rendimientos del trabajo de los asalariados a jornada completa es un 29,5 % menor para los nacidos fuera de la UE.

**Convergencia salarial con los años de residencia: NO ESTIMABLE con datos públicos.** Ni la EES ni la ECV tienen años de residencia; haría falta la MCVL.

![Gráfico 2](figuras/fig2_salarios_dfl.png)

### 3.4 Vivienda

**Propiedad**, en la ECV 2021-2025:
- nacidos en España: 81,9 %;
- resto de la UE: 52,6 %;
- resto del mundo: 32,9 %.

Eurostat, como segunda fuente, da 84,1 % para los nativos y 38,7 % para los nacidos fuera. A igual edad, sexo, educación y región, la diferencia en propiedad de los nacidos fuera de la UE es de -45,3 pp (C4). Viven de alquiler a precio de mercado el 9,6 % de los nacidos en España, el 38,3 % de los nacidos en el resto de la UE y el 56,9 % de los nacidos fuera de la UE.

**Sobrecarga del gasto en vivienda:** 26,1 % frente a 4,9 %.

**Hacinamiento** (Eurostat): 19,6 % frente a 5,6 %.

**Demanda de hogares** (C2). A tasa de jefatura constante, el aumento de población de 2015-2022 implica 477 mil hogares de nacidos fuera y -225 mil de nacidos en España. No incluye la formación de hogares por envejecimiento.

### 3.5 Prestaciones

Personas que perciben cada prestación o viven en un hogar que la percibe (ECV 2021-2025, rentas de 2020-2024):

| Prestación | España | Resto UE | Resto del mundo |
|---|---|---|---|
| Desempleo (16-64) | 18,2 % | 22,9 % | 21,1 % |
| Jubilación (65+) | 72,5 % | 55,9 % | 44,1 % |
| Rentas mínimas e IMV | 5,5 % | 6,5 % | 11,9 % |
| Ayudas a la vivienda | 1,8 % | 2,2 % | 4,9 % |

A igual edad, sexo, educación y región (C4), la diferencia en rentas mínimas de los nacidos fuera de la UE es de 6,0 pp, y en jubilación de -29,0 pp. Rentas mínimas, IMV y ayudas a la vivienda son el 2,5 % de las prestaciones monetarias. Errores agrupados por hogar y año (la ECV pública no trae estratos ni conglomerados). Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad; el contraste con ellos no se ha hecho y queda como mejora futura (docs/fuentes/admin.md). Las prestaciones del hogar se atribuyen a cada miembro, así que las tasas miden personas que viven en hogares perceptores, no hogares.

## 4. Contabilidad fiscal estática y de ciclo vital

**Método.** Se sigue la OCDE (2021; referencia NO VERIFICADA por discrepancia de autor en Crossref) adaptada a datos públicos. Los ingresos y los gastos de las administraciones de 2024 se reparten entre las personas de la ECV 2025:
- impuestos sobre la renta, cotizaciones y prestaciones, observados en la encuesta y calibrados a las cuentas;
- IVA e impuestos especiales con la Encuesta de Presupuestos Familiares (EPF);
- sanidad con el perfil de uso de la Encuesta Nacional de Salud (ENSE);
- educación según matrícula;
- bienes públicos puros (servicios generales e intereses, defensa) a coste medio o a coste marginal cero.

Los ingresos no tributarios se reparten por persona, de modo que la suma cuadra con el saldo de las administraciones.

**Resultado estático (capa C2, gráfico 3).** Contribución neta por persona en 2024: escenario principal de referencia, intervalo de las 64 combinaciones de supuestos e intervalo de muestreo del principal (bootstrap por hogares, 200 réplicas):
- **nacidos en España:** -1.367 €; supuestos [-1.953, -636]; muestreo [-1.591, -1.115];
- **resto de la UE:** 3.432 €; supuestos [761, 5.949], positiva en las 64 combinaciones; muestreo [2.479, 4.342];
- **resto del mundo:** -160 € (solo referencia, D11); supuestos [-2.087, 2.823]; muestreo [-534, 290]. El signo depende de los bienes públicos y de los hijos nacidos en España (output/f4/signo_por_supuestos.csv).

**Déficit y comparación con los nativos.** Las cifras anteriores reparten el déficit de 2024 entre todos, por lo que los nacidos en España salen negativos en todos los supuestos. Dos lecturas complementarias:
- **Presupuesto equilibrado** (criterio de la OCDE: el saldo se reparte por igual por persona y la suma es cero): nacidos en España -350 € [-936, 146]; resto de la UE 4.449 € [1.778, 6.729]; resto del mundo 857 € [-1.070, 3.615].
- **Diferencia con los nacidos en España** en cada combinación de supuestos: resto de la UE 4.799 € [1.764, 7.601]; resto del mundo 1.207 € [-1.215, 4.552]. Para el resto del mundo el intervalo contiene el cero.
- **Conjunto de nacidos fuera** (la cantidad de las afirmaciones A5 y F3): 525 € [-1.515, 3.339]; frente a los nativos, 1.892 € [-643, 5.061]. El signo lo deciden solo los bienes públicos y la asignación de los hijos: coste medio e hijos a los padres, [-1.515, -670]; coste medio e hijos al hijo, [458, 1.146]; coste marginal e hijos a los padres, [187, 1.032]; coste marginal e hijos al hijo, [2.651, 3.339].

**A igual edad y sexo (C4).** Las cifras anteriores son brutas: buena parte de la ventaja frente a los nativos procede de la estructura por edad, porque las pensiones y la sanidad de los mayores pesan en los nativos. Con la estructura por edad (tramos de 10 años) y sexo de los nacidos en España y cobertura de todas las edades (donde una celda del grupo tiene menos de 10 observaciones se usa la media de su tramo de edad), la diferencia con los nativos es 737 € para el resto de la UE, positiva en las 64 combinaciones ([415, 3.481]), y -1.627 € para el resto del mundo, con un intervalo de supuestos que contiene el cero ([-1.860, 1.737], positiva en 32 de 64). En el principal, el IC 95 % aproximado por muestreo (error típico de 100 réplicas bootstrap por hogares, no centradas en la estimación) es [-210, 1.683] para el resto de la UE, que contiene el cero, y [-2.055, -1.200] para el resto del mundo. Es decir: a igual edad y sexo la ventaja del resto de la UE se reduce mucho y deja de ser distinguible de cero por muestreo; la del resto del mundo depende de supuestos. Coincide en lo esencial con Fiorio et al. (2023), que no hallan diferencia significativa a igual composición (condicionando también por la situación laboral). Una primera versión de este cálculo usaba solo celdas con al menos 50 observaciones, lo que excluía las edades en que los nacidos fuera salen mejor y daba diferencias negativas para los dos grupos; se corrigió en la revisión (docs/desviaciones.md, 22).

En prestaciones monetarias, los nacidos fuera de la UE reciben 1.927 € por persona y los nacidos en España 6.252 €, sobre todo por las pensiones. A igual edad y sexo, sobre las celdas comunes, siguen recibiendo menos: -3.637 € (resto del mundo) y -3.312 € (resto de la UE).

**Ciclo vital (C2).** Valor actual en 2024 de la contribución neta de por vida según la edad de llegada. Supuestos del escenario principal:
- supervivencia de la tabla de mortalidad de España;
- salida (retorno o reemigración) con un riesgo que decrece con la duración de la residencia, calibrado a la tasa observada de 6,3 % anual (emigraciones de nacidos fuera de 2021-2024 sobre el stock medio del mismo periodo). El riesgo es del 14,9 % anual en los primeros cinco años. La tasa incluye bajas por caducidad del padrón que no siempre son salidas reales, así que es una cota superior de las salidas;
- quien sale conserva la pensión contributiva devengada (exportable), que exige 15 años cotizados;
- sin convergencia adicional: el perfil transversal por edad ya mezcla duraciones de residencia, y añadir convergencia la contaría dos veces;
- descuento del 3 % y bienes públicos a coste medio.

Resultados en miles de euros (principal y, entre corchetes, el intervalo de las 24 combinaciones de salida, descuento y bienes públicos sin convergencia adicional; las combinaciones con convergencia se informan aparte porque la contarían dos veces):
- llegada a los 20 años: resto de la UE 10 [-17, 121]; resto del mundo -15 [-112, 44];
- llegada a los 30 años: resto de la UE 27 [-23, 116]; resto del mundo 6 [-98, 52];
- llegada a los 40 años: resto de la UE 28 [-39, 80]; resto del mundo 1 [-108, 36];
- llegada a los 50 años: resto de la UE 4 [-97, 33]; resto del mundo -20 [-162, 5];
- comparador, nacido en España de 30 años (vida restante, sin salidas; intervalo: descuento y bienes públicos): 99 [52, 121]; recién nacido en España: -87 [-113, -82].

**Signo (D11).** Para los dos grupos, todos los intervalos de llegada entre 20 y 50 años contienen el cero (resto del mundo, llegada a los 20: [-112, 44]; a los 50: [-162, 5]), y por D11 no se les asigna signo. La diferencia con un nacido en España de la misma edad, en cambio, es negativa en las 24 combinaciones para quienes llegan de fuera de la UE a los 20 años (-112 [-176, -61]) y a los 30 (-94 [-150, -19]), y contiene el cero a los 40 y para el resto de la UE. El comparador nativo no tiene salidas, lo que favorece su valor. Con convergencia, que el texto considera una doble contabilización, los intervalos se amplían hacia arriba (llegada a los 30, resto del mundo: hasta 147). Para la llegada a los 30, la parte hasta los 64 años («población joven hoy») es 28 y la de 65 y más años -22 (resto del mundo). Una primera versión de este cálculo omitía los ingresos no tributarios que se reparten por persona (≈ 1.800 € al año), lo que sumaba esa cantidad al déficit de todos; se corrigió en la revisión (docs/desviaciones.md, 20).

**Qué supuesto empuja en qué dirección** (output/f4/ciclo_vital_signos.csv):
- Las salidas cuentan mucho. Sin salidas (toda la vida en España), la llegada a los 30 da -41 (resto del mundo) y 29 (resto de la UE). La razón es que quien sale deja de generar gasto en sanidad y servicios en la vejez, aunque se lleve la pensión devengada. El principal usa la tasa observada, que es una cota superior de las salidas porque incluye bajas por caducidad; si las salidas reales fueran la mitad, la llegada a los 30 daría -7 (resto del mundo) y 32 (resto de la UE). Es decir, el principal está sesgado al alza en la dirección del sesgo de las caducidades.
- La convergencia, un descuento más alto y los bienes públicos a coste marginal cero mejoran el resultado.
- Los perfiles incluyen el déficit de 2024: todos los valores, también los de los nativos, salen más negativos que con presupuesto equilibrado.
- No se cuentan los descendientes ni su educación.

**Otras variantes del principal** (output/f4/ciclo_vital_sensibilidad.csv). Con presupuesto equilibrado, la llegada a los 30 da 16 (resto del mundo) y 37 (resto de la UE), y un nacido en España de 30 años 133. Rellenar los tramos de edad suprimidos con el perfil nativo sin escalar da 30 para el resto de la UE (los tramos de 0 a 24 y de 70 y más años de este grupo tienen menos de 50 observaciones). Quitar el mínimo de 15 años cotizados, una aproximación a la totalización europea de periodos, da -1 (resto del mundo) y 19 (resto de la UE); quitar el suelo de pensión no contributiva, 6 (resto del mundo). Con la mitad de salidas y sin el mínimo de 15 años a la vez, la llegada a los 30 da 25 (resto de la UE) y -12 (resto del mundo). Dos sesgos de signo opuesto quedan sin cuantificar: el gasto sanitario se toma del perfil nativo, aunque la ENSE observa menos uso entre los nacidos fuera, lo que juega en contra; y el perfil por edad es el de quienes residen hoy. Sin convergencia, a quien llega a los 20 se le aplica a los 30-44 años un perfil que mezcla recién llegados (en contra), y a quien llega a los 40 o 50 un perfil de residentes antiguos (a favor). El IBI se imputa solo a los propietarios, sin traslado a los inquilinos.

**Sensibilidad.** En la contabilidad estática lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos. Imputar coste marginal cero a los nacidos fuera traslada su parte de los bienes públicos a los nacidos en España (-498 € por persona). Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Fiorio et al. (2023, *International Tax and Public Finance*) estiman para España, en 2014-2018, una contribución neta por persona de los inmigrantes mayor que la de los nativos, sin diferencia significativa a igual composición demográfica. La cantidad comparable de este estudio es la diferencia con los nativos, con dos diferencias de diseño: el periodo (2024 frente a 2014-2018) y los bienes públicos. En bruto, para el resto de la UE la diferencia es positiva en las 64 combinaciones, en la dirección de Fiorio et al.; para el resto del mundo el intervalo contiene el cero. A igual edad y sexo, que es el nivel en que Fiorio et al. no hallan diferencia, la de M1 es positiva para el resto de la UE en todos los supuestos pero no distinguible de cero por muestreo, y su intervalo de supuestos contiene el cero para el resto del mundo. Fiorio et al. no incluyen los bienes públicos puros, lo que se aproxima a la variante a coste marginal cero de M1. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda; etiqueta prereg-m1 en el commit c247555, cuyo historial está en el repositorio remoto antes de cualquier estimación; pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia, con cuotas de 1998 de los nacidos fuera con nacionalidad extranjera y shocks nacionales por país de nacimiento;
- 50 provincias y tres periodos apilados (2005-2009, 2009-2015, 2015-2022), con controles de periodo, suma de cuotas, paro inicial, construcción y Bartik sectorial;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler; pretendencia con la afiliación de 1999-2001; permutaciones; exclusión de los orígenes con mayor peso de Rotemberg; sensibilidad por nacionalidad; multiverso de 32 especificaciones por hipótesis, más 6 variantes de sensibilidad y las 2 lecturas alternativas del control de cuotas.

**Corrección de un error que cambió los signos.** En la revisión de este documento se detectó que el control de cuotas incompletas del shift-share (la suma de las exposiciones del instrumento, por periodo) estaba mal construido en el código: no se dividía por la población inicial, como sí se hace en el instrumento. Con el control corregido, tal como lo define la adenda A1, la primera etapa pasa a ser fuerte al nivel del shock y cambian los signos de las dos confirmatorias. Las cifras que siguen son las corregidas y la corrección se documenta en docs/desviaciones.md (13). La corrección se hizo después de ver resultados y el texto del pre-registro admite dos lecturas: la adenda A1, que prevalece, define la exposición como cuota de la provincia / población inicial con shocks en niveles (variante «bhj», la principal); el texto original habla de «cuota de nacidos fuera en 1998», que corresponde a escribir los shocks como tasas de crecimiento («cuota_1998», con la población de 2002, primer año de la ECP). Se publican las tres con el mismo rango:

| Control de cuotas incompletas | F al nivel del shock | P1-H1 (empleo) | P1-H2 (paro) | P1-E3a (empleo, educación baja) |
|---|---|---|---|---|
| bhj (principal, adenda A1) | 13,5 | 0,06 | -0,55 | -0,61 |
| original (con el error) | 6,6 | -0,23 | 0,28 | -0,69 |
| cuota_1998 (lectura literal) | 10,0 | -0,16 | -0,36 | -0,85 |

De las tres, la principal es la menos desfavorable para el empleo y el paro de los nativos y la menos negativa en P1-E3a; el signo positivo de P1-H1 solo aparece con ella. Ninguna de las tres rechaza el cero en las confirmatorias.

**Primera etapa.** F al nivel del shock = 13,5 y F efectivo agrupado por provincia = 17,9, los dos por encima del umbral pre-registrado de 10. Aun así, los conjuntos AKM0 no están acotados: en ocho de las diez hipótesis de P1 y P2 son la recta real entera; en P1-E1 excluyen un tramo positivo que no contiene el cero; en P1-E3a el conjunto es (−∞, -0,06]. Con estos datos, ninguna hipótesis cumple la condición de IDENTIFICADO (conjunto acotado y convexo).

**Resultados (estimación puntual de MC2E; clasificación según las reglas pre-registradas):**

| Pregunta | Resultado de los nacidos en España | Estimación | p (Holm o BH) | Clasificación |
|---|---|---|---|---|
| P1-H1 | tasa de empleo (pp por pp) | 0,06 | 0,892 | ASOCIACIÓN |
| P1-H2 | tasa de paro (pp por pp) | -0,55 | 0,366 | ASOCIACIÓN |
| P1-E1 | tasa de actividad (pp por pp) | -0,39 | 0,402 | ASOCIACIÓN |
| P1-E2 | log de ocupados (log por pp) | 0,03 | 0,981 | ASOCIACIÓN |
| P1-E3a | tasa de empleo, educación baja (pp por pp) | -0,61 | 0,245 | ASOCIACIÓN |
| P1-E3b | tasa de empleo, educación media (pp por pp) | 0,13 | 0,981 | ASOCIACIÓN |
| P1-E3c | tasa de empleo, educación alta (pp por pp) | 0,60 | 0,402 | ASOCIACIÓN |
| P1-E4 | log salario por hora de los españoles, celdas educación × edad (Borjas) | -0,10 [-0,56, 0,36] | wild bootstrap | ASOCIACIÓN (techo) |
| P1-E5 | salarios provinciales | — | — | NO ESTIMABLE (AEAT no accesible) |
| P1-E6 | log de la población nacida en España de 15-64 (log por pp) | 0,16 | 0,981 | ASOCIACIÓN |
| P2-E1 | cuota en ocupaciones no manuales | 0,14 | 0,752 | ASOCIACIÓN |
| P2-E2 | cuota en ocupaciones de alta cualificación | 0,74 | 0,745 | ASOCIACIÓN |
| P3 | alumnos por profesor en la enseñanza pública (por pp, 17 CCAA) | -0,17 [-0,75, 0,41] | wild bootstrap | ASOCIACIÓN (techo) |
| P3 | listas de espera quirúrgicas | — | — | NO ESTIMABLE (solo PDF) |
| P4 | vivienda | — | — | no se duplica (Econometr-a) |
| P5 | tasa de empleo 20-64 de los nativos, NUTS2 de la UE-27 (pp por pp) | -0,33 [-0,97, 0,32] | wild bootstrap | ASOCIACIÓN |

Los intervalos de P1-E4, P3 y P5 son orientativos (errores agrupados con pocos grupos); su inferencia es el wild bootstrap, que no rechaza el cero en ninguno. P1-E4 (15 celdas) y la heterogeneidad de P5 (de 3 a 9 países por grupo) quedan fuera de lo validado por Monte Carlo para el wild bootstrap, y sus p son poco informativos.

**Todas las señales, con el mismo formato para lo favorable y lo desfavorable** (p de permutación recentrado; wild bootstrap de la forma reducida por comunidad; variante por nacionalidad con la envolvente de su conjunto AKM0; especificaciones del multiverso, de 32, con β negativo y que rechazan el cero sin ajustar):

| Hipótesis | β | permutación | wild bootstrap | nacionalidad | multiverso β < 0 | rechazan |
|---|---|---|---|---|---|---|
| P1-H1 empleo | 0,06 | 0,754 | 0,914 | -0,07 [-0,54, 0,36] | 24 | 6 |
| P1-H2 paro | -0,55 | 0,026 | 0,303 | 0,12 [-0,44, 0,68] | 11 | 2 |
| P1-E1 actividad | -0,39 | 0,078 | 0,251 | 0,04 [-0,20, 0,25] | 32 | 4 |
| P1-E2 log ocupados | 0,03 | 0,892 | 0,983 | -0,22 [-1,42, 0,49] | 15 | 0 |
| P1-E3a empleo, educación baja | -0,61 | 0,006 | 0,331 | -0,26 [-0,46, -0,04] | 32 | 13 |
| P1-E3b empleo, educación media | 0,13 | 0,654 | 0,925 | 0,19 [-0,31, 0,89] | 26 | 4 |
| P1-E3c empleo, educación alta | 0,60 | 0,028 | 0,379 | 0,06 [-0,40, 0,62] | 24 | 4 |
| P1-E6 población nativa | 0,16 | 0,662 | 0,613 | -0,09 [-0,91, 0,41] | 3 | 0 |
| P2-E1 no manuales | 0,14 | 0,586 | 0,750 | 0,11 [-0,33, 0,37] | 18 | 0 |
| P2-E2 alta cualificación | 0,74 | 0,070 | 0,336 | 0,21 [-0,83, 0,74] | 12 | 0 |

Tres hipótesis tienen un t fuera del 95 % central de las permutaciones: P1-E3a (desfavorable), P1-H2 (menos paro, favorable) y P1-E3c (más empleo de los nativos con educación alta, favorable). Ninguna supera la corrección por multiplicidad ni el wild bootstrap. No tienen el mismo respaldo: en P1-E3a la variante por nacionalidad está acotada y es negativa, las 32 especificaciones del multiverso tienen el mismo signo (13 rechazan el cero, todas negativas) y el jackknife por comunidad no cambia el signo; en P1-H2 la variante por nacionalidad tiene el signo contrario (0,12), solo 11 de 32 especificaciones tienen el signo favorable y las que rechazan el cero (2) son de signo positivo (más paro); en P1-E3c, 24 de 32 especificaciones tienen signo negativo y las 4 que rechazan son negativas. En P1-H1, las 6 que rechazan son negativas. El signo favorable de P1-H1, P1-H2 y P1-E3c aparece sobre todo en las especificaciones ponderadas y apiladas. P1-E1 (actividad) tiene 32 de 32 especificaciones con β negativo y permutación p = 0,078. Excluyendo cada comunidad, P1-H1 va de -0,37 a 0,49, P1-H2 de -0,97 a -0,11 y P1-E3c de -0,03 a 1,11. Con 17 grupos, la potencia del wild bootstrap frente a β = 0,5 es baja en el Monte Carlo (en torno a 0,2), así que no rechazar con él informa poco en cualquier dirección. El wild bootstrap con 17 comunidades tiene una condición en el Monte Carlo: una comunidad concentra el 42,2 % de la variación del instrumento, lo que con grupos asimétricos lo hace sobre-rechazar; sus p no favorecen el rechazo, pero tampoco son plenamente fiables. Los pesos de Rotemberg más altos son Rumanía en el periodo A (0,3), Venezuela en C (0,2), Marruecos en A (0,2) y en C (0,1) y el Reino Unido en A (-0,1, negativo); el peso negativo es el 18,8 % del peso absoluto de los 15 mayores.

**Lectura.** Ninguna hipótesis rechaza el cero con la corrección por multiplicidad pre-registrada. Las dos confirmatorias tienen signos opuestos a los de la versión con el error y no son significativas: la tasa de empleo, 0,06 (p de Holm = 0,892), y la tasa de paro, -0,55 (p de Holm = 0,366). El wild bootstrap de la forma reducida por comunidad autónoma, pre-registrado como control de dependencia espacial, tampoco rechaza (p = 0,914 y 0,303). En la variante por nacionalidad, cuyos conjuntos sí están acotados (F al nivel del shock = 18,4), la tasa de empleo da -0,07 [-0,54, 0,36] y la de paro 0,12 [-0,44, 0,68]: no se detecta efecto, y esa variante es compatible con efectos de entre -0,54 y 0,36 puntos por punto en el empleo y de entre -0,44 y 0,68 en el paro. Esa variante usa como tratamiento la población de nacionalidad extranjera de todas las edades (padrón), por lo que su escala no es exactamente la de la principal.

**P1-E3a: un indicio desfavorable, no un resultado.** La tasa de empleo de los nacidos en España con educación baja da -0,61 puntos por punto. Con el p sin ajustar de AKM0 rechazaría el cero al 5 %, pero no tras la corrección BH pre-registrada entre las seis exploratorias de P1 (p = 0,245), ni con el wild bootstrap por comunidad (p = 0,331). Señales que apuntan en la misma dirección, todas sin valor confirmatorio:
- el t de la especificación principal (-2,22) cae fuera del 95 % central de las 500 permutaciones de los shocks ([-1,60, 0,78]; p recentrado = 0,006);
- en la variante por nacionalidad el conjunto está acotado y es negativo: -0,26 [-0,46, -0,04];
- las 32 especificaciones del multiverso tienen β negativo (mediana -0,67); 13 rechazan el cero sin ajustar, pero comparten datos y cuotas, así que no son pruebas independientes;
- excluyendo cada comunidad autónoma por turno (exploratorio, a posteriori), β va de -1,04 a -0,19;
- con la representación del instrumento en tasas de crecimiento (exploratoria, a posteriori; F al nivel del shock = 11,4), el conjunto AKM0 está acotado y es negativo: -0,85 [-3,04, -0,35]. En esa representación P1-H1 da -0,16 y P1-H2 -0,36, sin rechazar el cero. La representación pre-registrada es la de niveles, y esta variante no puede cambiar ninguna clasificación.
En sentido contrario, cuatro hechos lo debilitan: (i) buena parte es composición por edad dentro del grupo: la proporción de jóvenes de 16-24 años entre los nativos con estudios bajos sube con el instrumento (0,52, p sin ajustar = 0,008); con la tasa estandarizada por edad la estimación baja a -0,30 (p = 0,278) y las señales de apoyo desaparecen: la variante por nacionalidad da -0,22 [-0,41, 0,04], la permutación p = 0,116 y el wild bootstrap p = 0,604 (sin la segunda generación identificable, en cambio, sigue siendo -0,51, p sin ajustar = 0,041); con 25-64 años es -0,41 (p = 0,071) y sin la segunda generación identificable, -0,51; (ii) depende mucho de una comunidad: sin la Comunitat Valenciana es -0,19, donde coinciden el ciclo de la construcción y las cuotas de rumanos y británicos; (iii) la exclusión de los tres orígenes de mayor peso de Rotemberg no es informativa (deja el F al nivel del shock en 0,9); (iv) el conjunto AKM0 de la principal no tiene cota inferior y la pretendencia se contrasta con la afiliación total, no con la tasa de empleo de este grupo. Por la regla pre-registrada queda en ASOCIACIÓN. Se trata con el mismo tono que los indicios favorables: es compatible con un efecto negativo moderado sobre los trabajadores nativos con estudios bajos, pero buena parte se explica por la composición por edad del grupo y se concentra en una comunidad, y no permite afirmarlo.

**Lectura de P1-E3a (exploratorio, a posteriori; no cambia ninguna clasificación, docs/desviaciones.md, 12).**
- *Magnitud frente a la literatura.* Expresada como elasticidad de la tasa de empleo respecto a la cuota de nacidos fuera, con las medias de los años iniciales, equivale a -0,15. Carrasco, Jimeno y Ortega (2008) estiman en torno a −0,17 para el conjunto de los nativos con solo inmigrantes legales (no significativa con todos), y González y Ortega (2011) no hallan efecto sobre los trabajadores poco cualificados (fichas en docs/literatura/trabajo.md). Gálvez-Iniesta (2025; NO VERIFICADA, sin DOI) estima por celdas un coeficiente log-log sobre el nivel de empleo, entre +0,19 y −0,03 según el periodo, en una escala que no es directamente comparable con la de M1. Dustmann, Schönberg y Stuhler (2016) advierten de que los efectos relativos por celdas no son comparables con los efectos totales por región. P1-E3a es, pues, del mismo orden que la elasticidad de Carrasco, Jimeno y Ortega (2008) y más negativo que lo que encuentran González y Ortega (2011).
- *MCO.* Por MCO, con la misma especificación, la asociación es -0,16. Con una primera etapa débil o moderada el MC2E tiende a sesgarse hacia el MCO; que el MC2E sea más negativo que el MCO indica que su magnitud no se explica por ese sesgo, aunque un MCO negativo es compatible con él.
- *Empleo o población.* El número de ocupados nativos con educación baja cae (-1,86 en log por punto, p sin ajustar = 0,395) y también su población (-1,07, p = 0,566), mientras crece la población nativa con educación media o alta (0,93). Una población menor sube la tasa, no la baja: la caída de la tasa es la diferencia entre las dos. Algo más de la mitad de la caída del número de ocupados se corresponde con una población del grupo más pequeña (salida geográfica, mejora educativa de los jóvenes o envejecimiento, que las encuestas transversales no distinguen), y la caída de la tasa queda íntegra después de descontarla. Ninguna de las tres estimaciones tiene un conjunto acotado, así que la descomposición es solo descriptiva.
- *Agregación.* La educación baja pesa el 48,7 % de los nativos de 16-64. En la variante por nacionalidad, la media ponderada de las estimaciones por nivel educativo (educación media 0,19, alta 0,06) es -0,06, dentro del conjunto de la tasa total. La tasa total también cambia por la composición educativa (los pesos varían entre periodos), término que esta aritmética omite.

**Multiverso y otras pruebas.** En el multiverso pre-registrado (32 especificaciones por hipótesis, más 6 variantes de sensibilidad y 2 lecturas del control), P1-H1 tiene 24 especificaciones con β negativo y mediana -0,38; P1-H2, 11 con β negativo y mediana 0,28. Los valores extremos proceden de diferencias largas con primera etapa nula; en las especificaciones con F al nivel del shock ≥ 10 (5), las medianas son 0,09 (empleo) y -0,48 (paro). Con el control corregido, las permutaciones de los shocks se centran cerca de cero (mediana del t de P1-H1 = -0,03). La pretendencia (afiliación 1999-2001) no es significativa (p = 0,690), pero el instrumento del periodo previo está casi colineal con el del primer periodo (correlación 0,97), lo que resta poder a esa prueba. En P5 ningún grupo institucional de países tiene un p del wild bootstrap por debajo de 0,3, y el anglosajón (un solo país) no es estimable. Con la potencia de este diseño, no detectar un efecto no equivale a ausencia de efecto. El detalle está en output/f5 (resultado.json por pregunta, con los conjuntos AKM0 como unión de intervalos, los pesos de Rotemberg, el multiverso y el jackknife).

**Revisión.** El replicador ciego y el abogado del diablo solo actúan, según el pre-registro, sobre lo que quede IDENTIFICADO o SUGESTIVO; no hay nada en esas categorías. Las desviaciones de implementación respecto al texto pre-registrado se documentan en docs/desviaciones.md; ninguna cambia la clasificación.

**Literatura verificada sobre España** (no es un resultado de M1): González y Ortega (2011) y el Banco de España (2026, Informe Anual 2025) no encuentran en general efectos negativos significativos sobre el empleo de los nativos; Carrasco, Jimeno y Ortega (2008) obtienen un efecto negativo cuando solo cuentan a los inmigrantes con permiso de trabajo.

## 6. Pensiones y demografía

Las pensiones de vejez y supervivencia suponen el 11,9 % del PIB en 2024. Tasa de dependencia de mayores de EUROPOP2023 en 2050, por cada 100 personas de 20 a 64 años (gráfico 4):
- variante base: 63,7;
- sin migración: 76,7;
- con un tercio más de migración: 59,5.

Con una regla mecánica que mantiene constantes el empleo, la cobertura y la pensión relativa, el gasto de 2050 sería del 21,7 % del PIB en la base y del 26,1 % sin migración. El Ageing Report 2024, que modeliza empleo y reformas, da 17,3 %, 16,1 % con más migración y 18,7 % con menos.

La regla mecánica es una comparación de escenarios, no un efecto estimado: sobrestima el nivel del gasto, pero el orden de los escenarios coincide con el del Ageing Report (más migración, menos gasto en proporción del PIB). Las cotizaciones de hoy generan derechos futuros (sección 4). La cifra del Ageing Report se toma del informe publicado y figura como NO VERIFICADA (sin DOI).

![Gráfico 4](figuras/fig4_dependencia.png)

## 7. Afirmaciones del debate y su veredicto

Las fichas completas están en [afirmaciones.md](afirmaciones.md). Resumen:

| id | Afirmación | Sentido | Veredicto |
|---|---|---|---|
| A1 | «Los inmigrantes viven de las ayudas: reciben más prestaciones que los nacidos en España.» | desfavorable | engañosa (media) |
| A2 | «La inmigración quita empleo a los españoles.» | desfavorable | no se puede saber (media) |
| A3 | «La inmigración hunde los salarios de los españoles.» | desfavorable | no se puede saber (media) |
| A4 | «Los inmigrantes colapsan la sanidad pública.» | desfavorable | no se puede saber (media) |
| A5 | «Los inmigrantes suponen un coste fiscal neto para España.» | desfavorable | no se puede saber (alta) |
| A6 | «La inmigración es la causa de la subida del precio de la vivienda.» | desfavorable | no se puede saber (media) |
| F1 | «Los inmigrantes pagan nuestras pensiones.» | favorable | no se puede saber (media) |
| F2 | «Sin inmigrantes no habría crecido el empleo.» | favorable | no se puede saber (media) |
| F3 | «Los inmigrantes aportan más de lo que reciben.» | favorable | no se puede saber (alta) |
| F4 | «Los inmigrantes trabajan tanto como los españoles.» | favorable | engañosa (media) |
| F5 | «A los inmigrantes se les paga menos por el mismo trabajo.» | favorable | se sostiene con matices (media) |
| F6 | «Los inmigrantes hacen los trabajos que los españoles no quieren.» | favorable | no se puede saber (media) |

Criterio común: cuando la contabilidad apoya una parte de la afirmación pero su núcleo es contrafactual («quita», «la causa», «sin ellos», «pagan», «colapsan») o sobre preferencias («no quieren») y no está identificado, el veredicto es «no se puede saber», en los dos sentidos. «Engañosa» se reserva para afirmaciones cuya cantidad principal la contabilidad contradice; «se sostiene con matices», para las que la contabilidad apoya en la cantidad principal con excepciones.

## 8. Limitaciones

- La fase 5 no identifica efectos: los conjuntos de confianza AKM0 no están acotados aunque la primera etapa sea fuerte (sección 5). Un error de código en el control de cuotas, corregido en la revisión, cambió los signos de las confirmatorias: la fragilidad de los signos es en sí un resultado.
- La agrupación de origen está limitada por las fuentes: tres grupos en la ECV y Eurostat, y la EPA sin Magreb.
- La ECV y la EPA públicas no traen el diseño muestral completo: los errores se agrupan por hogar (ECV), por celda (EPA) o por establecimiento (EES), y con ello los intervalos pueden ser algo estrechos.
- Las encuestas de hogares cubren peor a los inmigrantes recién llegados y a los que están en situación irregular, y no incluyen hogares colectivos (residencias, centros de acogida). La dirección del sesgo en la contabilidad fiscal no es conocida.
- La ENSE es de 2017.
- La contabilidad fiscal depende de supuestos de imputación, que se muestran como intervalos. El ciclo vital, además, no incluye a los descendientes y aplica perfiles transversales de 2024 a vidas futuras.
- La tasa de salida del ciclo vital incluye bajas por caducidad del padrón, que no siempre son salidas reales, y el perfil de riesgo por duración es un supuesto.
- No hay salarios provinciales por nacionalidad: la estadística de la AEAT no fue accesible.
- La ECV pondera unos 0,5 millones de nacidos fuera menos que la ECP de 2025 (recién llegados, situación irregular, hogares colectivos); la clasificación «resto de la UE» de la ECV sigue la del INE en cada ola.
- La regla mecánica de pensiones supone que el empleo, la cobertura y la pensión relativa de cada cohorte no cambian, es decir, que los nuevos residentes tienen el empleo medio; con la brecha de empleo a igual edad, la diferencia de 4,4 puntos estaría sobrestimada.
- «Positiva en las 64 combinaciones» se refiere a los supuestos; el error de muestreo solo se calcula para el principal y sin recalibrar.
- La regla de tres niveles no está completa en todas las comparaciones: vivienda y prestaciones tienen el nivel bruto y el completo pero no el de edad y sexo, y la contabilidad fiscal tiene el bruto y el de edad y sexo pero no el completo.
- El criterio para emitir veredictos sobre la cantidad literal de cada afirmación (matizada por los niveles ajustados) se fijó en la revisión, después de ver los datos.

### Qué cambiaría con datos no públicos

- **Muestra Continua de Vidas Laborales (MCVL).** Trayectorias individuales: convergencia salarial con los años de residencia, cotizaciones y pensiones futuras observadas, y retorno.
- **Microdatos de investigación de la EU-LFS y la EU-SILC.** País de nacimiento detallado por NUTS2, réplica del método de la OCDE en Europa y un shift-share europeo con cuotas anteriores a la llegada.
- **Datos administrativos de uso de servicios por origen** (historias clínicas, registros escolares, listas de espera por paciente). Congestión local y gasto en especie observado.
- **Paneles fiscales del IEF.** IRPF observado por origen.

## Anexos

- **A. Métodos:** docs/preregistro.md, docs/preregistro_adenda.md, src/m1/econ.py.
- **B. Pruebas por estimación y validación Monte Carlo:** docs/montecarlo.md.
- **C. Supuestos fiscales:** docstrings de src/m1/f4_fiscal.py y src/m1/f4_ciclo_vital.py, docs/supuestos/impuestos_indirectos_coicop.csv y output/f4/rejilla.csv.
- **D. Inventario de fuentes públicas:** docs/fuentes_publicas.md, docs/fuentes/*.md y data/fuentes.csv (URL, licencia, edición, fecha y sha256).
- **E. Bibliografía con estado de verificación:** output/f1/referencias.csv (VERIFICADA en Crossref o DataCite, o NO VERIFICADA).
- **F. Declaración de pre-registro interno.** El plan de la fase 5 se fijó en la etiqueta git prereg-m1 (commit c247555), antes de construir el instrumento y de estimar cualquier efecto. No tiene sello de tiempo externo. El commit está en el repositorio remoto (https://github.com/Phraselium/Contribution, rama claude/m1-contribucion-origen) antes de los commits de la fase 5; la etiqueta, que el proxy de la sesión no dejó subir, se sube desde el ordenador del autor (docs/tareas_autor.md).
- **Tablas:** tablas_m1.xlsx (azul: dato introducido con su fuente; negro: calculado; verde: de otra pestaña).
