# Ronda 5 · Verificación de la ronda 4 y de los cambios a posteriori

Verificación tras el cierre (20-10-2026), punto 2 del encargo. No es un bucle de autocrítica: una sola pasada del árbitro final y
del verificador de cifras sobre los cambios, más la comprobación independiente (recalculando, no releyendo) de cada hallazgo de
docs/rondas/ronda_4.md. Todo es a posteriori.

## 1. Hallazgos de la ronda 4: cambio aplicado y comprobación independiente

| id | hallazgo (ronda 4) | cambio aplicado | comprobación independiente (recálculo) | resultado |
|---|---|---|---|---|
| E1 | Diferencia del ciclo vital con un nativo de 50 años sin calcular | Publicada (F4_VA_DIF_NAT_*_LLEGADA_50) | Recalculada desde output/f4/ciclo_vital.csv emparejando por descuento y bienes las 24 combinaciones sin convergencia: resto de la UE [22, 209], resto del mundo [−22, 182]; coincide con cifras_clave | Correcto. Pero solo con c = 0: con el escenario divergente añadido ahora (§2) su signo no sobrevive |
| E2 | El comparador nativo no cargaba con los bienes públicos con coste marginal cero | Se le suma F4_TRASLADO_BIENES_NAT (498 € al año) | VA del nativo de 30 años con bienes marginal − medio = −16.603 €; el valor actual de −498 € al año con la misma supervivencia, crecimiento y descuento da −16.612 € (la diferencia es el redondeo de 498) | Correcto |
| E3 | La estandarización con tramos de 10 años sesgaba a favor | Tramos de 5 años, 85+ | Reimplementación propia (estandarización directa por tramo × sexo, sin el respaldo por tramo con < 10 observaciones): resto de la UE +309 € (5 años), +737 € (10 años), +349 € (edad simple, cobertura 96 %); resto del mundo −1.708, −1.627 y −1.631 €. Publicado: +240 € y −1.708 € | Correcto el diagnóstico (10 años sesga a favor del resto de la UE en unos 500 €). La cifra del resto de la UE depende del tratamiento de las celdas con pocas observaciones (240 a 349 €); el signo no |
| E4 | «El comparador nativo no tiene salidas, lo que favorece su valor» era al revés | Corregido | VA a los 30 con salidas frente a sin salidas: resto de la UE 26 frente a 22; resto del mundo 5 frente a −42 miles de €: las salidas suben el VA de quien llega, así que no tenerlas juega en contra del nativo | Correcto |
| E5 | Los ingresos no tributarios se escalaban en los tramos suprimidos | Iguales para todos | En los perfiles del ciclo vital, ing_otros_ingresos = 1.835,56 € en todas las edades de los tres grupos (también tras la nueva imputación de los tramos suprimidos) | Correcto |
| E6 | «En una proporción parecida» en el resumen no técnico | Reescrito | Texto: la frase no aparece; ahora explica la composición por edad con cifras (F3_ALC_*) | Correcto |
| E7 | Fiorio et al. y muestreo «edad y sexo» asimétricos | Reescrito en los dos sentidos | Lectura del texto renderizado y cifras de Fiorio et al. leídas ahora en el original (tabla 5: nativos −814 €, migrantes +793 €; docs/literatura/comparacion_externa.md) | Correcto |
| E8 | Expresiones y números tecleados | Corregidos con ids nuevos | Los ids F4_OTROS_INGRESOS_PC y F4_TRASLADO_BIENES_NAT existen y cuadran con su cálculo (1.836 € y 498 €) | Correcto |
| E9 | Salidas del ciclo vital no regeneradas en orden | Regenerado a mano | `make m1_f4` (src/m1/fase.py) ejecutaba los scripts en orden alfabético: el ciclo vital antes que la contabilidad fiscal de la que lee los perfiles | **El arreglo era incompleto:** la regeneración se hizo a mano, pero el objetivo de make reproducía el error. Corregido ahora con un orden explícito en fase.py |
| R1 | Diferencia con el nativo con convergencia | Publicada (F4_VA_DIF_NAT_CONV_*) | Recalculada desde ciclo_vital.csv; coincide | Correcto |

Además, las nuevas pruebas de cuadre (docs/cuadre.md) detectaron dos errores que ninguna de las cuatro rondas vio: el D62
sanitario omitido (1.735 M€) y la imputación de los tramos suprimidos del ciclo vital, que no reproducía los totales estáticos
(resto de la UE, −20 % de la contribución neta total). Están corregidos y sus efectos, publicados antes y después.

## 2. Árbitro final (una pasada sobre los cambios a posteriori)

Veredicto: **REVISAR** (ninguna clasificación cambia). Hallazgos y acción:

| # | hallazgo | clase | acción |
|---|---|---|---|
| 1 | La explicación de por qué AR está acotado y AKM0 no era incorrecta: los errores típicos BHJ y agrupado por provincia son parecidos; la diferencia es la varianza con la nula impuesta y la debilidad al nivel del shock. Lo que deja fuera la AR agrupada debe leerse como «quedaría fuera con inferencia agrupada» | E | Reescrito (§5 y resumen): AKM0 es el contraste de tipo AR al nivel del shock; la AR agrupada tiende a rechazar de más en shift-share |
| 2 | La regla de «qué sobrevive» del ciclo vital no era neutral: c ∈ {0; 0,5; 1} solo mejora a los nacidos fuera | E | Añadido un escenario divergente simétrico (c = −0,5). **Con él ninguna diferencia con los nativos conserva el signo**: la del resto de la UE a los 50 pasa a [−3, 199] miles de €; la del resto del mundo a los 20 sigue negativa con divergencia, pero no con convergencia parcial. Resumen, §4, fichas, brief y autoevaluación reescritos |
| 3 | La frase automática «no se pueden descartar valores de hasta max(|lo|, |hi|)» era falsa con intervalos asimétricos | E | Corregida en el script y en el texto («no se pueden descartar los valores entre lo y hi») |
| 4 | La lectura omitía P1-E1 (desfavorable) y P1-E3c (favorable), y la curva no daba los rechazos de P1-E3a y P1-H2 | P | Añadidos los dos y los recuentos de rechazos de la curva |
| 5 | Frase del ciclo vital desactualizada y mal atribuida (rango de la llegada a los 50 del resto del mundo) | E | Corregida |
| 6 | κ de pensiones: se aplica también a los descendientes (exagera la reducción) y el salario por hora ignora la jornada (en sentido contrario) | P | Los dos sesgos declarados; presentado como intervalo [3,4; 4,4] |
| 7 | Cota de pensiones de la UE: decir que es unilateral y que se mantiene el D62 total | P | Añadido |
| 8 | Las celdas con < 50 observaciones vuelven a entrar como totales en el ciclo vital; remitir a la variante sin escalar también a los 50 años | P | Añadida la variante a los 50 años (F4_VA_IMPUT_UE_*_50 y su diferencia con el nativo) |
| 9 | Comparar el F al nivel del shock con el valor crítico de Montiel Olea-Pflueger es solo orientativo; citar el tF de Lee et al. (2022) | P / X | Lo primero, declarado. Lee et al. no se cita: no se ha leído ni verificado su ficha en esta verificación |
| 10 | Frase contradictoria sobre la EPF | P | Reescrita |

## 3. Verificador de cifras (una pasada)

473 marcadores, ningún id inexistente; las cifras renderizadas coinciden con cifras_clave. Recalculó de forma independiente el
anexo G, la tabla de convenciones, los escenarios de convergencia (antes del escenario divergente), la estandarización y el cuadre
(B9 −51.267 M€; diferencia 2·10⁻¹¹). Tres discrepancias, corregidas:
- AR de P1-H2: doble redondeo (−1,535 guardado con 3 decimales → −1,53; el valor es −1,5352 → −1,54). Las cifras F5V_AR_* se
  guardan ahora con 4 decimales.
- La curva de especificaciones y el multiverso usan rejillas distintas de 32 especificaciones sin avisarlo: aclarado en el texto.
- Brecha bruta de empleo: el id (−1,2 pp, sin redondear) frente a la resta de tasas redondeadas (−1,1). Se mantiene el id.

Números tecleados sin id: los de fuentes externas (anexo H), que coinciden con docs/literatura/comparacion_externa.md.

## 4. Lo que queda abierto
- El árbitro no ha visto la versión corregida (sin bucle, por instrucción).
- La cifra del resto de la UE a igual edad y sexo depende del tratamiento de las celdas pequeñas (240 a 349 €; §1, E3).
- El valor crítico de Montiel Olea-Pflueger no está derivado para el F al nivel del shock.

## Apéndice (congelación, 21-10-2026, a posteriori): segunda pasada del árbitro solo sobre los dos hallazgos mayores

Una sola pasada de arbitro-final limitada a los hallazgos mayores 1 y 2 de §2 y a su corrección. Veredicto: **REVISAR (menor)**: el
fondo de las dos correcciones es correcto; faltaban tres cambios de texto, sin rehacer cálculos.

| hallazgo | estado según el árbitro | lo que faltaba | acción |
|---|---|---|---|
| 1. AKM0 frente a Anderson-Rubin agrupado | PARCIAL. El código respalda que AKM0 es un contraste de tipo AR al nivel del shock (econ.akm0, t2 con la nula impuesta); las cifras de errores típicos cuadran con x_verificacion_emd.csv; la «Lectura» de §5 es correcta | (a) el motivo de la falta de acotación debía nombrar el estadístico límite (primera etapa al nivel del shock con la varianza bajo π = 0), para no contradecir el F al nivel del shock de 13,5; (b) el resumen ejecutivo seguía diciendo «se descartan…» y «no se pueden descartar valores de esa magnitud» | (a) reescrito en §5; (b) el resumen dice ahora «quedarían fuera los valores fuera de [lo, hi]… y no se pueden descartar los de dentro» |
| 2. Neutralidad de la regla del ciclo vital | RESUELTO. La regla es la misma en los dos sentidos; el valor actual y la diferencia crecen con c en todas las filas, así que c = −0,5 hace de cota pesimista; la malla asimétrica (hasta 1 hacia arriba, −0,5 hacia abajo) está justificada porque el perfil transversal ya contiene convergencia | Omisión: con divergencia también es negativa (por muy poco) la diferencia del resto de la UE a los 20 años; el resumen no técnico se quedaba corto con lo favorable. Reservas menores: k actúa componente a componente (la mejora con c es empírica en el agregado, no por construcción) y con c = −0,5 algunas prestaciones no contributivas a los 16-19 años salen negativas, sin suelo en cero (efecto pequeño) | Añadido el caso; resumen no técnico reescrito. Las dos reservas quedan declaradas aquí. Además, en la congelación el rango de c se ancla en la evidencia (c ∈ [0; 0,5], Izquierdo, Lacuesta y Vegas 2009) y c = −0,5 se presenta aparte como prueba de estrés |

El árbitro no ha visto la versión con estos tres cambios (sin bucle, por instrucción).
