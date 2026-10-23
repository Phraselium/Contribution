# M1 · Brief para revisores externos

Documento de trabajo M1: contribución e impacto económico de la población según su origen, España (por provincia) y Europa,
solo con datos públicos. Documento: publicacion/documento_m1/documento.md. Toda cifra está en output/cifras_clave.csv con su capa.
Capas: C1 hechos; C2 cotas con supuestos; C3 efectos identificados (vacía); C4 exploratorio. Clasificación causal: IDENTIFICADO,
SUGESTIVO, ASOCIACIÓN, NO ESTIMABLE. El documento solo ha tenido revisores internos simulados.

**Literatura (a posteriori).** De las fuentes externas con las que se comparan las cifras (anexo H y docs/literatura/comparacion_externa.md), solo una figura como VERIFICADA según la regla de M1 (DOI comprobado en Crossref y título coincidente): el Informe Anual 2025 del Banco de España. Las demás se leyeron en el original, pero no tienen DOI, la versión leída es de trabajo o el título no coincide. La comparación con la literatura es parcial: no hay ninguna estimación española publicada y leída en la misma escala que P1, y la convergencia salarial del ciclo vital se ancla en un único estudio (Izquierdo, Lacuesta y Vegas 2009, con datos de 2005, del periodo expansivo).

## Qué se afirma y con qué clasificación

| Afirmación | Capa / clasificación |
|---|---|
| El 19,3 % de la población nació fuera (ECP 2025). Tasa de empleo de 25-54 años: 73,2 % frente a 82,3 %; a igual edad y sexo (16-64), −5,3 pp; paro 14,0 % frente a 9,4 % | C1 (bruto); C4 (ajustado) |
| La brecha salarial por hora de los extranjeros es −18,1 % en bruto y −6,2 % con edad, sexo, estudios y región | C1 / C4 |
| Contribución fiscal neta estática 2024 por persona (con déficit): nacidos en España −1.404 € [−1.990, −673]; resto de la UE +3.398 € [726, 5.915]; resto del mundo −191 € [−2.118, 2.792]. Solo se afirma el intervalo de 64 combinaciones | C2 |
| A igual edad y sexo, la ventaja del resto de la UE baja a +240 € y la del resto del mundo es −1.708 € (intervalo de supuestos con el cero). La contribución del resto del mundo a igual edad y sexo, [−3.223, −12], está al límite: con un 10 % de infradeclaración diferencial de sus rentas contiene el cero | C4 |
| Cobertura de la ECV antes de escalar: 88 % en IRPF y cotizaciones del trabajador, 103 % en vejez; escalado con un factor único por partida, igual para todos los grupos. Con infradeclaración diferencial de los nacidos fuera del 10 %, su diferencia con los nativos pasa a ser positiva en las 64 combinaciones | C2 |
| El signo del conjunto de nacidos fuera lo decide la asignación de los hijos nacidos en España y el coste de los bienes públicos | C2 |
| Ciclo vital: con la convergencia salarial que estima la literatura española leída (c entre 0 y 0,5; Izquierdo, Lacuesta y Vegas 2009), quien llega del resto de la UE a los 50 años aporta más que un nativo de su edad; en la prueba de estrés con divergencia (c = −0,5) ninguna diferencia con los nativos conserva el signo | C2 |
| Pensiones: regla mecánica (PIB proporcional a la población de 20-64), en el anexo J. Con la misma variación de la migración que el Ageing Report 2024 (±33 %), +1,7 / −1,4 puntos en 2050 frente a +1,4 / −1,2 en el Ageing Report; sin migración, 4,4 (no comparable con ninguna fuente) | C2; como efecto, NO ESTIMABLE |
| Impacto en el empleo, el paro, los salarios y los servicios de los nativos (shift-share de Card por provincia, Borjas por celdas, P3 educación, P5 Europa) | Todo ASOCIACIÓN o NO ESTIMABLE. Conjuntos AKM0 no acotados; F efectivo 17,9 < 23,1 (Montiel Olea-Pflueger). Con información pública el diseño no tiene potencia: efecto mínimo detectable en el empleo de los nativos 1,15 pp por pp (1,21 con el error implícito de AKM0) |
| Indicio desfavorable P1-E3a (empleo de nativos con estudios bajos, −0,61 pp por pp) | C4 / ASOCIACIÓN; no supera BH ni el wild bootstrap; en parte composición por edad; depende de una comunidad |

Las sumas fiscales cuadran con el saldo B9 de 2024 y con cada partida de la contabilidad nacional (pruebas automáticas, docs/cuadre.md).

## Preguntas para un economista laboral (parte causal)

1. Con F efectivo 17,9 (por debajo de 23,1; el diagnóstico al nivel del shock, 13,5, está en el anexo A), ¿es preferible publicar solo la forma reducida y los
   conjuntos AKM0, sin la estimación puntual de MC2E?
2. Los intervalos de Anderson-Rubin agrupados por provincia están acotados y los AKM0 no. ¿Qué inferencia debe primar, y es
   correcto decir que los AR agrupados son optimistas por no recoger la correlación entre provincias con orígenes parecidos?
3. El control de cuotas incompletas se corrigió después de ver resultados y el plan admite tres lecturas que cambian los signos de
   las confirmatorias. ¿Es suficiente publicar las tres con el mismo rango, o la principal debería ser otra?
4. Con cuotas de 1998 y shocks persistentes (pretendencia casi colineal con el primer periodo, correlación 0,97), ¿qué diseño
   alternativo con datos públicos (EPA desde 1996, otros periodos base) recomendaría?
5. P1-E3a: ¿es la tasa estandarizada por edad la medida adecuada, dado que la composición por edad del grupo cambia con el
   instrumento? ¿Cómo separaría efecto y composición?
6. Los efectos mínimos detectables (0,7 a 3,5 pp por pp en P1 con el error al nivel del shock; parecidos con el implícito de AKM0) superan las estimaciones de la literatura española, aunque no hay ninguna publicada y leída en la misma escala (la más cercana, −0,18 pp por pp, es de una versión de trabajo). ¿Tiene
   sentido mantener esta parte en el documento, o debe presentarse como un ejercicio de potencia?
7. El wild bootstrap con 17 comunidades y una con el 42 % de la variación del instrumento: ¿es aceptable como control espacial?

## Preguntas para un economista de hacienda pública (C2 y ciclo vital)

1. El déficit se reparte entre todos (como OCDE C2) y se ofrece también el presupuesto equilibrado repartido por persona. ¿Qué
   reparto del déficit recomienda (por persona, proporcional a impuestos, a gasto)?
2. Bienes públicos puros a coste medio o marginal cero: ¿es razonable la cota del coste marginal cero para los nacidos fuera, y
   que el comparador nativo del ciclo vital cargue con el traslado?
3. La asignación de los hijos nacidos en España a sus padres cambia el signo. ¿Hasta qué edad o generación debería imputarse?
4. Las pensiones que reciben los nacidos en el resto de la UE pueden pagarlas otros Estados y la ECV pública no lo distingue. ¿Hay
   una fuente pública (INSS, pensiones en el extranjero) para acotarlo mejor que la cota extrema usada?
5. El ciclo vital da cotas con cuatro escenarios de convergencia (c = −0,5; 0; 0,5; 1). ¿Es razonable el rango, y cuál consideraría central? Aplica además perfiles transversales de 2024 y una tasa de salida que incluye bajas por caducidad del padrón (cota
   superior). ¿Qué calibración de salidas recomienda?
6. Los tramos de edad con menos de 50 observaciones se imputan con la forma por edad de los nativos reescalada al total del grupo.
   ¿Es aceptable, o preferiría suavizar los perfiles del grupo?
7. La regla mecánica de pensiones da diferencias diez veces mayores que la AIReF. ¿Debe retirarse del resumen ejecutivo?
8. Infradeclaración diferencial y renta informal: el documento explora que los nacidos fuera declaren en la ECV un 10 o 20 % menos de renta gravada (los impuestos se reasignan hacia ellos), de renta informal no gravada (solo cambia el IVA a través del consumo), o de prestaciones (se reasignan hacia ellos), y una base de consumo neta de remesas. ¿Qué evidencia hay sobre la magnitud y la dirección de la infradeclaración por origen en la ECV o en el IRPF, y cómo trataría la renta informal: como consumo gravado por el IVA y fuera del IRPF, o con otra regla?
9. La población de la ECV deja fuera a unos 0,45 millones de nacidos fuera (recién llegados, hogares colectivos). ¿Cómo imputaría su
   contribución?
