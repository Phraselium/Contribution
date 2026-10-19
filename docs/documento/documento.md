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

Las cifras incluyen el déficit de las administraciones, que se reparte entre todos; con presupuesto equilibrado (criterio de la OCDE) y frente a los nacidos en España las cifras cambian (sección 4). En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España: el principal es solo una referencia y lo que se afirma es el intervalo (decisión del autor, D11; tablas de signo en output/f4/signo_por_supuestos.csv y output/f4/ciclo_vital_signos.csv). En el ciclo vital (valor actual de por vida), los intervalos contienen el cero para los dos grupos de nacidos fuera y para todas las edades de llegada entre 20 y 50 años. Para la llegada a los 0 años son negativos en todos los supuestos, como el de un recién nacido en España, porque los perfiles incluyen el déficit de 2024 y no se cuentan los descendientes.

**Pensiones.** Con una regla demográfica mecánica, el gasto en pensiones de 2050 de la variante de EUROPOP2023 sin migración es {{F4_PEN_EFECTO_SIN_MIGRACION_2050}} puntos de PIB mayor que el de la variante base. Es una comparación de escenarios con supuestos, no una proyección del sistema ni un efecto estimado. En el Ageing Report 2024, que modeliza empleo y reformas, la diferencia entre un tercio menos y un tercio más de migración es de 2,6 puntos ({{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % frente a {{F4_PEN_AR2024_MAS_MIGRACION_2050}} %; referencia NO VERIFICADA, sin DOI).

**Impacto sobre la población local.** La estimación causal está pre-registrada, revisada y programada, pero **no se ha ejecutado**: la puerta del pre-registro interno exige que la etiqueta esté en un repositorio remoto, y en esta versión no lo está. Todas las preguntas causales quedan pendientes y se cita solo la literatura verificada.

**Afirmaciones del debate.** {{TEXTO_BALANCE}} (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. En conjunto trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales, y con grandes diferencias entre grupos. Cobran menos por hora; unos dos tercios de esa diferencia se corresponden con diferencias de edad, sexo, estudios y región, y el resto no se explica con esas variables. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas de un año (2024), los nacidos en otros países de la UE aportan más de lo que reciben en todas las combinaciones de supuestos estudiadas. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos. Cuando se mira toda la vida (impuestos de hoy y pensiones de mañana), el resultado depende de supuestos para todos los grupos.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. El estudio la deja preparada, pero sin resultados propios todavía.

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

**Segunda fuente.** Con la ECV, la mediana de los rendimientos del trabajo de los asalariados a jornada completa es un {{F3_SAL_ECV_BRECHA_Resto_del_mundo_2024}} % menor para los nacidos fuera de la UE.

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

Personas que perciben cada prestación o viven en un hogar que la percibe (ECV, media 2021-2025):

| Prestación | España | Resto UE | Resto del mundo |
|---|---|---|---|
| Desempleo (16-64) | {{F3_PRE_desempleo_España}} % | {{F3_PRE_desempleo_Resto_UE}} % | {{F3_PRE_desempleo_Resto_del_mundo}} % |
| Jubilación (65+) | {{F3_PRE_jubilacion_España}} % | {{F3_PRE_jubilacion_Resto_UE}} % | {{F3_PRE_jubilacion_Resto_del_mundo}} % |
| Rentas mínimas e IMV | {{F3_PRE_rentas_minimas_IMV_España}} % | {{F3_PRE_rentas_minimas_IMV_Resto_UE}} % | {{F3_PRE_rentas_minimas_IMV_Resto_del_mundo}} % |
| Ayudas a la vivienda | {{F3_PRE_ayuda_vivienda_España}} % | {{F3_PRE_ayuda_vivienda_Resto_UE}} % | {{F3_PRE_ayuda_vivienda_Resto_del_mundo}} % |

A igual edad, sexo, educación y región (C4), la diferencia en rentas mínimas de los nacidos fuera de la UE es de {{F3_PRE_BRECHA_perceptor_rentas_minimas_IMV_Resto_del_mundo_completo}} pp, y en jubilación de {{F3_PRE_BRECHA_perceptor_jubilacion_Resto_del_mundo_completo}} pp. Rentas mínimas, IMV y ayudas a la vivienda son el {{F6_PREST_NO_CONTRIB_CUOTA}} % de las prestaciones monetarias. Errores agrupados por hogar y año (la ECV pública no trae estratos ni conglomerados). Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad y se usan como contraste (docs/fuentes/admin.md).

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

En prestaciones monetarias, los nacidos fuera de la UE reciben {{F6_PREST_MONETARIAS_PC_Resto_del_mundo}} € por persona y los nacidos en España {{F6_PREST_MONETARIAS_PC_España}} €, sobre todo por las pensiones.

**Ciclo vital (C2).** Valor actual en 2024 de la contribución neta de por vida según la edad de llegada. Supuestos del escenario principal:
- supervivencia de la tabla de mortalidad de España;
- salida (retorno o reemigración) con un riesgo que decrece con la duración de la residencia, calibrado a la tasa observada de {{F4_RETORNO_OBSERVADO}} % anual (emigraciones de nacidos fuera de 2021-2024 sobre el stock medio del mismo periodo). El riesgo es del {{F4_RIESGO_SALIDA_0_4}} % anual en los primeros cinco años. La tasa incluye bajas por caducidad del padrón que no siempre son salidas reales, así que es una cota superior de las salidas;
- quien sale conserva la pensión contributiva devengada (exportable), que exige 15 años cotizados;
- sin convergencia adicional: el perfil transversal por edad ya mezcla duraciones de residencia, y añadir convergencia la contaría dos veces;
- descuento del 3 % y bienes públicos a coste medio.

Resultados en miles de euros (principal y, entre corchetes, el intervalo de las 72 combinaciones de salida, convergencia, descuento y bienes públicos):
- llegada a los 20 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_20}} [{{F4_VA_Resto_UE_LLEGADA_20:inf}}, {{F4_VA_Resto_UE_LLEGADA_20:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_20}} [{{F4_VA_Resto_del_mundo_LLEGADA_20:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_20:sup}}];
- llegada a los 30 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_30}} [{{F4_VA_Resto_UE_LLEGADA_30:inf}}, {{F4_VA_Resto_UE_LLEGADA_30:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_30}} [{{F4_VA_Resto_del_mundo_LLEGADA_30:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_30:sup}}];
- llegada a los 40 años: resto de la UE {{F4_VA_Resto_UE_LLEGADA_40}} [{{F4_VA_Resto_UE_LLEGADA_40:inf}}, {{F4_VA_Resto_UE_LLEGADA_40:sup}}]; resto del mundo {{F4_VA_Resto_del_mundo_LLEGADA_40}} [{{F4_VA_Resto_del_mundo_LLEGADA_40:inf}}, {{F4_VA_Resto_del_mundo_LLEGADA_40:sup}}];
- comparador, nacido en España de 30 años (vida restante): {{F4_VA_España_EDAD_30}} [{{F4_VA_España_EDAD_30:inf}}, {{F4_VA_España_EDAD_30:sup}}]; recién nacido en España: {{F4_VA_España_EDAD_0}} [{{F4_VA_España_EDAD_0:inf}}, {{F4_VA_España_EDAD_0:sup}}].

Todos los intervalos de llegada entre 20 y 50 años contienen el cero, y por D11 no se les asigna signo. La diferencia con un nacido en España de la misma edad también contiene el cero (llegada a los 30: resto del mundo {{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30}} [{{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30:inf}}, {{F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30:sup}}]). Para la llegada a los 30, la parte hasta los 64 años («población joven hoy») es {{F4_VA_HASTA64_Resto_del_mundo_LLEGADA_30}} y la de 65 y más años {{F4_VA_65MAS_Resto_del_mundo_LLEGADA_30}} (resto del mundo).

**Qué supuesto empuja en qué dirección** (output/f4/ciclo_vital_signos.csv):
- Las salidas cuentan mucho. Sin salidas (toda la vida en España), la llegada a los 30 da {{F4_VA_SIN_SALIDA_Resto_del_mundo_LLEGADA_30}} (resto del mundo) y {{F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_30}} (resto de la UE). La razón es que quien sale deja de generar gasto en sanidad y servicios en la vejez, aunque se lleve la pensión devengada. Si las bajas por caducidad sobrestiman las salidas, el principal está sesgado al alza.
- La convergencia, un descuento más alto y los bienes públicos a coste marginal cero mejoran el resultado.
- Los perfiles incluyen el déficit de 2024: todos los valores, también los de los nativos, salen más negativos que con presupuesto equilibrado.
- No se cuentan los descendientes ni su educación.

**Sensibilidad.** En la contabilidad estática lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos. Imputar coste marginal cero a los nacidos fuera traslada su parte de los bienes públicos a los nacidos en España ({{F4_BIENES_MARGINAL_TRASLADO_España_2024}} € por persona). Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Fiorio et al. (2023, *International Tax and Public Finance*) estiman para España, en 2014-2018, una contribución neta por persona de los inmigrantes mayor que la de los nativos, sin diferencia significativa a igual composición demográfica. La cantidad comparable de este estudio es la diferencia con los nativos. En el escenario principal es positiva para los dos grupos: la dirección coincide. Para los nacidos fuera de la UE, sin embargo, el intervalo de supuestos contiene el cero. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda, etiqueta local prereg-m1, pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia con cuotas de 1998;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler;
- pretendencia con la afiliación de 1999-2001, permutaciones, exclusión de los orígenes con mayor peso de Rotemberg y sensibilidad por nacionalidad.

**Estado: no ejecutado.** La puerta exige que el commit de la etiqueta esté en la rama de un repositorio remoto. Esta sesión no tuvo remoto y no pudo crearlo, así que la fase 5 queda pendiente y ninguna pregunta B tiene clasificación propia. En la literatura verificada sobre España (González y Ortega 2011; Banco de España 2026, Informe Anual 2025) no se encuentran en general efectos negativos significativos sobre el empleo de los nativos; Carrasco, Jimeno y Ortega (2008) obtienen un efecto negativo cuando solo cuentan a los inmigrantes con permiso de trabajo. Es literatura, no un resultado de M1.

**Situación de cada pregunta:**
- P3 (servicios públicos): NO ESTIMABLE con datos públicos procesables. Las listas de espera solo se publican en PDF por comunidad; el techo pre-registrado era ASOCIACIÓN.
- P4 (vivienda): no se duplica; se remite a Econometr-a.
- P5 (Europa): pendiente, con techo SUGESTIVO.

## 6. Pensiones y demografía

Las pensiones de vejez y supervivencia suponen el {{F4_PEN_GASTO_PIB_2024}} % del PIB en 2024. Tasa de dependencia de mayores de EUROPOP2023 en 2050, por cada 100 personas de 20 a 64 años (gráfico 4):
- variante base: {{F4_PEN_DEPENDENCIA_BSL_2050}};
- sin migración: {{F4_PEN_DEPENDENCIA_NMIGR_2050}};
- con un tercio más de migración: {{F4_PEN_DEPENDENCIA_HMIGR_2050}}.

Con una regla mecánica que mantiene constantes el empleo, la cobertura y la pensión relativa, el gasto de 2050 sería del {{F4_PEN_GASTO_MECANICO_BSL_2050}} % del PIB en la base y del {{F4_PEN_GASTO_MECANICO_NMIGR_2050}} % sin migración. El Ageing Report 2024, que modeliza empleo y reformas, da {{F4_PEN_AR2024_BASE_2050}} %, {{F4_PEN_AR2024_MAS_MIGRACION_2050}} % con más migración y {{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % con menos.

La regla mecánica es una comparación de escenarios, no un efecto estimado: sobrestima el nivel del gasto, pero el orden de los escenarios coincide con el del Ageing Report (más migración, menos gasto en proporción del PIB). Las cotizaciones de hoy generan derechos futuros (sección 4). La cifra del Ageing Report se toma del informe publicado y figura como NO VERIFICADA (sin DOI).

![Gráfico 4](figuras/fig4_dependencia.png)

## 7. Afirmaciones del debate y su veredicto

Las fichas completas están en `afirmaciones.md`. Resumen:

| id | Afirmación | Veredicto |
|---|---|---|
{{TABLA_AFIRMACIONES}}

Criterio común: cuando la contabilidad apoya una parte de la afirmación pero su núcleo es contrafactual («quita», «la causa», «sin ellos», «pagan», «colapsan») o sobre preferencias («no quieren») y no está identificado, el veredicto es «no se puede saber», en los dos sentidos. «Engañosa» se reserva para afirmaciones cuya cantidad principal la contabilidad contradice; «se sostiene con matices», para las que la contabilidad apoya en la cantidad principal con excepciones.

## 8. Limitaciones

- La fase 5 no se ejecutó (sección 5).
- La agrupación de origen está limitada por las fuentes: tres grupos en la ECV y Eurostat, y la EPA sin Magreb.
- La ECV y la EPA públicas no traen el diseño muestral completo: los errores se agrupan por hogar (ECV), por celda (EPA) o por establecimiento (EES), y con ello los intervalos pueden ser algo estrechos.
- Las encuestas de hogares cubren peor a los inmigrantes recién llegados y a los que están en situación irregular, y no incluyen hogares colectivos (residencias, centros de acogida). La dirección del sesgo en la contabilidad fiscal no es conocida.
- La ENSE es de 2017.
- La contabilidad fiscal depende de supuestos de imputación, que se muestran como intervalos. El ciclo vital, además, no incluye a los descendientes y aplica perfiles transversales de 2024 a vidas futuras.
- La tasa de salida del ciclo vital incluye bajas por caducidad del padrón, que no siempre son salidas reales, y el perfil de riesgo por duración es un supuesto.
- No hay salarios provinciales por nacionalidad: la estadística de la AEAT no fue accesible.

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
- **F. Declaración de pre-registro interno.** El plan de la fase 5 se fijó en la etiqueta git local prereg-m1, antes de construir el instrumento y de estimar cualquier efecto. No tiene sello de tiempo externo. La etiqueta no está en un remoto, por lo que la puerta permanece cerrada.
- **Tablas:** tablas_m1.xlsx (azul: dato introducido con su fuente; negro: calculado; verde: de otra pestaña).
