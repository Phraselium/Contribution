# Estado del estudio M1

Leer docs/plan.md y este fichero al empezar o tras compactar.

## Situación (19-10-2026)
- Fases 0, 1, 2, 3, 4, 6 y 7: hechas en local (rama claude/m1-contribucion-origen). `make check` limpio.
- **Fase 5: pre-registrada y programada, NO ejecutada.** La etiqueta local prereg-m1 fija docs/preregistro.md y su adenda; la puerta exige que su commit esté en una rama remota. No hay remoto: el autor decidió no crearlo todavía y esta sesión no puede crear repositorios (HTTP 403). Para ejecutarla: subir la rama y la etiqueta a un remoto y lanzar `make m1_f5` (src/m1/f5_p1_shiftshare.py; P1-E4, P3 y P5 quedan por programar según la adenda).
- Paradas D atendidas: guarda que no se aplica a esta sesión (D5, el autor decidió seguir); signo fiscal dependiente de supuestos (D11, el autor decidió publicar solo intervalos).

## Hecho por fase
- **F0** · Infraestructura B (Makefile m1_f0…m1_f7, check, publicacion, web; /m1-fase0…7 y /m1-estado; 11 subagentes; guardas con 78 tests; puerta prereg-m1; descargador con política de fuentes no públicas). Inventario de lo público y de lo no público (docs/fuentes_publicas.md).
- **F1** · 73 fichas (57 VERIFICADA, 16 NO VERIFICADA); tablas por pregunta en output/f1/. Ningún estudio español con paquete de replicación público (D9).
- **F2** · Microdatos INE (EPA 86 trimestres, ECV, EPF, EES, ENSE), padrón y ECP, Eurostat (36 tablas + filtradas), GISCO y 598 ficheros administrativos (TGSS, SEPE, IMV, Educación, Sanidad). Catálogo íntegro con sha256. No accesibles: AEAT (TLS), pensiones por nacionalidad (certificado), SISLE solo en PDF.
- **F3** · Población, empleo (tres niveles, Oaxaca, contribución al crecimiento, provincias, cohortes, generaciones, Europa NUTS2), salarios (EES por establecimiento, DFL por deciles), vivienda (ECV y Eurostat; demanda de hogares C2), prestaciones (tres niveles).
- **F4** · Contabilidad fiscal estática 2022-2024 con 64 combinaciones de supuestos y bootstrap; ciclo vital por edad de llegada; pensiones con EUROPOP2023 (variante sin migración) frente al Ageing Report 2024.
- **F5** · Pre-registro, revisión del abogado del diablo («resiste con limitaciones»), adenda, Monte Carlo (AKM0 agrupado APTO; MC2E con dos endógenas APTO; Wald BHJ y Conley NO APTO), datos de apoyo (ECP 15-64, afiliación 1999-2003), código de P1/P2. Sin estimaciones.
- **F6** · 12 fichas (6 favorables, 6 desfavorables) con veredicto.
- **F7** · Documento generado (publicacion/documento_m1/), versión web, figuras y mapas por provincia y NUTS2, tablas_m1.xlsx con la convención de colores. Revisión del árbitro y del verificador de cifras: en curso.

## Subagentes y tokens por fase
| fase | subagentes | tokens aprox. |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 3 bibliotecario | ≈ 585.000 |
| 2 | 1 adquisidor-datos | ≈ 330.000 |
| 5 (preparación) | 1 montecarlo, 1 abogado-del-diablo | ≈ 260.000 |
| 7 | 1 arbitro-final, 1 verificador-cifras | en curso |
Ninguna fase supera 6 millones de tokens.

## Siguiente
1. Incorporar la revisión del árbitro y del verificador.
2. Cuando exista el remoto: push de la rama y de prereg-m1; `make m1_f5`; replicador-ciego y abogado-del-diablo para lo que quede IDENTIFICADO o SUGESTIVO; regenerar F6-F7.
