# Ronda 2 de autocrítica

Revisores: AD- (resiste con limitaciones), AD+ (resiste con limitaciones), AR (REVISAR: «tras corregir, aceptable»), VC (11 discrepancias, ningún error de valor). Tokens ≈ 650.000 (acumulado desde el inicio del cierre ≈ 1,3 millones).

## Errores (E)
| id | origen | hallazgo | acción |
|---|---|---|---|
| E1 | AR M1, AD+ 1, AD- 2 | Las sensibilidades del control de cuotas («original», «cuota_1998») se anunciaban pero no se estimaban; «cuota_1998» divide por la población de 2002 y el comentario decía 1998. | Estimadas en el multiverso y publicadas con el mismo rango que la principal (tabla en la sección 5); comentario corregido (la ECP empieza en 2002). |
| E2 | AR M2, AD- 10, VC 3 | Frases con signo para el nivel «edad y sexo» del resto del mundo, cuyo intervalo contiene el cero; para el resto de la UE la cobertura es de edades centrales; sin error de muestreo. | Redacción según D11; bootstrap de la diferencia estandarizada; cobertura explícita. |
| E3 | AR M4, VC 1, AD+ 12 | La ficha F2 decía «primera etapa débil». | Corregida. |
| E4 | VC 2 | F1 decía que los intervalos del ciclo vital contienen el cero. | Corregida (negativos a los 20 y 50 años desde fuera de la UE). |
| E5 | AR m2, VC 4 | Contradicción sobre el ajuste por composición en la comparación con Fiorio et al. | Reescrita; se añade que Fiorio et al. no incluyen los bienes públicos puros y se compara también con la variante a coste marginal cero. |
| E6 | AD+ (E7 parcial) | Los quintiles de la EPF no estaban ponderados. | Ponderados por FACTOR. |
| E7 | VC 5-11 | Doble signo en A3; 4,4 y 0,45 tecleados; periodo «2021-2025» de las prestaciones; Ageing Report sin «NO VERIFICADA» en F1; unidades en la tabla; tres cifras sin clasificación. | Corregido. |
| E8 | AR m1 | La comparación de pensiones no era homogénea (4,4 frente a 2,6). | Se da la diferencia mecánica comparable (menos frente a más migración). |
| E9 | AR m3 | La comparación con Gálvez-Iniesta mezclaba escalas. | Se retira la ubicación «por debajo de su rango». |

## Robustez (R)
| id | origen | hallazgo | acción |
|---|---|---|---|
| R1 | AR M3 | Las señales de permutación, nacionalidad, wild bootstrap y multiverso se daban solo para P1-E3a; también hay señales favorables (P1-H2, P1-E3c). | Tabla de señales para las diez hipótesis con el mismo formato. |
| R2 | AR m4, m5 | Pesos de Rotemberg y apalancamiento por comunidad (condición de wcr_boot con 17 grupos) sin informar. | Informados (cinco mayores pesos, peso negativo, apalancamiento máximo). |
| R3 | AD+ 5 | Variante conjunta del ciclo vital (mitad de salidas y sin mínimo de 15 años). | Hecha y publicada junto al principal. |

## Presentación (P)
P1 «48 de 64» no mide robustez: el signo del conjunto depende de la tabla 2×2 bienes públicos × hijos; se publica por celdas (AD+ 3). P2 «hasta 0,5 en cualquier sentido» → intervalo explícito (AD+ 10). P3 confianza de A1 a media, con la cobertura de la estandarización; el criterio «cantidad literal» se fijó en la ronda 1, después de ver datos, y se declara (AD+ 6, 7). P4 resumen no técnico con matices (nativo de 40 años, déficit, diferencia con nativos) (AR m6). P5 regla de tres niveles incompleta en vivienda, prestaciones y fiscal, declarada (AR m7). P6 F6 cita P2 (AR m10). P7 enlace a las fichas en la web (AR m11). P8 la primera etapa de la variante «original» y la permutación de E3a en el resumen (AD- 6). P9 sesgo del perfil transversal para quien llega a los 20 y regla del IBI (AD- 8, 11). P10 P1-E4 (15 celdas) y la heterogeneidad de P5 (5-6 países) quedan fuera de lo validado por Monte Carlo para el wild bootstrap (AR m5). P11 potencia: P1-E4, P3 y P5 admiten efectos grandes (AD+ 11).

## Exploratorio a posteriori (X), aprobado y rotulado
X1 Representación del instrumento con shocks en tasas de crecimiento (AD- 1): mismo z, otra inferencia AKM0. Se publica como sensibilidad exploratoria; **no cambia ninguna clasificación**, porque la adenda A1 fijó los shocks en niveles («para que el instrumento sea exactamente z = S̃·g y la inferencia AKM0 sea la del diseño validado»). X2 Composición por edad y segunda generación en P1-E3a (AD- 3). X3 Comunidad autónoma cuya exclusión más mueve P1-E3a (AD- 4).

## Mejoras futuras (F)
Perfiles fiscales por edad × años de residencia (AD- 8); pretendencia con la tasa de empleo de los nativos con educación baja antes de 2005 (EPA anterior a 2005 no descargada; AD- 5); control del ciclo inmobiliario no contaminado por el tratamiento (AD- 4); IBI trasladado a inquilinos (AD- 11); bootstrap con recalibración (AD+ 4); recalibrar la ECV a la ECP y simular la población irregular (AD+ 8); razones de la ENSE por tramos finos (AD+ 9); efecto mínimo detectable (AD+ 11).

## Discrepancias de criterio (D)
- D1 (AD+ 2, AD- 1: ¿cuál es el control «tal como lo describe el pre-registro»?). La adenda A1, que prevalece, define s̃_lo = cuota / población 15-64 inicial y shocks en niveles, y justifica esa elección por la inferencia AKM0 validada; la suma de esas exposiciones es la variante «bhj». La lectura del texto original («cuota de nacidos fuera en 1998») corresponde a la representación con shocks en tasas de crecimiento. Se mantiene la principal de A1, se publican las tres variantes con el mismo rango y se reconoce que la corrección se hizo después de ver resultados y que es, de las tres, la menos desfavorable en P1-H1 y P1-H2 y la menos negativa en P1-E3a. No es una parada D: no se cambia la especificación pre-registrada, se corrige el código para que coincida con ella.
- D2 (AD- 12). La brecha de empleo «edad y sexo» es una MCO con efectos de edad × sexo (método fijado en la fase 3 para todas las comparaciones); una estandarización directa no cambiaría el signo con −5,3 pp.
- D3 (AR m8, simetría de vivienda). Comprobado, no es un error: las brechas completas de propiedad (−0,28242) y alquiler de mercado (+0,28243) del resto de la UE difieren en la quinta cifra; casi coinciden porque las otras dos formas de tenencia (alquiler reducido y cesión gratuita) tienen brechas que se compensan en ese grupo (+1,7 y −1,6 pp en bruto).
