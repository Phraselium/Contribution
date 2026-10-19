# Fase 1 · Servicios públicos: inmigración y congestión en sanidad y educación

Fecha de lectura: 19-10-2026. Lector: bibliotecario (una pregunta por invocación). Todas las fichas quedan sin estado hasta que pase `src/m1/verificar_referencias.py`.

Alcance: de todos los trabajos se ha leído solo el **resumen** (IDEAS/RePEc, IZA, Europe PMC, OpenAlex o el registro de Crossref). No se ha descargado ningún PDF. Los DOI se han comprobado uno a uno en api.crossref.org el 19-10-2026 (título, autores, revista, volumen y páginas coinciden). Las líneas «Validez para España» mezclan lo que dice el resumen con inferencia propia, marcada «(inferencia)».

Notas al encargo: Hunt se publicó en 2017 (Journal of Human Resources 52(4), en línea en 2016), no como trabajo de 2017 sin revista. De Anghel y Cabrales he localizado el trabajo de 2014 sobre primaria en Madrid; su resumen no da resultados sobre alumnado extranjero. Se añaden, por pertinencia, Wadsworth (2013), Jensen y Rasmussen (2011), Juanmarti Mestres et al. (2021), Tanaka, Farré y Ortega (2018) y Zinovyeva, Felgueroso y Vázquez (2014).

Neutralidad: estos trabajos miden uso de servicios o efectos sobre resultados de otros; se describen agregados y su variación, no rasgos de grupos.

---

## Sanidad

### Giuntella, O., Nicodemo, C. y Vargas-Silva, C. (2018). The effects of immigration on NHS waiting times
- DOI: 10.1016/j.jhealeco.2018.02.001 · Revista: Journal of Health Economics, 58, 123-143; versiones previas en SSRN (2015 y 2017)
- Leído: resumen (https://ideas.repec.org/a/eee/jhecon/v58y2018icp123-143.html; DOI en Crossref)
- Diseño e identificación: panel de áreas locales de Inglaterra que relaciona la población inmigrante con los tiempos de espera; el resumen no detalla el instrumento.
- Datos, país y periodo: Inglaterra; registros administrativos hospitalarios (Hospital Episode Statistics) 2003-2012 enlazados con la inmigración medida en la Labour Force Survey.
- Resultado principal (con su unidad, tal como lo da el autor): la inmigración redujo los tiempos de espera de las derivaciones a consultas externas y no tuvo efectos significativos en urgencias ni en cirugía programada; la reducción se explica porque la inmigración aumenta la movilidad interna de los nativos y porque los inmigrantes tienden a estar más sanos que los nativos que se marchan. En áreas más desfavorecidas fuera de Londres la espera de consultas externas aumentó, sobre todo en los años inmediatamente posteriores a la ampliación de la UE de 2004, y el efecto desaparece a medio plazo (3-4 años). El resumen no da magnitudes en minutos o días.
- Validez para España: (inferencia) sistema nacional de salud universal comparable; el mecanismo de movilidad de nativos y el efecto transitorio en zonas desfavorecidas son trasladables, pero en España no hay microdatos hospitalarios públicos equivalentes por área pequeña: las listas de espera publicadas son agregadas por comunidad.
- Replicación pública: no público (los registros HES son de acceso restringido)
- Estado: (lo escribe el verificador)

### Wadsworth, J. (2013). Mustn't Grumble: Immigration, Health and Health Service Use in the UK and Germany
- DOI: 10.1111/j.1475-5890.2013.00177.x · Revista: Fiscal Studies, 34(1), 55-82
- Leído: resumen (https://ideas.repec.org/a/ifs/fistud/v34y2013i1p55-82.html; DOI en Crossref)
- Diseño e identificación: comparación longitudinal del uso de servicios entre inmigrantes y nativos a la llegada y con el tiempo, con controles por diferencias observadas y no observadas (efectos individuales); descriptivo-asociativo, no causal sobre congestión.
- Datos, país y periodo: Reino Unido y Alemania, encuestas longitudinales de hogares; el resumen no da el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): los inmigrantes en Alemania, no en el Reino Unido, declaran peor salud con más frecuencia que los nativos, pero en ambos países usan los servicios hospitalarios y de medicina general a tasas muy parecidas a las de los nativos; los controles apenas cambian esa conclusión.
- Validez para España: (inferencia) útil como contraste de la hipótesis de uso diferencial que se aplicará en la imputación del gasto sanitario de la fase 4; en España la comparación equivalente se hace con la Encuesta Nacional de Salud y la Encuesta Europea de Salud (públicas).
- Replicación pública: no público (no se ha localizado paquete; las encuestas BHPS/UKHLS y SOEP requieren registro o solicitud)
- Estado: (lo escribe el verificador)

### Antón, J.-I. y Muñoz de Bustillo, R. (2010). Health care utilisation and immigration in Spain
- DOI: 10.1007/s10198-009-0204-z · Revista: The European Journal of Health Economics, 11(5), 487-498 (en línea en 2009)
- Leído: resumen (https://ideas.repec.org/a/spr/eujhec/v11y2010i5p487-498.html; DOI en Crossref)
- Diseño e identificación: modelos binomiales negativos y de obstáculo (hurdle) sobre el número de visitas y estancias; comparación condicional, no causal.
- Datos, país y periodo: España, Encuesta Nacional de Salud 2006-2007 (representativa).
- Resultado principal (con su unidad, tal como lo da el autor): no hay diferencias estadísticamente significativas entre inmigrantes y nativos en las visitas al médico ni en las estancias hospitalarias; los inmigrantes acceden menos al especialista y acuden a urgencias con más frecuencia. El resumen no da magnitudes.
- Validez para España: alta en ámbito; (inferencia) es anterior a la reforma de 2012 que restringió la cobertura de los inmigrantes en situación irregular y a la llegada de 2015-2025, por lo que conviene reproducirlo con encuestas más recientes.
- Replicación pública: no público (no se ha localizado paquete; la Encuesta Nacional de Salud tiene microdatos públicos del INE y del Ministerio de Sanidad, lo que permitiría reproducirlo)
- Estado: (lo escribe el verificador)

### Jiménez-Rubio, D. y Hernández-Quevedo, C. (2011). Inequalities in the use of health services between immigrants and the native population in Spain: what is driving the differences?
- DOI: 10.1007/s10198-010-0220-z · Revista: The European Journal of Health Economics, 12(1), 17-28 (en línea en 2010)
- Leído: resumen (Europe PMC, PMID 20135189: https://europepmc.org/article/MED/20135189; DOI en Crossref)
- Diseño e identificación: descomposición de Oaxaca-Blinder de la probabilidad de uso de servicios en una parte explicada por características (estructura demográfica, salud declarada, enfermedades crónicas) y una parte no explicada asociada a la condición de inmigrante.
- Datos, país y periodo: España; el resumen no da la encuesta ni el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): las diferencias en la probabilidad de usar hospital, especialista y urgencias se deben en gran medida a factores no explicados ligados a la condición de inmigrante; en medicina general pesan mucho más las características individuales, sobre todo la salud declarada y las enfermedades crónicas. El resumen no da magnitudes ni el signo de cada brecha.
- Validez para España: alta en ámbito y en método (coincide con la descomposición que exige M1 en la sección A); (inferencia) la parte «no explicada» puede recoger barreras de acceso o diferencias de información, no solo preferencias.
- Replicación pública: no público (no se ha localizado paquete)
- Estado: (lo escribe el verificador)

### Juanmarti Mestres, A., López Casasnovas, G. y Vall Castelló, J. (2021). The deadly effects of losing health insurance
- DOI: 10.1016/j.euroecorev.2020.103608 · Revista: European Economic Review, 131, 103608
- Leído: resumen (https://ideas.repec.org/a/eee/eecrev/v131y2021ics0014292120302385.html; DOI en Crossref)
- Diseño e identificación: experimento natural de la reforma de septiembre de 2012 (Real Decreto-ley 16/2012) que restringió el acceso a la sanidad pública de los inmigrantes en situación irregular.
- Datos, país y periodo: España, mortalidad de la población afectada, tres primeros años de aplicación de la reforma.
- Resultado principal (con su unidad, tal como lo da el autor): la restricción elevó la tasa de mortalidad mensual de los inmigrantes irregulares en 0,31 muertes por 100.000 personas, equivalente a 82 muertes adicionales al año; los cambios de composición de la población tratada explican solo un 3,45 % del efecto.
- Validez para España: alta; (inferencia) no mide congestión, sino el efecto de restringir el acceso; es relevante para valorar políticas que reducen el gasto imputado a este grupo y sus costes en salud.
- Replicación pública: no público (no se ha localizado paquete)
- Estado: (lo escribe el verificador)

## Educación

### Geay, C., McNally, S. y Telhaj, S. (2013). Non-Native Speakers of English in the Classroom: What are the Effects on Pupil Performance?
- DOI: 10.1111/ecoj.12054 · Revista: The Economic Journal, 123(570), F281-F307
- Leído: resumen (resumen de la versión publicada en OpenAlex, https://api.openalex.org/works/doi:10.1111/ecoj.12054; DOI en Crossref)
- Diseño e identificación: la correlación bruta se contrasta con estrategias para aislar el efecto causal de cambios en el porcentaje de alumnos que no tienen el inglés como primera lengua; el resumen no detalla cuáles.
- Datos, país y periodo: Inglaterra, resultados al final de primaria; el resumen no da el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): la correlación negativa de los datos brutos es sobre todo un artefacto de selección (los no nativos asisten más a escuelas con nativos desfavorecidos); el efecto estimado es cero y los autores descartan efectos negativos. El resumen no da magnitudes.
- Validez para España: (inferencia) la lección de selección es directamente aplicable: en España una parte del alumnado extranjero es hispanohablante, lo que reduce la barrera lingüística respecto al caso inglés.
- Replicación pública: no público (no se ha localizado paquete; los datos de alumnos ingleses son de acceso restringido)
- Estado: (lo escribe el verificador)

### Ohinata, A. y van Ours, J. C. (2013). How Immigrant Children Affect the Academic Achievement of Native Dutch Children
- DOI: 10.1111/ecoj.12052 · Revista: The Economic Journal, 123(570), F308-F331; versión previa IZA DP 6212 (2011)
- Leído: resumen (versión IZA, https://ideas.repec.org/p/iza/izadps/dp6212.html; DOI de la versión publicada en Crossref)
- Diseño e identificación: efecto del porcentaje de alumnos inmigrantes en el aula sobre los resultados de los nativos y de los propios inmigrantes; el resumen no detalla la estrategia de identificación.
- Datos, país y periodo: Países Bajos, varias fuentes de evaluación de lectura, matemáticas y ciencias; el resumen no da el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): no hay evidencia sólida de efectos negativos de desbordamiento sobre los nativos; los propios inmigrantes sufren efectos negativos de lengua cuando su proporción en el aula es alta, pero no en matemáticas ni ciencias. El resumen no da magnitudes.
- Validez para España: (inferencia) sistema europeo con escolarización comparable; transferible como orden de magnitud cualitativo.
- Replicación pública: no público (no se ha localizado paquete)
- Estado: (lo escribe el verificador)

### Jensen, P. y Rasmussen, A. W. (2011). The effect of immigrant concentration in schools on native and immigrant children's reading and math skills
- DOI: 10.1016/j.econedurev.2011.08.002 · Revista: Economics of Education Review, 30(6), 1503-1515
- Leído: resumen (https://ideas.repec.org/a/eee/ecoedu/v30y2011i6p1503-1515.html; DOI en Crossref)
- Diseño e identificación: MCO e IV que tienen en cuenta la selección de los padres entre barrios.
- Datos, país y periodo: Dinamarca, datos PISA enriquecidos; el resumen no da el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): los alumnos de escuelas con alta concentración de inmigrantes obtienen peores resultados en lectura y matemáticas; con IV el efecto se mantiene en matemáticas y es impreciso en lectura; el efecto es mayor para los nativos que para los inmigrantes, sobre todo en matemáticas. El resumen no da magnitudes.
- Validez para España: (inferencia) contrasta con Geay et al. y Ohinata y van Ours; muestra que el resultado depende del país y del diseño, por lo que España requiere evidencia propia.
- Replicación pública: no público (no se ha localizado paquete; la ampliación danesa de PISA no es pública)
- Estado: (lo escribe el verificador)

### Hunt, J. (2017). The Impact of Immigration on the Educational Attainment of Natives
- DOI: 10.3368/jhr.52.4.0115-6913R1 · Revista: Journal of Human Resources, 52(4), 1060-1118 (en línea en 2016); versión previa NBER WP 18047 (2012)
- Leído: resumen (https://ideas.repec.org/a/uwp/jhriss/v52y2017i4p1060-1118.html; DOI en Crossref)
- Diseño e identificación: panel de estados; instrumentos basados en los patrones de asentamiento de 1940.
- Datos, país y periodo: EE. UU., estados, 1940-2010.
- Resultado principal (con su unidad, tal como lo da el autor): un aumento de 1 punto porcentual del porcentaje de inmigrantes en la población de 11 a 64 años eleva en 0,3 puntos porcentuales la probabilidad de que los nativos de 11 a 17 años completen 12 años de escolarización; la autora encuentra tanto un canal escolar como uno de expectativas laborales, con efecto neto positivo.
- Validez para España: (inferencia) periodo y sistema muy distintos; el canal de expectativas laborales (más incentivo a estudiar si los inmigrantes compiten en empleos poco cualificados) es plausible en España.
- Replicación pública: no público (no se ha localizado paquete; los datos censales de EE. UU. son públicos vía IPUMS con registro gratuito)
- Estado: (lo escribe el verificador)

### Farré, L., Ortega, F. y Tanaka, R. (2018). Immigration and the public–private school choice
- DOI: 10.1016/j.labeco.2018.01.001 · Revista: Labour Economics, 51, 184-201
- Leído: resumen (https://ideas.repec.org/a/eee/labeco/v51y2018icp184-201.html; DOI en Crossref)
- Diseño e identificación: efecto de la densidad de alumnado inmigrante en la escuela sobre la elección de escuela de los nativos; el resumen no detalla la identificación.
- Datos, país y periodo: España, datos de hogares 2000-2015.
- Resultado principal (con su unidad, tal como lo da el autor): el aumento de la densidad inmigrante en las escuelas desencadenó una salida importante de nativos de la escuela pública gratuita hacia la privada, más intensa en los hogares nativos más educados; la inmigración elevó la ratio alumnos/profesor en la pública. El resumen no da magnitudes.
- Validez para España: alta; (inferencia) es la principal evidencia española de congestión educativa (ratio alumnos/profesor) y de reordenación entre redes; las estadísticas públicas del Ministerio de Educación permiten un análisis agregado parecido por provincia.
- Replicación pública: no público (no se ha localizado paquete)
- Estado: (lo escribe el verificador)

### Tanaka, R., Farré, L. y Ortega, F. (2018). Immigration, assimilation, and the future of public education
- DOI: 10.1016/j.ejpoleco.2017.06.001 · Revista: European Journal of Political Economy, 52, 141-165
- Leído: resumen (https://ideas.repec.org/a/eee/poleco/v52y2018icp141-165.html; DOI en Crossref)
- Diseño e identificación: modelo cuantitativo de economía política con población inmigrante heterogénea, calibrado; distingue corto y largo plazo, naturalización y asimilación. No es una estimación causal.
- Datos, país y periodo: España, oleada de inmigración de 2000-2008.
- Resultado principal (con su unidad, tal como lo da el autor): a corto plazo la inmigración llevó a un aumento del 15 % de la matrícula pública, una reducción del 3 % del gasto en educación pública y casi 1 punto porcentual más de hogares nativos en la privada; según el grado de asimilación, estas tendencias se intensifican o se atenúan cuando los inmigrantes se naturalizan y votan.
- Validez para España: alta en ámbito; capa equivalente a C2/C4 (simulación con supuestos), no a efecto identificado.
- Replicación pública: no público (no se ha localizado paquete)
- Estado: (lo escribe el verificador)

### Zinovyeva, N., Felgueroso, F. y Vázquez, P. (2014). Immigration and student achievement in Spain: evidence from PISA
- DOI: 10.1007/s13209-013-0101-7 · Revista: SERIEs, 5(1), 25-60 (en línea en 2013)
- Leído: resumen (https://ideas.repec.org/a/spr/series/v5y2014i1p25-60.html; DOI en Crossref)
- Diseño e identificación: descriptivo-descomposicional: evolución de los resultados del alumnado inmigrante con los años en España y descomposición de la brecha en calidad de escuela y características familiares. No mide efectos sobre los nativos.
- Datos, país y periodo: España, PISA 2003, 2006 y 2009 (microdatos públicos de la OCDE).
- Resultado principal (con su unidad, tal como lo da el autor): el alumnado inmigrante obtiene peores resultados que el nativo y mejora con el tiempo de estancia; la ventaja lingüística inicial de los latinoamericanos no acelera su convergencia; la mayor parte de la brecha se explica por características individuales y familiares y menos del 15 % por la escuela a la que asisten.
- Validez para España: alta; reproducible con PISA posteriores (públicos); (inferencia) que la escuela explique poco de la brecha limita, pero no descarta, un canal de congestión.
- Replicación pública: datos públicos (PISA, https://www.oecd.org/pisa/data/); no se ha localizado paquete de código
- Estado: (lo escribe el verificador)

### Cabrales, A. y Anghel, B. (2014). The determinants of success in primary education in Spain
- DOI: 10.5944/reppp.2.2014.12030 · Revista: Revista de Evaluación de Programas y Políticas Públicas, 2, 22-
- Leído: resumen (OpenAlex, https://api.openalex.org/works/doi:10.5944/reppp.2.2014.12030; texto abierto en https://revistas.uned.es/index.php/REPPP/article/download/12030/11377, no leído)
- Diseño e identificación: relación entre recursos del centro, entorno socioeconómico y características de los padres y el resultado en una prueba estandarizada; el resumen no detalla la estrategia.
- Datos, país y periodo: Comunidad de Madrid, prueba de 6.º de primaria (CDI), con nacionalidad del alumno y, en centros públicos, composición por nacionalidad; el resumen no da el periodo.
- Resultado principal (con su unidad, tal como lo da el autor): el resumen describe los datos y las variables, pero no da resultados ni magnitudes sobre el alumnado extranjero; no los atribuyo.
- Validez para España: alta en ámbito (Madrid); pendiente de lectura del texto completo, que es de acceso abierto.
- Replicación pública: no público (los datos de la prueba CDI no son públicos a nivel de alumno)
- Estado: (lo escribe el verificador)

---

## Tabla de la pregunta

| trabajo | diseño | datos | resultado (unidad) | validez para España |
|:--|:--|:--|:--|:--|
| Giuntella, Nicodemo y Vargas-Silva (2018) | panel de áreas locales (identificación no detallada en resumen) | Inglaterra, HES 2003-2012 + LFS | menos espera en consultas externas; sin efecto en urgencias y cirugía programada; aumento transitorio en áreas desfavorecidas (sin magnitud en resumen) | media: SNS comparable; sin datos públicos equivalentes en España |
| Wadsworth (2013) | comparación longitudinal con efectos individuales | Reino Unido y Alemania, paneles de hogares | uso hospitalario y de medicina general parecido al de los nativos | media: referencia para el supuesto de uso en la fase 4 |
| Antón y Muñoz de Bustillo (2010) | binomial negativa y hurdle | España, ENS 2006-2007 | sin diferencias en visitas y estancias; menos especialista y más urgencias (sin magnitud) | alta; anterior a 2012 |
| Jiménez-Rubio y Hernández-Quevedo (2011) | Oaxaca-Blinder | España (encuesta no indicada en resumen) | brecha en hospital, especialista y urgencias sobre todo no explicada; en medicina general, explicada por salud | alta |
| Juanmarti Mestres et al. (2021) | experimento natural (RDL 16/2012) | España, mortalidad, 3 años tras 2012 | +0,31 muertes por 100.000 al mes (≈ 82 al año) | alta; mide acceso, no congestión |
| Geay, McNally y Telhaj (2013) | identificación causal frente a selección | Inglaterra, final de primaria | efecto cero sobre nativos; se descartan efectos negativos | media |
| Ohinata y van Ours (2013) | efecto del porcentaje de inmigrantes en el aula | Países Bajos, varias evaluaciones | sin efectos negativos sólidos sobre nativos (sin magnitud) | media |
| Jensen y Rasmussen (2011) | MCO e IV por selección residencial | Dinamarca, PISA ampliado | peor resultado en matemáticas con más concentración; mayor en nativos (sin magnitud) | media |
| Hunt (2017) | IV con asentamientos de 1940, panel de estados | EE. UU., 1940-2010 | +0,3 pp en completar 12 años de escuela por +1 pp de inmigrantes | baja-media |
| Farré, Ortega y Tanaka (2018) | densidad inmigrante por escuela y elección de red | España, hogares 2000-2015 | salida de nativos a la privada; más alumnos por profesor en la pública (sin magnitud) | alta |
| Tanaka, Farré y Ortega (2018) | modelo de economía política calibrado | España, 2000-2008 | +15 % matrícula pública, −3 % gasto público en educación, ≈ +1 pp nativos en privada | alta en ámbito; simulación |
| Zinovyeva, Felgueroso y Vázquez (2014) | descomposición de la brecha | España, PISA 2003-2009 | convergencia con la estancia; < 15 % de la brecha por la escuela | alta; no mide efecto sobre nativos |
| Cabrales y Anghel (2014) | determinantes del resultado (no detallado) | Madrid, prueba CDI de 6.º | el resumen no da resultados sobre alumnado extranjero | alta en ámbito; pendiente de texto |

## Qué esperamos en España y por qué

1. Uso sanitario: tras ajustar por edad y salud, un uso total de servicios parecido al de los nativos, con más urgencias y menos especialista (Antón y Muñoz de Bustillo; Jiménez-Rubio y Hernández-Quevedo; Wadsworth en otros países). Por eso el perfil de gasto por edad y sexo es un punto de partida razonable para la fase 4, con sensibilidad para urgencias y especialista.
2. Congestión sanitaria: no hay evidencia causal española. Con las listas de espera públicas, agregadas por comunidad, cabe esperar a lo sumo una ASOCIACIÓN; la evidencia inglesa sugiere efectos pequeños, transitorios y concentrados en áreas desfavorecidas.
3. Educación: la evidencia europea sobre los resultados de los nativos va de nula (Inglaterra, Países Bajos) a negativa en matemáticas (Dinamarca); en España el canal mejor documentado es la reordenación entre redes y la ratio alumnos/profesor en la pública (Farré, Ortega y Tanaka), más que una caída medida de resultados.
4. Lo que sí es reproducible con datos públicos: brechas de PISA por origen y su convergencia (Zinovyeva et al.) y, por provincia, alumnado extranjero por red y ratio alumnos/profesor (estadísticas del Ministerio de Educación). Los efectos causales sobre resultados de nativos por escuela probablemente quedarán NO ESTIMABLES por falta de microdatos públicos por centro.
5. Las restricciones de acceso (reforma de 2012) tienen costes medidos en salud (Juanmarti Mestres et al.), que deben pesar igual que el ahorro en la evaluación de esas políticas.
