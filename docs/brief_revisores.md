# M1 · Brief para revisores externos

Documento de trabajo M1: contribución e impacto económico de la población según su origen, España (por provincia) y Europa,
solo con datos públicos. Documento: publicacion/documento_m1/documento.md. Toda cifra está en output/cifras_clave.csv con su capa.
Capas: C1 hechos; C2 cotas con supuestos; C3 efectos identificados (vacía); C4 exploratorio. Clasificación causal: IDENTIFICADO,
SUGESTIVO, ASOCIACIÓN, NO ESTIMABLE. El documento solo ha tenido revisores internos simulados.

## Qué se afirma y con qué clasificación

| Afirmación | Capa / clasificación |
|---|---|
| El 19,3 % de la población nació fuera (ECP 2025). Tasa de empleo de 25-54 años: 73,2 % frente a 82,3 %; a igual edad y sexo (16-64), −5,3 pp; paro 14,0 % frente a 9,4 % | C1 (bruto); C4 (ajustado) |
| La brecha salarial por hora de los extranjeros es −18,1 % en bruto y −6,2 % con edad, sexo, estudios y región | C1 / C4 |
| Contribución fiscal neta estática 2024 por persona (con déficit): nacidos en España −1.404 € [−1.990, −673]; resto de la UE +3.398 € [726, 5.915]; resto del mundo −191 € [−2.118, 2.792]. Solo se afirma el intervalo de 64 combinaciones | C2 |
| A igual edad y sexo, la ventaja del resto de la UE baja a +240 € y la del resto del mundo es −1.708 € (intervalo de supuestos con el cero) | C4 |
| El signo del conjunto de nacidos fuera lo decide la asignación de los hijos nacidos en España y el coste de los bienes públicos | C2 |
| Ciclo vital: con cualquier ritmo de convergencia salarial, quien llega del resto de la UE a los 50 años aporta más que un nativo de esa edad; las demás comparaciones dependen de supuestos | C2 |
| Pensiones: regla mecánica, 4,4 puntos de PIB más en 2050 sin migración (3,4 con empleo y salario relativos) | C2; como efecto, NO ESTIMABLE |
| Impacto en el empleo, el paro, los salarios y los servicios de los nativos (shift-share de Card por provincia, Borjas por celdas, P3 educación, P5 Europa) | Todo ASOCIACIÓN o NO ESTIMABLE. Conjuntos AKM0 no acotados; F efectivo 17,9 < 23,1 (Montiel Olea-Pflueger) |
| Indicio desfavorable P1-E3a (empleo de nativos con estudios bajos, −0,61 pp por pp) | C4 / ASOCIACIÓN; no supera BH ni el wild bootstrap; en parte composición por edad; depende de una comunidad |

Las sumas fiscales cuadran con el saldo B9 de 2024 y con cada partida de la contabilidad nacional (pruebas automáticas, docs/cuadre.md).

## Preguntas para un economista laboral (parte causal)

1. Con F al nivel del shock 13,5 y F efectivo 17,9 (por debajo de 23,1), ¿es preferible publicar solo la forma reducida y los
   conjuntos AKM0, sin la estimación puntual de MC2E?
2. Los intervalos de Anderson-Rubin agrupados por provincia están acotados y los AKM0 no. ¿Qué inferencia debe primar, y es
   correcto decir que los AR agrupados son optimistas por no recoger la correlación entre provincias con orígenes parecidos?
3. El control de cuotas incompletas se corrigió después de ver resultados y el plan admite tres lecturas que cambian los signos de
   las confirmatorias. ¿Es suficiente publicar las tres con el mismo rango, o la principal debería ser otra?
4. Con cuotas de 1998 y shocks persistentes (pretendencia casi colineal con el primer periodo, correlación 0,97), ¿qué diseño
   alternativo con datos públicos (EPA desde 1996, otros periodos base) recomendaría?
5. P1-E3a: ¿es la tasa estandarizada por edad la medida adecuada, dado que la composición por edad del grupo cambia con el
   instrumento? ¿Cómo separaría efecto y composición?
6. Los efectos mínimos detectables (0,7 a 3,5 pp por pp en P1) superan las estimaciones de la literatura española (≈ −0,2). ¿Tiene
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
5. El ciclo vital aplica perfiles transversales de 2024 y una tasa de salida que incluye bajas por caducidad del padrón (cota
   superior). ¿Qué calibración de salidas y de convergencia salarial considera central?
6. Los tramos de edad con menos de 50 observaciones se imputan con la forma por edad de los nativos reescalada al total del grupo.
   ¿Es aceptable, o preferiría suavizar los perfiles del grupo?
7. La regla mecánica de pensiones da diferencias diez veces mayores que la AIReF. ¿Debe retirarse del resumen ejecutivo?
8. La población de la ECV deja fuera a unos 0,45 millones de nacidos fuera (recién llegados, hogares colectivos). ¿Cómo imputaría su
   contribución?
