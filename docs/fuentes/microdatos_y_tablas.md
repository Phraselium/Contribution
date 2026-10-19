# Fichas de fuentes (fase 2): microdatos y tablas del INE, Eurostat y GISCO

El inventario máquina (URL, licencia, edición, fecha de descarga, sha256, tamaño y si se versiona) está en `data/fuentes.csv` y `data/CHECKSUMS.sha256`; aquí se documenta lo que permite cada fuente. Todas se descargan sin registro con los scripts `src/m1/f2_*_descarga.py`. Licencias: INE (reutilización citando la fuente, https://www.ine.es/aviso_legal), Eurostat (CC BY 4.0), GISCO (© EuroGeographics para los límites administrativos).

## INE · EPA, microdatos trimestrales (2005T1-2026T2, 86 ficheros)
- Origen: REGNA1 (región de nacimiento, 12 regiones), NAC1 (española / doble / extranjera), EXREGNA1 (región de la nacionalidad), ANORE1 (años de residencia). Agrupación del plan aproximada (D6): África sin separar Magreb; México en «América del Norte»; el Reino Unido en «resto de Europa» desde 2020 (antes en UE-15).
- Segunda generación: solo hijos que conviven con un progenitor nacido fuera (NPADRE, NMADRE).
- Territorio: provincia. Diseño: solo FACTOREL (sin estratos ni secciones). Rupturas: diseño de registro de 2021 (EDAD1 en lugar de EDAD5), reponderación de la serie a la población del Censo 2021 (los microdatos descargados ya traen los factores revisados), códigos 127/128 para Bulgaria, Rumanía y Croacia.
- Salidas: `data/processed/epa_celdas.csv.gz` (560.301 celdas año × provincia × origen × sexo × edad × educación × residencia) y `epa_sectores.csv.gz`. Contraste: 22,22 millones de ocupados de media en 2025.
- Limitación: no trae salarios (solo las tablas de deciles por nacionalidad, t66240 y t66205).

## INE · ECV, microdatos transversales (2009-2025)
- Origen: RB280/RB290 (2021-2025, todas las personas) y PB210/PB220A (2009-2020, solo mayores de 16; los menores toman el origen de la madre o del padre convivientes, marcado). Solo tres grupos: España, resto UE, resto del mundo.
- Territorio: NUTS2 (DB040). Diseño: pesos; DB060 (UPM) solo hasta 2015.
- Variables: renta por fuentes, impuestos sobre la renta y cotizaciones (HY140G), cotizaciones empresariales (PY030G), prestaciones (PY090G-PY140G, HY050G-HY070G), tenencia y costes de vivienda.
- Salida: `data/processed/ecv_personas.csv.gz` (744.810 personas-año). Contraste: 18,5 % de nacidos fuera en la ECV 2025.

## INE · EPF, microdatos (2016-2024; se usan 2022-2024)
- Origen del sustentador principal: PAISNACSP (España / resto UE-27 / resto de Europa / resto del mundo) y NACIONASP. Territorio: CCAA.
- Uso: distribución de los impuestos indirectos (IVA por grupo ECOICOP con los tipos efectivos de `docs/supuestos/impuestos_indirectos_coicop.csv`, y base de impuestos especiales). En 2024 el ingreso exacto solo consta en el 38 % de los hogares.
- Salida: `data/processed/epf_hogares.csv.gz`.

## INE · Encuesta de Estructura Salarial, microdatos (2010, 2014, 2018, 2022)
- Origen: solo TIPOPAIS (nacionalidad España / resto del mundo); no hay país de nacimiento ni años de residencia. Territorio: NUTS1.
- Salida: `data/processed/ees.csv.gz` (ganancia por hora de octubre y anual equivalente).

## INE · Encuesta Nacional de Salud 2017, microdatos
- Origen: país de nacimiento (España / extranjero) y nacionalidad. Territorio: CCAA. Uso sanitario: consultas de primaria y especialista, días de hospital, urgencias, medicamentos recetados (menores sin urgencias ni medicamentos).
- Salida: `data/processed/ense_uso.csv.gz`. Limitación: 2017 (la ENSE de 2023 no estaba publicada en microdatos al descargar; la EESE 2020 no se localizó en la ruta pública).

## INE · Padrón continuo, tablas PC-Axis (1998-2022) y Estadística Continua de Población (2002-2025)
- 03006: provincia × país de nacimiento (≈ 110 países y restos) × nacionalidad española/extranjera × sexo × año. 03005: extranjeros por nacionalidad y provincia. 03002: edad.
- ECP 56948/56947: provincia × edad × región de nacimiento / nacionalidad (agrupación como la EPA), trimestral.
- Ocho grupos completos (Magreb separado). Diferencias de hasta 13 personas entre la suma de países y el agregado en 1998-2002 (país no consta). Salida: `data/processed/padron_*.csv.gz`.

## INE · otras tablas (Tempus)
Migraciones por provincia y nacionalidad o nacimiento (69692, 69693, 69707, 69708, 69765), proyecciones 2026-2075 (36642, 36776, 36777), Censo 2021 (66611, 66596, 69947), EPA por nacionalidad (66240, 66205, 65115, 65336, 65310), ECV (9995, 75484).

## Eurostat (36 tablas) y GISCO
- EU-LFS por país de nacimiento (nativos / otro UE / fuera de la UE) a nivel país (lfsa_*) y NUTS2 (lfst_r_*); EU-SILC por grupo de país de nacimiento (ilc_*); flujos por país de nacimiento (migr_imm3ctb, migr_emi4ctb); población por nacimiento y ciudadanía; censos 2011 (NUTS2, país de nacimiento) y 2021 (NUTS3, país de nacimiento detallado: cuotas de asentamiento para P5); EUROPOP2023; COFOG (gov_10a_exp), impuestos (gov_10a_taxag), PIB.
- GISCO NUTS 2021 (polígonos 1:20M y puntos de etiqueta) para mapas.
- Microdatos de uso público de Eurostat (PUF): no se han usado; serían solo complemento (regla de la fase 2).
