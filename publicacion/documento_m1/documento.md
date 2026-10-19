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
- nacidos en España: -1.366 [-1.953, -635];
- nacidos en el resto de la UE: 3.428 [757, 5.949];
- nacidos fuera de la UE: -164 [-2.091, 2.823].

Las cifras incluyen el déficit de las administraciones, que se reparte entre todos; con presupuesto equilibrado (criterio de la OCDE) las cifras suben para todos (sección 4). Para el conjunto de nacidos fuera, la contribución es positiva en 48 de las 64 combinaciones. Estas comparaciones son brutas: a igual edad y sexo, la contribución neta de los nacidos fuera es menor que la de los nativos (-3.301 € el resto de la UE y -2.814 € el resto del mundo por persona). En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España: el principal es solo una referencia y lo que se afirma es el intervalo (decisión del autor, D11; tablas de signo en output/f4/signo_por_supuestos.csv y output/f4/ciclo_vital_signos.csv). En el ciclo vital (valor actual de por vida, sin convergencia adicional), para los nacidos fuera de la UE las llegadas a los 20 y a los 50 años son negativas en todos los supuestos y las de 30 y 40 años dependen de supuestos; para los nacidos en la UE todas las llegadas entre 20 y 50 años dependen de supuestos. Para la llegada a los 0 años son negativos en todos los supuestos, como el de un recién nacido en España, porque los perfiles incluyen el déficit de 2024 y no se cuentan los descendientes.

**Pensiones.** Con una regla demográfica mecánica, el gasto en pensiones de 2050 de la variante de EUROPOP2023 sin migración es 4,4 puntos de PIB mayor que el de la variante base. Es una comparación de escenarios con supuestos, no una proyección del sistema ni un efecto estimado. En el Ageing Report 2024, que modeliza empleo y reformas, la diferencia entre un tercio menos y un tercio más de migración es de 2,6 puntos (18,7 % frente a 16,1 %; referencia NO VERIFICADA, sin DOI).

**Impacto sobre la población local.** La estimación causal se hizo con el diseño pre-registrado (shift-share provincial con cuotas de 1998). Tras corregir un error de código en el control de cuotas incompletas detectado en la revisión, la primera etapa es fuerte al nivel del shock (F = 13,5), pero los conjuntos de confianza AKM0 no están acotados. Por las reglas fijadas antes de estimar, **ningún efecto queda IDENTIFICADO ni SUGESTIVO**: todas las preguntas causales son ASOCIACIÓN o NO ESTIMABLE, y ninguna rechaza el cero con la corrección por multiplicidad. Los datos públicos no permiten afirmar ni descartar un efecto de la inmigración sobre el empleo, los salarios o los servicios de la población local. El indicio más consistente es desfavorable y exploratorio: una asociación negativa con la tasa de empleo de los nacidos en España con educación baja (-0,61 puntos por punto), que no supera la corrección por multiplicidad ni el wild bootstrap (sección 5).

**Afirmaciones del debate.** Se evalúan doce afirmaciones: de las seis desfavorables a la inmigración, cinco con veredicto «no se puede saber» y una con veredicto «engañosa»; de las seis favorables a la inmigración, cuatro con veredicto «no se puede saber» y dos con veredicto «se sostiene con matices» (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. En conjunto trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales, y con grandes diferencias entre grupos. Cobran menos por hora; unos dos tercios de esa diferencia se corresponden con diferencias de edad, sexo, estudios y región, y el resto no se explica con esas variables. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas de un año (2024), los nacidos en otros países de la UE aportan más de lo que reciben en todas las combinaciones de supuestos estudiadas. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos. Esa ventaja se debe sobre todo a que son más jóvenes: comparados con nativos de la misma edad y sexo, aportan menos en neto. Cuando se mira toda la vida (impuestos de hoy y pensiones de mañana), el resultado depende de supuestos y, para quienes llegan de fuera de la UE muy jóvenes o ya mayores, es negativo.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. Con los datos públicos y el diseño fijado de antemano, la respuesta es que no se puede saber: las estimaciones son demasiado imprecisas para afirmar un efecto en cualquier sentido. Hay un indicio, no concluyente, de menor tasa de empleo de los nativos con estudios bajos en las provincias con más llegadas.

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

Personas que perciben cada prestación o viven en un hogar que la percibe (ECV, media 2021-2025):

| Prestación | España | Resto UE | Resto del mundo |
|---|---|---|---|
| Desempleo (16-64) | 18,2 % | 22,9 % | 21,1 % |
| Jubilación (65+) | 72,5 % | 55,9 % | 44,1 % |
| Rentas mínimas e IMV | 5,5 % | 6,5 % | 11,9 % |
| Ayudas a la vivienda | 1,8 % | 2,2 % | 4,9 % |

A igual edad, sexo, educación y región (C4), la diferencia en rentas mínimas de los nacidos fuera de la UE es de 6,0 pp, y en jubilación de -29,0 pp. Rentas mínimas, IMV y ayudas a la vivienda son el 2,5 % de las prestaciones monetarias. Errores agrupados por hogar y año (la ECV pública no trae estratos ni conglomerados). Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad; el contraste con ellos no se ha hecho y queda como mejora futura (docs/fuentes/admin.md). Las prestaciones del hogar se atribuyen a cada miembro, así que las tasas miden personas que viven en hogares perceptores, no hogares.

## 4. Contabilidad fiscal estática y de ciclo vital

**Método.** Se sigue la OCDE (2021) adaptada a datos públicos. Los ingresos y los gastos de las administraciones de 2024 se reparten entre las personas de la ECV 2025:
- impuestos sobre la renta, cotizaciones y prestaciones, observados en la encuesta y calibrados a las cuentas;
- IVA e impuestos especiales con la Encuesta de Presupuestos Familiares (EPF);
- sanidad con el perfil de uso de la Encuesta Nacional de Salud (ENSE);
- educación según matrícula;
- bienes públicos puros (servicios generales e intereses, defensa) a coste medio o a coste marginal cero.

Los ingresos no tributarios se reparten por persona, de modo que la suma cuadra con el saldo de las administraciones.

**Resultado estático (capa C2, gráfico 3).** Contribución neta por persona en 2024: escenario principal de referencia, intervalo de las 64 combinaciones de supuestos e intervalo de muestreo del principal (bootstrap por hogares, 200 réplicas):
- **nacidos en España:** -1.366 €; supuestos [-1.953, -635]; muestreo [-1.590, -1.114];
- **resto de la UE:** 3.428 €; supuestos [757, 5.949], positiva en las 64 combinaciones; muestreo [2.474, 4.338];
- **resto del mundo:** -164 € (solo referencia, D11); supuestos [-2.091, 2.823]; muestreo [-537, 286]. El signo depende de los bienes públicos y de los hijos nacidos en España (output/f4/signo_por_supuestos.csv).

**Déficit y comparación con los nativos.** Las cifras anteriores reparten el déficit de 2024 entre todos, por lo que los nacidos en España salen negativos en todos los supuestos. Dos lecturas complementarias:
- **Presupuesto equilibrado** (criterio de la OCDE: el saldo se reparte por igual por persona y la suma es cero): nacidos en España -349 € [-936, 147]; resto de la UE 4.445 € [1.774, 6.729]; resto del mundo 853 € [-1.073, 3.615].
- **Diferencia con los nacidos en España** en cada combinación de supuestos: resto de la UE 4.794 € [1.759, 7.601]; resto del mundo 1.203 € [-1.220, 4.552]. Para el resto del mundo el intervalo contiene el cero.
- **Conjunto de nacidos fuera** (la cantidad de las afirmaciones A5 y F3): 521 € [-1.519, 3.339], positiva en 48 de las 64 combinaciones; frente a los nativos, 1.887 € [-648, 5.061].

**A igual edad y sexo (C4).** Las cifras anteriores son brutas: la ventaja frente a los nativos procede en buena parte de la estructura por edad, porque las pensiones y la sanidad de los mayores pesan en los nativos. Con la estructura por edad y sexo de los nacidos en España, y comparando solo en las celdas de edad y sexo con al menos 50 observaciones del grupo (que cubren el 42,0 % del peso nativo para el resto de la UE y el 87,0 % para el resto del mundo), la diferencia con los nativos es -3.301 € para el resto de la UE (negativa en las 64 combinaciones: [-3.911, -358]) y -2.814 € para el resto del mundo ([-3.262, 602], positiva en 12 de 64). Es decir, a igual edad y sexo los nacidos fuera aportan, en neto, menos que los nativos. Coincide con Fiorio et al. (2023) en que la ventaja bruta desaparece a igual composición, y aquí incluso se invierte. Para el resto de la UE la cobertura es parcial (los tramos de 0 a 24 y de 70 y más años tienen menos de 50 observaciones), así que la cifra se refiere sobre todo a las edades de trabajo.

En prestaciones monetarias, los nacidos fuera de la UE reciben 1.927 € por persona y los nacidos en España 6.252 €, sobre todo por las pensiones. A igual edad y sexo, sobre las celdas comunes, siguen recibiendo menos: -2.741 € (resto del mundo) y -938 € (resto de la UE).

**Ciclo vital (C2).** Valor actual en 2024 de la contribución neta de por vida según la edad de llegada. Supuestos del escenario principal:
- supervivencia de la tabla de mortalidad de España;
- salida (retorno o reemigración) con un riesgo que decrece con la duración de la residencia, calibrado a la tasa observada de 6,3 % anual (emigraciones de nacidos fuera de 2021-2024 sobre el stock medio del mismo periodo). El riesgo es del 14,9 % anual en los primeros cinco años. La tasa incluye bajas por caducidad del padrón que no siempre son salidas reales, así que es una cota superior de las salidas;
- quien sale conserva la pensión contributiva devengada (exportable), que exige 15 años cotizados;
- sin convergencia adicional: el perfil transversal por edad ya mezcla duraciones de residencia, y añadir convergencia la contaría dos veces;
- descuento del 3 % y bienes públicos a coste medio.

Resultados en miles de euros (principal y, entre corchetes, el intervalo de las 24 combinaciones de salida, descuento y bienes públicos sin convergencia adicional; las combinaciones con convergencia se informan aparte porque la contarían dos veces):
- llegada a los 20 años: resto de la UE -9 [-101, 68]; resto del mundo -34 [-197, -4];
- llegada a los 30 años: resto de la UE 9 [-95, 68]; resto del mundo -13 [-173, 24];
- llegada a los 40 años: resto de la UE 12 [-100, 50]; resto del mundo -16 [-172, 16];
- llegada a los 50 años: resto de la UE -11 [-145, 15]; resto del mundo -36 [-214, -11];
- comparador, nacido en España de 30 años (vida restante, sin salidas; intervalo: descuento y bienes públicos): 38 [-25, 72]; recién nacido en España: -163 [-218, -140].

**Signo (D11).** Para el resto del mundo, las llegadas a los 20 y a los 50 años son negativas en todas las combinaciones sin convergencia, y las de 30 y 40 años tienen intervalos que contienen el cero. Para el resto de la UE, todos los intervalos de llegada entre 20 y 50 años contienen el cero. Con convergencia, que el texto considera una doble contabilización, los intervalos se amplían hacia arriba (llegada a los 30, resto del mundo: hasta 98). Los perfiles incluyen el déficit de 2024, que hace más negativos todos los valores, también los de los nativos. La diferencia con un nacido en España de la misma edad contiene el cero (llegada a los 30: resto del mundo -51 [-148, 33]). Para la llegada a los 30, la parte hasta los 64 años («población joven hoy») es 12 y la de 65 y más años -24 (resto del mundo).

**Qué supuesto empuja en qué dirección** (output/f4/ciclo_vital_signos.csv):
- Las salidas cuentan mucho. Sin salidas (toda la vida en España), la llegada a los 30 da -101 (resto del mundo) y -30 (resto de la UE). La razón es que quien sale deja de generar gasto en sanidad y servicios en la vejez, aunque se lleve la pensión devengada. El principal usa la tasa observada, que es una cota superior de las salidas porque incluye bajas por caducidad; si las salidas reales fueran la mitad, la llegada a los 30 daría -39 (resto del mundo) y 0 (resto de la UE). Es decir, el principal está sesgado al alza en la dirección del sesgo de las caducidades.
- La convergencia, un descuento más alto y los bienes públicos a coste marginal cero mejoran el resultado.
- Los perfiles incluyen el déficit de 2024: todos los valores, también los de los nativos, salen más negativos que con presupuesto equilibrado.
- No se cuentan los descendientes ni su educación.

**Otras variantes del principal** (output/f4/ciclo_vital_sensibilidad.csv). Con presupuesto equilibrado, la llegada a los 30 da -3 (resto del mundo) y 19 (resto de la UE), y un nacido en España de 30 años 72. Rellenar los tramos de edad suprimidos con el perfil nativo sin escalar da 11 para el resto de la UE (los tramos de 0 a 24 y de 70 y más años de este grupo tienen menos de 50 observaciones). Quitar el mínimo de 15 años cotizados, una aproximación a la totalización europea de periodos, da -19 (resto del mundo) y 1 (resto de la UE); quitar el suelo de pensión no contributiva, -13 (resto del mundo). Para el resto de la UE la regla de los 15 años sí importa. Dos sesgos de signo opuesto quedan sin cuantificar: el gasto sanitario se toma del perfil nativo, aunque la ENSE observa menos uso entre los nacidos fuera, lo que juega en contra; y el perfil por edad es el de quienes residen hoy, con más años de residencia que los recién llegados, lo que juega a favor.

**Sensibilidad.** En la contabilidad estática lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos. Imputar coste marginal cero a los nacidos fuera traslada su parte de los bienes públicos a los nacidos en España (-498 € por persona). Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Fiorio et al. (2023, *International Tax and Public Finance*) estiman para España, en 2014-2018, una contribución neta por persona de los inmigrantes mayor que la de los nativos, sin diferencia significativa a igual composición demográfica. La cantidad comparable de este estudio es la diferencia con los nativos, con dos diferencias de diseño: el periodo (2024 frente a 2014-2018) y que M1 no ajusta esa diferencia por composición. En bruto, para el resto de la UE la diferencia es positiva en las 64 combinaciones, en la dirección de Fiorio et al.; para el resto del mundo el intervalo contiene el cero. A igual edad y sexo, que es el nivel en que Fiorio et al. no hallan diferencia, la diferencia de M1 es negativa para los dos grupos. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda; etiqueta prereg-m1 en el commit c247555, cuyo historial está en el repositorio remoto antes de cualquier estimación; pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia, con cuotas de 1998 de los nacidos fuera con nacionalidad extranjera y shocks nacionales por país de nacimiento;
- 50 provincias y tres periodos apilados (2005-2009, 2009-2015, 2015-2022), con controles de periodo, suma de cuotas, paro inicial, construcción y Bartik sectorial;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler; pretendencia con la afiliación de 1999-2001; permutaciones; exclusión de los orígenes con mayor peso de Rotemberg; sensibilidad por nacionalidad; multiverso de 38 especificaciones por hipótesis confirmatoria.

**Corrección de un error que cambió los signos.** En la revisión de este documento se detectó que el control de cuotas incompletas del shift-share (la suma de las exposiciones del instrumento, por periodo) estaba mal construido en el código: no se dividía por la población inicial, como sí se hace en el instrumento. Con el control corregido, tal como lo describe el pre-registro, la primera etapa pasa a ser fuerte al nivel del shock y cambian los signos de las dos confirmatorias. Las cifras que siguen son las corregidas; la versión anterior queda como sensibilidad en output/f5/multiverso_p1.csv y la corrección se documenta en docs/desviaciones.md (13).

**Primera etapa.** F al nivel del shock = 13,5 y F efectivo agrupado por provincia = 17,9, los dos por encima del umbral pre-registrado de 10. Aun así, los conjuntos AKM0 no están acotados: en ocho de las diez hipótesis de P1 y P2 son la recta real entera; en P1-E1 excluyen un tramo positivo que no contiene el cero; en P1-E3a el conjunto es (−∞, -0,06]. Con estos datos, ninguna hipótesis cumple la condición de IDENTIFICADO (conjunto acotado y convexo).

**Resultados (estimación puntual de MC2E; clasificación según las reglas pre-registradas):**

| Pregunta | Resultado de los nacidos en España | Estimación | p (Holm o BH) | Clasificación |
|---|---|---|---|---|
| P1-H1 | tasa de empleo (pp por pp) | 0,06 | 0,892 | ASOCIACIÓN |
| P1-H2 | tasa de paro (pp por pp) | -0,55 | 0,366 | ASOCIACIÓN |
| P1-E1 | tasa de actividad | -0,39 | 0,402 | ASOCIACIÓN |
| P1-E2 | log de ocupados (log por pp) | 0,03 | 0,981 | ASOCIACIÓN |
| P1-E3a | tasa de empleo, educación baja | -0,61 | 0,245 | ASOCIACIÓN |
| P1-E3b | tasa de empleo, educación media | 0,13 | 0,981 | ASOCIACIÓN |
| P1-E3c | tasa de empleo, educación alta | 0,60 | 0,402 | ASOCIACIÓN |
| P1-E4 | log salario por hora de los españoles, celdas educación × edad (Borjas) | -0,10 [-0,56, 0,36] | wild bootstrap | ASOCIACIÓN (techo) |
| P1-E5 | salarios provinciales | — | — | NO ESTIMABLE (AEAT no accesible) |
| P1-E6 | log de la población nacida en España de 15-64 (log por pp) | 0,16 | 0,981 | ASOCIACIÓN |
| P2-E1 | cuota en ocupaciones no manuales | 0,14 | 0,752 | ASOCIACIÓN |
| P2-E2 | cuota en ocupaciones de alta cualificación | 0,74 | 0,745 | ASOCIACIÓN |
| P3 | alumnos por profesor en la enseñanza pública (por pp, 17 CCAA) | -0,17 [-0,75, 0,41] | wild bootstrap | ASOCIACIÓN (techo) |
| P3 | listas de espera quirúrgicas | — | — | NO ESTIMABLE (solo PDF) |
| P4 | vivienda | — | — | no se duplica (Econometr-a) |
| P5 | tasa de empleo 20-64 de los nativos, NUTS2 de la UE-27 (pp por pp) | -0,33 [-0,97, 0,32] | wild bootstrap | ASOCIACIÓN |

Los intervalos de P1-E4, P3 y P5 son orientativos (errores agrupados con pocos grupos); su inferencia es el wild bootstrap, que no rechaza el cero en ninguno.

**Lectura.** Ninguna hipótesis rechaza el cero con la corrección por multiplicidad pre-registrada. Las dos confirmatorias tienen signos opuestos a los de la versión con el error y no son significativas: la tasa de empleo, 0,06 (p de Holm = 0,892), y la tasa de paro, -0,55 (p de Holm = 0,366). El wild bootstrap de la forma reducida por comunidad autónoma, pre-registrado como control de dependencia espacial, tampoco rechaza (p = 0,914 y 0,303). En la variante por nacionalidad, cuyos conjuntos sí están acotados (F al nivel del shock = 18,4), la tasa de empleo da -0,07 [-0,55, 0,36] y la de paro 0,12 [-0,44, 0,68]: no se detecta efecto, y esa variante es compatible con efectos de hasta unos 0,5 puntos por punto en el empleo y 0,7 en el paro, en cualquier sentido. Esa variante usa como tratamiento la población de nacionalidad extranjera de todas las edades (padrón), por lo que su escala no es exactamente la de la principal.

**P1-E3a: un indicio desfavorable, no un resultado.** La tasa de empleo de los nacidos en España con educación baja da -0,61 puntos por punto. Con el p sin ajustar de AKM0 rechazaría el cero al 5 %, pero no tras la corrección BH pre-registrada entre las seis exploratorias de P1 (p = 0,245), ni con el wild bootstrap por comunidad (p = 0,331). Señales que apuntan en la misma dirección, todas sin valor confirmatorio:
- el t de la especificación principal (-2,22) cae fuera del 95 % central de las 500 permutaciones de los shocks ([-1,60, 0,78]; p recentrado = 0,006);
- en la variante por nacionalidad el conjunto está acotado y es negativo: -0,26 [-0,46, -0,04];
- las 32 especificaciones del multiverso tienen β negativo (mediana -0,67); 13 rechazan el cero sin ajustar, pero comparten datos y cuotas, así que no son pruebas independientes;
- excluyendo cada comunidad autónoma por turno (exploratorio, a posteriori), β va de -1,04 a -0,19.
En sentido contrario, la exclusión de los tres orígenes de mayor peso de Rotemberg no es informativa (deja el F al nivel del shock en 0,9) y el conjunto AKM0 de la principal no tiene cota inferior. Por la regla pre-registrada queda en ASOCIACIÓN. Se trata con el mismo tono que los indicios favorables: es compatible con un efecto negativo moderado sobre los trabajadores nativos con estudios bajos, y no permite afirmarlo.

**Lectura de P1-E3a (exploratorio, a posteriori; no cambia ninguna clasificación, docs/desviaciones.md, 12).**
- *Magnitud frente a la literatura.* Expresada como elasticidad de la tasa de empleo respecto a la cuota de nacidos fuera, con las medias de los años iniciales, equivale a -0,15. Carrasco, Jimeno y Ortega (2008) estiman en torno a −0,17 para el conjunto de los nativos con solo inmigrantes legales (no significativa con todos), y González y Ortega (2011) no hallan efecto sobre los trabajadores poco cualificados (fichas en docs/literatura/trabajo.md). Gálvez-Iniesta (2025; NO VERIFICADA, sin DOI) estima por celdas un coeficiente sobre el nivel de empleo, no sobre la tasa, entre +0,19 y −0,03 según el periodo; lo comparable de M1 es el log de ocupados con educación baja, -1,86 por punto. Dustmann, Schönberg y Stuhler (2016) advierten de que los efectos relativos por celdas no son comparables con los efectos totales por región. P1-E3a es, pues, del mismo orden que la elasticidad de Carrasco, Jimeno y Ortega (2008) y más negativo que el resto de la literatura española citada; en la comparación por nivel de empleo con Gálvez-Iniesta queda por debajo de su rango.
- *MCO.* Por MCO, con la misma especificación, la asociación es -0,16. Con una primera etapa débil o moderada el MC2E tiende a sesgarse hacia el MCO; que el MC2E sea más negativo que el MCO indica que su magnitud no se explica por ese sesgo, aunque un MCO negativo es compatible con él.
- *Empleo o población.* El número de ocupados nativos con educación baja cae (-1,86 en log por punto, p sin ajustar = 0,395) y también su población (-1,07, p = 0,566), mientras crece la población nativa con educación media o alta (0,93). Una población menor sube la tasa, no la baja: la caída de la tasa es la diferencia entre las dos. Algo más de la mitad de la caída del número de ocupados se corresponde con una población del grupo más pequeña (salida geográfica, mejora educativa de los jóvenes o envejecimiento, que las encuestas transversales no distinguen), y la caída de la tasa queda íntegra después de descontarla. Ninguna de las tres estimaciones tiene un conjunto acotado, así que la descomposición es solo descriptiva.
- *Agregación.* La educación baja pesa el 48,7 % de los nativos de 16-64. En la variante por nacionalidad, la media ponderada de las estimaciones por nivel educativo (educación media 0,19, alta 0,06) es -0,06, dentro del conjunto de la tasa total. La tasa total también cambia por la composición educativa (los pesos varían entre periodos), término que esta aritmética omite.

**Multiverso y otras pruebas.** En el multiverso pre-registrado (32 especificaciones por hipótesis, más 6 variantes de sensibilidad), P1-H1 tiene 24 especificaciones con β negativo y mediana -0,38; P1-H2, 11 con β negativo y mediana 0,28. Los valores extremos proceden de diferencias largas con primera etapa nula; en las especificaciones con F al nivel del shock ≥ 10 (5), las medianas son 0,09 (empleo) y -0,48 (paro). Con el control corregido, las permutaciones de los shocks se centran cerca de cero (mediana del t de P1-H1 = -0,03). La pretendencia (afiliación 1999-2001) no es significativa (p = 0,690), pero el instrumento del periodo previo está casi colineal con el del primer periodo (correlación 0,97), lo que resta poder a esa prueba. En P5 ningún grupo institucional de países tiene un p del wild bootstrap por debajo de 0,3, y el anglosajón (un solo país) no es estimable. Con la potencia de este diseño, no detectar un efecto no equivale a ausencia de efecto. El detalle está en output/f5 (resultado.json por pregunta, con los conjuntos AKM0 como unión de intervalos, los pesos de Rotemberg, el multiverso y el jackknife).

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

Las fichas completas están en `afirmaciones.md`. Resumen:

| id | Afirmación | Sentido | Veredicto |
|---|---|---|---|
| A1 | «Los inmigrantes viven de las ayudas: reciben más prestaciones que los nacidos en España.» | desfavorable | engañosa (alta) |
| A2 | «La inmigración quita empleo a los españoles.» | desfavorable | no se puede saber (media) |
| A3 | «La inmigración hunde los salarios de los españoles.» | desfavorable | no se puede saber (media) |
| A4 | «Los inmigrantes colapsan la sanidad pública.» | desfavorable | no se puede saber (media) |
| A5 | «Los inmigrantes suponen un coste fiscal neto para España.» | desfavorable | no se puede saber (alta) |
| A6 | «La inmigración es la causa de la subida del precio de la vivienda.» | desfavorable | no se puede saber (media) |
| F1 | «Los inmigrantes pagan nuestras pensiones.» | favorable | no se puede saber (media) |
| F2 | «Sin inmigrantes no habría crecido el empleo.» | favorable | no se puede saber (media) |
| F3 | «Los inmigrantes aportan más de lo que reciben.» | favorable | no se puede saber (alta) |
| F4 | «Los inmigrantes trabajan tanto como los españoles.» | favorable | se sostiene con matices (media) |
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
- La ECV pondera unos 0,45 millones de nacidos fuera menos que la ECP de 2025 (recién llegados, situación irregular, hogares colectivos); la clasificación «resto de la UE» de la ECV sigue la del INE en cada ola.
- La regla mecánica de pensiones supone que el empleo, la cobertura y la pensión relativa de cada cohorte no cambian, es decir, que los nuevos residentes tienen el empleo medio; con la brecha de empleo a igual edad, la diferencia de 4,4 puntos estaría sobrestimada.
- «Positiva en las 64 combinaciones» se refiere a los supuestos del principal; el error de muestreo solo se calcula para el principal.

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
