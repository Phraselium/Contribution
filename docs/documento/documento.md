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

**Población.** La población nacida fuera de España era el {{F3_POB_FUERA_PADRON_2022}} % en el padrón de 2022 y el {{F3_POB_FUERA_ECP_2025}} % en la Estadística Continua de Población de 2025. En 1998 era el {{F3_POB_FUERA_PADRON_1998}} %. En la UE-27 la cifra es del {{F3_POB_FUERA_UE27_2025}} %. Es una población más joven: el {{F3_POB_65MAS_nacidos fuera_2025}} % tiene 65 o más años, frente al {{F3_POB_65MAS_España_2025}} % de los nacidos en España.

**Empleo.** En 2025 la tasa de empleo de 16 a 64 años es del {{F3_EMP_TASA_FUERA_2025}} % entre los nacidos fuera y del {{F3_EMP_TASA_España_2025}} % entre los nacidos en España. La variación interna es amplia: África {{F3_EMP_TASA_África_2025}} %, UE-14 {{F3_EMP_TASA_UE-14_2025}} %. El paro es mayor entre los nacidos fuera: {{F3_EMP_PARO_FUERA_2025}} % frente a {{F3_EMP_PARO_España_2025}} %. Al aumento de la ocupación entre 2014 y 2025, de {{F3_EMP_AUMENTO_OCUPADOS_2014_2025}} millones, los nacidos fuera aportan el {{F3_EMP_CONTRIB_FUERA_2014_2025}} %. Es contabilidad: no dice qué habría ocurrido sin inmigración.

**Salarios.** Los extranjeros cobran por hora un {{F3_SAL_BRECHA_bruto_2022}} % menos que los españoles (Encuesta de Estructura Salarial, EES, 2022). A igual edad, sexo, estudios y región la diferencia baja al {{F3_SAL_BRECHA_completo_2022}} %. Alrededor del {{F3_SAL_OAXACA_COMPOSICION_2022}} % de la brecha media es composición.

**Vivienda.** Vive en vivienda en propiedad el {{F3_VIV_propietario_España_2021_2025}} % de los nacidos en España, frente al {{F3_VIV_propietario_Resto_del_mundo_2021_2025}} % de los nacidos fuera de la UE. La sobrecarga del gasto en vivienda afecta al {{F3_VIV_sobrecarga_Resto_del_mundo_2021_2025}} % de los segundos y al {{F3_VIV_sobrecarga_España_2021_2025}} % de los primeros.

**Cuentas públicas.** Contribución neta estática en 2024, en euros por persona, con el intervalo de 64 combinaciones de supuestos:
- nacidos en España: entre {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}} y {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}};
- nacidos en el resto de la UE: entre {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}} y {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}};
- nacidos fuera de la UE: entre {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}} y {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}.

En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España. Por eso solo se publica el intervalo (decisión del autor, D11). La contabilidad de ciclo vital da intervalos que contienen el cero para todos los grupos de llegada.

**Pensiones.** En una regla demográfica mecánica, sin migración el gasto en pensiones de 2050 sería {{F4_PEN_EFECTO_SIN_MIGRACION_2050}} puntos de PIB mayor que en la proyección base de EUROPOP2023. Es una cota con supuestos, no una proyección del sistema.

**Impacto sobre la población local.** La estimación causal está pre-registrada, revisada y programada, pero **no se ha ejecutado**: la puerta del pre-registro interno exige que la etiqueta esté en un repositorio remoto, y en esta versión no lo está. Todas las preguntas causales quedan pendientes y se cita solo la literatura verificada.

**Afirmaciones del debate.** De las doce evaluadas, seis en cada sentido, tres son engañosas, cinco no se pueden saber con datos públicos y cuatro se sostienen con matices (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. Trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales. Cobran menos por hora, sobre todo porque son más jóvenes, tienen otros estudios y trabajan en otras ocupaciones. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas, los nacidos en otros países de la UE aportan más de lo que reciben en cualquier supuesto razonable. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. El estudio la deja preparada, pero sin resultados propios todavía.

## 1. Introducción

Este documento mide la contribución de cada grupo de origen al empleo, a los salarios, a la vivienda y a las cuentas públicas en España (nacional, comunidad y provincia) y en Europa (país y NUTS2). Además prepara, con un pre-registro interno, la estimación del impacto causal de la inmigración sobre la población local.

Las dos preguntas se responden por separado. La contribución (A) es contabilidad, capas C1 y C2. El impacto (B) exige identificación, capa C3, y solo se describe con lenguaje causal si queda IDENTIFICADO según reglas fijadas antes de estimar.

Reglas comunes a todo el documento:
- Las comparaciones se dan en tres niveles: bruto; ajustado por edad y sexo; ajustado además por educación, años de residencia (cuando la fuente los tiene) y región.
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

En Europa, España ocupa el puesto {{F3_POB_FUERA_ES_RANKING_2025}} por cuota de nacidos fuera ({{F3_POB_FUERA_ES_EUROSTAT_2025}} % según Eurostat).

![Mapa 1](figuras/mapa1_provincias_nacidos_fuera.png)

### 3.2 Empleo

Tasas de empleo de 16 a 64 años en 2025 (gráfico 1):
- nacidos en España: {{F3_EMP_TASA_España_2025}} %;
- UE-14: {{F3_EMP_TASA_UE-14_2025}} %;
- UE-13 y otros de Europa: {{F3_EMP_TASA_UE-13 y otros de Europa_2025}} %;
- América Latina: {{F3_EMP_TASA_América Latina_2025}} %;
- África: {{F3_EMP_TASA_África_2025}} %;
- Asia: {{F3_EMP_TASA_Asia_2025}} %.

**Tres niveles.** La brecha de África con los nacidos en España es de {{F3_EMP_BRECHA_África_bruto_2025}} pp en bruto, {{F3_EMP_BRECHA_África_edad_y_sexo_2025}} pp a igual edad y sexo, y {{F3_EMP_BRECHA_África_completo_2025}} pp al añadir educación, residencia y provincia. La de América Latina pasa de {{F3_EMP_BRECHA_América Latina_bruto_2025}} pp a {{F3_EMP_BRECHA_América Latina_completo_2025}} pp.

**Por provincias**, la brecha de empleo entre nacidos fuera y nacidos en España va de {{F3_EMP_BRECHA_PROV_MIN_2025}} a {{F3_EMP_BRECHA_PROV_MAX_2025}} pp. En {{F3_EMP_BRECHA_PROV_POSITIVAS_2025}} provincias los nacidos fuera tienen una tasa mayor (mapa 2).

**Crecimiento del empleo.** En 2014-2025 los nacidos fuera aportan el {{F3_EMP_CONTRIB_FUERA_2014_2025}} % del aumento de la ocupación y el {{F3_EMP_CONTRIB_HORAS_FUERA_2014_2025}} % del de las horas.

**Europa.** La brecha de empleo de 20 a 64 años entre nacidos fuera y nativos es de {{F3_EMP_EU_ES_BRECHA_2025}} pp en España y de {{F3_EMP_EU_UE27_BRECHA_2025}} pp en la UE-27 (mapa 3).

**Cohortes y generaciones.** El pseudopanel de cohortes de llegada indica que las cohortes llegadas después de 2008 tienen tasas de empleo menores que los nativos, más que las anteriores, a igual tiempo de residencia (C4). La segunda generación que convive con sus padres tiene, a igual tramo de edad, una tasa de empleo unos puntos menor que la de los nativos que también conviven con sus padres (output/f3/empleo_generaciones.csv).

![Gráfico 1](figuras/fig1_empleo.png)

![Mapa 2](figuras/mapa2_provincias_brecha_empleo.png)

![Mapa 3](figuras/mapa3_europa_nuts2.png)

### 3.3 Salarios

**Brecha de salario por hora** entre extranjeros y españoles (EES 2022, errores agrupados por establecimiento):
- bruta: {{F3_SAL_BRECHA_bruto_2022}} %;
- a igual edad y sexo: {{F3_SAL_BRECHA_edad_2022}} %;
- además a igual estudios y región: {{F3_SAL_BRECHA_completo_2022}} %;
- además a igual ocupación, sector, contrato y jornada: {{F3_SAL_BRECHA_completo_inf_2022}} % (informativo).

**Por percentiles**, la brecha es de {{F3_SAL_BRECHA_P10_2022}} % en el 10, {{F3_SAL_BRECHA_P50_2022}} % en la mediana y {{F3_SAL_BRECHA_P90_2022}} % en el 90. La reponderación DFL atribuye a la composición en torno a dos tercios en cada percentil (gráfico 2).

**Segunda fuente.** Con la ECV, la mediana de los rendimientos del trabajo de los asalariados a jornada completa es un {{F3_SAL_ECV_BRECHA_Resto_del_mundo_2024}} % menor para los nacidos fuera de la UE.

**Convergencia salarial con los años de residencia: NO ESTIMABLE con datos públicos.** Ni la EES ni la ECV tienen años de residencia; haría falta la MCVL.

![Gráfico 2](figuras/fig2_salarios_dfl.png)

### 3.4 Vivienda

**Propiedad**, en la ECV 2021-2025:
- nacidos en España: {{F3_VIV_propietario_España_2021_2025}} %;
- resto de la UE: {{F3_VIV_propietario_Resto_UE_2021_2025}} %;
- resto del mundo: {{F3_VIV_propietario_Resto_del_mundo_2021_2025}} %.

Eurostat, como segunda fuente, da {{F3_VIV_EU_ilc_lvps16_NAT_ES_2025}} % para los nativos y {{F3_VIV_EU_ilc_lvps16_FOR_ES_2025}} % para los nacidos fuera. A igual edad, sexo, educación y región, la diferencia en propiedad de los nacidos fuera de la UE es de {{F3_VIV_propietario_BRECHA_COMPLETO_Resto_del_mundo}} pp.

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

A igual edad, sexo, educación y región, la diferencia en rentas mínimas de los nacidos fuera de la UE es de {{F3_PRE_BRECHA_perceptor_rentas_minimas_IMV_Resto_del_mundo_completo}} pp, y en jubilación de {{F3_PRE_BRECHA_perceptor_jubilacion_Resto_del_mundo_completo}} pp. Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad y se usan como contraste (docs/fuentes/admin.md).

## 4. Contabilidad fiscal estática y de ciclo vital

**Método.** Se sigue la OCDE (2021) adaptada a datos públicos. Los ingresos y los gastos de las administraciones de 2024 se reparten entre las personas de la ECV 2025:
- impuestos sobre la renta, cotizaciones y prestaciones, observados en la encuesta y calibrados a las cuentas;
- IVA e impuestos especiales con la Encuesta de Presupuestos Familiares (EPF);
- sanidad con el perfil de uso de la Encuesta Nacional de Salud (ENSE);
- educación según matrícula;
- bienes públicos puros (servicios generales e intereses, defensa) a coste medio o a coste marginal cero.

Los ingresos no tributarios se reparten por persona, de modo que la suma cuadra con el saldo de las administraciones.

**Resultado estático (capa C2, gráfico 3).** Contribución neta por persona en 2024:
- **nacidos en España:** {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024}} € en el escenario principal; intervalo de supuestos [{{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_España_2024:sup}}];
- **resto de la UE:** [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024:sup}}], positiva en todos los supuestos;
- **resto del mundo:** [{{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:inf}}, {{F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024:sup}}]; el signo depende de los bienes públicos y de los hijos nacidos en España, y por decisión D11 solo se publica el intervalo.

En prestaciones monetarias, los nacidos fuera de la UE reciben {{F6_PREST_MONETARIAS_PC_Resto_del_mundo}} € por persona y los nacidos en España {{F6_PREST_MONETARIAS_PC_España}} €, sobre todo por las pensiones.

**Ciclo vital (C2).** Valor actual de por vida según la edad de llegada, con supervivencia, retorno, convergencia, descuento y pensiones futuras ligadas a la carrera de cotización:
- llegada a los 30 años desde fuera de la UE: entre {{F4_VA_Resto_del_mundo_LLEGADA_30:inf}} y {{F4_VA_Resto_del_mundo_LLEGADA_30:sup}} miles de euros;
- desde la UE: entre {{F4_VA_Resto_UE_LLEGADA_30:inf}} y {{F4_VA_Resto_UE_LLEGADA_30:sup}}.

Los dos intervalos contienen el cero. La parte hasta los 64 años («población joven hoy») se presenta separada de la de 65 y más años (pensiones y sanidad futuras) en output/f4/ciclo_vital.csv.

**Sensibilidad.** Lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos; en el ciclo vital, también el retorno y la convergencia. Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Según el JRC (Fiorio et al. 2023), los inmigrantes en España muestran una contribución neta por persona mayor que la de los nativos en 2014-2018, y no hay diferencia significativa a igual composición demográfica. Este estudio coincide en la dirección para los nacidos en la UE y no para los nacidos fuera de ella, cuyo signo depende de los supuestos. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda, etiqueta local prereg-m1, pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia con cuotas de 1998;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler;
- pretendencia con la afiliación de 1999-2001, permutaciones, exclusión de los orígenes con mayor peso de Rotemberg y sensibilidad por nacionalidad.

**Estado: no ejecutado.** La puerta exige que el commit de la etiqueta esté en la rama de un repositorio remoto. Esta sesión no tuvo remoto y no pudo crearlo, así que la fase 5 queda pendiente y ninguna pregunta B tiene clasificación propia. En la literatura verificada sobre España (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Banco de España 2025) no se encuentran efectos negativos significativos sobre el empleo de los nativos. Es literatura, no un resultado de M1.

**Situación de cada pregunta:**
- P3 (servicios públicos): pendiente, con techo ASOCIACIÓN. Las listas de espera solo se publican en PDF.
- P4 (vivienda): no se duplica; se remite a Econometr-a.
- P5 (Europa): pendiente, con techo SUGESTIVO.

## 6. Pensiones y demografía

Las pensiones de vejez y supervivencia suponen el {{F4_PEN_GASTO_PIB_2024}} % del PIB en 2024. Tasa de dependencia de mayores de EUROPOP2023 en 2050, por cada 100 personas de 20 a 64 años (gráfico 4):
- variante base: {{F4_PEN_DEPENDENCIA_BSL_2050}};
- sin migración: {{F4_PEN_DEPENDENCIA_NMIGR_2050}};
- con un tercio más de migración: {{F4_PEN_DEPENDENCIA_HMIGR_2050}}.

Con una regla mecánica que mantiene constantes el empleo, la cobertura y la pensión relativa, el gasto de 2050 sería del {{F4_PEN_GASTO_MECANICO_BSL_2050}} % del PIB en la base y del {{F4_PEN_GASTO_MECANICO_NMIGR_2050}} % sin migración. El Ageing Report 2024, que modeliza empleo y reformas, da {{F4_PEN_AR2024_BASE_2050}} %, {{F4_PEN_AR2024_MAS_MIGRACION_2050}} % con más migración y {{F4_PEN_AR2024_MENOS_MIGRACION_2050}} % con menos.

La regla mecánica es una cota: sobrestima el nivel, pero la dirección del efecto de la migración coincide. Las cotizaciones de hoy generan derechos futuros (sección 4).

![Gráfico 4](figuras/fig4_dependencia.png)

## 7. Afirmaciones del debate y su veredicto

Las fichas completas están en `afirmaciones.md`. Resumen:

| id | Afirmación | Veredicto |
|---|---|---|
| A1 | Los inmigrantes viven de las ayudas | engañosa (alta) |
| A2 | Quitan empleo a los españoles | engañosa (media) |
| A3 | Hunden los salarios | no se puede saber (media) |
| A4 | Colapsan la sanidad | engañosa (media) |
| A5 | Suponen un coste fiscal neto | no se puede saber (alta) |
| A6 | Son la causa de la subida de la vivienda | no se puede saber (media) |
| F1 | Pagan nuestras pensiones | se sostiene con matices (media) |
| F2 | Sin ellos no habría crecido el empleo | no se puede saber (media) |
| F3 | Aportan más de lo que reciben | no se puede saber (alta) |
| F4 | Trabajan tanto como los españoles | se sostiene con matices (alta) |
| F5 | Se les paga menos por el mismo trabajo | se sostiene con matices (media) |
| F6 | Hacen los trabajos que los españoles no quieren | se sostiene con matices (baja) |

## 8. Limitaciones

- La fase 5 no se ejecutó (sección 5).
- La agrupación de origen está limitada por las fuentes: tres grupos en la ECV y Eurostat, y la EPA sin Magreb.
- La ECV y la EPA públicas no traen el diseño muestral completo.
- La ENSE es de 2017.
- La contabilidad fiscal depende de supuestos de imputación, que se muestran como intervalos.
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
