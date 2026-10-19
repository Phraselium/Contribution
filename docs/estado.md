# Estado del estudio M1

Leer docs/plan.md y este fichero al empezar o tras compactar.

## Fase en curso
Fase 2 · Datos públicos (descargas y normalización). Fase 1 cerrada; fase 0 cerrada.

## Hecho
- T0.1 docs/plan.md (mensaje completo) y CLAUDE.md con las reglas A.
- T0.2 Infraestructura B: Makefile (m1_f0…m1_f7, check, publicacion, web), comandos /m1-fase0…7 y /m1-estado, 11 subagentes adaptados de Econometr-a, guardas (.claude/hooks/guardas_m1.py) con tests, puerta prereg-m1 (src/m1/etiquetas.py), descargador con registro y checksum (src/m1/fuentes.py), política de fuentes no públicas (src/m1/politica_fuentes.py), verificador de referencias, cifras_clave y check.

- T0.3 docs/fuentes_publicas.md (qué permite cada fuente por origen, territorio y periodo) y lista de lo no público (sección 3; va a limitaciones). Decisiones D5-D7.
- F1 · 73 fichas en docs/literatura (fiscal 23, trabajo 26, vivienda 11, servicios 13): 57 VERIFICADA (Crossref/DataCite), 16 NO VERIFICADA (sin DOI o discrepancia de metadatos, D8). Tablas por pregunta en output/f1/. Réplicas: ningún estudio español con paquete público; la réplica con datos públicos va a P1 (D9).
- F2 (en curso) · Descargas con URL, licencia, fecha y sha256 (data/fuentes.csv): microdatos INE (EPA 2005-2026, ECV 2008-2025, EPF 2016-2025, EES 2010-2022), tablas INE (padrón 1998-2022 por país, ECP, migraciones, proyecciones, Censo 2021, salarios EPA), Eurostat (36 tablas EU-LFS, EU-SILC, censos 2011/2021, flujos, COFOG) y GISCO. Normalizados: padrón por provincia y grupo, ECV de personas 2009-2025. Crudos > 10 MB fuera de git con checksum (D10).

## Siguiente
- F2: EPA agregada en celdas; registros administrativos (subagente adquisidor); EPF y EES.
- Validación Monte Carlo de las herramientas (subagente montecarlo, en paralelo).

## Remoto
- El repositorio remoto lo crea el autor; hasta entonces los commits quedan en local (rama claude/m1-contribucion-origen).

## Subagentes y tokens por fase
| fase | subagentes | tokens aprox. |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 3 bibliotecario | ≈ 585.000 |
| 2 | 1 adquisidor-datos (en curso) | — |
| 5 (preparación) | 1 montecarlo (en curso) | — |
