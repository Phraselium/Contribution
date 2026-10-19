# Ronda 3 de autocrítica

Revisores: AD- («no resiste en lo desfavorable fiscal»; P1-E3a resiste con limitaciones), AD+ (resiste con limitaciones si se corrigen E1 y E2), AR (REVISAR, cambios menores), VC (10 discrepancias más el aviso del ciclo vital). Tokens ≈ 710.000 (acumulado desde el inicio del cierre ≈ 2,0 millones).

## Errores (E)
| id | origen | hallazgo | acción |
|---|---|---|---|
| E1 | AD+ E1, AD- E1, VC aviso | El ciclo vital omitía los ingresos no tributarios repartidos por persona (≈ 1.836 € al año) y restaba el gasto repartido por persona: sumaba esa cantidad al déficit de todos. | Corregido (desviación 20). Los niveles de las llegadas entre 20 y 50 años pasan a contener el cero para los dos grupos; la diferencia con un nativo de la misma edad pasa a ser negativa en todas las combinaciones para quienes llegan de fuera de la UE a los 20 y 30 años. Las dos cosas se publican. |
| E2 | AD- E2 | La estandarización «edad y sexo» solo usaba celdas con ≥ 50 observaciones: para el resto de la UE excluía 0-34 y 65+ años, donde los nacidos fuera salen mejor (sesgo en contra). | Estandarización con cobertura completa (tramos de 10 años × sexo; sexos juntos si una celda tiene menos de 10 observaciones). El umbral de 50 se aplica a lo publicado, no a los términos de un agregado. Se publica como salga. |
| E3 | AR M1, AD+ E2 | «Indicios favorables de la misma fuerza» no se sostenía: los favorables solo tienen la permutación y la columna «rechazan» no daba el signo. | Reescrito; rechazos del multiverso con signo. |
| E4 | AD+ E3 | El jackknife solo se usaba para debilitar P1-E3a. | Jackknife de P1-H1, P1-H2 y P1-E3c publicado en la misma frase. |
| E5 | AD+ E4 | F4 «se sostiene con matices» dependía del tramo 16-64: a 25-54 años la brecha bruta es de unos 9 puntos. | F4 pasa a «engañosa» con el mismo criterio que A1 (desviación 21). |
| E6 | VC 1-10, AR m1-m8 | Redondeo de la variante por nacionalidad; «nativo de 40 años» tecleado; «5 o 6 países»; «en las demás edades» incluía la llegada a los 0 años; descripciones «primera etapa débil»; unidades log; enlace web literal; atribución de la base de pensiones al Ageing Report; fármacos en A4; 38 frente a 40 especificaciones; «tal como lo describe el pre-registro»; Fiorio «desaparece» frente a «se invierte»; OCDE sin «NO VERIFICADA»; «48 de 64» en A5 y F3. | Corregido. |

## Robustez (R)
R1 (AD- S1) Señales de P1-E3a con la tasa estandarizada por edad (variante por nacionalidad, permutación y wild bootstrap), para ver si sobreviven a la composición. Hecho; se publica.

## Presentación (P)
P1 Potencia baja del wild bootstrap con 17 grupos (AR m11). P2 Bootstrap de la diferencia estandarizada: 100 réplicas no centradas (AR m10). P3 P1-E3a sin la segunda generación sigue rechazando sin ajustar (AR m9). P4 La EES cuenta a los nacionalizados como «españoles» (AD+ M1). P5 El control de la representación en tasas de crecimiento usa la población de 2002 fija (AD+ M2), declarado.

## Discrepancias de criterio (D)
- D1 (AD+ M4, F5). «Por el mismo trabajo» se aproxima con el nivel que iguala ocupación, sector, contrato y jornada (−3,0 %): es una medida observada, aunque parcial; no es un contrafactual ni una preferencia. Se mantiene «se sostiene con matices», con confianza media y la advertencia de que el resto no explicado no prueba discriminación.
- D2 (AD- S1). La estimación pre-registrada de P1-E3a es la tasa sin estandarizar; la estandarizada por edad es un análisis a posteriori. El resumen cita las dos, sin sustituir una por otra.
