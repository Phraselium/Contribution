# Ronda 4 de autocrítica (última)

Revisores: AR (REVISAR, «cambios menores en extensión»), AD- (resiste con limitaciones; ningún error de cálculo que cambie una conclusión desfavorable), AD+ (resiste con limitaciones), VC (11 discrepancias, ninguna de valor ni de marcador). Tokens ≈ 635.000 (acumulado desde el inicio del cierre ≈ 2,65 millones).

## Errores (E)
| id | origen | hallazgo | acción |
|---|---|---|---|
| E1 | AR M1, VC 4 | La diferencia del ciclo vital con un nativo de la misma edad no se calculaba a los 50 años, donde es favorable (resto de la UE positiva en todas las combinaciones). | Calculada y publicada; frases reescritas. |
| E2 | AR M2 | Con coste marginal cero para los nacidos fuera, el comparador nativo no asumía su parte de los bienes públicos (la contabilidad estática sí la traslada). | Corregido: se le carga el traslado medido en la estática (F4_TRASLADO_BIENES_NAT). La diferencia a los 30 años del resto del mundo pasa a contener el cero. |
| E3 | AD+ 2 | La estandarización «edad y sexo» con tramos de 10 años sesgaba a favor: los nacidos fuera son más jóvenes dentro de cada tramo. | Tramos de 5 años (85+). |
| E4 | AD- 1 | «El comparador nativo no tiene salidas, lo que favorece su valor»: es al revés. | Corregido. |
| E5 | AD- (resto menor) | Los ingresos no tributarios por persona se escalaban con el bloque de impuestos en los tramos de edad suprimidos. | Corregido: son iguales para todos. |
| E6 | AR M3, VC 1 | El resumen no técnico decía que trabajan «en una proporción parecida», lo que F4 califica de engañoso. | Reescrito con la tasa de 25-54 años y la brecha a igual edad y sexo. |
| E7 | AR M4, VC 5 | Comparación con Fiorio et al. y muestreo del nivel «edad y sexo» presentados de forma asimétrica. | Reescrito en los dos sentidos. |
| E8 | VC 2, 3, 6-11; AR m6-m9 | «sobre las celdas comunes»; prestaciones sí tienen nivel de edad y sexo; F4 con una explicación causal sin cifra; F1 «retorno y convergencia»; números tecleados (1.800, potencia 0,2); cifra repetida; grupos sin nombrar en vivienda. | Corregido; ids nuevos (F4_OTROS_INGRESOS_PC, F4_TRASLADO_BIENES_NAT). |
| E9 | AD+ 1 | Salidas del ciclo vital no regeneradas en orden (fiscal y luego ciclo vital). | Regenerado en orden. |

## Robustez (R)
R1 (AD- 2) La diferencia con el nativo con convergencia, para mostrar que «en todas las combinaciones» depende de excluirla. Publicada (F4_VA_DIF_NAT_CONV_*).

## Presentación (P)
P1 Criterio de «engañosa» explicitado («en bruto con edades comparables o a igual edad y sexo») (AR m10). P2 Jackknife de P1-H2 en la misma frase que P1-E3a (AR m8). P3 Nivel completo de la EPA = residencia 10-19 años (AD- mejora).

## Abiertos al cerrar el bucle (cuarta ronda alcanzada)
- Ajuste del presupuesto equilibrado proporcional a los impuestos, no solo igual por persona (AD+ mejora). Mejora futura.
- Totalización de periodos de cotización (Reglamento 883/2004 y Convenio Iberoamericano) para quien sale (AD+ mejora). Mejora futura; la variante sin mínimo de 15 años la aproxima.
- Bootstrap que tenga en cuenta los hogares repetidos en el recuento de celdas (AD+ mejora); el IC del nivel «edad y sexo» se declara aproximado.
- Desglose por sexo de la brecha de empleo a igual edad (AD- mejora: casi toda la brecha está en las mujeres). No hecho por falta de rondas; queda en mejoras futuras.
- Definición de «no contributivas» sin las prestaciones familiares ni las pensiones no contributivas (AD- mejora); la conclusión de A1 no cambia.
- Otros sesgos menores del ciclo vital (gasto universitario, impuestos de los pensionistas, mortalidad única) (AD- mejora).
- El árbitro no ha dado ACEPTAR en ninguna ronda; su última valoración es «REVISAR, cambios menores en extensión», con los hallazgos 1-4 de esta ronda ya aplicados. No hay una quinta ronda para comprobarlo.
