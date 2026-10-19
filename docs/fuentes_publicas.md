# Inventario de fuentes públicas (fase 0)

Para cada variable que necesita el estudio: qué fuente pública la da, con qué desagregación por origen, territorial y temporal, y con qué limitaciones. «Verificado» significa que el diseño de registro o la tabla se ha abierto el 19-10-2026; «por verificar» se confirma en la fase 2 (docs/fuentes/<familia>.md). Todas las fuentes son descargables sin registro salvo indicación expresa.

Abreviaturas de origen: **N8** = los ocho grupos del plan; **Nac/Ext** = solo española / extranjera; **3R** = España / resto UE / resto del mundo.

## 1. Qué permite cada fuente para la definición de origen

| Fuente | Nacimiento | Nacionalidad | Años de residencia | Nacionalizados | Segunda generación | Territorio mínimo | Diseño muestral publicado |
|---|---|---|---|---|---|---|---|
| Padrón continuo / Estadística Continua de Población (INE) | país (≈ 40 países y grandes áreas) | país | no | cruce nacimiento × nacionalidad (nacidos fuera con nacionalidad española) | no | provincia (municipio en padrón) | registro, sin muestreo |
| Censo 2021 (tablas) | país y grandes áreas | país | año de llegada (tablas seleccionadas) | sí (cruce) | no | provincia; municipio en tablas seleccionadas | registro |
| EPA, microdatos trimestrales (INE) — **verificado (dr_EPA_2021)** | REGNA1: 12 regiones (UE-15; UE-25 no UE-15; UE-28 no UE-27; resto de Europa; África; América del Norte; Centroamérica y Caribe; Sudamérica; Asia Oriental; Asia Occidental; Asia del Sur; Oceanía) | NAC1 (española / española y otra / extranjera) y EXREGNA1 (mismas regiones) | ANORE1 (años de residencia en España) | sí: nacidos fuera con NAC1 = española | parcial: hijos que conviven con sus padres (NPADRE, NMADRE → región de nacimiento del padre o la madre) | provincia (PROV) | solo FACTOREL; sin estratos ni conglomerados públicos |
| ECV, microdatos (INE) — **verificado (ECV 2025)** | RB280: 3R | RB290: 3R | no | sí (cruce RB280 × RB290) | parcial: RB220/RB230 (padre o madre en el hogar) | NUTS2 (DB040) | solo pesos (RB050, DB090, PB040); sin estratos ni UPM públicos |
| EPF, microdatos (INE) | por verificar (se espera nacionalidad del sustentador principal) | Nac/Ext o 3R | no | no | no | CCAA | solo factor de elevación |
| Encuesta de Estructura Salarial, microdatos (INE) | no | por verificar (en ediciones 2010-2022 se espera nacionalidad agrupada: España / resto de Europa / resto del mundo) | no | no | no | NUTS1 | factor de elevación |
| Afiliación a la Seguridad Social (estadísticas públicas) | no | país (principales) y grandes áreas | no | no (cuentan como españoles) | no | provincia | registro |
| Paro registrado y contratos (SEPE) | no | Nac/Ext y principales países (por verificar) | no | no | no | provincia (municipio en paro) | registro |
| AEAT, Mercado de Trabajo y Pensiones en las Fuentes Tributarias | no | por verificar (españoles / extranjeros por áreas) | no | no | no | provincia | registro (régimen común; sin País Vasco ni Navarra) |
| Eurostat, tablas EU-LFS | país de nacimiento: nativos / otro UE / fuera de la UE | ídem por ciudadanía | sí en tablas ad hoc (duración de residencia) | no | módulos ad hoc 2008, 2014, 2021 (segunda generación por país) | país; NUTS2 (3 grupos) | — |
| Eurostat, tablas EU-SILC | nativos / otro UE / fuera de la UE | ídem | no | no | no | país (algunas NUTS2) | — |
| Microdatos de uso público de Eurostat (PUF EU-LFS, EU-SILC) | agregado | agregado | no | no | no | país | anonimizados; solo como complemento |
| OCDE/UE, Indicators of Immigrant Integration 2023 | nativos / nacidos fuera | — | sí (recientes / asentados) | — | sí (indicadores de hijos de inmigrantes) | país (algunos indicadores regionales) | — |

Consecuencia: los **ocho grupos** solo se pueden construir con el padrón, la ECP, el Censo y (aproximadamente) la afiliación. En la EPA los grupos son una **aproximación** fijada ahora, antes de mirar resultados (decisión D6): UE-14 ≈ UE-15 (115; el Reino Unido pasa a «resto de Europa» desde 2020 en el diseño de la EPA); UE-13 y otros de Europa = 125 + 128 + 100; América Latina ≈ 310 + 350 (México queda en «América del Norte»); Magreb y resto de África **no se separan** (200 = África); Asia = 400 + 410 + 420; resto = 300 + 500. En la ECV y en Eurostat solo hay 3R; los resultados fiscales por grupo se dan en 3R y, con supuestos explícitos (capa C2), se reparten entre los ocho grupos con la estructura de la EPA.

## 2. Variables del estudio y su fuente

### 2.1 Población y flujos
| Variable | Fuente pública | Origen | Territorio / periodo | Limitaciones |
|---|---|---|---|---|
| Población por país de nacimiento, nacionalidad, edad y sexo | INE, Estadística Continua de Población (trimestral, 2021-) y Estadística del Padrón Continuo (anual, 1998-) | N8 (por país) | provincia; 1998-2026 | el padrón sobrestima a extranjeros con bajas tardías (caducidad de inscripciones desde 2006); la ECP corrige con fuentes administrativas |
| Flujos de inmigración y emigración | INE, Estadística de Migraciones (2008-) y Estadística de Variaciones Residenciales | país de nacimiento y nacionalidad | provincia; anual | la emigración de extranjeros se mide con retraso (bajas por caducidad) |
| Años de residencia | EPA (ANORE1); Censo 2021 (año de llegada) | EPA aproximado N8; Censo N8 | provincia | ANORE1 solo a extranjeros y nacidos en España con largas estancias fuera |
| Proyecciones de población | INE, Proyecciones 2026-2076 (si está publicada la edición; si no, 2024-2074); Eurostat EUROPOP2023 | totales con supuestos de saldo migratorio | España, CCAA; países | escenarios de migración del propio INE y de Eurostat |

### 2.2 Empleo
| Variable | Fuente | Origen | Territorio / periodo | Limitaciones |
|---|---|---|---|---|
| Actividad, empleo, paro, horas, temporalidad, parcialidad, sector (1 dígito), ocupación (1 dígito), educación | EPA microdatos | aproximado N8 por nacimiento; nacionalidad como sensibilidad | provincia; 2005T1-2026 | muestra pequeña por provincia y grupo → supresión < 50 obs.; sin estratos públicos (errores agrupados por provincia como aproximación conservadora) |
| Sobrecualificación | EPA (NFORMA × OCUP1) | aproximado N8 | provincia | ocupación a 1 dígito |
| Afiliados por nacionalidad, régimen, sector | Seguridad Social, «Afiliados extranjeros» (mensual) | país de nacionalidad (principales) | provincia; 1999-2026 | nacionalizados cuentan como españoles; no hay nacimiento |
| Paro registrado y contratos de extranjeros | SEPE, estadísticas mensuales | Nac/Ext y por continente o país (por verificar) | provincia | ídem |
| Europa: empleo, paro y actividad por nacimiento | Eurostat lfsa_ergacob, lfsa_urgacob, lfsa_argacob y tablas regionales lfst_r_* | 3R | país, NUTS2 | 3 grupos |

### 2.3 Salarios
| Variable | Fuente | Origen | Territorio / periodo | Limitaciones |
|---|---|---|---|---|
| Salario por hora y anual, deciles, componentes | Encuesta de Estructura Salarial, microdatos (2002, 2006, 2010, 2014, 2018, 2022) | nacionalidad agrupada (por verificar) | NUTS1 | no hay país de nacimiento ni años de residencia: la convergencia con la residencia no se estima con la EES |
| Deciles de salario del empleo principal | EPA, «Salarios del empleo principal» (tablas anuales) | Nac/Ext | nacional, CCAA | tablas, no microdatos |
| Salario medio por provincia | AEAT, Mercado de Trabajo y Pensiones en las Fuentes Tributarias | nacionalidad agrupada (por verificar) | provincia (régimen común) | sin País Vasco ni Navarra |
| Renta del trabajo de los asalariados | ECV (PY010G) | 3R | NUTS2 | renta anual, no salario por hora |
| Europa | Eurostat, EU-SILC (ilc_di* por nacimiento), EES europea (earn_ses*) | 3R / ciudadanía | país | — |

### 2.4 Ingresos públicos imputables
| Partida | Fuente | Observado o imputado |
|---|---|---|
| IRPF y cotizaciones del trabajador | ECV HY140G (impuestos sobre la renta y cotizaciones) | observado en encuesta (la ECV imputa con modelos fiscales del INE) |
| Cotizaciones empresariales | ECV PY030G | observado en encuesta |
| Cotizaciones con registro | Seguridad Social: afiliación por nacionalidad × bases medias publicadas | imputado (base media por régimen) |
| IVA e impuestos especiales | EPF (gasto por partidas y nacionalidad del sustentador) × tipos legales; recaudación de la AEAT para calibrar | imputado |
| Impuesto de sociedades, patrimonio, sucesiones | Recaudación AEAT/IGAE; reparto por renta de capital (ECV) | imputado (supuesto explícito) |
| IBI e impuestos sobre la vivienda | ECV (tenencia, HH021) × IBI medio (Catastro, estadísticas públicas) | imputado |
| Totales por figura | IGAE / Eurostat gov_10a_taxag | dato oficial para calibrar |

### 2.5 Gasto público imputable
| Partida | Fuente | Observado o imputado |
|---|---|---|
| Pensiones (jubilación, supervivencia, incapacidad) | ECV PY100G, PY110G, PY130G; Seguridad Social, pensionistas extranjeros (por verificar) | observado en encuesta |
| Desempleo | ECV PY090G; SEPE, beneficiarios extranjeros | observado |
| IMV y rentas mínimas | ECV HY060G; estadísticas del IMV por nacionalidad (por verificar) | observado / imputado |
| Familia, vivienda, educación (prestaciones monetarias) | ECV HY050G, HY070G, PY140G | observado |
| Educación (en especie) | Ministerio de Educación: alumnado extranjero por nivel y CCAA; gasto público por alumno | imputado por edad y escolarización |
| Sanidad (en especie) | perfil de gasto por edad y sexo publicado (Ageing Report de la Comisión Europea o estudios del Ministerio de Hacienda / Sanidad, por verificar) | imputado; sensibilidad con diferencias de uso de la literatura |
| Bienes públicos puros (defensa, intereses, administración general) | IGAE/Eurostat COFOG (gov_10a_exp) | dos criterios: coste medio per cápita y coste marginal cero |
| Gasto por funciones y por CCAA | IGAE (COFOG por subsectores), Eurostat gov_10a_exp | dato oficial |

### 2.6 Vivienda
| Variable | Fuente | Origen | Territorio |
|---|---|---|---|
| Tenencia, hacinamiento, esfuerzo (gasto/renta), tipo de hogar | ECV (HH021, HH030, HX…) | 3R | NUTS2 |
| Tenencia y superficie por origen | Censo 2021 (tablas de hogares y viviendas por nacionalidad) | N8 (por verificar) | provincia |
| Compraventas por extranjeros | Notariado / Registradores (estadísticas públicas trimestrales; residentes y no residentes) | nacionalidad del comprador | provincia |
| Europa | Eurostat ilc_lvho05b (hacinamiento por nacimiento), ilc_lvho25 (sobrecarga), ilc_lvps* | 3R | país |

### 2.7 Servicios públicos (congestión)
| Variable | Fuente | Territorio / periodo | Limitaciones |
|---|---|---|---|
| Listas de espera quirúrgicas y de consultas | Ministerio de Sanidad, SISLE-SNS | CCAA; semestral, 2016- (series anteriores en informes) | 17 CCAA: pocos clusters |
| Profesionales sanitarios por habitante | Ministerio de Sanidad (SIAP, SIAE) | CCAA / provincia (por verificar) | — |
| Alumnado por grupo y por profesor; alumnado extranjero | Ministerio de Educación, EDUCAbase | CCAA y provincia (por verificar) | — |

### 2.8 Contexto provincial
PIB y VAB por provincia (INE, Contabilidad Regional); renta de los hogares (INE, Atlas de Distribución de Renta, 2015-); estructura sectorial (EPA, afiliación); precios de vivienda (INE IPV por CCAA; MIVAU valor tasado por provincia). La base pública de Econometr-a tiene licencia por partes (LICENSE): se enlaza, no se copia (regla A).

### 2.9 Europa
Eurostat: migr_pop3ctb y migr_pop1ctz (población por nacimiento y ciudadanía), lfst_r_* regionales, migr_imm*/migr_emi* (flujos), proj_23np (proyecciones), ilc_* por nacimiento (renta, pobreza, privación, vivienda). OCDE: International Migration Outlook (tablas en línea y StatLinks), Indicators of Immigrant Integration 2023 (OCDE/UE). JRC: resultados publicados del impacto fiscal por país. Comisión Europea: Ageing Report 2024 (supuestos y resultados por país).

## 3. Lo que NO es público y qué pregunta queda afectada (va a limitaciones; no genera tareas)

| Dato no público | Acceso | Pregunta afectada | Tratamiento en M1 |
|---|---|---|---|
| Muestra Continua de Vidas Laborales (MCVL) | solicitud a la Seguridad Social | trayectorias laborales y salariales individuales por país de nacimiento; asimilación con datos de panel; cotizaciones y pensiones de por vida | convergencia salarial con cortes transversales (EPA, EES) y cohortes sintéticas (C4); ciclo vital fiscal con perfiles transversales (C2) |
| Microdatos de investigación de la EU-LFS y la EU-SILC | solicitud a Eurostat (entidades acreditadas) | país de nacimiento detallado y NUTS2 en Europa; shift-share europeo por origen | P5 con tablas agregadas de 3 grupos; probablemente ASOCIACIÓN o NO ESTIMABLE |
| Microdatos del Censo 2021 con país detallado y municipio | el fichero público es una muestra con variables agregadas (por verificar) | cuotas de asentamiento por país a nivel fino | cuotas por provincia con el padrón (público, completo por país) |
| Uso individual de servicios sanitarios y educativos por origen (historias clínicas, registros escolares) | restringido | gasto en especie por origen; congestión individual | perfiles por edad y sexo (C2) con sensibilidad de la literatura; P3 a nivel agregado o NO ESTIMABLE |
| Declaraciones de IRPF por nacionalidad (muestras del IEF) | solicitud | IRPF pagado por origen | IRPF de la ECV (HY140G), con calibración a la recaudación |
| Pensiones contributivas individuales por país de nacimiento | registro administrativo restringido | pensiones futuras de inmigrantes | perfiles de la ECV y reglas legales (C2) |
| Estratos y conglomerados de la EPA y de la ECV | no publicados | errores de diseño exactos | errores agrupados por provincia (EPA) o región (ECV) y se declara |
| Retorno y emigración individual de inmigrantes | registros no públicos | tasas de retorno para el ciclo vital | escenarios de retorno de la literatura y de la Estadística de Migraciones (C2) |
