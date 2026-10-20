# Estado del estudio M1

Leer docs/plan.md y este fichero al empezar o tras compactar.

## Situación (19-10-2026)
- Fases 0, 1, 2, 3, 4, 6 y 7: hechas en local (rama claude/m1-contribucion-origen). `make check` limpio.
- **Remoto:** https://github.com/Phraselium/Contribution (origin; la rama claude/m1-contribucion-origen está subida). La etiqueta prereg-m1 no se pudo subir (HTTP 403 del proxy): la puerta acepta la etiqueta local porque su commit c247555 está en origin/claude/m1-contribucion-origen; la orden para subirla está en docs/tareas_autor.md.
- **Fase 5: ejecutada** con `make m1_f5` (P1/P2 shift-share provincial, P1-E4 Borjas, P3 educación y sanidad, P5 NUTS2 UE-27). Primera etapa débil al nivel del shock (F = 6,6) y conjuntos AKM0 no acotados: todo ASOCIACIÓN o NO ESTIMABLE; la exploratoria P1-E3a (empleo de nativos con educación baja) rechaza el cero (BH p ≈ 0,008) con conjunto no acotado. Desviaciones de implementación en docs/desviaciones.md. Replicador-ciego y abogado-del-diablo no proceden (nada IDENTIFICADO ni SUGESTIVO).
- Paradas D atendidas: guarda que no se aplica a esta sesión (D5, el autor decidió seguir); signo fiscal dependiente de supuestos (D11, el autor decidió publicar solo intervalos).

## Hecho por fase
- **F0** · Infraestructura B (Makefile m1_f0…m1_f7, check, publicacion, web; /m1-fase0…7 y /m1-estado; 11 subagentes; guardas con 78 tests; puerta prereg-m1; descargador con política de fuentes no públicas). Inventario de lo público y de lo no público (docs/fuentes_publicas.md).
- **F1** · 73 fichas (57 VERIFICADA, 16 NO VERIFICADA); tablas por pregunta en output/f1/. Ningún estudio español con paquete de replicación público (D9).
- **F2** · Microdatos INE (EPA 86 trimestres, ECV, EPF, EES, ENSE), padrón y ECP, Eurostat (36 tablas + filtradas), GISCO y 598 ficheros administrativos (TGSS, SEPE, IMV, Educación, Sanidad). Catálogo íntegro con sha256. No accesibles: AEAT (TLS), pensiones por nacionalidad (certificado), SISLE solo en PDF.
- **F3** · Población, empleo (tres niveles, Oaxaca, contribución al crecimiento, provincias, cohortes, generaciones, Europa NUTS2), salarios (EES por establecimiento, DFL por deciles), vivienda (ECV y Eurostat; demanda de hogares C2), prestaciones (tres niveles).
- **F4** · Contabilidad fiscal estática 2022-2024 con 64 combinaciones de supuestos y bootstrap; ciclo vital por edad de llegada; pensiones con EUROPOP2023 (variante sin migración) frente al Ageing Report 2024.
- **F5** · Pre-registro, revisión del abogado del diablo, adenda, Monte Carlo; ejecutada tras subir la rama al remoto (ver Situación). Sensibilidades nuevas del ciclo vital: presupuesto equilibrado, imputación de tramos suprimidos de la UE, reglas de pensiones (output/f4/ciclo_vital_sensibilidad.csv).
- **F6** · 12 fichas (6 favorables, 6 desfavorables) con veredicto.
- **F7** · Documento generado (publicacion/documento_m1/), versión web, figuras y mapas por provincia y NUTS2, tablas_m1.xlsx con la convención de colores. Revisión del verificador de cifras (19 puntos) y del árbitro (veredicto REVISAR, 15 hallazgos) incorporada: ciclo vital rehecho (D14), veredictos armonizados (D15: balance 1/5/0 desfavorables y 0/4/2 favorables), presupuesto equilibrado y diferencia con nativos, D11 aplicado a todos los grupos, edad −1 de la ECV corregida. Segunda ronda del árbitro: no lanzada.

## Subagentes y tokens por fase
| fase | subagentes | tokens aprox. |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 3 bibliotecario | ≈ 585.000 |
| 2 | 1 adquisidor-datos | ≈ 330.000 |
| 5 (preparación) | 1 montecarlo, 1 abogado-del-diablo | ≈ 260.000 |
| 7 | 2 arbitro-final, 1 verificador-cifras | ≈ 462.000 |
Ninguna fase supera 6 millones de tokens.

## Siguiente
1. El autor sube la etiqueta prereg-m1 (docs/tareas_autor.md).
2. Opcional: tercera ronda del árbitro tras las correcciones de la segunda.

## Segunda ronda del árbitro (REVISAR) incorporada
Conjuntos AKM0 como unión de intervalos; P1-E6 añadida y BH con seis; batería y multiverso para todas las hipótesis; separabilidad JRS por periodo (no separable); P1-E3a con variante por nacionalidad (conjunto acotado y negativo) y permutación; multiverso en el texto (signo desfavorable sistemático, sin significación); D11 en la comparación con Fiorio; variante de mitad de salidas del ciclo vital; neutralidad de A2, A3 y F3; P5 con IC orientativo y heterogeneidad publicada; desviaciones 7-11 declaradas como posteriores a ver estimaciones.

## Cierre autónomo · Ronda 1 de autocrítica (docs/rondas/ronda_1.md)
Cuatro revisores (≈ 630.000 tokens): árbitro REVISAR, 18 discrepancias de cifras. Errores corregidos: control de cuotas incompletas de P1 mal construido (al corregirlo, F del shock 13,5; P1-H1 +0,06 y P1-H2 −0,55, sin significación; P1-E3a −0,61 deja de rechazar tras BH), descomposición de P1-E3a, permutaciones no centradas, intervalo del ciclo vital con convergencia (el resto del mundo queda negativo a los 20 y 50 años), umbral ENSE, edad −1, quintiles. Robustez: wild bootstrap por CCAA, Rotemberg, nivel «edad y sexo» fiscal (a igual edad los nacidos fuera aportan menos que los nativos) y de empleo. Exploratorio: jackknife por CCAA.

## Ronda 2 de autocrítica (docs/rondas/ronda_2.md)
Árbitro REVISAR («tras corregir, aceptable»); abogados «resiste con limitaciones»; 11 discrepancias de cifras sin errores de valor. Errores: sensibilidades del control anunciadas y no estimadas (ahora publicadas las tres: la principal es la menos desfavorable), D11 en el nivel «edad y sexo», F2 y F1 desactualizadas, quintiles EPF, comparación de pensiones. Robustez: señales para las diez hipótesis (también favorables: P1-H2 y P1-E3c fuera del 95 % de permutaciones), Rotemberg, apalancamiento (42 %), variante conjunta del ciclo vital (UE −6 a los 30). P1-E3a: en parte composición por edad (−0,30 estandarizada) y dependiente de la Comunitat Valenciana (−0,19 sin ella). Tokens ≈ 650.000 (acumulado ≈ 1,3 M).

## Ronda 3 de autocrítica (docs/rondas/ronda_3.md)
Árbitro REVISAR (menores). Dos errores de cálculo con cambio de conclusión, publicados tal como salen: (1) el ciclo vital omitía los ingresos no tributarios por persona: las llegadas de 20 a 50 años pasan a depender de supuestos, pero frente a un nativo de la misma edad quienes llegan de fuera de la UE a los 20-30 años aportan menos en todas las combinaciones; (2) la estandarización por edad excluía las edades en que los nacidos fuera salen mejor: a igual edad y sexo la ventaja del resto de la UE es positiva pero no distinguible de cero y la del resto del mundo depende de supuestos. F4 pasa a «engañosa». P1-E3a estandarizada por edad (−0,30) pierde sus señales. Tokens ≈ 710.000 (acumulado ≈ 2,0 M).

## Ronda 4 de autocrítica (última; docs/rondas/ronda_4.md)
Árbitro REVISAR («cambios menores en extensión»), abogados «resiste con limitaciones», 11 discrepancias de cifras sin errores de valor. Corregido: diferencia del ciclo vital a los 50 años (favorable para el resto de la UE) y bienes públicos del comparador nativo; estandarización por tramos de 5 años (la ventaja del resto de la UE a igual edad baja a +239 €, no distinguible de cero); resumen no técnico coherente con F4; Fiorio en los dos sentidos. Se alcanzan las 4 rondas; los abiertos están en ronda_4.md. Tokens ≈ 635.000 (acumulado ≈ 2,65 M).

## Cierre (sección C)
Revisión final de coherencia (10 incoherencias, una grave en tablas_m1.xlsx: ocupados de todas las edades junto a la población 16-64) corregida; docs/mejoras_futuras.md y docs/autoevaluacion.md escritos; publicación y web regeneradas; make check limpio. Tokens de subagentes desde el inicio del cierre ≈ 2,8 millones (por debajo del límite de 6). Pendiente del autor: subir la etiqueta prereg-m1 (docs/tareas_autor.md) y una revisión externa.

## Verificación a posteriori tras el cierre (20-10-2026)
Encargo de 12 puntos sin bucles de autocrítica; todo rotulado «a posteriori» (desviación 25). Cuadre contable en `make check` (tests/test_cuadre_fiscal.py): fallaban (a) y (b) por 1.735 M€ (D62 sanitario omitido) y (c) para el resto de la UE (−20 % de la neta total): corregidos; 86 cifras cambian, en decenas de euros (docs/cuadre.md). Orden de la fase 4 corregido en fase.py. Fase 5: F efectivo 17,9 < 23,1 (se retira «fuerte»); EMD, Anderson-Rubin, curva de especificaciones y quitar una comunidad (anexo G). Ciclo vital: con cuatro escenarios de convergencia (incluido uno divergente, pedido por el árbitro en la ronda 5) ninguna diferencia con los nativos conserva el signo. Convenciones fiscales, cruce nacimiento × nacionalidad, empleo por provincia y grupo, κ de pensiones, comparación externa (anexo H), inventario (docs/inventario_entregas.md), brief (docs/brief_revisores.md), ronda 5 (docs/rondas/ronda_5_verificacion.md). Etiqueta: c247555 (docs/tareas_autor.md); no se crea ni se empuja.
