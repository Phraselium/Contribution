# Pre-registro interno M1 · Fase 5 (impacto causal, pregunta B)

Pre-registro **interno, sin sello de tiempo externo**: se fija con la etiqueta git `prereg-m1` en el commit que contiene este fichero y su adenda; la puerta (src/m1/etiquetas.py, hook y `make m1_f5`) impide estimar antes. Cualquier cambio posterior va a docs/desviaciones.md con su motivo.

## 0. Lo ya visto antes de fijar el plan
- Fases 0-4: datos descriptivos por origen (tasas de empleo, paro, salarios, vivienda, prestaciones; contribución fiscal). En particular se han visto las tasas de empleo provinciales de nacidos en España y fuera en 2014, 2019 y 2025 (output/f3/empleo_provincias.csv) y la evolución de la población por grupo y provincia (padrón).
- No se ha estimado ninguna regresión de resultados de la población local sobre la inmigración, ni se ha construido el instrumento ni su primera etapa.
- Literatura (docs/literatura/trabajo.md): efectos pequeños o nulos en España (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Informe Anual del Banco de España 2025 con shift-share provincial). Esto fija expectativas, no la especificación.

## 1. Preguntas e hipótesis
| id | pregunta | resultado (población local = nacidos en España, 16-64) | tipo |
|---|---|---|---|
| P1-H1 | ¿Cambia la tasa de empleo de los nacidos en España cuando aumenta la población nacida fuera en su provincia? | Δ tasa de empleo (EPA) | confirmatoria |
| P1-H2 | ídem, tasa de paro | Δ tasa de paro (EPA) | confirmatoria |
| P1-E1 | tasa de actividad | Δ tasa de actividad | exploratoria |
| P1-E2 | ocupación de nacidos en España (escala) | Δ log ocupados nacidos en España | exploratoria |
| P1-E3 | por nivel educativo (réplica ampliada de González y Ortega 2011 y Carrasco, Jimeno y Ortega 2008) | Δ tasa de empleo por celda provincia × educación (baja, media, alta) | exploratoria |
| P1-E4 | salarios: celdas nacionales educación × edad (Borjas 2003) | Δ log salario por hora de los españoles por celda (EES 2010-2022) frente a Δ cuota de extranjeros en la celda (EPA) | exploratoria |
| P1-E5 | salarios provinciales | si hay una serie pública de salarios por provincia y nacionalidad (AEAT); si no, NO ESTIMABLE | exploratoria |
| P2-E1 | ocupaciones (Peri y Sparber 2009) | Δ cuota de ocupados nacidos en España en ocupaciones CNO 1-4 (no manuales, más intensivas en comunicación) | exploratoria |
| P2-E2 | ocupaciones de alta cualificación | Δ cuota en CNO 1-3 | exploratoria |
| P3 | servicios públicos (congestión) | listas de espera quirúrgicas (días) y alumnos por profesor, por CCAA, si existen series públicas suficientes; si no, NO ESTIMABLE | exploratoria |
| P4 | vivienda | enlace con Econometr-a (sin duplicar: no se estima en M1) | — |
| P5 | Europa | Δ tasa de empleo 20-64 de los nativos por NUTS2 (EU-LFS) frente a Δ cuota de nacidos fuera | exploratoria |

## 2. Diseño principal (P1, P2)
- **Unidad**: 52 provincias (con sensibilidad sin Ceuta y Melilla). **Periodos apilados**: A = 2005→2009, B = 2009→2015, C = 2015→2022 (la última fecha del padrón por país es el 1-1-2022). Resultados con medias anuales de la EPA del año inicial y final.
- **Tratamiento**: x_lp = (nacidos fuera_l,fin − nacidos fuera_l,inicio) / población 16-64_l,inicio (padrón, total de nacidos fuera; población 16-64 de la EPA del año inicial).
- **Instrumento (Card 2001)**: z_lp = Σ_o s_ol,1998 · ΔM_o,p(−l) / población 16-64_l,inicio, con s_ol,1998 = cuota de la provincia l en los nacidos en el país o (padrón 1998, ≈ 110 países y restos) y ΔM_o,p(−l) la variación nacional de nacidos en o en el periodo excluida la provincia l.
- **Ajuste dinámico (Jaeger, Ruist y Stuhler 2018)**: especificación con el instrumento del periodo y el del periodo anterior (z_lp y z_l,p−1, este último disponible para B y C); el coeficiente del periodo es el efecto de corto plazo y la suma, el de largo plazo. Especificación de largo plazo adicional: diferencia larga 2005→2022.
- **Controles** (fijados): efectos fijos de periodo; cuota de nacidos fuera en 1998 × periodo (suma de cuotas, BHJ); tasa de paro de nacidos en España al inicio del periodo; efectos fijos de CCAA en la variante «completo».
- **Pesos**: población 16-64 al inicio (principal); sin pesos (sensibilidad).
- **Estimador**: MC2E (econ.iv2sls) con un instrumento; coeficiente de interés β (efecto en puntos de la tasa por cada punto de aumento de la población nacida fuera respecto a la población 16-64).
- **Inferencia (según docs/montecarlo.md)**: principal **AKM0** (Adão, Kolesár y Morales 2019, nulo impuesto, intervalo por inversión; APTO); se informa también el error BHJ (NO APTO como inferencia principal), el F de primera etapa al nivel del shock y el F efectivo agrupado por provincia; con F efectivo < 10 se informa el conjunto de Anderson-Rubin. Nunca errores convencionales como inferencia del shift-share. Para controles de dependencia espacial: wild cluster bootstrap restringido (Webb, B = 9.999) agrupando por CCAA (17, APTO con condición de apalancamiento); Conley no se usa (NO APTO).
- **P1-E4 (Borjas)**: celdas nacionales educación (3) × edad (5 tramos de la EES) × año (2010, 2014, 2018, 2022); Δ log salario medio por hora de los españoles (EES) sobre Δ cuota de nacidos fuera en la celda (EPA), con efectos fijos de celda y año; MCO con errores agrupados por celda y wild bootstrap (15 celdas). Sin instrumento: la clasificación máxima es SUGESTIVO.

## 3. Pruebas
1. **Pretendencias**: (a) Δ resultado del periodo A sobre el instrumento de los periodos B y C (sin el de A); (b) correlación de las cuotas de 1998 con la tasa de empleo y de paro de los nativos de 2005 (balance).
2. **Rotemberg** (Goldsmith-Pinkham, Sorkin y Swift 2020): pesos α_o, β_o de los 5 orígenes de más peso y su heterogeneidad.
3. **Exclusión de orígenes**: se excluyen, uno a uno y juntos, los 3 orígenes de mayor peso de Rotemberg.
4. **Placebos**: (a) resultado placebo: Δ tasa de empleo de los nacidos en España de 65-74 años (población poco expuesta al mercado de trabajo); (b) instrumento con shocks permutados entre orígenes (500 permutaciones, SEED=20261019): distribución del t.
5. **Definición de origen**: instrumento y tratamiento con nacionalidad (padrón 03005) en lugar de nacimiento.
6. **Montecarlo**: solo herramientas APTO (docs/montecarlo.md).
7. **Revisión**: replicador-ciego reimplementa la especificación principal de P1-H1 y P1-H2; abogado-del-diablo ataca todo lo que quede IDENTIFICADO o SUGESTIVO.

## 4. Multiverso (todas las especificaciones al Registry; ninguna se elige por p-valor)
año base de las cuotas (1998, 2002) × pesos (sí, no) × controles (básico, completo) × muestra (52, 50 provincias) × periodos (apilado A-C, diferencia larga) = 32 especificaciones por resultado. Se publica la distribución completa de β.

## 5. Corrección por multiplicidad
Holm sobre las dos confirmatorias (P1-H1, P1-H2) con el p de AKM0 de la especificación principal. BH sobre las exploratorias.

## 6. Reglas de clasificación (fijadas ahora)
- **IDENTIFICADO**: F de primera etapa ≥ 10 (al nivel del shock y efectivo) o intervalo AKM0/AR acotado; pretendencia (1a) no significativa al 10 %; placebo (4a) no significativo al 10 % y t de la especificación principal fuera del 95 % central de las permutaciones solo si hay efecto; signo y orden de magnitud estables al excluir los 3 orígenes principales y con nacionalidad; herramienta APTO; replicador-ciego dentro del IC95; abogado-del-diablo «resiste» o «resiste con limitaciones». Un efecto nulo con intervalo estrecho puede quedar IDENTIFICADO («no se detecta efecto mayor que …»).
- **SUGESTIVO**: diseño creíble con una prueba débil o fallida no decisiva (p. ej., pretendencia con p entre 0,05 y 0,10, o sensibilidad moderada a la exclusión de un origen). Techo para P1-E4, P3 y P5.
- **ASOCIACIÓN**: primera etapa débil (F < 10 y AR no acotado), pretendencia significativa al 5 % o cambio de signo al excluir orígenes.
- **NO ESTIMABLE**: falta el dato público (se indica cuál y si existe con acceso restringido).
Sin lenguaje causal fuera de IDENTIFICADO.

## 7. P3, P4 y P5
- **P3**: si las series públicas lo permiten (SISLE-SNS por CCAA desde 2016; EDUCAbase por CCAA), panel de CCAA × año con Δ resultado sobre Δ cuota de nacidos fuera instrumentada con el shift-share de CCAA (cuotas de 1998); inferencia wild bootstrap Webb con 17 clusters; techo SUGESTIVO. Si no hay series suficientes: NO ESTIMABLE (dato que faltaría: uso y espera por paciente y origen, solo en registros clínicos restringidos).
- **P4**: no se estima: se enlaza con el resultado de Econometr-a (panel de CCAA con shift-share, sin efectos que sobrevivan al wild bootstrap ni a Holm).
- **P5**: NUTS2 de la UE con datos del censo 2021 (cuotas por país de nacimiento, cens_21cob_r3 agregadas a NUTS2) y flujos nacionales por país de nacimiento 2021-2024 (migr_imm3ctb) excluido el propio país; resultado Δ tasa de empleo 20-64 de los nativos 2021→2024; efectos fijos de país; inferencia AKM0 y wild bootstrap por país; comparación de países por instituciones (agrupación fijada: mediterráneos, continentales, nórdicos, anglosajón, centro y este). Techo SUGESTIVO (periodo corto, cuotas del año inicial de un censo posterior a la COVID).
