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
| 7 | 1 arbitro-final, 1 verificador-cifras | ≈ 328.000 |
Ninguna fase supera 6 millones de tokens.

## Siguiente
1. Segunda ronda del árbitro sobre el documento con la fase 5.
2. El autor sube la etiqueta prereg-m1 (docs/tareas_autor.md).
