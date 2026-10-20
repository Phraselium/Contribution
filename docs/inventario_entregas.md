# Inventario de lo pedido y no entregado al cierre (a posteriori)

Verificación tras el cierre (20-10-2026), puntos 3 y 4 del encargo. Para cada pieza: estado al cierre (0b6f323), qué se ha hecho
ahora, ruta y cifra. Todo lo nuevo es a posteriori y no cambia ninguna clasificación.

## Punto 3. Piezas pedidas

| Pieza | Al cierre | Ahora | Ruta | Cifra |
|---|---|---|---|---|
| (i) Tabla de sensibilidad de C2 por convención: déficit, bienes públicos, sociedades, sanidad, pensiones de jubilados de la UE | Parcial: rejilla de 64 combinaciones (output/f4/rejilla.csv), efecto medio por supuesto (sensibilidad_supuestos.csv) y presupuesto equilibrado; sin tabla por convención y sin la de pensiones | Hecha: una fila por convención (una cada vez), más indirectos e hijos; la de pensiones es una cota (la ECV pública no dice qué Estado paga la pensión) | output/f4/sensibilidad_convenciones.csv; src/m1/f4_convenciones.py; documento §4 | Resto de la UE: principal 3.398 €; con sus pensiones pagadas fuera, 4.433 € (F4_CONV_PENS_UE). Rango por convención: España [−1.901, −351]; resto de la UE [1.016, 5.590]; resto del mundo [−2.081, 2.002] (F4_CONV_*) |
| (ii) Cruce «nacidos fuera» × nacionalidad para C1 y C2 | C2: solo nacionalidad sola (neta_por_nacionalidad_2024.csv). C1: nacionalizados frente a no nacionalizados en empleo_generaciones.csv, sin cifra en el documento | Hecho en los dos | C2: output/f4/neta_nacimiento_x_nacionalidad_2024.csv (celdas < 50 suprimidas). C1: cifras F3_ALC_EMP_FUERA_* | C2: nacidos fuera de la UE con nacionalidad española +1.303 €, sin ella −1.547 € (F4_CRUCE_*). C1: tasa de empleo 16-64 de los nacidos fuera (de cualquier origen) nacionalizados 73,2 % y no nacionalizados 64,5 % (ASOCIACIÓN, con selección) |
| (iii) Tratamiento de los +4,4 puntos de pensiones | Declarado como regla mecánica con supuestos | La regla es un PIB endógeno proporcional a la población de 20-64; variante κ con empleo y salario relativos; como efecto, NO ESTIMABLE | output/f4/pensiones_kappa.csv; documento §6 | 4,4 (κ = 1) a 3,4 (κ = 0,73) puntos en 2050 (F4_PEN_DIF_SIN_MIGRACION_KAPPA_2050). Ageing Report: +1,4 frente a la base; AIReF: ±0,1 con flujos ±15 % (anexo H) |
| (iv) Presentación simétrica de los tres grupos fiscales | El resumen y §4 listaban los tres, pero las sensibilidades y el texto se centraban en el resto del mundo | La tabla de convenciones da los tres grupos y el conjunto con la misma fila; las diferencias con los nativos, para los tres | documento §4 | — |

## Punto 4. Alcance frente al plan

El plan pedía 8 grupos de origen, España por provincia y Europa por país y NUTS2.

| Dimensión | Entregado | Fuera de alcance con datos públicos y motivo |
|---|---|---|
| C1 población, 8 grupos × provincia | Sí (padrón 1998-2022): output/f3/poblacion_provincias.csv | — |
| C1 empleo, 8 grupos | 7 grupos nacionales (EPA): África sin separar Magreb y resto | La EPA pública codifica el nacimiento por regiones; el padrón no tiene empleo. La afiliación por nacionalidad no da país de nacimiento |
| C1 empleo, grupo × provincia | Hecho ahora (EPA 2023-2025, celdas ≥ 50): output/f3/empleo_provincias_grupos.csv. Publicables: América Latina 50 provincias, África 50, UE-13 y otros 50, UE-14 44, Asia 27, resto 3 | El resto de celdas, por tamaño muestral |
| C1 salarios por provincia | No | La EES no publica provincia; la estadística de la AEAT por provincia y nacionalidad no fue accesible (NO ESTIMABLE) |
| C2 fiscal, 8 grupos («resto del mundo» desagregado) | No: 3 grupos | ECV pública (PB210) y EPF (PAISNACSP) no distinguen más; harían falta microdatos de investigación de la EU-SILC o registros fiscales (restringidos). Lo más cercano: el cruce por nacionalidad, que separa dentro del resto del mundo a nacionalizados y extranjeros |
| C2 fiscal por provincia | No (solo comunidad autónoma, C4: output/f4/neta_por_region_2024.csv) | La ECV pública solo trae la comunidad (DB040) |
| Europa por país y NUTS2 | C1 (población, empleo, vivienda por NUTS2) y P5 | Contabilidad fiscal europea: microdatos de la EU-SILC restringidos (se comparan cifras publicadas: OCDE y Fiorio et al., anexo H) |

## Otras piezas nuevas de esta verificación
- Cuadre contable: docs/cuadre.md, tests/test_cuadre_fiscal.py.
- Fase 5: output/f5/x_verificacion_emd.csv (EMD, Anderson-Rubin, F de Montiel Olea-Pflueger), x_verificacion_curva.csv, x_verificacion_sin_ccaa.csv.
- Ciclo vital en cuatro escenarios de convergencia (divergente, nula, parcial, completa): output/f4/ciclo_vital_convergencia.csv.
- Referencias externas: docs/literatura/comparacion_externa.md.
- Brief para revisores: docs/brief_revisores.md.
