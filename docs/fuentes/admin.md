# Ficha de fuentes · Registros administrativos de España (familia `admin`)

Fase 2 de M1. Estadísticas públicas agregadas de registros administrativos (no microdatos). Descarga reproducible con
`python3 src/m1/f2_admin_descarga.py [ss|ss_hist|sepe|imv|edu|san|todo]`, que llama a `fuentes.descargar(...)`. Cada fichero
queda en `data/raw/admin/` con su URL exacta, licencia, edición, fecha de descarga (2026-10-19) y sha256 en
`data/fuentes.csv` (filtrar `familia == admin`) y `data/CHECKSUMS.sha256`. Los crudos no se transforman.

Versionado: todos los ficheros de datos están versionados (ninguno supera 50 MB; el mayor, 16 MB). Excepción deliberada:
los **documentos de referencia en PDF** (Ageing Report 2024 IP279 e IP257, ficha de España del Ageing Report, Ley 22/2009
del BOE y el artículo de Gaceta Sanitaria 2013) quedan en `data/raw/admin/grandes/` (ignorado por git) con URL y checksum,
porque CLAUDE.md prohíbe versionar PDFs de referencias. Los PDF de SISLE sí se versionan: son la única forma en que el
Ministerio publica los datos por CCAA.

Formato máquina: PC-Axis (`.px`) en Seguridad Social (PX-Web de la TGSS) y Educación (EDUCAbase); Excel en SEPE, IMV,
pensionistas, histórico de afiliación y «Las cifras de la educación»; PDF o HTML solo cuando no hay otro formato (SISLE,
«Sanidad en datos»).

Regla general de origen: **todas estas fuentes clasifican por nacionalidad, nunca por país de nacimiento**. Los
nacionalizados cuentan como españoles; la doble nacionalidad con la española, como española. Por tanto, en M1 sirven como
sensibilidad (nacionalidad) y como denominadores o controles, no para el criterio principal (país de nacimiento). Ninguna
permite separar segunda generación ni años de residencia.

---

## 1. Seguridad Social (TGSS, INSS)

Licencia (todas): «La información disponible en este sitio web, salvo indicación expresa en contrario, es susceptible de
reutilización; quedando autorizada su reproducción total o parcial, modificación, distribución y comunicación, para usos
comerciales y no comerciales», con obligación de citar la fuente y la fecha de última actualización y sin desnaturalizar
el contenido. Aviso legal: https://www.seg-social.es/wps/portal/wss/internet/AvisoLegal

### 1.1 Base estadística PX-Web de la TGSS (afiliación y bases de cotización), 2012-2026

URL base: `https://w6.seg-social.es/PXWeb/Resources/PX/Databases/<base>/<carpeta>/<tabla>.px` (ficheros PC-Axis
completos, descarga directa; interfaz de consulta en https://w6.seg-social.es/PXWeb). Edición: la publicada a
2026-10-19 (periodo y fecha de actualización de cada tabla en la columna `edicion` de `data/fuentes.csv`). Ficheros
`ss_px_*` (23).

| Fichero (prefijo) | Contenido | Origen | Territorio | Periodo |
|---|---|---|---|---|
| `ss_px_ext_1m` | afiliados medios, total sistema, por **país de nacionalidad** (≈200 países + España, apátridas, no consta), sexo y edad (<35, 35-54, >54) | país | España | mensual 2012-01 a 2026-09 |
| `ss_px_ext_2m` | ídem por país, régimen (RG, SE agrario, SE hogar, RETA, mar, carbón) y sexo | país | España | 2012-01 a 2026-09 |
| `ss_px_ext_3m`, `3mb` | afiliados medios **extranjeros** por provincia (CCAA), régimen, sexo y UE / no UE | UE / no UE | provincia, CCAA | 2012-01 a 2026-09 |
| `ss_px_ext_5m09`, `5m25` | extranjeros por RG y RETA, provincia, sección CNAE-2009 (hasta 2025-12) y CNAE-2025 (desde 2026-01), UE / no UE | UE / no UE | provincia | 2012-2025 y 2026 |
| `ss_px_01m`, `03m`, `03mb`, `11m` | afiliados medios **totales** por sexo, edad y régimen; por provincia y régimen; por provincia, edad quinquenal y sexo | — (total) | provincia | 2012-01 a 2026-09 |
| `ss_px_04m09`, `04m25` | afiliados medios totales por provincia, sección CNAE y RG/RETA | — | provincia | 2012-2026 |
| `ss_px_10f` | afiliados último día por edad simple, sexo, régimen y **españoles / extranjeros** | española / extranjera | España | mensual 2014-01 a 2026-09 |
| `ss_px_bases_01`…`06` | **cotizantes y base media de cotización** del Régimen General por sexo y edad, contrato y jornada, actividad (sección y 2 dígitos), provincia, CCAA, grupo de cotización | — | provincia, CCAA | mensual 2018-01 a 2026-03 |
| `ss_px_bases_07` | cotizantes y base media del RG por **nacionalidad** (total extranjeros y 36 países: UE, Marruecos, China, Ucrania, Colombia, Ecuador, Perú, Venezuela, Bolivia, Argentina…, resto) y sexo | país (principales) | España | 2018-01 a 2026-03 |

Españoles = total − extranjeros (por provincia con `03m` − `ext_3m`; nacional por edad con `10f`). En bases de cotización
no hay fila de españoles ni desglose provincial por nacionalidad: la base media de los españoles se obtiene por diferencia
ponderada entre `bases_05` (total nacional) y `bases_07` (total extranjeros). Solo Régimen General (sin RETA, que cotiza
por base elegida).

Limitaciones: afiliaciones (situaciones), no personas (un pluriempleado cuenta varias veces); nacionalidad, no
nacimiento; el país con <1 000 afiliados aparece igualmente (no hay supresión: agregado administrativo, sin riesgo
muestral); cambio CNAE-2009 → CNAE-2025 en 2026-01 (dos tablas); bases de cotización topadas (máximo y mínimo legales), no
salario.

### 1.2 Histórico de estadísticas de afiliación publicadas (Excel mensuales), 1999-2011

URL: páginas bajo https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8/EST167
(bloques 1999-2003, 2004-2005, 2006-2008, 2009-2020); cada Excel en `https://www.seg-social.es/wps/wcm/connect/wss/<id>/<fichero>?MOD=AJPERES`.
El script recorre las páginas y selecciona. Ficheros `ss_hist_<año>_<clase>_*` (ver resumen al final).

- `ext_prov`: afiliados **extranjeros** por CCAA y provincia, régimen y sexo. Último día del mes 2006-2008; media mensual
  2009-2011 (desde 2012 la serie sigue en el PX-Web, 1.1).
- `ext_nac`: afiliados extranjeros por **nacionalidad** (países principales) y régimen; mismas fechas.
- `tot_prov_ud` (1999-2003, último día) y `tot_prov_med` (2004-2011, media mensual y media anual): afiliados totales por
  régimen y provincia, para calcular españoles por diferencia.

Limitaciones: antes de 2006 las estadísticas publicadas de la Seguridad Social **no** desagregan extranjeros por
provincia (no hay extranjeros en los libros de 1999-2005); para 2001-2005 no hay serie provincial pública de afiliados
extranjeros en esta fuente (alternativa: padrón y EPA). Mezcla de último día (2006-2008) y media mensual (2009-): no son
comparables sin ajuste. Formatos `.xls` antiguos con estructuras de hoja cambiantes entre años.

### 1.3 Pensionistas (INSS)

`ss_pensionistas_PTAS202609.xlsx`: https://www.seg-social.es/wps/wcm/connect/wss/f56092d1-579a-458c-90ad-be7fcceb9abe/PTAS202609.xlsx?MOD=AJPERES
(página EST23 > Pensionistas). Pensionistas a 1-9-2026 por CCAA y provincia, sexo, edad (<65, ≥65), mínimos,
pluripensionistas, tramos de cuantía; serie de pensiones por pensionista 2006-2026. **Sin nacionalidad.**

**Pensiones o pensionistas por nacionalidad: no publicado en abierto.** La única vía sería eSTADISS en la sede
electrónica (sede.seg-social.gob.es), bloqueada por la política de fuentes de M1 (exige certificado o Cl@ve). Queda NO
ESTIMABLE con dato directo; se imputarán con perfiles por edad y la ECV (docs/fuentes_publicas.md, §3).

### 1.4 Ingreso Mínimo Vital (INSS)

Página: https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/cbe2fda1-3ac7-4bc8-a5ec-06c178839e11

- `imv_dossier_202412.xlsx`, `imv_dossier_202512.xlsx`, `imv_dossier_202609.xlsx`: «Dossier comunidad autónoma y
  provincia», nómina de diciembre de 2024 y 2025 y septiembre de 2026 (último publicado). La tabla 1.5 da **titulares por
  sexo y nacionalidad (española / extranjera) por CCAA y provincia** (sep-2026: 905 792 titulares, 157 289 de nacionalidad
  extranjera). Otras tablas: hogares, beneficiarios, cuantías, composición del hogar, altas.
- `imv_nomina_*.xlsx` (mismos meses): prestaciones, beneficiarios e importes por CCAA y provincia, sin nacionalidad.

Limitaciones: nacionalidad del **titular**, no de los beneficiarios del hogar; solo española/extranjera (sin país); el
dosier con nacionalidad solo se publica desde 2024 (no hay serie 2020-2023 por nacionalidad en abierto); se tomó el último
mes de cada año (el script puede ampliarse a todos los meses).

## 2. SEPE (paro registrado, contratos, prestaciones)

Licencia: reutilización conforme a la Ley 37/2007 y al RD 1495/2011, con las condiciones generales de datos.gob.es
(usos comerciales y no comerciales, citar la fuente, no desnaturalizar). Aviso legal:
https://www.sepe.es/HomeSepe/mas-informacion-contacto/aviso-legal.html y https://datos.gob.es/es/aviso-legal

- **Resumen mensual «Avance»** `sepe_avance_AAAAMM.xls`, de
  `https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/estadisticas/datos_avance/datos/datos_AAAA/Av_sispe_AAMM.xls`
  (índice: https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/datos-avance/datos.html): diciembre de 2005 a 2025 y
  enero-septiembre de 2026 (30 ficheros). En las ediciones con desglose (2007-2008 y 2010-2026; las de 2005, 2006 y 2009
  son un resumen de una hoja sin extranjeros): **paro registrado de extranjeros** por sexo, edad y sector, con series, y por
  **provincia y CCAA**; **contratos a extranjeros** por sexo, edad, sector, **zona de origen (comunitario /
  extracomunitario)** y CCAA; **beneficiarios de prestaciones por desempleo extranjeros** por tipo de prestación, provincia
  y CCAA (comunitarios / no comunitarios) y los 60 países con más beneficiarios (desde 2012 al menos). Las prestaciones
  van con un mes de retraso (ej.: el de 2026-09 trae agosto).
- **Contratos acumulados anuales** `sepe_contratos_acum_AAAA12.xls` (2006-2025), de
  `.../estadisticas/datos_estadisticos/contratos/datos/AAAA/diciembre_AAAA/ESTADISTICA_DE_CONTRATOS_ACUM.xls`: contratos
  del año a **extranjeros por provincia** (comunitarios / extracomunitarios, tipo de contrato, sexo, edad y sector). Las
  tablas de extranjeros están en 2007 y 2009-2025 (no en los ficheros de 2006 y 2008, que la página enlaza con otro
  contenido).
- `sepe_paroprovsector.xls` (paro total y de extranjeros por sector y provincia, último mes: sep-2026),
  `sepe_evolparoseries2001.xls` (2001-2016) y `sepe_evolparoseries.xls` (2017-2026): series mensuales nacionales de paro;
  `sepe_evolprovsectores.xls`: evolución por provincia y sector.

Desagregación por origen: solo español/extranjero y comunitario/extracomunitario; país solo en el ranking de
beneficiarios de prestaciones. **Paro registrado por país o continente por provincia: no encontrado en descarga
abierta** (el «Informe del Mercado de Trabajo de los Extranjeros» del Observatorio de las Ocupaciones da países a escala
estatal en PDF; no se ha descargado). Limitaciones: paro registrado ≠ paro EPA (depende de la inscripción, que difiere por
origen); stock a fin de mes; se tomó diciembre (no medias anuales) salvo 2026 (ampliable a todos los meses en el script).

## 3. AEAT · «Mercado de Trabajo y Pensiones en las Fuentes Tributarias» — NO DESCARGADO

La estadística (modelo 190; salario medio por provincia y por nacionalidad española/extranjera desde 2008) se publica
hoy en `sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/mercado/<año>/...`.
- Ese dominio está **bloqueado por la política de fuentes de M1** (`src/m1/politica_fuentes.py`: «sede de la AEAT: exige
  identificación»), aunque las páginas de estadísticas en sí parecen consultables sin identificarse.
- La ruta pública indicada (`www.agenciatributaria.es/.../sites/mercado/...`) **no es accesible desde este entorno**: el
  servidor presenta una cadena de certificados con una CA firmada con un algoritmo de resumen débil y la verificación TLS
  falla («CA signature digest algorithm too weak»); por HTTP plano responde 503. No se ha desactivado la verificación.
Pregunta afectada: salario medio por nacionalidad y provincia de fuente tributaria (C1 con dos fuentes junto a la EES).
Tratamiento: queda pendiente de una decisión del autor sobre la política (permitir las páginas estadísticas de la sede,
que no piden identificación) o de un entorno con otra cadena de certificados; mientras, salarios por nacionalidad con la
EES (microdatos) y las bases de cotización por nacionalidad (1.1).

## 4. Ministerio de Educación, FP y Deportes (EDUCAbase y publicaciones)

Licencia: «Se autoriza la reproducción total o parcial de los textos proporcionados por el portal, siempre que se mantenga
su integridad y que se cite expresamente al Ministerio de Educación, Formación Profesional y Deportes como fuente de la
información»; las estadísticas se ofrecen además en datos.gob.es bajo las condiciones generales de reutilización. Aviso
legal: https://www.educacionfpydeportes.gob.es/comunes/aviso-legal.html. Nota: el aviso añade que «para el resto de
contenidos» el uso se limita a la descarga y uso privado; las tablas estadísticas se tratan como información del sector
público reutilizable (Ley 37/2007), lo que conviene confirmar antes de redistribuir los crudos fuera del repositorio.

Ficheros PC-Axis: `https://estadisticas.educacion.gob.es/EducaJaxiPx/files/_px/es/px/<ruta>/<tabla>.px` (menús en
`https://estadisticas.educacion.gob.es/EducaDynPx/educabase/index.htm?type=pcaxis&path=<ruta>&file=pcaxis&l=s0`).

| Ficheros | Contenido | Origen | Territorio | Periodo |
|---|---|---|---|---|
| `edu_series_extran_extran_01`…`14` | alumnado extranjero por titularidad (pública/privada), CCAA y curso; por enseñanza (Infantil 1.º y 2.º ciclo, Primaria, Especial, ESO, Bachillerato, FP, Régimen Especial); % de extranjeros en el alumnado y en centros públicos | extranjero | CCAA | 1994-95 a 2025-26 (avance) |
| `edu_series_extran_extran_15`…`23` | alumnado extranjero por **área de nacionalidad** (UE, resto de Europa, África, América del Norte, Central, del Sur, Asia, Oceanía, no definido), sexo y CCAA | área (continente) | CCAA | 1994-95 a 2025-26 |
| `edu_series_alumnado_alumnado_1_01`, `1_02` | alumnado total de Régimen General por titularidad, sexo y CCAA (denominador) | — | CCAA | 1990-91 a 2025-26 |
| `edu_2024-25_extran_extran_01`…`03` | resultados detallados 2024-25: extranjeros por enseñanza, titularidad/financiación (concertada) y **provincia**; por provincia y área de nacionalidad; por **país de nacionalidad** (146) y enseñanza | país (nacional), área (provincia) | provincia | 2024-25 |
| `edu_2025-26da_extran_*` (6) | datos de avance 2025-26 por CCAA/provincia, área y país | área/país | provincia | 2025-26 |
| `edu_AAAA-AA_alumnos_grupo_*` | número medio de alumnos por unidad/grupo por titularidad/financiación, CCAA/provincia y enseñanza | — | provincia | 2016-17 a 2024-25 (2015-16 no localizado con el mismo título) |
| `edu_AAAA-AA_alumnos_profesor_resumen02/03` | alumnos por profesor (equivalente a tiempo completo y en valores absolutos) por titularidad, CCAA y tipo de centro | — | CCAA | 2015-16 a 2024-25 |
| `edu_AAAA-AA_profesorado_reggen_1_01` | profesorado por titularidad, CCAA/provincia, sexo y tipo de centro | — | provincia | 2021-22 a 2024-25 |
| `edu_gasto_series_series_01`…`14` | Estadística del Gasto Público en Educación: gasto por administración, actividad (no universitaria, universitaria…), naturaleza económica, becas, conciertos; en % del PIB y del gasto público | — | España / administraciones | 1992-2024 |
| `edu_gasto_2024_gasto01`…`08` | gasto 2024 por actividad, administración (Consejerías de cada CCAA) y naturaleza económica; corporaciones locales por CCAA; transferencias a centros privados | — | CCAA (por administración financiadora) | 2024 |
| `edu_cifras_2023-24_*.xlsx` (32) y `edu_cifras_AAAA-AA_b4.*` (ediciones anteriores) | «Las cifras de la educación en España», URL `https://www.educacionfpydeportes.gob.es/dam/jcr:<id>/<tabla>.xlsx`; **B4.6: gasto público por alumno en enseñanza no universitaria por CCAA** (público+concertado y solo público; 2023: 6 851 € y 7 943 € de media nacional); E5: alumnado extranjero; B1, B3: centros y profesorado | extranjero (E5) | CCAA | edición 2026 (curso 2023-24, gasto 2023); B4 de ediciones previas |

Limitaciones: nacionalidad, no nacimiento (hijos de inmigrantes nacidos en España con nacionalidad española no figuran
como extranjeros; doble nacionalidad = española); no hay gasto por alumno según origen (se imputa el gasto medio por
alumno y nivel a cada grupo: C2); ratios por grupo y profesor no distinguen origen del alumnado (contexto de congestión
agregada, P3); los títulos y la numeración de tablas cambian entre cursos (el script selecciona por título).

## 5. Ministerio de Sanidad y perfiles de gasto sanitario por edad

Licencia Sanidad: «La información disponible en este sitio web, salvo indicación expresa en contrario, es susceptible de
reutilización; quedando autorizada su reproducción total o parcial, modificación, distribución y comunicación, para usos
comerciales y no comerciales», citando fuente y fecha de actualización. Aviso legal:
https://www.sanidad.gob.es/avisoLegal/home.htm

- **Listas de espera SISLE-SNS** (`san_sisle_*.pdf`, 64 ficheros): de
  https://www.sanidad.gob.es/estadEstudios/estadisticas/inforRecopilaciones/listaEspera.htm, `ListaEsperaInfAntCCAA.htm` y
  `listaEsperaInfAnt.htm` (`.../inforRecopilaciones/docs/<fichero>.pdf`). Datos por CCAA (`Datos_ccaa_*`,
  `Datos_por_comunidades_*`, `LE_PUBLICACION_DIC16_CCAA`): todos los cortes semestrales publicados, dic-2012 a dic-2025
  (dic-2025 rectificado; faltan jun-2013, jun-2014 y jun-2015, que no se publicaron por CCAA). Informes SNS
  (`LISTAS_PUBLICACION_*`, `ListaEspera*_CISNS`, `listaJunio08CI`…): cortes nacionales 2006-2025. Indicadores:
  pacientes en espera estructural, tasa por 1 000 habitantes, tiempo medio, % > 6 meses, por especialidad quirúrgica y
  consultas externas. Formato **solo PDF** (no hay tabla máquina pública: INCLASNS exige clave de API, que se concede a
  solicitud, y su exportación se envía por correo → no público en formato máquina). Limitación: 17 CCAA (pocos clusters);
  cambios de criterio (RD 1039/2011, rectificación de dic-2025).
- **Profesionales del SNS por CCAA** (`san_sanidad_en_datos_tabla13.htm` medicina, `tabla14.htm` enfermería): tablas HTML
  de «Sanidad en datos» (https://www.sanidad.gob.es/estadEstudios/sanidadDatos/tablas/tabla13.htm y tabla14.htm), último
  año publicado (2024/2025), por CCAA y ámbito (equipos de AP, otros AP, hospitales, urgencias 112/061, residentes). Las
  series del SIAP solo están en el Portal Estadístico interactivo (pestadistico.inteligenciadegestion.sanidad.gob.es), sin
  fichero descargable directo: no descargadas.
- **Perfil de gasto sanitario por edad y sexo para España**:
  - Comisión Europea, *2024 Ageing Report* (licencia CE, Decisión 2011/833/UE, reutilización citando la fuente,
    https://commission.europa.eu/legal-notice_en). Datos versionados: `ar2024_anexo_tablas_horizontales.xlsx` y
    `ar2024_anexo_fichas_pais.xlsx` (anexo estadístico: gasto sanitario público proyectado en % del PIB por país,
    escenarios). Referencias (no versionadas, en `grandes/`): `ar2024_ip279_informe.pdf` (gráfico I.2.2: perfiles
    edad-coste del gasto sanitario público por sexo, **solo agregados UE14/NMS/UE**), `ar2024_ip257_metodologia.pdf`,
    `ar2024_ficha_espana.pdf`. **El perfil edad-coste de España que España envía al AWG no se publica como dato**: el
    Ageing Report solo muestra agregados.
  - BOE, Ley 22/2009 (`boe_ley_22_2009_financiacion_ccaa.pdf`, en `grandes/`;
    https://www.boe.es/boe/dias/2009/12/19/pdfs/BOE-A-2009-20375.pdf; licencia BOE, https://www.boe.es/informacion/aviso_legal/):
    la «población protegida equivalente» pondera el gasto sanitario por **siete grupos de edad** (art. 9 y anexo): perfil
    oficial y normativo, sin sexo.
  - Blanco Moreno, Urbanos Garrido y Thuissard Vasallo (2013), «Evolución de la prestación real media en España por edad
    y sexo (1998-2008)», *Gac Sanit* 27(3):220-225 (`gs2013_blanco_urbanos_thuissard_prestacion_edad_sexo.pdf`, en
    `grandes/`; https://gacetasanitaria.org/es-download-pdf-S0213911112002701; acceso abierto, uso no comercial citando a
    los autores; DOI 10.1016/j.gaceta.2012.09.003, por verificar en Crossref): perfiles por edad quinquenal y sexo
    elaborados con datos del Ministerio de Sanidad (los usados por España en el AWG), 1998, 2003 y 2008.
  Tratamiento: perfil principal con la estructura por edad y sexo de Blanco Moreno et al. (escalado al gasto sanitario
  público actual, EGSP) y sensibilidad con las ponderaciones de la Ley 22/2009 y con el perfil UE14 del Ageing Report (C2).

## 6. Lo que no se ha podido descargar y por qué

| Dato | Motivo | Pregunta afectada |
|---|---|---|
| AEAT, salarios por nacionalidad y provincia (Mercado de Trabajo y Pensiones en las Fuentes Tributarias) | dominio sede bloqueado por la política de M1; www.agenciatributaria.es falla la verificación TLS en este entorno | salario por nacionalidad de fuente tributaria |
| Pensiones / pensionistas por nacionalidad | solo en eSTADISS (sede con certificado) → no público | pensiones de extranjeros |
| Afiliados extranjeros por provincia 1999-2005 | no publicados en las estadísticas abiertas de la Seguridad Social | serie larga de afiliación por origen |
| Paro registrado por país/continente y provincia | no hay tabla abierta (solo comunitario/extracomunitario) | paro por grupo de origen fino |
| IMV por nacionalidad antes de 2024; por país | no publicado | uso del IMV por origen |
| Listas de espera y profesionales en formato máquina | INCLASNS con clave de API a solicitud; Portal Estadístico interactivo | P3 (congestión) |
| Perfil edad-coste sanitario de España del AWG | no publicado (solo agregados UE) | imputación del gasto sanitario |

## 7. Recuento de ficheros y checksums

598 ficheros (593 versionados, 194 MB; 5 PDF de referencia en `grandes/`). URL, edición y sha256 de cada uno en
`data/fuentes.csv` (`familia == admin`) y `data/CHECKSUMS.sha256`; `python3 src/m1/fuentes.py` comprueba la integridad.

| Grupo (prefijo) | Ficheros | MB |
|---|---|---|
| `ss_px_*` (TGSS PX-Web) | 23 | 58,8 |
| `ss_hist_*` (afiliación 1999-2011: `tot_prov` 1999-2011, `ext_prov` y `ext_nac` 2006-2011, 12-13 por año y clase) | 306 | 11,7 |
| `ss_pensionistas_*` | 1 | 0,1 |
| `imv_*` | 6 | 1,6 |
| `sepe_*` | 54 | 40,4 |
| `edu_*` (EDUCAbase y Cifras; B4 de las ediciones 2008-09 y 2010-11 a 2023-24; la de 2009-10 no publica B4 en xlsx) | 141 | 7,9 |
| `san_sisle_*`, `san_sanidad_en_datos_*` | 66 | 46,2 |
| `ar2024_*` (2 xlsx versionados; 3 PDF en `grandes/`) | 5 | 32,9 |
| `boe_*`, `gs2013_*` (en `grandes/`) | 2 | 1,7 |

sha256 de ficheros clave:

| Fichero | sha256 |
|---|---|
| `ss_px_ext_2m` (afiliados medios por país y régimen) | 56628f4419d168013f5bfb55eb91052cbdc16e732b76cbba344156edcbb97dc3 |
| `ss_px_ext_3m` (extranjeros por provincia, UE/no UE) | e1110b92a2cf67ca9ac01c2da2b820b5a0d3ec3423da944c21b34d6cd9c46a35 |
| `ss_px_10f` (españoles/extranjeros por edad) | 523a0969e43a5bc37f8e2e3af25590bdf25663153b259cea3ccb9e8f591e909c |
| `ss_px_bases_07` (bases medias por nacionalidad) | 2d5dbd5fa17f62ca40dc920f45543158ae31fcfd42f0a9b2992155c8611e2032 |
| `imv_dossier_202609.xlsx` | aa3f4049df9504f97b782c6796c34a805e91e43a6b00012ae0b0ced01eded164 |
| `sepe_avance_202609.xls` | 3893a644db3e62e9a2c9a692998d71f02e955f810b430a555d7a2ab29c10c10c |
| `sepe_contratos_acum_202512.xls` | 649cbe2d2f9becaaeb084fa4b8f654c6ce6a75614e90f7405b2f0f56d6bce000 |
| `edu_series_extran_extran_01.px` | 4029643c633ab9674572043f1254e2dd1ec9dd9f663124439428f15ce3a6de57 |
| `edu_cifras_2023-24_b4.xlsx` (gasto por alumno) | e33aa51497943eba696f03614197781226abd0cbf051e1a7877adb534960d8d1 |
| `san_sisle_Datos_ccaa_dic2025_rectificado.pdf` | 6fe3e65b851a2023e262339bc665bf6c4c63c4e263f36b41a5496e10eef85c0e |
| `ar2024_anexo_tablas_horizontales.xlsx` | 3507c3759bdc5d0f2bbf721290d1cae48f25688025aeadbee1a79adc896378f6 |
| `gs2013_…prestacion_edad_sexo.pdf` (no versionado) | acfba3e601a3e769abfcc46f3f51228553789a635680c9c4bea21c014d22f10f |
| `boe_ley_22_2009_financiacion_ccaa.pdf` (no versionado) | b1e50efb5bb277924c5f21e34b4605f0a4b07c1d800f785c5c0da70c2bc38650 |

Diseño muestral: no aplica (registros administrativos censales; sin pesos, estratos ni conglomerados). Errores de
medida conocidos: altas/bajas tardías, afiliaciones múltiples, inscripción voluntaria en el paro registrado.
