# Autoevaluación de M1

**Qué es sólido.** Los hechos descriptivos (capa C1): población por origen y provincia, tasas de empleo y paro, salarios, vivienda y prestaciones, con dos fuentes cuando existen, supresión de celdas y tres niveles de comparación en casi todas las comparaciones. El inventario de fuentes públicas con checksum, la reproducibilidad sin red y la trazabilidad de cada cifra a output/cifras_clave.csv, que `make check` verifica. Que las prestaciones monetarias por persona de los nacidos fuera son menores que las de los nativos también a igual edad y sexo. Que, a 25-54 años y a igual edad y sexo, los nacidos fuera tienen menos empleo y más paro que los nativos.

**Qué es frágil.**
- La contabilidad fiscal depende de supuestos de imputación; solo se publican intervalos (D11). Tres errores de cálculo detectados en las revisiones cambiaron conclusiones fiscales: el ciclo vital omitía unos ingresos por persona, el nivel «edad y sexo» excluía las edades en que los nacidos fuera salen mejor y luego usaba tramos demasiado anchos. Que errores así sobrevivieran a varias revisiones indica que puede haber otros.
- El ciclo vital: perfiles transversales de 2024 aplicados a vidas futuras, salidas calibradas con una cota superior, sin descendientes y con el déficit actual incluido. Solo dos diferencias frente a nativos de la misma edad tienen signo (negativa para quien llega de fuera de la UE a los 20 años, positiva para quien llega del resto de la UE a los 50), y las dos dependen de excluir la convergencia.
- El indicio desfavorable P1-E3a (empleo de los nativos con estudios bajos): no supera la corrección por multiplicidad, en buena parte es composición por edad y depende de una comunidad autónoma.
- El signo de las confirmatorias P1-H1 y P1-H2 dependió de un error de código corregido después de ver resultados; la corrección elegida es, de las tres lecturas posibles del control, la menos desfavorable, y se publican las tres.
- Los criterios de veredicto de las afirmaciones se precisaron durante la revisión, después de ver datos (F4 pasó de «se sostiene con matices» a «engañosa»).

**Qué no permite concluir nada.**
- El impacto causal de la inmigración sobre el empleo, los salarios o los servicios de los nativos: ninguna hipótesis queda IDENTIFICADA ni SUGESTIVA; los conjuntos de confianza AKM0 no están acotados aunque la primera etapa sea fuerte, y la inferencia depende de cómo se escriba el instrumento.
- P3 (listas de espera), P1-E5 (salarios provinciales) y la convergencia salarial con los años de residencia: NO ESTIMABLES con datos públicos.
- P5 (Europa): periodo corto y poca potencia.

**Qué haría distinto un equipo profesional con más recursos.**
- Acceso a la MCVL y a los registros fiscales y de prestaciones por origen (mejoras_futuras.md, 1, 7 y 14): trayectorias, salidas y carreras de cotización observadas en lugar de supuestas.
- Revisión de código por pares independientes antes de producir el documento, con pruebas unitarias de cada partida contable (por ejemplo, que la suma de las contribuciones netas sea igual al saldo de las administraciones en cada perfil y en el ciclo vital). Las pruebas habrían detectado los errores del ciclo vital.
- Pre-registro con sello de tiempo externo, separado del código, con las desviaciones registradas en commits propios antes de ejecutar; y con la representación del instrumento y los criterios de veredicto fijados de antemano.
- Un diseño causal con más variación: panel anual de provincias con la EPA desde 1996, instrumentos anteriores a la llegada y pretendencias sobre los mismos resultados.
- Revisión externa real: este documento solo ha tenido revisores internos simulados.
