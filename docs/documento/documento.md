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

**Población.** La población nacida fuera de España era el {{F3_POB_FUERA_PADRON_2022}} % en el padrón de 2022 y el {{F3_POB_FUERA_ECP_2025}} % en la Estadística Continua de Población de 2025. En 1998 era el {{F3_POB_FUERA_PADRON_1998}} %. En la UE-27 la cifra es del {{F3_POB_FUERA_UE27_2025}} % (Eurostat, que para España se basa en la misma estadística del INE). Es una población más joven: el {{F3_POB_65MAS_nacidos fuera_2025}} % tiene 65 o más años, frente al {{F3_POB_65MAS_España_2025}} % de los nacidos en España.

**Empleo.** En 2025 la tasa de empleo de 16 a 64 años es del {{F3_EMP_TASA_FUERA_2025}} % entre los nacidos fuera y del {{F3_EMP_TASA_España_2025}} % entre los nacidos en España. La variación interna es amplia: África {{F3_EMP_TASA_África_2025}} %, UE-14 {{F3_EMP_TASA_UE-14_2025}} %. El paro es mayor entre los nacidos fuera: {{F3_EMP_PARO_FUERA_2025}} % frente a {{F3_EMP_PARO_España_2025}} %. Al aumento de la ocupación entre 2014 y 2025, de {{F3_EMP_AUMENTO_OCUPADOS_2014_2025}} millones, los nacidos fuera aportan el {{F3_EMP_CONTRIB_FUERA_2014_2025}} %. Es contabilidad: no dice qué habría ocurrido sin inmigración.

**Salarios.** Los extranjeros cobran por hora un {{F3_SAL_BRECHA_bruto_2022:abs}} % menos que los españoles (Encuesta de Estructura Salarial, EES, 2022). A igual edad, sexo, estudios y región la diferencia baja al {{F3_SAL_BRECHA_completo_2022:abs}} % menos (exploratorio, C4). En la descomposición de Oaxaca-Blinder, alrededor del {{F3_SAL_OAXACA_COMPOSICION_2022}} % de la brecha media corresponde a diferencias de composición observables.

**Vivienda.** Vive en vivienda en propiedad el {{F3_VIV_propietario_España_2021_2025}} % de los nacidos en España, frente al {{F3_VIV_propietario_Resto_del_mundo_2021_2025}} % de los nacidos fuera de la UE. La sobrecarga del gasto en vivienda afecta al {{F3_VIV_sobrecarga_Resto_del_mundo_2021_2025}} % de los segundos y al {{F3_VIV_sobrecarga_España_2021_2025}} % de los primeros.

**Cuentas públicas.** Contribución neta estática en 2024, en euros por persona: escenario principal de referencia e intervalo de las 64 combinaciones de supuestos (capa C2):
- nacidos en España: {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024}} [{{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}}];
- nacidos en el resto de la UE: {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024}} [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}}];
- nacidos fuera de la UE: {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024}} [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}].

Las cifras incluyen el déficit de las administraciones, que se reparte entre todos; con presupuesto equilibrado (criterio de la OCDE) las cifras suben para todos (sección 4). Para el conjunto de nacidos fuera, el signo depende de dos supuestos: con bienes públicos a coste medio y los hijos nacidos en España asignados a sus padres es negativo en todas las combinaciones de los demás supuestos ([{{F4_NETA_FUERA_MEDIO_PADRES:inf}}, {{F4_NETA_FUERA_MEDIO_PADRES:sup}}] €), y en las otras tres celdas, positivo. Estas comparaciones son brutas. A igual edad y sexo, frente a los nativos de las mismas celdas, la diferencia del principal es {{F4_NETA_EST_DIF_NAT_Resto_UE_2024}} € para el resto de la UE (negativa en las 64 combinaciones, pero solo en las edades centrales, las únicas con datos suficientes: {{F4_COBERTURA_EST_Resto_UE}} % del peso nativo) y {{F4_NETA_EST_DIF_NAT_Resto_del_mundo_2024}} € para el resto del mundo, cuyo intervalo de supuestos contiene el cero (positiva en {{F4_NETA_EST_DIF_NAT_POSITIVAS_Resto_del_mundo}} de 64). En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España: el principal es solo una referencia y lo que se afirma es el intervalo (decisión del autor, D11; tablas de signo en output/f4/signo_por_supuestos.csv y output/f4/ciclo_vital_signos.csv). En el ciclo vital (valor actual de por vida, sin convergencia adicional), para los nacidos fuera de la UE las llegadas a los 20 y a los 50 años son negativas en las 24 combinaciones de supuestos y las de 30 y 40 años dependen de supuestos; para los nacidos en la UE todas las llegadas entre 20 y 50 años dependen de supuestos. Las llegadas a los 0 años son negativas en todos los supuestos, como el valor de un recién nacido en España. Todos los valores incluyen el déficit de 2024 y excluyen a los descendientes; con convergencia, los intervalos se amplían hacia arriba.

**Pensiones.** Con una regla demográfica mecánica, el gasto en pensiones de 2050 de la variante de EUROPOP2023 sin migración es {{F4_PEN_DIF_SIN_MIGRACION_2050}} puntos de PIB mayor que el de la variante base, y entre las variantes con menos y con más migración la diferencia es de {{F4_PEN_MEC_DIF_LMIGR_HMIGR_2050}} puntos. Es una comparación de escenarios con supuestos, no una proyección del sistema ni un efecto estimado. En el Ageing Report 2024, que modeliza empleo y reformas, la diferencia entre un tercio menos y un tercio más de migración es de {{F4_PEN_AR2024_DIF_MIGRACION_2050}} puntos ({{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % frente a {{F4_PEN_AR2024_MAS_MIGRACION_2050}} %; referencia NO VERIFICADA, sin DOI).

**Impacto sobre la población local.** La estimación causal se hizo con el diseño pre-registrado (shift-share provincial con cuotas de 1998). Tras corregir un error de código en el control de cuotas incompletas detectado en la revisión (que cambió los signos de las confirmatorias; las tres lecturas del control se publican), la primera etapa es fuerte al nivel del shock (F = {{F5_P1_F_SHOCK}}), pero los conjuntos de confianza AKM0 no están acotados. Por las reglas fijadas antes de estimar, **ningún efecto queda IDENTIFICADO ni SUGESTIVO**: todas las preguntas causales son ASOCIACIÓN o NO ESTIMABLE, y ninguna rechaza el cero con la corrección por multiplicidad. Los datos públicos no permiten afirmar ni descartar un efecto de la inmigración sobre el empleo, los salarios o los servicios de la población local. El indicio más consistente es desfavorable y exploratorio: la tasa de empleo de los nacidos en España con educación baja tiene una estimación de {{F5_P1_E3a_beta}} puntos por punto, con un conjunto de confianza sin cota inferior, que no supera la corrección por multiplicidad ni el wild bootstrap y que en parte se debe a la composición por edad y a una sola comunidad. Hay también indicios favorables de la misma fuerza en el paro y en el empleo de los nativos con educación alta (sección 5).

**Afirmaciones del debate.** {{TEXTO_BALANCE}} (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. En conjunto trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales, y con grandes diferencias entre grupos. Cobran menos por hora; unos dos tercios de esa diferencia se corresponden con diferencias de edad, sexo, estudios y región, y el resto no se explica con esas variables. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas de un año (2024), los nacidos en otros países de la UE aportan más de lo que reciben en todas las combinaciones de supuestos estudiadas. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos. Esa ventaja se debe sobre todo a que son más jóvenes: comparados con nativos de la misma edad y sexo, los nacidos en otros países de la UE aportan menos en las edades de trabajo, y para los nacidos fuera de la UE el resultado depende de supuestos. Cuando se mira toda la vida (impuestos de hoy y pensiones de mañana), el resultado depende de supuestos y, para quienes llegan de fuera de la UE muy jóvenes o ya mayores, es negativo; también lo es para un nativo de 40 años, porque las cuentas incluyen el déficit actual, y la diferencia con un nativo de la misma edad depende de supuestos.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. Con los datos públicos y el diseño fijado de antemano, la respuesta es que no se puede saber: las estimaciones son demasiado imprecisas para afirmar un efecto en cualquier sentido. Hay un indicio, no concluyente, de menor tasa de empleo de los nativos con estudios bajos en las provincias con más llegadas, y otros de la misma fuerza en sentido favorable (menos paro y más empleo de los nativos con estudios altos).

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

Los nacionalizados son el {{F3_POB_NACIONALIZADOS_2022}} % de los nacidos fuera. La segunda generación solo se identifica si convive con sus padres (EPA, ECV).

El inventario de fuentes, con URL, licencia, fecha y sha256, está en el anexo D y en `data/fuentes.csv`. Lo que no es público, y qué pregunta afecta, está en la sección 8.

**Protección de datos.** Solo se publican agregados y se suprimen las celdas con menos de 50 observaciones muestrales. Las encuestas públicas no traen estratos ni conglomerados, salvo la EES (establecimiento), y los errores se agrupan en consecuencia (D7).

## 3. Hechos: población, empleo, salarios, vivienda y prestaciones

### 3.1 Población

La población nacida fuera pasó del {{F3_POB_FUERA_PADRON_1998}} % en 1998 al {{F3_POB_FUERA_PADRON_2022}} % en 2022. Por grupos, en 2022: América Latina {{F3_POB_CUOTA_América Latina_2022}} %, UE-13 y otros de Europa {{F3_POB_CUOTA_UE-13 y otros de Europa_2022}} %, UE-14 {{F3_POB_CUOTA_UE-14_2022}} %, Magreb {{F3_POB_CUOTA_Magreb_2022}} %, Asia {{F3_POB_CUOTA_Asia_2022}} % y resto de África {{F3_POB_CUOTA_Resto de África_2022}} %.

Por provincias va del {{F3_POB_FUERA_PROV_MIN_2022}} % al {{F3_POB_FUERA_PROV_MAX_2022}} % (mapa 1).

Entre 2021 y 2024 el saldo migratorio exterior de los nacidos fuera fue de {{F3_POB_SALDO_EXTERIOR_FUERA_2021_2024}} millones, y el de los nacidos en España de {{F3_POB_SALDO_EXTERIOR_ESPANA_2021_2024}} millones.

El {{F3_POB_RESID_20MAS_2025}} % de los nacidos fuera de 16 o más años lleva 20 años o más en España, y el {{F3_POB_RESID_0A4_2025}} % menos de 5.

En Europa, España ocupa el puesto {{F3_POB_FUERA_ES_RANKING_2025}} por cuota de nacidos fuera ({{F3_POB_FUERA_ES_EUROSTAT_2025}} % según Eurostat, que procede de la misma estadística del INE y no es una fuente independiente).

![Mapa 1](figuras/mapa1_provincias_nacidos_fuera.png)

### 3.2 Empleo

Tasas de empleo de 16 a 64 años en 2025 (gráfico 1):
- nacidos en España: {{F3_EMP_TASA_España_2025}} %;
- UE-14: {{F3_EMP_TASA_UE-14_2025}} %;
- UE-13 y otros de Europa: {{F3_EMP_TASA_UE-13 y otros de Europa_2025}} %;
- América Latina: {{F3_EMP_TASA_América Latina_2025}} %;
- África: {{F3_EMP_TASA_África_2025}} %;
- Asia: {{F3_EMP_TASA_Asia_2025}} %.

**Tres niveles** (los ajustados son C4). La brecha de África con los nacidos en España es de {{F3_EMP_BRECHA_África_bruto_2025}} pp en bruto, {{F3_EMP_BRECHA_África_edad_y_sexo_2025}} pp a igual edad y sexo, y {{F3_EMP_BRECHA_África_completo_2025}} pp al añadir educación, residencia (10 a 19 años) y región. La de América Latina es de {{F3_EMP_BRECHA_América Latina_bruto_2025}} pp en bruto, {{F3_EMP_BRECHA_América Latina_edad_y_sexo_2025}} pp a igual edad y sexo y {{F3_EMP_BRECHA_América Latina_completo_2025}} pp en el nivel completo: el nivel intermedio cambia el signo.

**Calidad del empleo** (2025): contrato temporal, {{F3_EMP_TEMPORALIDAD_FUERA_2025}} % de los asalariados nacidos fuera frente al {{F3_EMP_TEMPORALIDAD_España_2025}} %; ocupaciones elementales, {{F3_EMP_OCUP_ELEMENTALES_FUERA_2025}} % frente al {{F3_EMP_OCUP_ELEMENTALES_España_2025}} %; ocupaciones de alta cualificación, {{F3_EMP_OCUP_ALTA_CUALIF_FUERA_2025}} % frente al {{F3_EMP_OCUP_ALTA_CUALIF_España_2025}} %; titulados superiores en ocupaciones que no lo requieren, {{F3_EMP_SOBRECUALIFICACION_FUERA_2025}} % frente al {{F3_EMP_SOBRECUALIFICACION_España_2025}} %.

**Por provincias**, la brecha de empleo entre nacidos fuera y nacidos en España va de {{F3_EMP_BRECHA_PROV_MIN_2025}} a {{F3_EMP_BRECHA_PROV_MAX_2025}} pp. En {{F3_EMP_BRECHA_PROV_POSITIVAS_2025}} provincias los nacidos fuera tienen una tasa mayor (mapa 2).

**Crecimiento del empleo.** En 2014-2025 los nacidos fuera aportan el {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del aumento de la ocupación y el {{F3_EMP_CONTRIB_HORAS_FUERA_2014_2025}} % del de las horas.

**Europa.** La brecha de empleo de 20 a 64 años entre nacidos fuera y nativos es de {{F3_EMP_EU_ES_BRECHA_2025}} pp en España y de {{F3_EMP_EU_UE27_BRECHA_2025}} pp en la UE-27 (mapa 3).

**Cohortes y generaciones** (C4). En el pseudopanel de cohortes de llegada (EPA 2005-2025, 25-54 años), la tasa de empleo relativa a los nativos de la cohorte llegada en 2015 o después es {{F3_EMP_COHORTE_2015_REL}} pp distinta de la de la cohorte de 1995-2001 a igual tramo de residencia (IC 95 % [{{F3_EMP_COHORTE_2015_REL:inf}}, {{F3_EMP_COHORTE_2015_REL:sup}}]). Supuestos: efectos de periodo comunes a todas las cohortes y cohorte de referencia 1995-2001; la composición de cada cohorte cambia con las salidas. Los nacidos en España que conviven con un progenitor nacido fuera tienen una tasa de empleo {{F3_EMP_SEGUNDA_GEN_16_24}} pp distinta (16-24 años) y {{F3_EMP_SEGUNDA_GEN_25_34}} pp distinta (25-34) de la de quienes conviven con progenitores nacidos en España; solo se observa a quien convive con sus padres (output/f3/empleo_generaciones.csv).

![Gráfico 1](figuras/fig1_empleo.png)

![Mapa 2](figuras/mapa2_provincias_brecha_empleo.png)

![Mapa 3](figuras/mapa3_europa_nuts2.png)

### 3.3 Salarios

**Brecha de salario por hora** entre extranjeros y españoles (EES 2022, errores agrupados por establecimiento):
- bruta: {{F3_SAL_BRECHA_bruto_2022}} %;
- a igual edad y sexo: {{F3_SAL_BRECHA_edad_2022}} %;
- además a igual estudios y región: {{F3_SAL_BRECHA_completo_2022}} %;
- además a igual ocupación, sector, contrato y jornada: {{F3_SAL_BRECHA_completo_inf_2022}} % (informativo).

**Por percentiles**, la brecha es de {{F3_SAL_BRECHA_P10_2022}} % en el 10, {{F3_SAL_BRECHA_P50_2022}} % en la mediana y {{F3_SAL_BRECHA_P90_2022}} % en el 90. La reponderación DFL atribuye a la composición el {{F3_SAL_COMPOSICION_P10_2022}} %, el {{F3_SAL_COMPOSICION_P50_2022}} % y el {{F3_SAL_COMPOSICION_P90_2022}} % de la brecha en esos percentiles (gráfico 2; C4). Las cuotas de composición no llevan intervalo de confianza, y la de Oaxaca-Blinder usa como referencia la regresión agrupada; con otra referencia cambian.

**Segunda fuente.** Con la ECV, la mediana de los rendimientos del trabajo de los asalariados a jornada completa es un {{F3_SAL_ECV_BRECHA_Resto_del_mundo_2024:abs}} % menor para los nacidos fuera de la UE.

**Convergencia salarial con los años de residencia: NO ESTIMABLE con datos públicos.** Ni la EES ni la ECV tienen años de residencia; haría falta la MCVL.

![Gráfico 2](figuras/fig2_salarios_dfl.png)

### 3.4 Vivienda

**Propiedad**, en la ECV 2021-2025:
- nacidos en España: {{F3_VIV_propietario_España_2021_2025}} %;
- resto de la UE: {{F3_VIV_propietario_Resto_UE_2021_2025}} %;
- resto del mundo: {{F3_VIV_propietario_Resto_del_mundo_2021_2025}} %.

Eurostat, como segunda fuente, da {{F3_VIV_EU_ilc_lvps16_NAT_ES_2025}} % para los nativos y {{F3_VIV_EU_ilc_lvps16_FOR_ES_2025}} % para los nacidos fuera. A igual edad, sexo, educación y región, la diferencia en propiedad de los nacidos fuera de la UE es de {{F3_VIV_propietario_BRECHA_COMPLETO_Resto_del_mundo}} pp (C4). Viven de alquiler a precio de mercado el {{F3_VIV_alquiler_mercado_España_2021_2025}} % de los nacidos en España, el {{F3_VIV_alquiler_mercado_Resto_UE_2021_2025}} % de los nacidos en el resto de la UE y el {{F3_VIV_alquiler_mercado_Resto_del_mundo_2021_2025}} % de los nacidos fuera de la UE.

**Sobrecarga del gasto en vivienda:** {{F3_VIV_sobrecarga_Resto_del_mundo_2021_2025}} % frente a {{F3_VIV_sobrecarga_España_2021_2025}} %.

**Hacinamiento** (Eurostat): {{F3_VIV_EU_ilc_lvho16_FOR_ES_2025}} % frente a {{F3_VIV_EU_ilc_lvho16_NAT_ES_2025}} %.

**Demanda de hogares** (C2). A tasa de jefatura constante, el aumento de población de 2015-2022 implica {{F3_VIV_DEMANDA_FUERA_2015_2022}} mil hogares de nacidos fuera y {{F3_VIV_DEMANDA_ESPANA_2015_2022}} mil de nacidos en España. No incluye la formación de hogares por envejecimiento.

### 3.5 Prestaciones

Personas que perciben cada prestación o viven en un hogar que la percibe (ECV 2021-2025, rentas de 2020-2024):

| Prestación | España | Resto UE | Resto del mundo |
|---|---|---|---|
| Desempleo (16-64) | {{F3_PRE_desempleo_España}} % | {{F3_PRE_desempleo_Resto_UE}} % | {{F3_PRE_desempleo_Resto_del_mundo}} % |
| Jubilación (65+) | {{F3_PRE_jubilacion_España}} % | {{F3_PRE_jubilacion_Resto_UE}} % | {{F3_PRE_jubilacion_Resto_del_mundo}} % |
| Rentas mínimas e IMV | {{F3_PRE_rentas_minimas_IMV_España}} % | {{F3_PRE_rentas_minimas_IMV_Resto_UE}} % | {{F3_PRE_rentas_minimas_IMV_Resto_del_mundo}} % |
| Ayudas a la vivienda | {{F3_PRE_ayuda_vivienda_España}} % | {{F3_PRE_ayuda_vivienda_Resto_UE}} % | {{F3_PRE_ayuda_vivienda_Resto_del_mundo}} % |

A igual edad, sexo, educación y región (C4), la diferencia en rentas mínimas de los nacidos fuera de la UE es de {{F3_PRE_BRECHA_perceptor_rentas_minimas_IMV_Resto_del_mundo_completo}} pp, y en jubilación de {{F3_PRE_BRECHA_perceptor_jubilacion_Resto_del_mundo_completo}} pp. Rentas mínimas, IMV y ayudas a la vivienda son el {{F6_PREST_NO_CONTRIB_CUOTA}} % de las prestaciones monetarias. Errores agrupados por hogar y año (la ECV pública no trae estratos ni conglomerados). Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad; el contraste con ellos no se ha hecho y queda como mejora futura (docs/fuentes/admin.md). Las prestaciones del hogar se atribuyen a cada miembro, así que las tasas miden personas que viven en hogares perceptores, no hogares.

## 4. Contabilidad fiscal estática y de ciclo vital

**Método.** Se sigue la OCDE (2021) adaptada a datos públicos. Los ingresos y los gastos de las administraciones de 2024 se reparten entre las personas de la ECV 2025:
- impuestos sobre la renta, cotizaciones y prestaciones, observados en la encuesta y calibrados a las cuentas;
- IVA e impuestos especiales con la Encuesta de Presupuestos Familiares (EPF);
- sanidad con el perfil de uso de la Encuesta Nacional de Salud (ENSE);
- educación según matrícula;
- bienes públicos puros (servicios generales e intereses, defensa) a coste medio o a coste marginal cero.

Los ingresos no tributarios se reparten por persona, de modo que la suma cuadra con el saldo de las administraciones.

**Resultado estático (capa C2, gráfico 3).** Contribución neta por persona en 2024: escenario principal de referencia, intervalo de las 64 combinaciones de supuestos e intervalo de muestreo del principal (bootstrap por hogares, 200 réplicas):
- **nacidos en España:** {{F4_NETA_PC_España_2024}} €; supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}}]; muestreo [{{F4_NETA_PC_España_2024:inf}}, {{F4_NETA_PC_España_2024:sup}}];
- **resto de la UE:** {{F4_NETA_PC_Resto_UE_2024}} €; supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}}], positiva en las 64 combinaciones; muestreo [{{F4_NETA_PC_Resto_UE_2024:inf}}, {{F4_NETA_PC_Resto_UE_2024:sup}}];
- **resto del mundo:** {{F4_NETA_PC_Resto_del_mundo_2024}} € (solo referencia, D11); supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}]; muestreo [{{F4_NETA_PC_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_Resto_del_mundo_2024:sup}}]. El signo depende de los bienes públicos y de los hijos nacidos en España (output/f4/signo_por_supuestos.csv).

**Déficit y comparación con los nativos.** Las cifras anteriores reparten el déficit de 2024 entre todos, por lo que los nacidos en España salen negativos en todos los supuestos. Dos lecturas complementarias:
- **Presupuesto equilibrado** (criterio de la OCDE: el saldo se reparte por igual por persona y la suma es cero): nacidos en España {{F4_NETA_EQUILIBRADA_PC_España_2024}} € [{{F4_NETA_EQUILIBRADA_PC_España_2024:inf}}, {{F4_NETA_EQUILIBRADA_PC_España_2024:sup}}]; resto de la UE {{F4_NETA_EQUILIBRADA_PC_Resto_UE_2024}} € [{{F4_NETA_EQUILIBRADA_PC_Resto_UE_2024:inf}}, {{F4_NETA_EQUILIBRADA_PC_Resto_UE_2024:sup}}]; resto del mundo {{F4_NETA_EQUILIBRADA_PC_Resto_del_mundo_2024}} € [{{F4_NETA_EQUILIBRADA_PC_Resto_del_mundo_2024:inf}}, {{F4_NETA_EQUILIBRADA_PC_Resto_del_mundo_2024:sup}}].
- **Diferencia con los nacidos en España** en cada combinación de supuestos: resto de la UE {{F4_NETA_DIF_NAT_Resto_UE_2024}} € [{{F4_NETA_DIF_NAT_Resto_UE_2024:inf}}, {{F4_NETA_DIF_NAT_Resto_UE_2024:sup}}]; resto del mundo {{F4_NETA_DIF_NAT_Resto_del_mundo_2024}} € [{{F4_NETA_DIF_NAT_Resto_del_mundo_2024:inf}}, {{F4_NETA_DIF_NAT_Resto_del_mundo_2024:sup}}]. Para el resto del mundo el intervalo contiene el cero.
- **Conjunto de nacidos fuera** (la cantidad de las afirmaciones A5 y F3): {{F4_NETA_PC_FUERA_2024}} € [{{F4_NETA_PC_FUERA_2024:inf}}, {{F4_NETA_PC_FUERA_2024:sup}}]; frente a los nativos, {{F4_NETA_DIF_NAT_FUERA_2024}} € [{{F4_NETA_DIF_NAT_FUERA_2024:inf}}, {{F4_NETA_DIF_NAT_FUERA_2024:sup}}]. El signo lo deciden solo los bienes públicos y la asignación de los hijos: coste medio e hijos a los padres, [{{F4_NETA_FUERA_MEDIO_PADRES:inf}}, {{F4_NETA_FUERA_MEDIO_PADRES:sup}}]; coste medio e hijos al hijo, [{{F4_NETA_FUERA_MEDIO_HIJO:inf}}, {{F4_NETA_FUERA_MEDIO_HIJO:sup}}]; coste marginal e hijos a los padres, [{{F4_NETA_FUERA_MARGINAL_PADRES:inf}}, {{F4_NETA_FUERA_MARGINAL_PADRES:sup}}]; coste marginal e hijos al hijo, [{{F4_NETA_FUERA_MARGINAL_HIJO:inf}}, {{F4_NETA_FUERA_MARGINAL_HIJO:sup}}].

**A igual edad y sexo (C4).** Las cifras anteriores son brutas: la ventaja frente a los nativos procede en buena parte de la estructura por edad, porque las pensiones y la sanidad de los mayores pesan en los nativos. Con la estructura por edad y sexo de los nacidos en España, y comparando solo en las celdas de edad y sexo con al menos 50 observaciones del grupo (que cubren el {{F4_COBERTURA_EST_Resto_UE}} % del peso nativo para el resto de la UE y el {{F4_COBERTURA_EST_Resto_del_mundo}} % para el resto del mundo), la diferencia con los nativos es {{F4_NETA_EST_DIF_NAT_Resto_UE_2024}} € para el resto de la UE (negativa en las 64 combinaciones: [{{F4_NETA_EST_DIF_NAT_Resto_UE_2024:inf}}, {{F4_NETA_EST_DIF_NAT_Resto_UE_2024:sup}}]) y {{F4_NETA_EST_DIF_NAT_Resto_del_mundo_2024}} € para el resto del mundo ([{{F4_NETA_EST_DIF_NAT_Resto_del_mundo_2024:inf}}, {{F4_NETA_EST_DIF_NAT_Resto_del_mundo_2024:sup}}], positiva en {{F4_NETA_EST_DIF_NAT_POSITIVAS_Resto_del_mundo}} de 64). En el principal, el error de muestreo no cambia el signo (IC 95 % aproximado: resto de la UE [{{F4_NETA_EST_DIF_NAT_MUESTREO_Resto_UE:inf}}, {{F4_NETA_EST_DIF_NAT_MUESTREO_Resto_UE:sup}}]; resto del mundo [{{F4_NETA_EST_DIF_NAT_MUESTREO_Resto_del_mundo:inf}}, {{F4_NETA_EST_DIF_NAT_MUESTREO_Resto_del_mundo:sup}}]); entre supuestos, para el resto del mundo, sí. Coincide con Fiorio et al. (2023) en que la ventaja bruta desaparece a igual composición. Para el resto de la UE la comparación se limita a las edades centrales, porque los tramos de 0 a 24 y de 70 y más años tienen menos de 50 observaciones.

En prestaciones monetarias, los nacidos fuera de la UE reciben {{F6_PREST_MONETARIAS_PC_Resto_del_mundo}} € por persona y los nacidos en España {{F6_PREST_MONETARIAS_PC_España}} €, sobre todo por las pensiones. A igual edad y sexo, sobre las celdas comunes, siguen recibiendo menos: {{F4_PREST_MONET_EST_DIF_Resto_del_mundo_2024}} € (resto del mundo) y {{F4_PREST_MONET_EST_DIF_Resto_UE_2024}} € (resto de la UE).

**Ciclo vital (C2).** Valor actual en 2024 de la contribución neta de por vida según la edad de llegada. Supuestos del escenario principal:
- supervivencia de la tabla de mortalidad de España;
- salida (retorno o reemigración) con un riesgo que decrece con la duración de la residencia, calibrado a la tasa observada de {{F4_RETORNO_OBSERVADO}} % anual (emigraciones de nacidos fuera de 2021-2024 sobre el stock medio del mismo periodo). El riesgo es del {{F4_RIESGO_SALIDA_0_4}} % anual en los primeros cinco años. La tasa incluye bajas por caducidad del padrón que no siempre son salidas reales, así que es una cota superior de las salidas;
- quien sale conserva la pensión contributiva devengada (exportable), que exige 15 años cotizados;
- sin convergencia adicional: el perfil transversal por edad ya mezcla duraciones de residencia, y añadir convergencia la contaría dos veces;
- descuento del 3 % y bienes públicos a coste medio.

Resultados en miles de euros (principal y, entre corchetes, el intervalo de las 24 combinaciones de salida, descuento y bienes públicos sin convergencia adicional; las combinaciones con convergencia se informan aparte porque la contarían dos veces):
- llegada a los 20 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_20}} [{{F4_VA_Resto_UE_LLEGADA_20:inf}}, {{F4_VA_Resto_UE_LLEGADA_20:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_20}} [{{F4_VA_Resto_del_mundo_LLEGADA_20:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_20:sup}}];
- llegada a los 30 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_30}} [{{F4_VA_Resto_UE_LLEGADA_30:inf}}, {{F4_VA_Resto_UE_LLEGADA_30:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_30}} [{{F4_VA_Resto_del_mundo_LLEGADA_30:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_30:sup}}];
- llegada a los 40 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_40}} [{{F4_VA_Resto_UE_LLEGADA_40:inf}}, {{F4_VA_Resto_UE_LLEGADA_40:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_40}} [{{F4_VA_Resto_del_mundo_LLEGADA_40:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_40:sup}}];
- llegada a los 50 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_50}} [{{F4_VA_Resto_UE_LLEGADA_50:inf}}, {{F4_VA_Resto_UE_LLEGADA_50:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_50}} [{{F4_VA_Resto_del_mundo_LLEGADA_50:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_50:sup}}];
- comparador, nacido en España de 30 años (vida restante, sin salidas; intervalo: descuento y bienes públicos): {{F4_VA_España_EDAD_30}} [{{F4_VA_España_EDAD_30:inf}}, {{F4_VA_España_EDAD_30:sup}}]; recién nacido en España: {{F4_VA_España_EDAD_0}} [{{F4_VA_España_EDAD_0:inf}}, {{F4_VA_España_EDAD_0:sup}}].

**Signo (D11).** Para el resto del mundo, las llegadas a los 20 y a los 50 años son negativas en todas las combinaciones sin convergencia, y las de 30 y 40 años tienen intervalos que contienen el cero. Para el resto de la UE, todos los intervalos de llegada entre 20 y 50 años contienen el cero. Con convergencia, que el texto considera una doble contabilización, los intervalos se amplían hacia arriba (llegada a los 30, resto del mundo: hasta {{F4_VA_CONVERG_Resto_del_mundo_LLEGADA_30:sup}}). Los perfiles incluyen el déficit de 2024, que hace más negativos todos los valores, también los de los nativos. La diferencia con un nacido en España de la misma edad contiene el cero (llegada a los 30: resto del mundo {{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30}} [{{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30:inf}}, {{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30:sup}}]). Para la llegada a los 30, la parte hasta los 64 años («población joven hoy») es {{F4_VA_HASTA64_Resto_del_mundo_LLEGADA_30}} y la de 65 y más años {{F4_VA_65MAS_Resto_del_mundo_LLEGADA_30}} (resto del mundo).

**Qué supuesto empuja en qué dirección** (output/f4/ciclo_vital_signos.csv):
- Las salidas cuentan mucho. Sin salidas (toda la vida en España), la llegada a los 30 da {{F4_VA_SIN_SALIDA_Resto_del_mundo_LLEGADA_30}} (resto del mundo) y {{F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_30}} (resto de la UE). La razón es que quien sale deja de generar gasto en sanidad y servicios en la vejez, aunque se lleve la pensión devengada. El principal usa la tasa observada, que es una cota superior de las salidas porque incluye bajas por caducidad; si las salidas reales fueran la mitad, la llegada a los 30 daría {{F4_VA_MITAD_SALIDA_Resto_del_mundo_LLEGADA_30}} (resto del mundo) y {{F4_VA_MITAD_SALIDA_Resto_UE_LLEGADA_30}} (resto de la UE). Es decir, el principal está sesgado al alza en la dirección del sesgo de las caducidades.
- La convergencia, un descuento más alto y los bienes públicos a coste marginal cero mejoran el resultado.
- Los perfiles incluyen el déficit de 2024: todos los valores, también los de los nativos, salen más negativos que con presupuesto equilibrado.
- No se cuentan los descendientes ni su educación.

**Otras variantes del principal** (output/f4/ciclo_vital_sensibilidad.csv). Con presupuesto equilibrado, la llegada a los 30 da {{F4_VA_EQUILIBRADO_Resto_del_mundo_30}} (resto del mundo) y {{F4_VA_EQUILIBRADO_Resto_UE_30}} (resto de la UE), y un nacido en España de 30 años {{F4_VA_EQUILIBRADO_España_30}}. Rellenar los tramos de edad suprimidos con el perfil nativo sin escalar da {{F4_VA_IMPUT_UE_Resto_UE_30}} para el resto de la UE (los tramos de 0 a 24 y de 70 y más años de este grupo tienen menos de 50 observaciones). Quitar el mínimo de 15 años cotizados, una aproximación a la totalización europea de periodos, da {{F4_VA_SIN_MIN15_Resto_del_mundo_30}} (resto del mundo) y {{F4_VA_SIN_MIN15_Resto_UE_30}} (resto de la UE); quitar el suelo de pensión no contributiva, {{F4_VA_SIN_SUELO_Resto_del_mundo_30}} (resto del mundo). Para el resto de la UE la regla de los 15 años sí importa: con la mitad de salidas y sin el mínimo a la vez, la llegada a los 30 da {{F4_VA_CONJUNTA_Resto_UE_30}} (resto de la UE) y {{F4_VA_CONJUNTA_Resto_del_mundo_30}} (resto del mundo), de modo que el valor positivo del principal para el resto de la UE no es robusto. Dos sesgos de signo opuesto quedan sin cuantificar: el gasto sanitario se toma del perfil nativo, aunque la ENSE observa menos uso entre los nacidos fuera, lo que juega en contra; y el perfil por edad es el de quienes residen hoy. Sin convergencia, a quien llega a los 20 se le aplica a los 30-44 años un perfil que mezcla recién llegados (en contra), y a quien llega a los 40 o 50 un perfil de residentes antiguos (a favor). El IBI se imputa solo a los propietarios, sin traslado a los inquilinos.

**Sensibilidad.** En la contabilidad estática lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos. Imputar coste marginal cero a los nacidos fuera traslada su parte de los bienes públicos a los nacidos en España ({{F4_BIENES_MARGINAL_TRASLADO_España_2024}} € por persona). Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Fiorio et al. (2023, *International Tax and Public Finance*) estiman para España, en 2014-2018, una contribución neta por persona de los inmigrantes mayor que la de los nativos, sin diferencia significativa a igual composición demográfica. La cantidad comparable de este estudio es la diferencia con los nativos, con dos diferencias de diseño: el periodo (2024 frente a 2014-2018) y los bienes públicos. En bruto, para el resto de la UE la diferencia es positiva en las 64 combinaciones, en la dirección de Fiorio et al.; para el resto del mundo el intervalo contiene el cero. A igual edad y sexo, que es el nivel en que Fiorio et al. no hallan diferencia, la de M1 es negativa en las edades centrales para el resto de la UE y su intervalo contiene el cero para el resto del mundo. Fiorio et al. no incluyen los bienes públicos puros, lo que se aproxima a la variante a coste marginal cero de M1. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda; etiqueta prereg-m1 en el commit c247555, cuyo historial está en el repositorio remoto antes de cualquier estimación; pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia, con cuotas de 1998 de los nacidos fuera con nacionalidad extranjera y shocks nacionales por país de nacimiento;
- 50 provincias y tres periodos apilados (2005-2009, 2009-2015, 2015-2022), con controles de periodo, suma de cuotas, paro inicial, construcción y Bartik sectorial;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler; pretendencia con la afiliación de 1999-2001; permutaciones; exclusión de los orígenes con mayor peso de Rotemberg; sensibilidad por nacionalidad; multiverso de 38 especificaciones por hipótesis confirmatoria.

**Corrección de un error que cambió los signos.** En la revisión de este documento se detectó que el control de cuotas incompletas del shift-share (la suma de las exposiciones del instrumento, por periodo) estaba mal construido en el código: no se dividía por la población inicial, como sí se hace en el instrumento. Con el control corregido, tal como lo describe el pre-registro, la primera etapa pasa a ser fuerte al nivel del shock y cambian los signos de las dos confirmatorias. Las cifras que siguen son las corregidas y la corrección se documenta en docs/desviaciones.md (13). La corrección se hizo después de ver resultados y el texto del pre-registro admite dos lecturas: la adenda A1, que prevalece, define la exposición como cuota de la provincia / población inicial con shocks en niveles (variante «bhj», la principal); el texto original habla de «cuota de nacidos fuera en 1998», que corresponde a escribir los shocks como tasas de crecimiento («cuota_1998», con la población de 2002, primer año de la ECP). Se publican las tres con el mismo rango:

| Control de cuotas incompletas | F al nivel del shock | P1-H1 (empleo) | P1-H2 (paro) | P1-E3a (empleo, educación baja) |
|---|---|---|---|---|
| bhj (principal, adenda A1) | {{F5_P1_F_SHOCK}} | {{F5_P1_H1_beta}} | {{F5_P1_H2_beta}} | {{F5_P1_E3a_beta}} |
| original (con el error) | {{F5_P1_F_CTRL_ORIGINAL}} | {{F5_P1_H1_CTRL_ORIGINAL}} | {{F5_P1_H2_CTRL_ORIGINAL}} | {{F5_P1_E3a_CTRL_ORIGINAL}} |
| cuota_1998 (lectura literal) | {{F5_P1_F_CTRL_CUOTA_1998}} | {{F5_P1_H1_CTRL_CUOTA_1998}} | {{F5_P1_H2_CTRL_CUOTA_1998}} | {{F5_P1_E3a_CTRL_CUOTA_1998}} |

De las tres, la principal es la menos desfavorable para el empleo y el paro de los nativos y la menos negativa en P1-E3a; el signo positivo de P1-H1 solo aparece con ella. Ninguna de las tres rechaza el cero en las confirmatorias.

**Primera etapa.** F al nivel del shock = {{F5_P1_F_SHOCK}} y F efectivo agrupado por provincia = {{F5_P1_F_EFECTIVO}}, los dos por encima del umbral pre-registrado de 10. Aun así, los conjuntos AKM0 no están acotados: en ocho de las diez hipótesis de P1 y P2 son la recta real entera; en P1-E1 excluyen un tramo positivo que no contiene el cero; en P1-E3a el conjunto es (−∞, {{F5_P1_E3a_beta:sup}}]. Con estos datos, ninguna hipótesis cumple la condición de IDENTIFICADO (conjunto acotado y convexo).

**Resultados (estimación puntual de MC2E; clasificación según las reglas pre-registradas):**

| Pregunta | Resultado de los nacidos en España | Estimación | p (Holm o BH) | Clasificación |
|---|---|---|---|---|
| P1-H1 | tasa de empleo (pp por pp) | {{F5_P1_H1_beta}} | {{F5_P1_H1_p}} | ASOCIACIÓN |
| P1-H2 | tasa de paro (pp por pp) | {{F5_P1_H2_beta}} | {{F5_P1_H2_p}} | ASOCIACIÓN |
| P1-E1 | tasa de actividad (pp por pp) | {{F5_P1_E1_beta}} | {{F5_P1_E1_p}} | ASOCIACIÓN |
| P1-E2 | log de ocupados (log por pp) | {{F5_P1_E2_beta}} | {{F5_P1_E2_p}} | ASOCIACIÓN |
| P1-E3a | tasa de empleo, educación baja (pp por pp) | {{F5_P1_E3a_beta}} | {{F5_P1_E3a_p}} | ASOCIACIÓN |
| P1-E3b | tasa de empleo, educación media (pp por pp) | {{F5_P1_E3b_beta}} | {{F5_P1_E3b_p}} | ASOCIACIÓN |
| P1-E3c | tasa de empleo, educación alta (pp por pp) | {{F5_P1_E3c_beta}} | {{F5_P1_E3c_p}} | ASOCIACIÓN |
| P1-E4 | log salario por hora de los españoles, celdas educación × edad (Borjas) | {{F5_P1_E4_beta}} [{{F5_P1_E4_beta:inf}}, {{F5_P1_E4_beta:sup}}] | wild bootstrap | ASOCIACIÓN (techo) |
| P1-E5 | salarios provinciales | — | — | NO ESTIMABLE (AEAT no accesible) |
| P1-E6 | log de la población nacida en España de 15-64 (log por pp) | {{F5_P1_E6_beta}} | {{F5_P1_E6_p}} | ASOCIACIÓN |
| P2-E1 | cuota en ocupaciones no manuales | {{F5_P2_E1_beta}} | {{F5_P2_E1_p}} | ASOCIACIÓN |
| P2-E2 | cuota en ocupaciones de alta cualificación | {{F5_P2_E2_beta}} | {{F5_P2_E2_p}} | ASOCIACIÓN |
| P3 | alumnos por profesor en la enseñanza pública (por pp, 17 CCAA) | {{F5_P3_EDUC_beta}} [{{F5_P3_EDUC_beta:inf}}, {{F5_P3_EDUC_beta:sup}}] | wild bootstrap | ASOCIACIÓN (techo) |
| P3 | listas de espera quirúrgicas | — | — | NO ESTIMABLE (solo PDF) |
| P4 | vivienda | — | — | no se duplica (Econometr-a) |
| P5 | tasa de empleo 20-64 de los nativos, NUTS2 de la UE-27 (pp por pp) | {{F5_P5_beta}} [{{F5_P5_beta:inf}}, {{F5_P5_beta:sup}}] | wild bootstrap | ASOCIACIÓN |

Los intervalos de P1-E4, P3 y P5 son orientativos (errores agrupados con pocos grupos); su inferencia es el wild bootstrap, que no rechaza el cero en ninguno. P1-E4 (15 celdas) y la heterogeneidad de P5 (5 o 6 países por grupo) quedan fuera de lo validado por Monte Carlo para el wild bootstrap, y sus p son poco informativos.

**Todas las señales, con el mismo formato para lo favorable y lo desfavorable** (p de permutación recentrado; wild bootstrap de la forma reducida por comunidad; variante por nacionalidad con la envolvente de su conjunto AKM0; especificaciones del multiverso, de 32, con β negativo y que rechazan el cero sin ajustar):

| Hipótesis | β | permutación | wild bootstrap | nacionalidad | multiverso β < 0 | rechazan |
|---|---|---|---|---|---|---|
| P1-H1 empleo | {{F5_P1_H1_beta}} | {{F5_P1_H1_PERMR_p}} | {{F5_P1_H1_WCBT_p}} | {{F5_P1_H1_NACT}} [{{F5_P1_H1_NACT:inf}}, {{F5_P1_H1_NACT:sup}}] | {{F5_P1_H1_MNEG}} | {{F5_P1_H1_MREJ}} |
| P1-H2 paro | {{F5_P1_H2_beta}} | {{F5_P1_H2_PERMR_p}} | {{F5_P1_H2_WCBT_p}} | {{F5_P1_H2_NACT}} [{{F5_P1_H2_NACT:inf}}, {{F5_P1_H2_NACT:sup}}] | {{F5_P1_H2_MNEG}} | {{F5_P1_H2_MREJ}} |
| P1-E1 actividad | {{F5_P1_E1_beta}} | {{F5_P1_E1_PERMR_p}} | {{F5_P1_E1_WCBT_p}} | {{F5_P1_E1_NACT}} [{{F5_P1_E1_NACT:inf}}, {{F5_P1_E1_NACT:sup}}] | {{F5_P1_E1_MNEG}} | {{F5_P1_E1_MREJ}} |
| P1-E2 log ocupados | {{F5_P1_E2_beta}} | {{F5_P1_E2_PERMR_p}} | {{F5_P1_E2_WCBT_p}} | {{F5_P1_E2_NACT}} [{{F5_P1_E2_NACT:inf}}, {{F5_P1_E2_NACT:sup}}] | {{F5_P1_E2_MNEG}} | {{F5_P1_E2_MREJ}} |
| P1-E3a empleo, educación baja | {{F5_P1_E3a_beta}} | {{F5_P1_E3a_PERMR_p}} | {{F5_P1_E3a_WCBT_p}} | {{F5_P1_E3a_NACT}} [{{F5_P1_E3a_NACT:inf}}, {{F5_P1_E3a_NACT:sup}}] | {{F5_P1_E3a_MNEG}} | {{F5_P1_E3a_MREJ}} |
| P1-E3b empleo, educación media | {{F5_P1_E3b_beta}} | {{F5_P1_E3b_PERMR_p}} | {{F5_P1_E3b_WCBT_p}} | {{F5_P1_E3b_NACT}} [{{F5_P1_E3b_NACT:inf}}, {{F5_P1_E3b_NACT:sup}}] | {{F5_P1_E3b_MNEG}} | {{F5_P1_E3b_MREJ}} |
| P1-E3c empleo, educación alta | {{F5_P1_E3c_beta}} | {{F5_P1_E3c_PERMR_p}} | {{F5_P1_E3c_WCBT_p}} | {{F5_P1_E3c_NACT}} [{{F5_P1_E3c_NACT:inf}}, {{F5_P1_E3c_NACT:sup}}] | {{F5_P1_E3c_MNEG}} | {{F5_P1_E3c_MREJ}} |
| P1-E6 población nativa | {{F5_P1_E6_beta}} | {{F5_P1_E6_PERMR_p}} | {{F5_P1_E6_WCBT_p}} | {{F5_P1_E6_NACT}} [{{F5_P1_E6_NACT:inf}}, {{F5_P1_E6_NACT:sup}}] | {{F5_P1_E6_MNEG}} | {{F5_P1_E6_MREJ}} |
| P2-E1 no manuales | {{F5_P2_E1_beta}} | {{F5_P2_E1_PERMR_p}} | {{F5_P2_E1_WCBT_p}} | {{F5_P2_E1_NACT}} [{{F5_P2_E1_NACT:inf}}, {{F5_P2_E1_NACT:sup}}] | {{F5_P2_E1_MNEG}} | {{F5_P2_E1_MREJ}} |
| P2-E2 alta cualificación | {{F5_P2_E2_beta}} | {{F5_P2_E2_PERMR_p}} | {{F5_P2_E2_WCBT_p}} | {{F5_P2_E2_NACT}} [{{F5_P2_E2_NACT:inf}}, {{F5_P2_E2_NACT:sup}}] | {{F5_P2_E2_MNEG}} | {{F5_P2_E2_MREJ}} |

Tres hipótesis tienen un t fuera del 95 % central de las permutaciones: P1-E3a (desfavorable), P1-H2 (menos paro, favorable) y P1-E3c (más empleo de los nativos con educación alta, favorable). Ninguna supera la corrección por multiplicidad ni el wild bootstrap. El wild bootstrap con 17 comunidades tiene una condición en el Monte Carlo: una comunidad concentra el {{F5_P1_APALANC_MAX}} % de la variación del instrumento, lo que con grupos asimétricos lo hace sobre-rechazar; sus p no favorecen el rechazo, pero tampoco son plenamente fiables. Los pesos de Rotemberg más altos son Rumanía en el periodo A ({{F5_P1_ROT_1}}), Venezuela en C ({{F5_P1_ROT_2}}), Marruecos en A ({{F5_P1_ROT_3}}) y en C ({{F5_P1_ROT_4}}) y el Reino Unido en A ({{F5_P1_ROT_5}}, negativo); el peso negativo es el {{F5_P1_ROT_NEG}} % del peso absoluto de los 15 mayores.

**Lectura.** Ninguna hipótesis rechaza el cero con la corrección por multiplicidad pre-registrada. Las dos confirmatorias tienen signos opuestos a los de la versión con el error y no son significativas: la tasa de empleo, {{F5_P1_H1_beta}} (p de Holm = {{F5_P1_H1_p}}), y la tasa de paro, {{F5_P1_H2_beta}} (p de Holm = {{F5_P1_H2_p}}). El wild bootstrap de la forma reducida por comunidad autónoma, pre-registrado como control de dependencia espacial, tampoco rechaza (p = {{F5_P1_H1_WCB_p}} y {{F5_P1_H2_WCB_p}}). En la variante por nacionalidad, cuyos conjuntos sí están acotados (F al nivel del shock = {{F5_P1_F_NACIONALIDAD}}), la tasa de empleo da {{F5_P1_H1_NACIONALIDAD}} [{{F5_P1_H1_NACIONALIDAD:inf}}, {{F5_P1_H1_NACIONALIDAD:sup}}] y la de paro {{F5_P1_H2_NACIONALIDAD}} [{{F5_P1_H2_NACIONALIDAD:inf}}, {{F5_P1_H2_NACIONALIDAD:sup}}]: no se detecta efecto, y esa variante es compatible con efectos de entre {{F5_P1_H1_NACIONALIDAD:inf}} y {{F5_P1_H1_NACIONALIDAD:sup}} puntos por punto en el empleo y de entre {{F5_P1_H2_NACIONALIDAD:inf}} y {{F5_P1_H2_NACIONALIDAD:sup}} en el paro. Esa variante usa como tratamiento la población de nacionalidad extranjera de todas las edades (padrón), por lo que su escala no es exactamente la de la principal.

**P1-E3a: un indicio desfavorable, no un resultado.** La tasa de empleo de los nacidos en España con educación baja da {{F5_P1_E3a_beta}} puntos por punto. Con el p sin ajustar de AKM0 rechazaría el cero al 5 %, pero no tras la corrección BH pre-registrada entre las seis exploratorias de P1 (p = {{F5_P1_E3a_p}}), ni con el wild bootstrap por comunidad (p = {{F5_P1_E3a_WCB_p}}). Señales que apuntan en la misma dirección, todas sin valor confirmatorio:
- el t de la especificación principal ({{F5_P1_E3a_T}}) cae fuera del 95 % central de las 500 permutaciones de los shocks ([{{F5_P1_E3a_PERM_MED:inf}}, {{F5_P1_E3a_PERM_MED:sup}}]; p recentrado = {{F5_P1_E3a_PERM_p}});
- en la variante por nacionalidad el conjunto está acotado y es negativo: {{F5_P1_E3a_NACIONALIDAD}} [{{F5_P1_E3a_NACIONALIDAD:inf}}, {{F5_P1_E3a_NACIONALIDAD:sup}}];
- las {{F5_P1_E3a_MULT_NEG}} especificaciones del multiverso tienen β negativo (mediana {{F5_P1_E3a_MULT_MED}}); {{F5_P1_E3a_MULT_RECHAZA}} rechazan el cero sin ajustar, pero comparten datos y cuotas, así que no son pruebas independientes;
- excluyendo cada comunidad autónoma por turno (exploratorio, a posteriori), β va de {{F5X_JK_P1_E3a:inf}} a {{F5X_JK_P1_E3a:sup}};
- con la representación del instrumento en tasas de crecimiento (exploratoria, a posteriori; F al nivel del shock = {{F5X_CREC_F}}), el conjunto AKM0 está acotado y es negativo: {{F5X_CREC_E3a}} [{{F5X_CREC_E3a:inf}}, {{F5X_CREC_E3a:sup}}]. En esa representación P1-H1 da {{F5X_CREC_H1}} y P1-H2 {{F5X_CREC_H2}}, sin rechazar el cero. La representación pre-registrada es la de niveles, y esta variante no puede cambiar ninguna clasificación.
En sentido contrario, cuatro hechos lo debilitan: (i) una parte es composición por edad dentro del grupo: la proporción de jóvenes de 16-24 años entre los nativos con estudios bajos sube con el instrumento ({{F5X_E3a_CUOTA1624}}, p sin ajustar = {{F5X_E3a_CUOTA1624_p}}), y con la tasa estandarizada por edad la estimación baja a {{F5X_E3a_ESTEDAD}} (p = {{F5X_E3a_ESTEDAD_p}}); con 25-64 años es {{F5X_E3a_2564}} (p = {{F5X_E3a_2564_p}}) y sin la segunda generación identificable, {{F5X_E3a_SINSG}}; (ii) depende mucho de una comunidad: sin la Comunitat Valenciana es {{F5X_JK_E3a_MAX}}, donde coinciden el ciclo de la construcción y las cuotas de rumanos y británicos; (iii) la exclusión de los tres orígenes de mayor peso de Rotemberg no es informativa (deja el F al nivel del shock en {{F5_P1_F_SIN_TOP3}}); (iv) el conjunto AKM0 de la principal no tiene cota inferior y la pretendencia se contrasta con la afiliación total, no con la tasa de empleo de este grupo. Por la regla pre-registrada queda en ASOCIACIÓN. Se trata con el mismo tono que los indicios favorables: es compatible con un efecto negativo moderado sobre los trabajadores nativos con estudios bajos, en parte explicado por composición por edad y concentrado en una comunidad, y no permite afirmarlo.

**Lectura de P1-E3a (exploratorio, a posteriori; no cambia ninguna clasificación, docs/desviaciones.md, 12).**
- *Magnitud frente a la literatura.* Expresada como elasticidad de la tasa de empleo respecto a la cuota de nacidos fuera, con las medias de los años iniciales, equivale a {{F5X_E3a_ELAST}}. Carrasco, Jimeno y Ortega (2008) estiman en torno a −0,17 para el conjunto de los nativos con solo inmigrantes legales (no significativa con todos), y González y Ortega (2011) no hallan efecto sobre los trabajadores poco cualificados (fichas en docs/literatura/trabajo.md). Gálvez-Iniesta (2025; NO VERIFICADA, sin DOI) estima por celdas un coeficiente log-log sobre el nivel de empleo, entre +0,19 y −0,03 según el periodo, en una escala que no es directamente comparable con la de M1. Dustmann, Schönberg y Stuhler (2016) advierten de que los efectos relativos por celdas no son comparables con los efectos totales por región. P1-E3a es, pues, del mismo orden que la elasticidad de Carrasco, Jimeno y Ortega (2008) y más negativo que lo que encuentran González y Ortega (2011).
- *MCO.* Por MCO, con la misma especificación, la asociación es {{F5X_E3a_MCO}}. Con una primera etapa débil o moderada el MC2E tiende a sesgarse hacia el MCO; que el MC2E sea más negativo que el MCO indica que su magnitud no se explica por ese sesgo, aunque un MCO negativo es compatible con él.
- *Empleo o población.* El número de ocupados nativos con educación baja cae ({{F5X_E3a_OCU}} en log por punto, p sin ajustar = {{F5X_E3a_OCU_p}}) y también su población ({{F5X_E3a_POB}}, p = {{F5X_E3a_POB_p}}), mientras crece la población nativa con educación media o alta ({{F5X_E3a_POB_MA}}). Una población menor sube la tasa, no la baja: la caída de la tasa es la diferencia entre las dos. Algo más de la mitad de la caída del número de ocupados se corresponde con una población del grupo más pequeña (salida geográfica, mejora educativa de los jóvenes o envejecimiento, que las encuestas transversales no distinguen), y la caída de la tasa queda íntegra después de descontarla. Ninguna de las tres estimaciones tiene un conjunto acotado, así que la descomposición es solo descriptiva.
- *Agregación.* La educación baja pesa el {{F5X_PESO_BAJA}} % de los nativos de 16-64. En la variante por nacionalidad, la media ponderada de las estimaciones por nivel educativo (educación media {{F5X_E3b_NAC}}, alta {{F5X_E3c_NAC}}) es {{F5X_NAC_IMPLICITO}}, dentro del conjunto de la tasa total. La tasa total también cambia por la composición educativa (los pesos varían entre periodos), término que esta aritmética omite.

**Multiverso y otras pruebas.** En el multiverso pre-registrado (32 especificaciones por hipótesis, más 6 variantes de sensibilidad), P1-H1 tiene {{F5_P1_H1_MULT_NEG}} especificaciones con β negativo y mediana {{F5_P1_H1_MULT_MED}}; P1-H2, {{F5_P1_H2_MULT_NEG}} con β negativo y mediana {{F5_P1_H2_MULT_MED}}. Los valores extremos proceden de diferencias largas con primera etapa nula; en las especificaciones con F al nivel del shock ≥ 10 ({{F5_P1_H1_MULT_FUERTE_N}}), las medianas son {{F5_P1_H1_MULT_FUERTE_MED}} (empleo) y {{F5_P1_H2_MULT_FUERTE_MED}} (paro). Con el control corregido, las permutaciones de los shocks se centran cerca de cero (mediana del t de P1-H1 = {{F5_P1_H1_PERM_MED}}). La pretendencia (afiliación 1999-2001) no es significativa (p = {{F5_P1_PRETEND_p}}), pero el instrumento del periodo previo está casi colineal con el del primer periodo (correlación {{F5_P1_PRETEND_CORR}}), lo que resta poder a esa prueba. En P5 ningún grupo institucional de países tiene un p del wild bootstrap por debajo de 0,3, y el anglosajón (un solo país) no es estimable. Con la potencia de este diseño, no detectar un efecto no equivale a ausencia de efecto. El detalle está en output/f5 (resultado.json por pregunta, con los conjuntos AKM0 como unión de intervalos, los pesos de Rotemberg, el multiverso y el jackknife).

**Revisión.** El replicador ciego y el abogado del diablo solo actúan, según el pre-registro, sobre lo que quede IDENTIFICADO o SUGESTIVO; no hay nada en esas categorías. Las desviaciones de implementación respecto al texto pre-registrado se documentan en docs/desviaciones.md; ninguna cambia la clasificación.

**Literatura verificada sobre España** (no es un resultado de M1): González y Ortega (2011) y el Banco de España (2026, Informe Anual 2025) no encuentran en general efectos negativos significativos sobre el empleo de los nativos; Carrasco, Jimeno y Ortega (2008) obtienen un efecto negativo cuando solo cuentan a los inmigrantes con permiso de trabajo.

## 6. Pensiones y demografía

Las pensiones de vejez y supervivencia suponen el {{F4_PEN_GASTO_PIB_2024}} % del PIB en 2024. Tasa de dependencia de mayores de EUROPOP2023 en 2050, por cada 100 personas de 20 a 64 años (gráfico 4):
- variante base: {{F4_PEN_DEPENDENCIA_BSL_2050}};
- sin migración: {{F4_PEN_DEPENDENCIA_NMIGR_2050}};
- con un tercio más de migración: {{F4_PEN_DEPENDENCIA_HMIGR_2050}}.

Con una regla mecánica que mantiene constantes el empleo, la cobertura y la pensión relativa, el gasto de 2050 sería del {{F4_PEN_GASTO_MECANICO_BSL_2050}} % del PIB en la base y del {{F4_PEN_GASTO_MECANICO_NMIGR_2050}} % sin migración. El Ageing Report 2024, que modeliza empleo y reformas, da {{F4_PEN_AR2024_BASE_2050}} %, {{F4_PEN_AR2024_MAS_MIGRACION_2050}} % con más migración y {{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % con menos.

La regla mecánica es una comparación de escenarios, no un efecto estimado: sobrestima el nivel del gasto, pero el orden de los escenarios coincide con el del Ageing Report (más migración, menos gasto en proporción del PIB). Las cotizaciones de hoy generan derechos futuros (sección 4). La cifra del Ageing Report se toma del informe publicado y figura como NO VERIFICADA (sin DOI).

![Gráfico 4](figuras/fig4_dependencia.png)

## 7. Afirmaciones del debate y su veredicto

Las fichas completas están en [afirmaciones.md](afirmaciones.md). Resumen:

{{TABLA_AFIRMACIONES}}

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
- La ECV pondera unos {{F4_ECV_DEFICIT_ECP_FUERA}} millones de nacidos fuera menos que la ECP de 2025 (recién llegados, situación irregular, hogares colectivos); la clasificación «resto de la UE» de la ECV sigue la del INE en cada ola.
- La regla mecánica de pensiones supone que el empleo, la cobertura y la pensión relativa de cada cohorte no cambian, es decir, que los nuevos residentes tienen el empleo medio; con la brecha de empleo a igual edad, la diferencia de {{F4_PEN_DIF_SIN_MIGRACION_2050}} puntos estaría sobrestimada.
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
