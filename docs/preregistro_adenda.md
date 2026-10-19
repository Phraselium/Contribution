# Adenda al pre-registro M1 (tras la revisión del abogado del diablo)

Veredicto de la revisión: «resiste con limitaciones; no resiste sin los cambios 1-6». Esta adenda incorpora todos los cambios de prioridad alta y media. Prevalece sobre docs/preregistro.md donde lo contradiga. Pre-registro interno sin sello de tiempo externo.

## A1. Especificación principal única (por hipótesis P1-H1 y P1-H2)
- 50 provincias (sin Ceuta ni Melilla; con ellas, sensibilidad informada siempre).
- Periodos apilados A = 2005→2009, B = 2009→2015, C = 2015→2022; una sola endógena (sin retardo).
- **Tratamiento**: x_lp = Δ población nacida fuera de **16-64 años** (ECP, t56948, 1 de enero) / población 16-64 al inicio (ECP).
- **Instrumento**: z_lp = Σ_o s_ol,1998 · ΔM_o,p(−l) / población 16-64_l,inicio, con s_ol,1998 = cuota de la provincia l en los nacidos en o **con nacionalidad extranjera** en 1998 (padrón 03006; excluye la emigración española de retorno) y ΔM_o,p = variación nacional de nacidos en o (todas las nacionalidades; padrón 03006; 2022 como fin de C). Se usa el shock nacional (sin excluir la provincia) para que el instrumento sea exactamente z = S̃·g y la inferencia AKM0 sea la del diseño validado; la versión que excluye la propia provincia (ΔM_o,p(−l)) pasa al multiverso.
- **Controles**: efectos fijos de periodo; suma de cuotas de 1998 × periodo; tasa de paro de los nacidos en España al inicio del periodo; **cuota de ocupados en la construcción en 2005 × periodo** (EPA); **Bartik sectorial de nativos** (crecimiento nacional del empleo de nacidos en España por sector CNAE a 1 dígito × estructura provincial de 2005).
- Pesos: población 16-64 al inicio. Estimador: MC2E (econ.iv2sls). Inferencia: **AKM0** con rejilla β̂ ± 15 EE(BHJ) en 3.001 puntos; se informa si el conjunto aceptado es convexo.

## A2. Ajuste dinámico (Jaeger, Ruist y Stuhler), especificación secundaria
- Se añade el periodo previo P0 = 1998→2005 como retardo de A (instrumento z_l,P0 con las mismas cuotas). Especificación con dos endógenas (x_lp, x_l,p−1) y dos instrumentos (z_lp, z_l,p−1): econ.iv2sls generalizado a varias endógenas y validado por Monte Carlo (A5) antes de usarse.
- Se informa corr(z_lp, z_l,p−1) entre provincias y la correlación entre periodos de los shocks ΔM_o. Si |corr(z_p, z_p−1)| > 0,8, se declara que el corto y el largo plazo no se pueden separar con estos datos.

## A3. Pretendencia y placebo (sustituyen a 1a y 4a)
- **Pretendencia (condición de IDENTIFICADO)**: Δ log afiliados a la Seguridad Social por provincia 1999→2001 (Excel histórico de la TGSS; antes de la gran ola, con pocos extranjeros) sobre z_A, controlando z_P0 y los controles de A1. Además, balance: correlación de z_A con Δ log población nacida en España 1998→2002 (padrón).
- **Placebo**: Δ log población nacida en España 16-64 no se usa como placebo sino como **resultado adicional** (movilidad interna de los nativos, P1-E6). Placebo de permutación (500 permutaciones de los shocks entre orígenes) se mantiene: el t principal se compara con la distribución permutada.
- Se elimina el placebo de 65-74 años (sin potencia).

## A4. Variantes adicionales del multiverso
Se añaden: cuotas con todos los nacidos fuera (incluida nacionalidad española), cuotas con suelo (orígenes con menos de 1.000 personas en 1998 agregados en «resto»), exclusión de los shocks de la UE-14 (incluido el Reino Unido), tratamiento con todas las edades (padrón), sin controles de construcción ni Bartik, e instrumento con shocks que excluyen la propia provincia. (No es factible usar la ECP para los shocks de C: la ECP no tiene país de nacimiento; la sensibilidad a las bajas por caducidad se aproxima con el periodo C acortado a 2015→2020.) La distribución completa de β se publica.

## A5. Monte Carlo adicional (antes de estimar)
- AKM0 con shocks persistentes entre periodos (ρ = 0,6 y −0,5), O efectivo ≈ 15 y apilado de 3 periodos, agrupando los residuos por origen entre periodos.
- MC2E con dos endógenas (A2): sesgo y cobertura con instrumentos correlacionados (corr 0,5 y 0,8).
Si alguna herramienta sale NO APTO, la especificación que la usa pasa a exploratoria y se dice.

## A6. Reglas de clasificación endurecidas
- IDENTIFICADO exige **F ≥ 10 al nivel del shock y F efectivo ≥ 10**, y conjunto AKM0 **acotado y convexo**; pretendencia A3 con p > 0,10; estabilidad al excluir los 3 orígenes de mayor peso de Rotemberg (mismo signo e intervalos solapados); **con nacionalidad, solo mismo signo e intervalos solapados**; t principal fuera del 95 % central de las permutaciones si se afirma un efecto; replicador-ciego con **diferencia relativa < 5 % o < 0,1 EE**; abogado-del-diablo «resiste» o «resiste con limitaciones».
- Techos: **P1-E4 (Borjas) y P3: ASOCIACIÓN** (sin instrumento creíble o con 17 unidades y respuesta de política); P5: SUGESTIVO.
- El wild cluster bootstrap por CCAA se aplica solo a la **forma reducida** (y sobre z), con p ≤ 0,05 estricto.

## A7. Medida
- Denominadores con la ECP (población 16-64), no con la EPA.
- Ceuta y Melilla fuera de la principal.
- La regularización de 2005 (efectiva tras el 1-1-2005) queda en el periodo A: se informa A por separado.

## A8. P3 y P5
- P3: resultado educativo = alumnos por profesor en la enseñanza pública no universitaria por CCAA (EDUCAbase, 2015-16 a 2024-25); listas de espera (SISLE, PDF por CCAA): se intenta su extracción; si no es fiable, NO ESTIMABLE con datos públicos en formato procesable. Techo ASOCIACIÓN.
- P5: shock de cada origen = inmigración en la UE-27 desde ese origen en 2021-2024 **excluido el propio país** (leave-one-country-out); cuotas NUTS2 del censo 2021 dentro de cada país; efectos fijos de país; se excluyen las celdas con bandera de baja fiabilidad de la EU-LFS; los flujos desde Ucrania se excluyen en una variante (protección temporal registrada de forma desigual). Techo SUGESTIVO.

## A9. Familias de corrección
Holm: {P1-H1, P1-H2}. BH por familias: P1 exploratorias (E1-E3, E6, con E3 contando sus 3 niveles educativos), P2 (E1, E2), P5. Rotemberg se calcula con columnas origen × periodo en el apilado.

## A10. Resultado del Monte Carlo de A5 (antes de fijar)
docs/montecarlo.md, sección «Adenda A5»: con shocks persistentes, AKM0 **sin agrupar** cubre 0,87-0,94 (NO APTO con ρ = 0,6) y **agrupando por origen entre periodos** cubre 0,96-0,97 con tamaño 0,03 (APTO). En consecuencia, la inferencia principal de A1 es **AKM0 agrupado por origen** (econ.akm0 con `grupos`). MC2E con dos endógenas (econ.iv2sls_k) cubre 0,94-0,95 con corr(z_p, z_p−1) de 0,5 y 0,8 (APTO).
