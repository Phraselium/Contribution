# Ronda 1 de autocrítica (cierre autónomo)

Revisores (solo lectura): abogado del diablo «desfavorables» (AD-), abogado del diablo «favorables» (AD+), árbitro final (AR, veredicto REVISAR), verificador de cifras (VC, 18 discrepancias). Tokens de subagentes ≈ 630.000.

Tipos: (E) error, se corrige; (R) robustez exigida por el pre-registro o el estándar, se hace; (P) presentación; (X) análisis nuevo a posteriori, rotulado; (F) mejora futura; (D) discrepancia de criterio, se responde.

## Errores (E)
| id | origen | hallazgo | acción |
|---|---|---|---|
| E1 | AD- 1 | El control de cuotas incompletas de P1 era Σ_o cuota_lo sin dividir por la población inicial, no la suma de exposiciones del instrumento (BHJ) que pide el pre-registro. | Corregido (control_cuotas = "bhj"); la versión anterior y la lectura literal («cuota de nacidos fuera en 1998») quedan como sensibilidad. Desviación 13. Se reestima toda la fase 5 y se publica en la dirección que salga. |
| E2 | AR M1 | La descomposición de P1-E3a decía que la caída de la tasa «se reparte» entre ocupados y población; una población menor sube la tasa. | Reescrito: la mitad de la caída del número de ocupados coincide con menos población; la caída de la tasa es íntegra. |
| E3 | AR M2 | El p de permutación se centraba en cero aunque la distribución permutada no lo está; el criterio A6 es «t fuera del 95 % central». | Se publican mediana, 95 % central y p recentrado; la clasificación usa «fuera del 95 % central». |
| E4 | AR M4 | «La única con primera etapa fuerte» era falso (nueve especificaciones del multiverso tienen F ≥ 10). | Corregido; se informa también el multiverso de P1-E3a. |
| E5 | AR M6, AD+ 2 | El intervalo del ciclo vital incluía combinaciones con convergencia que el propio texto dice que la cuentan dos veces. | El intervalo D11 usa solo las 24 combinaciones sin convergencia; la convergencia pasa a sensibilidad aparte. Para el resto del mundo, las llegadas a los 20 y a los 50 años son negativas en todas esas combinaciones. |
| E6 | AD+ 10 | Las razones de uso de la ENSE se calculaban con ≥ 30 observaciones, por debajo del umbral de supresión de 50. | Umbral a 50; se recalcula la contabilidad fiscal. |
| E7 | AD+ 13 | Quedaba un tramo de edad −5 en la ECV de 2024 (la corrección de la edad solo cubría una rama) y los quintiles de renta no estaban ponderados. | Edad ≥ 0 en las dos ramas; quintiles ponderados por el factor de la ECV. |
| E8 | AD- 9 | El documento y el script de prestaciones prometían un contraste con registros administrativos (output/f3/prestaciones_admin.csv) que no existe. | Se retira la promesa; queda como mejora futura. |
| E9 | VC 1-18 | P1-E2 «excluye un tramo que contiene el cero» (falso); 32 frente a 38 especificaciones; recuentos con decimal; comparador del ciclo vital con intervalo mal rotulado; doble negativo; ámbito de jubilación («o vive en un hogar que la percibe»); razones a un decimal; unidades «p ajustado» para p sin ajustar; «pp por pp» para logaritmos; grupo de origen mal en tres cifras; separador inglés; id con «EFECTO»; cifras a posteriori sin clasificación; números tecleados (2,6; 0,97; llegada a los 50). | Todo corregido: formatos en render(), unidades e ids nuevos (F4_PEN_AR2024_DIF_MIGRACION_2050, F5_P1_PRETEND_CORR, LLEGADA_50), F4_PEN_EFECTO… renombrado a F4_PEN_DIF…, cifras de la literatura con referencia a su ficha. |
| E10 | AR m1, m2, m3 | Comparación con la literatura (Gálvez-Iniesta es un coeficiente sobre el nivel de empleo; Carrasco et al. sobre todos los nativos), lógica del párrafo de MCO y término de composición en la agregación por educación. | Reescrito. |

## Robustez (R)
| id | origen | hallazgo | acción |
|---|---|---|---|
| R1 | AR M3 | Faltaban el wild bootstrap de la forma reducida por CCAA (pre-registrado) y los pesos de Rotemberg en resultado.json. | Hecho (F5_*_WCB_p; Rotemberg en diagnosticos). |
| R2 | AD+ 1, AR m5 | La comparación fiscal con los nativos no tenía el nivel «edad y sexo» que exige la regla de tres niveles, y faltaba la cifra del conjunto de nacidos fuera. | Hecho: estandarización directa por edad y sexo sobre las celdas comunes con ≥ 50 observaciones (cobertura declarada) y cifra conjunta. A igual edad y sexo, la diferencia con los nativos es negativa para los dos grupos de nacidos fuera. |
| R3 | AD+ 9 | F4 y A1 debían juzgarse con los tres niveles. | Hecho: brecha de empleo del conjunto de nacidos fuera en tres niveles (−1,2; −5,3; −2,0 pp) y prestaciones monetarias a igual edad y sexo (menores también a igual edad). |

## Presentación (P)
P1 «descartan» → «son compatibles con efectos de hasta…» y potencia (AD+ 11). P2 el signo del multiverso no es evidencia independiente: comparte cuotas y la distribución permutada tiene el mismo signo (AD- 2, AR M2). P3 P1-E3a: el conjunto no identifica el signo; se describe el conjunto, no «asociación negativa» a secas (AD- 3). P4 la variante por nacionalidad usa el tratamiento de todas las edades del padrón y no es comparable en escala (AD- 6). P5 sesgos del ciclo vital en las dos direcciones: perfil sanitario nativo y sin descendientes (en contra), perfil de quienes se quedan y salidas como cota superior (a favor) (AD- 7, AD+ 3, 5). P6 regla mecánica de pensiones: supone empleo y productividad medios (AD+ 12). P7 la pensión sin mínimo de 15 años, para los dos grupos (AD+ 4). P8 «positiva en las 64» no incluye el error de muestreo (AD+ 6). P9 comparador nativo sin salidas (AR m6). P10 «rechaza el cero según AKM0», y el t BHJ y la permutación no rechazan (AR m7). P11 cobertura de la ECV frente a la ECP (AD+ 8).

## Exploratorio a posteriori (X)
X1 Jackknife por comunidad autónoma de P1-E3a, P1-H1 y P1-H2 (AD- 4). Aprobado; rotulado; no cambia clasificaciones (desviación 14).

## Mejoras futuras (F)
Tasas de salida por grupo de nacimiento y prorrata europea de pensiones (AD+ 3, 4); pseudopanel de cohortes × educación por provincia (AD- 5); bootstrap de cada combinación fiscal (AD+ 6); recalibrar la ECV a la ECP (AD+ 8); ENSE más reciente por grupo (AD+ 10); contraste administrativo de prestaciones por nacionalidad (AD- 9); hijos de 18 y más años y descendientes en el ciclo vital (AD+ 7). Van a docs/mejoras_futuras.md.

## Discrepancias de criterio (D)
- D1 (AD+ 9, asimetría A1/F4). Criterio: el veredicto se da sobre la cantidad literal de la afirmación (bruta) y los niveles ajustados la matizan. A1 es falsa en bruto y también a igual edad y sexo (prestaciones monetarias menores), salvo en las no contributivas: «engañosa». F4 es cierta en bruto y no a igual edad y sexo (−5,3 pp) ni en paro: «se sostiene con matices», con la confianza rebajada a media y los matices explícitos.
- D2 (AD- 10, F3). La afirmación F3 es sobre todos los inmigrantes; para el conjunto de nacidos fuera el signo depende de supuestos (positiva en 48 de 64 combinaciones); se mantiene «no se puede saber» con el detalle por grupo.
- D3 (AD- 8, IVA). El IVA se imputa con la EPF por origen y quintil (no con la renta registrada sola); la infracobertura de renta informal se declara como limitación.
- D4 (AD+ 13, Reino Unido). En la ECV el grupo «resto de la UE» sigue la clasificación del INE de cada ola; se declara en limitaciones.
