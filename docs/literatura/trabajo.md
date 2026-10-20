# M1 · Fase 1 · Literatura: mercado de trabajo

Pregunta: impacto de la inmigración sobre salarios y empleo de la población nacida en el país (nativos) y asimilación laboral y salarial de los inmigrantes. Fichas elaboradas por el subagente bibliotecario el 2026-10-19. DOI comprobados en api.crossref.org antes de anotarlos (búsqueda bibliográfica y consulta directa del DOI); los resúmenes se han leído en OpenAlex, IDEAS/RePEc, los repositorios de los autores o el texto del editor, según se indica en cada ficha. Todo es paráfrasis. El estado lo escribe `src/m1/verificar_referencias.py`.

Nota sobre PDF: por instrucción de esta tarea solo se escribe este fichero; los PDF abiertos consultados no se han copiado a data/bib/pdf/, pero se anota su sha256 para que puedan guardarse después con la misma huella.

Convención de la línea «Replicación pública»: se indica (a) si existe paquete de código y datos de los autores y dónde, y (b) si los datos de base son públicos según la regla A del plan (descarga sin solicitud, o registro gratuito y automático). «No localizado» significa que se buscó y no se encontró; no que no exista.

## 1. Marco general y método (EE. UU. y teoría)

### Card (2001). Immigrant inflows, native outflows, and the local labor market impacts of higher immigration
- DOI: 10.1086/209979 · Revista: Journal of Labor Economics 19(1)
- Leído: resumen (https://api.openalex.org/works/doi:10.1086/209979)
- Diseño e identificación: enfoque espacial por ciudad × ocupación; compara resultados ocupacionales en ciudades con distinta oferta relativa de inmigrantes y estudia si los nativos y los inmigrantes anteriores se marchan cuando llegan otros (respuesta de movilidad). Es el origen del instrumento de asentamientos previos por país de origen que luego se generaliza.
- Datos, país y periodo: Censo de EE. UU. de 1990; flujos de los años ochenta.
- Resultado principal (con su unidad, tal como lo da el autor): la movilidad entre ciudades de nativos e inmigrantes antiguos apenas responde a las llegadas; salarios y tasas de empleo por ocupación son menores donde la oferta relativa es mayor; en ciudades de entrada tradicionales (Miami, Los Ángeles) las llegadas de los ochenta habrían reducido salarios y tasas de empleo de los nativos poco cualificados en 1–3 puntos porcentuales.
- Validez para España: alta como diseño (provincia × ocupación o × educación con EPA y padrón); el resultado de ausencia de «salida» de nativos debe contrastarse con la EVR del INE. Mercado laboral y composición de orígenes muy distintos.
- Replicación pública: paquete de los autores no localizado; datos de base públicos (microdatos censales de EE. UU. vía IPUMS, registro gratuito). Texto abierto en http://hdl.handle.net/2027/pst.000031163163.
- Estado: VERIFICADA (Crossref)

### Borjas (2003). The labor demand curve is downward sloping: reexamining the impact of immigration on the labor market
- DOI: 10.1162/003355303322552810 · Revista: Quarterly Journal of Economics 118(4)
- Leído: resumen (https://api.openalex.org/works/doi:10.1162/003355303322552810)
- Diseño e identificación: enfoque nacional por celdas de educación × experiencia; supone un mercado nacional en el que trabajadores con igual educación pero distinta experiencia no son sustitutos perfectos, y explota la variación en el tiempo del peso inmigrante en cada celda.
- Datos, país y periodo: EE. UU.; censos y encuestas de varias décadas (el resumen no detalla años).
- Resultado principal (con su unidad, tal como lo da el autor): un aumento del 10 % de la oferta de trabajo en una celda reduce el salario de los trabajadores competidores entre un 3 % y un 4 % (elasticidad salarial −0,3 a −0,4).
- Validez para España: diseño replicable con la EPA (celdas educación × experiencia potencial), pero es un efecto relativo entre celdas, no el efecto total (véase Dustmann, Schönberg y Stuhler 2016) y es sensible al «downgrading» de los inmigrantes, muy documentado en España (Simón, Ramos y Sanromá 2014).
- Replicación pública: paquete de los autores no localizado; datos de base públicos (IPUMS, registro gratuito).
- Estado: VERIFICADA (Crossref)

### Ottaviano y Peri (2012). Rethinking the effect of immigration on wages
- DOI: 10.1111/j.1542-4774.2011.01052.x · Revista: Journal of the European Economic Association 10(1)
- Leído: resumen (https://api.openalex.org/works/doi:10.1111/j.1542-4774.2011.01052.x)
- Diseño e identificación: modelo estructural de producción CES anidada; se estiman las elasticidades de sustitución entre grupos (incluida la de nativos frente a inmigrantes dentro de la misma celda educación × experiencia) y se simulan los efectos totales de largo plazo.
- Datos, país y periodo: EE. UU., 1990–2006.
- Resultado principal (con su unidad, tal como lo da el autor): sustituibilidad imperfecta pequeña pero significativa entre nativos e inmigrantes; efecto de la inmigración 1990–2006 sobre el salario de los nativos sin secundaria entre +0,6 % y +1,7 %; salario medio nativo +0,6 %; salario de los inmigrantes anteriores −6,7 % a largo plazo.
- Validez para España: el marco es trasladable (EPA + EES por celdas), pero los resultados dependen críticamente de la elasticidad de sustitución y del supuesto de ajuste completo del capital; en España la proximidad lingüística de los latinoamericanos podría aumentar la sustituibilidad.
- Replicación pública: paquete de los autores no localizado; datos de base públicos (IPUMS, registro gratuito).
- Estado: VERIFICADA (Crossref)

### Peri y Sparber (2009). Task specialization, immigration, and wages
- DOI: 10.1257/app.1.3.135 · Revista: American Economic Journal: Applied Economics 1(3)
- Leído: resumen (https://api.openalex.org/works/doi:10.1257/app.1.3.135)
- Diseño e identificación: especialización por tareas; combina la intensidad de tareas de cada ocupación (O*NET) con microdatos censales por estado para mostrar que, ante la llegada de inmigrantes poco educados, los nativos se reasignan hacia tareas comunicativas.
- Datos, país y periodo: EE. UU., microdatos censales individuales (el resumen no da años ni unidad geográfica) y O*NET.
- Resultado principal (con su unidad, tal como lo da el autor): los nacidos fuera se concentran en ocupaciones intensivas en tareas manuales y físicas y los nativos en ocupaciones intensivas en comunicación y lenguaje; este mecanismo explica efectos salariales solo modestos para los nativos poco educados (el resumen no da magnitudes).
- Validez para España: muy relevante para P2 del plan; el canal lingüístico es menos claro en España por el peso de inmigrantes hispanohablantes (véase Amuedo-Dorantes y De la Rica 2011). Requiere asignar a la CNO de la EPA medidas de tareas (O*NET con tabla de paso ISCO, pública).
- Replicación pública: paquete de los autores no localizado; datos de base públicos (IPUMS con registro gratuito; O*NET de descarga libre).
- Estado: VERIFICADA (Crossref)

### Dustmann, Schönberg y Stuhler (2016). The impact of immigration: why do studies reach such different results?
- DOI: 10.1257/jep.30.4.31 · Revista: Journal of Economic Perspectives 30(4)
- Leído: resumen (https://api.openalex.org/works/doi:10.1257/jep.30.4.31)
- Diseño e identificación: revisión y marco teórico; clasifica los estudios en dos grupos que estiman efectos relativos (entre celdas de cualificación, o entre celdas dentro de regiones) y un tercero que estima el efecto total, y los interpreta con el modelo canónico, relajando la oferta de trabajo nativa (inelástica y heterogénea) y permitiendo el «downgrading» de los inmigrantes.
- Datos, país y periodo: no aplica (síntesis conceptual).
- Resultado principal (con su unidad, tal como lo da el autor): las estimaciones de los distintos enfoques no son comparables entre sí; el «downgrading» sesga los enfoques de efectos relativos pero no los de efecto total, y la heterogeneidad de la oferta nativa complica sobre todo la lectura de los efectos relativos; recomiendan estimar efectos totales.
- Validez para España: guía directa para el pre-registro de P1: preferir el efecto total por provincia (o provincia × grupo asignado por posición en la distribución, no por educación declarada) y documentar el «downgrading».
- Replicación pública: no aplica (ensayo sin estimaciones propias que replicar). Texto abierto: https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.30.4.31
- Estado: VERIFICADA (Crossref)

### Jaeger, Ruist y Stuhler (2018). Shift-share instruments and the impact of immigration
- DOI: 10.3386/w24285 · Revista: NBER Working Paper 24285 (también IZA DP 11307 y CEPR DP 12701)
- Leído: texto completo (https://humcap.uchicago.edu/RePEc/hka/wpaper/Jaeger_Ruist_Stuhler_2018_shift-share_impact-immigration.pdf; PDF consultado sha256 cd42b8fbaccf7d244b22df6c66283d0acc3889aefe9115e53db77fc36db01756; lectura del resumen, la introducción y la sección de datos)
- Diseño e identificación: muestra que el instrumento de asentamientos previos mezcla la respuesta de corto plazo con el ajuste en curso a choques anteriores cuando la distribución espacial de los flujos es estable en el tiempo; propone la «instrumentación múltiple» (instrumentar a la vez la llegada actual y la retardada) que aprovecha los cambios en la composición nacional por país de origen.
- Datos, país y periodo: EE. UU., censos 1960–2000 y ACS agregadas como 2010, por área metropolitana (zonas de desplazamiento en apéndice).
- Resultado principal (con su unidad, tal como lo da el autor): solo en los años setenta hay un cambio suficiente en la composición por origen (correlación de cuotas entre llegados en los sesenta y en los setenta 0,59, frente a 0,96–0,99 en décadas posteriores); el impacto inicial sobre los salarios nativos en los setenta es más negativo que con el instrumento convencional y el efecto de la llegada retardada es positivo y, en algunas especificaciones, de magnitud similar (recuperación).
- Validez para España: crítica central para P1. En España la composición por origen sí cambió mucho (Marruecos, Ecuador, Rumanía, Colombia, Venezuela…) entre 1998–2008 y 2015–2025, lo que favorece la instrumentación múltiple; la correlación de cuotas entre olas debe medirse con el padrón antes de estimar.
- Replicación pública: paquete de los autores no localizado; datos de base públicos (IPUMS, registro gratuito).
- Estado: VERIFICADA (Crossref)

### Goldsmith-Pinkham, Sorkin y Swift (2020). Bartik instruments: what, when, why, and how
- DOI: 10.1257/aer.20181047 · Revista: American Economic Review 110(8)
- Leído: resumen (https://api.openalex.org/works/doi:10.1257/aer.20181047)
- Diseño e identificación: econometría del instrumento de Bartik como diseño de exposición agrupado en el que la identificación descansa en la exogeneidad de las cuotas; descomposición en pesos de Rotemberg para ver qué cuotas mandan y cómo evaluar su plausibilidad.
- Datos, país y periodo: dos aplicaciones en EE. UU.: elasticidad de oferta de trabajo y elasticidad de sustitución entre inmigrantes y nativos (y, según la versión de trabajo, importaciones chinas).
- Resultado principal (con su unidad, tal como lo da el autor): resultado metodológico (sin cifra única): el estimador equivale a una combinación ponderada de estimadores que usan cada cuota como instrumento; los pesos de Rotemberg identifican qué cuotas deben defenderse como exógenas.
- Validez para España: obligatorio en las pruebas mínimas del plan (pesos de Rotemberg por país de origen; exclusión de los orígenes de más peso).
- Replicación pública: paquete y datos públicos en openICPSR (proyecto 117405, https://doi.org/10.3886/E117405V1).
- Estado: VERIFICADA (Crossref)

### Adão, Kolesár y Morales (2019). Shift-share designs: theory and inference
- DOI: 10.1093/qje/qjz025 · Revista: Quarterly Journal of Economics 134(4)
- Leído: resumen (https://api.openalex.org/works/doi:10.1093/qje/qjz025)
- Diseño e identificación: inferencia en regresiones shift-share; ejercicio placebo con choques sectoriales aleatorios y derivación de errores estándar válidos con correlación arbitraria entre regiones de cuotas parecidas (AKM, AKM0).
- Datos, país y periodo: zonas de desplazamiento de EE. UU. (placebo con resultados reales del mercado de trabajo).
- Resultado principal (con su unidad, tal como lo da el autor): con errores convencionales al 5 % nominal, el nulo de efecto se rechaza hasta en el 55 % de las muestras placebo; sus métodos dan intervalos de confianza sustancialmente más anchos en aplicaciones habituales.
- Validez para España: inferencia exigida por el plan (AKM o BHJ). Con 50 provincias y pocos orígenes dominantes, la corrección puede ser grande.
- Replicación pública: paquete R público ShiftShareSE (CRAN, https://cran.r-project.org/web/packages/ShiftShareSE/index.html; código en https://github.com/kolesarm/ShiftShareSE); paquete de datos del artículo no comprobado.
- Estado: VERIFICADA (Crossref)

### Borusyak, Hull y Jaravel (2022). Quasi-experimental shift-share research designs
- DOI: 10.1093/restud/rdab030 · Revista: Review of Economic Studies 89(1)
- Leído: resumen (https://api.crossref.org/works/10.1093/restud/rdab030)
- Diseño e identificación: identificación por la asignación cuasi aleatoria de los choques (aquí, flujos nacionales por país de origen) permitiendo cuotas endógenas; equivalencia con una regresión al nivel del choque.
- Datos, país y periodo: ilustración con Autor, Dorn y Hanson (2013) (importaciones chinas y empleo manufacturero en zonas de desplazamiento de EE. UU.).
- Resultado principal (con su unidad, tal como lo da el autor): resultado metodológico: la ortogonalidad instrumento-residuo equivale a la ortogonalidad choques-inobservable al nivel del choque; la consistencia exige muchos choques con exposición dispersa.
- Validez para España: alternativa a GPSS; con pocos países de origen de gran peso (Marruecos, Rumanía, Colombia…) la condición de «muchos choques» puede fallar; hay que informar del número efectivo de choques.
- Replicación pública: paquete y datos públicos (https://github.com/borusyak/shift-share; Zenodo, https://doi.org/10.5281/zenodo.4516266; comando de Stata ssaggregate en SSC).
- Estado: VERIFICADA (Crossref)

## 2. España

### Carrasco, Jimeno y Ortega (2008). The effect of immigration on the labor market performance of native-born workers: some evidence for Spain
- DOI: 10.1007/s00148-006-0112-9 · Revista: Journal of Population Economics 21(3)
- Leído: resumen (de la versión de trabajo FEDEA DT 2004-17, «The effect of immigration on the employment opportunities of native-born workers: some evidence for Spain», https://documentos.fedea.net/pubs/dt/2004/dt-2004-17.pdf; PDF consultado sha256 a6887218c16d02cc00aa53841affa670f0ecdfb7b2eaf18369b1640c3e7106f8; IDEAS no publica resumen de la versión de revista)
- Diseño e identificación: efecto de la inmigración legal y total sobre la tasa de empleo de los nativos, con y sin movilidad ocupacional y geográfica de inmigrantes y nativos, con varias muestras y estimadores (celdas región × ocupación).
- Datos, país y periodo: España, segunda mitad de los noventa; registro de permisos de trabajo de extranjeros, EPA y censos de 1991 y 2001.
- Resultado principal (con su unidad, tal como lo da el autor): no encuentran un efecto negativo significativo sobre la tasa de empleo nativa; elasticidad en torno a −0,17 con solo inmigrantes legales, no significativa al incluir legales e irregulares. La versión publicada añade salarios (no leído).
- Validez para España: directa, pero periodo previo al gran auge (2000–2008) y con flujos pequeños (permisos ≈ 1,5 % de la población activa en 2000). Réplica prevista en el plan; los permisos de trabajo históricos y los censos son públicos en agregados.
- Replicación pública: no público (sin paquete); datos de base parcialmente públicos (censos 1991 y 2001 y EPA del INE; serie de permisos de trabajo en anuarios públicos del Ministerio de Trabajo).
- Estado: VERIFICADA (Crossref)

### González y Ortega (2011). How do very open economies adjust to large immigration flows? Evidence from Spanish regions
- DOI: 10.1016/j.labeco.2010.06.001 · Revista: Labour Economics 18(1)
- Leído: resumen (https://ideas.repec.org/a/eee/labeco/v18y2011i1p57-70.html)
- Diseño e identificación: variación entre regiones españolas de las llegadas de inmigrantes, instrumentada con la localización de los asentamientos de inmigrantes de los años ochenta; descomposición del ajuste en salarios, empleo, intensidad de factores dentro de las ramas y composición de la producción (modelo de economía abierta).
- Datos, país y periodo: España, 2001–2006, regiones; población nacida fuera del 6 % al 13 % (más de tres millones de llegadas).
- Resultado principal (con su unidad, tal como lo da el autor): las llegadas de inmigrantes poco cualificados no redujeron salarios ni tasas de empleo de los trabajadores poco cualificados de las regiones receptoras; el aumento de la oferta se absorbió con más empleo, mediante cambios de intensidad de cualificación dentro de las ramas (comercio, construcción, hostelería, servicio doméstico) y no por cambios en la composición sectorial de la producción. El resumen no da elasticidades.
- Validez para España: máxima; réplica prevista en el plan con datos ampliados (padrón por país de nacimiento y EPA hasta 2025). Hereda la crítica de Jaeger, Ruist y Stuhler (2018).
- Replicación pública: no público (sin paquete localizado); datos de base públicos (EPA y padrón del INE; la versión publicada usa además la Encuesta de Estructura Salarial, cuyos microdatos son públicos).
- Estado: VERIFICADA (Crossref)

### Amuedo-Dorantes y De la Rica (2007). Labour market assimilation of recent immigrants in Spain
- DOI: 10.1111/j.1467-8543.2007.00614.x · Revista: British Journal of Industrial Relations 45(2)
- Leído: resumen (https://api.openalex.org/works/doi:10.1111/j.1467-8543.2007.00614.x)
- Diseño e identificación: análisis descriptivo-econométrico de asimilación en empleo y ocupación según años de residencia (cohortes de llegada en sección cruzada).
- Datos, país y periodo: España; Censo de Población 2001 y Encuesta de Estructura Salarial 2002.
- Resultado principal (con su unidad, tal como lo da el autor): hay asimilación de empleo y ocupacional a medida que se alarga la residencia, con diferencias significativas por sexo, origen y nivel educativo (el resumen no da magnitudes).
- Validez para España: directa; con sección cruzada no se separa asimilación de efectos de cohorte ni de retorno selectivo.
- Replicación pública: no público (sin paquete); datos de base públicos (microdatos del Censo 2001 y de la EES 2002 del INE).
- Estado: VERIFICADA (Crossref)

### Amuedo-Dorantes y De la Rica (2011). Complements or substitutes? Task specialization by gender and nativity in Spain
- DOI: 10.1016/j.labeco.2011.02.002 · Revista: Labour Economics 18(5)
- Leído: resumen (https://ideas.repec.org/a/eee/labeco/v18y2011i5p697-707.html)
- Diseño e identificación: réplica para España del enfoque de especialización por tareas de Peri y Sparber (2009), por sexo.
- Datos, país y periodo: España, década en la que la cuota inmigrante pasa del 4 % al 13 %; la fuente concreta no figura en el resumen.
- Resultado principal (con su unidad, tal como lo da el autor): la inmigración cambió la especialización por tareas de los nativos sin alterar su nivel de empleo; el efecto sobre la oferta relativa de tareas de los nativos es aproximadamente el doble que en EE. UU.; el dominio del idioma no basta para explicarlo (muchos inmigrantes hispanohablantes) y el efecto difiere por sexo.
- Validez para España: directa; referencia para P2 del plan.
- Replicación pública: no público (sin paquete localizado); datos de base no verificados en el resumen.
- Estado: VERIFICADA (Crossref)

### Amuedo-Dorantes y De la Rica (2010). Immigrants' responsiveness to labor market conditions and their impact on regional employment disparities: evidence from Spain
- DOI: 10.1007/s13209-009-0002-y · Revista: SERIEs 1(4)
- Leído: resumen (https://api.openalex.org/works/doi:10.1007/s13209-009-0002-y)
- Diseño e identificación: elección regional de residencia de los inmigrantes en función de las oportunidades de empleo para su cualificación, y efecto de las llegadas sobre las disparidades regionales de la tasa de empleo.
- Datos, país y periodo: España, EPA 1999–2007.
- Resultado principal (con su unidad, tal como lo da el autor): los inmigrantes eligen regiones con tasas de empleo más altas para su cualificación; el choque migratorio solo redujo temporalmente las disparidades regionales de tasa de empleo (sin magnitudes en el resumen).
- Validez para España: directa; confirma la endogeneidad de la localización que exige el instrumento en P1.
- Replicación pública: no público (sin paquete); datos de base públicos (microdatos de la EPA del INE). Texto abierto en https://link.springer.com/content/pdf/10.1007/s13209-009-0002-y.pdf
- Estado: VERIFICADA (Crossref)

### Izquierdo, Lacuesta y Vegas (2009). Assimilation of immigrants in Spain: a longitudinal analysis
- DOI: 10.1016/j.labeco.2009.08.011 · Revista: Labour Economics 16(6) (versión previa: Documento de Trabajo del Banco de España 0904)
- Leído: texto completo (versión de trabajo, Banco de España DT 0904: https://repositorio.bde.es/bitstream/123456789/6982/1/dt0904e.pdf; la versión de Labour Economics no se ha leído) y resumen (https://ideas.repec.org/a/eee/labeco/v16y2009i6p669-678.html)
- Diseño e identificación: asimilación salarial con un panel longitudinal nuevo (seguimiento de los mismos individuos), que separa la convergencia dentro de la empresa de la movilidad entre empresas.
- Datos, país y periodo: España; un panel nuevo de datos individuales (el resumen no lo nombra; probablemente registros de la Seguridad Social del tipo MCVL, no comprobado).
- Resultado principal (con su unidad, tal como lo da el autor): en los primeros 5–6 años tras la llegada los inmigrantes cierran unos 15 puntos porcentuales de la brecha salarial con los nativos, sin cerrarla del todo; más rápido para sudamericanos y nacionales de los nuevos Estados miembros de la UE que para africanos; la mayor parte se debe a acumulación de capital humano dentro de la misma empresa más que a la movilidad.
- Cifras leídas en la versión de trabajo (congelación, a posteriori): MCVL 2005, varones de 25-54 años de fuera de la UE-15, mediana censurada; brecha de entrada −0,305 / −0,282 log en el corte transversal y −0,395 / −0,406 en el panel (tabla 2, p. 23); recuperación de +0,143 / +0,115 a los 5-6 años y +0,201 / +0,183 con más de 13 años en el panel; en el texto (pp. 22-24), unos 20 puntos a partir de 8 años y sin más reducciones. Es decir, se cierra en torno a la mitad de la brecha de entrada y se detiene.
- Validez para España: directa; ancla el rango de convergencia c ∈ [0; 0,5] del ciclo vital de M1 (comparación con nativos de igual experiencia, educación y cohorte, no de igual edad).
- Replicación pública: no público. Si la fuente es la MCVL (a confirmar en el texto completo), queda excluida por la regla A: NO ESTIMABLE la réplica longitudinal; solo cabe una aproximación por cohortes sintéticas con la EPA o la EES.
- Estado: VERIFICADA (Crossref)

### Simón, Sanromá y Ramos (2008). Labour segregation and immigrant and native-born wage distributions in Spain: an analysis using matched employer–employee data
- DOI: 10.1007/s10108-007-9035-1 · Revista: Spanish Economic Review 10(2)
- Leído: resumen (https://diposit.ub.edu/dspace/handle/2445/64968?mode=full)
- Diseño e identificación: descomposición de las diferencias en la distribución salarial entre inmigrantes y nativos, con atención a la segregación ocupacional y por establecimiento.
- Datos, país y periodo: España; datos emparejados empresa-trabajador (el resumen no nombra la encuesta; por el tipo de datos corresponde a la Encuesta de Estructura Salarial, a confirmar).
- Resultado principal (con su unidad, tal como lo da el autor): los inmigrantes de países en desarrollo tienen salarios medios menores y una distribución más comprimida que los nativos; los de países desarrollados, salarios medios mayores y distribución más dispersa; la mayor parte de las diferencias se explica por características observadas, sobre todo la segregación ocupacional y por centro de trabajo (sin magnitudes en el resumen).
- Validez para España: directa; base para la descomposición (Oaxaca-Blinder/DFL) de las brechas en tres niveles exigida por el plan.
- Replicación pública: no público (sin paquete); si es la EES, datos de base públicos (microdatos del INE). Versión aceptada abierta en el depósito de la UB (hdl.handle.net/2445/64968).
- Estado: VERIFICADA (Crossref)

### Simón, Ramos y Sanromá (2014). Immigrant occupational mobility: longitudinal evidence from Spain
- DOI: 10.1007/s10680-014-9313-1 · Revista: European Journal of Population 30(2)
- Leído: resumen (https://ideas.repec.org/a/spr/eurpop/v30y2014i2p223-255.html)
- Diseño e identificación: trayectoria ocupacional desde el país de origen hasta España con información retrospectiva longitudinal (una de las pocas encuestas que recogen el empleo en ambos países).
- Datos, país y periodo: España; encuesta a inmigrantes con historia laboral en origen y destino (el resumen no la nombra; por su descripción corresponde a la Encuesta Nacional de Inmigrantes 2007, a confirmar).
- Resultado principal (con su unidad, tal como lo da el autor): la situación ocupacional en España es sustancialmente peor que en el país de origen, por un fuerte descenso inicial y una movilidad ascendente muy lenta; la evidencia encaja con la asimilación segmentada (movilidad bloqueada por un amplio segmento secundario) y no con la trayectoria en U observada en otros países avanzados (sin magnitudes en el resumen).
- Validez para España: directa; documenta el «downgrading» que, según Dustmann, Schönberg y Stuhler (2016), sesga los enfoques por celdas de cualificación.
- Replicación pública: no público (sin paquete); si es la ENI 2007, microdatos públicos del INE.
- Estado: VERIFICADA (Crossref)

### Fernández-Huertas Moraga, Ferrer-i-Carbonell y Saiz (2019). Immigrant locations and native residential preferences: emerging ghettos or new communities?
- DOI: 10.1016/j.jue.2019.06.002 · Revista: Journal of Urban Economics 112
- Leído: resumen (https://ideas.repec.org/a/eee/juecon/v112y2019icp133-151.html)
- Diseño e identificación: cuasi experimento con la oleada migratoria española 1998–2008 (población +10 %); respuesta residencial de los nativos a las llegadas en barrios.
- Datos, país y periodo: España, 1998–2008 (fuentes no detalladas en el resumen).
- Resultado principal (con su unidad, tal como lo da el autor): desplazamiento leve de nativos desde barrios densos y consolidados, acompañado de más construcción residencial en esas zonas; nativos e inmigrantes se mudan a la vez a nuevos suburbios en expansión, de modo que la segregación agregada no cambia; los métodos convencionales sobrestiman la «huida» de nativos.
- Validez para España: directa, pero es un trabajo de movilidad residencial, no de mercado de trabajo: se ficha porque condiciona la elección de la unidad geográfica (la salida de nativos de la unidad sesga hacia cero los efectos locales). Para vivienda, se enlaza con docs/literatura/vivienda.md.
- Replicación pública: no público (sin paquete localizado); versión de trabajo abierta en https://doi.org/10.2139/ssrn.5241963.
- Estado: VERIFICADA (Crossref)

### Fernández-Huertas Moraga (2021). Inmigración y políticas migratorias en España
- DOI: sin DOI · Revista: FEDEA, Estudios sobre la Economía Española 2021/10
- Leído: resumen (https://ideas.repec.org/p/fda/fdaeee/eee2021-10.html)
- Diseño e identificación: síntesis descriptiva de la inmigración y de la política migratoria española.
- Datos, país y periodo: España, hasta enero de 2020.
- Resultado principal (con su unidad, tal como lo da el autor): la inmigración es probablemente el principal motor del cambio demográfico español del siglo XXI; el 14,8 % de la población había nacido fuera en enero de 2020; lo singular de España fue la facilidad de entrada de latinoamericanos por tratados bilaterales no pensados para regular flujos, por lo que la inmigración no respondió a una política diseñada para atraerla. El resumen no contiene resultados sobre salarios o empleo de nativos.
- Validez para España: contexto institucional (canales de entrada, regularizaciones) útil para defender el instrumento; no aporta una estimación de efectos laborales.
- Replicación pública: no aplica (síntesis); texto abierto en https://documentos.fedea.net/pubs/eee/eee2021-10.pdf
- Estado: NO VERIFICADA (sin DOI)

### Gálvez-Iniesta (2025). Inmigración y mercado de trabajo: revisión y evidencia para España
- DOI: sin DOI · Revista: FEDEA, Estudios sobre la Economía Española 2025/15
- Leído: texto completo (https://documentos.fedea.net/pubs/eee/2025/eee2025-15.pdf; PDF consultado sha256 b9d035c6e029f2efe28eeb7239c66d89dc4dd48a34514428d26a338f913eb6d6; lectura de la aplicación empírica y las conclusiones)
- Diseño e identificación: revisión de enfoques (estructural, espacial y por celdas) y aplicación propia por celdas educación (3 niveles) × experiencia potencial (8 tramos de 5 años) con variables instrumentales basadas en asentamientos pasados por país de origen, educación y experiencia; efectos fijos e interacciones; errores agrupados por celda.
- Datos, país y periodo: España, EPA 2005–2024 (trimestral).
- Resultado principal (con su unidad, tal como lo da el autor): coeficiente IV del log de la cuota inmigrante sobre el log de la tasa de empleo nativa de la celda: 0,038 (significativo solo al 10 %) en 2005–2024; 0,191 (al 1 %) en 2005–2013; −0,028 (al 5 %) en 2014–2024 (−0,042 en hombres). F de Kleibergen-Paap 123. El autor lo lee como elasticidad, pero en el texto lo traduce como «+1 % de cuota → +3,8 % de empleo», lectura incoherente con un coeficiente log-log de 0,038 (debería ser ≈ +0,04 %); conviene citar el coeficiente, no la traducción.
- Validez para España: directa y reciente, la más próxima a lo que hará P1 con datos públicos; limitaciones: enfoque de efecto relativo (sensible al «downgrading»), 1.944 observaciones con pocas celdas (24) para agrupar errores (exige wild cluster bootstrap), y la definición de inmigrante en la EPA (nacionalidad o nacimiento) no se ha comprobado.
- Replicación pública: paquete no publicado; datos de base públicos (microdatos trimestrales de la EPA del INE), por lo que es reproducible.
- Estado: NO VERIFICADA (sin DOI)

### Cuadrado, Gómez y Sastre (2024). Una caracterización de los flujos migratorios hacia España y otros países de la Unión Europea
- DOI: 10.53479/37372 · Revista: Banco de España, Boletín Económico 2024/T3, artículo 06
- Leído: texto completo (https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/24/T3/Fich/be2403-art06.pdf; PDF consultado sha256 9ca256e133b8e1699a87fd582f3b2e8aec6930f9b1a7a7896724df576e4f6eb0; lectura de las ideas principales y la introducción)
- Diseño e identificación: descriptivo comparado (sin identificación causal): origen, sexo, edad, educación y participación laboral de los inmigrantes que llegan a España frente a Alemania, Francia, Italia, Suecia y Países Bajos.
- Datos, país y periodo: estadísticas de migraciones internacionales y encuestas de fuerza de trabajo (Eurostat, INE), hasta 2022–2024.
- Resultado principal (con su unidad, tal como lo da el autor): los inmigrantes en España proceden sobre todo de Latinoamérica, son de más edad, con más nivel educativo y mayor presencia femenina que en otros destinos; su tasa de actividad es de las más altas de la UE y, a diferencia de otros países, superior a la de los nacionales; se concentran en actividades de baja exigencia formativa con indicios recientes de desplazamiento a sectores más cualificados; en 2022 la población extranjera residente era el 17,1 %.
- Validez para España: hechos C1 para la sección 3 del documento; no aporta efectos.
- Replicación pública: no hay paquete; los datos de base son públicos (Eurostat e INE).
- Estado: VERIFICADA (Crossref)

### Cuadrado y Regil (2025). Una estimación de la contribución de la población extranjera en España al crecimiento del PIB per cápita en el período 2022-2024
- DOI: 10.53479/40025 · Revista: Banco de España, Boletín Económico 2025/T2, artículo 10
- Leído: texto completo (https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/25/T2/Fich/be2502-art10.pdf; PDF consultado sha256 e1b800069dcd136730e70379a5a9a06f30d3e6019199feceefe438864f345c66; lectura de las ideas principales, la introducción y el método)
- Diseño e identificación: descomposición contable (mecánica) del PIB per cápita en factor demográfico (16–67 años), tasa de empleo, horas por ocupado y productividad por hora, por nacionalidad y por país de nacimiento; no identifica efectos de equilibrio general.
- Datos, país y periodo: España, 2022–2024; Contabilidad Nacional, EPA (desde 2005) y Encuesta de Estructura Salarial para la productividad relativa por ramas (la EES solo cubre extranjeros en situación regular).
- Resultado principal (con su unidad, tal como lo da el autor): el PIB per cápita creció un 2,9 % anual medio; la aportación directa de la población extranjera sería de 0,4 a 0,7 puntos porcentuales, similar en términos relativos a otras expansiones, condicionada por la asimilación de los llegados a principios de siglo y por la mejora educativa y ocupacional de los recientes. A finales de 2024, 6,7 millones de extranjeros por nacionalidad (13,8 %) y casi 9 millones de nacidos fuera (18,4 %), según la EPA.
- Validez para España: directa; capa C2 (contabilidad con supuestos), útil para la fase 4 y para el debate de la fase 6; no es evidencia causal sobre los nativos.
- Replicación pública: no hay paquete; datos de base públicos (CN, EPA y EES del INE): reproducible.
- Estado: VERIFICADA (Crossref)

### Banco de España (2026). Informe Anual 2025
- DOI: 10.53479/43565 · Revista: Banco de España, Informe Anual 2025 (capítulo 1, apartado 4.5 «El papel de la inmigración en el actual ciclo expansivo de la economía española», gráficos 1.27–1.28, y apartado sobre salarios)
- Leído: texto completo (https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/PublicacionesAnuales/InformesAnuales/25/InfAnual_2025.pdf; PDF consultado sha256 6e8f806640969f264c5803565fb75a880654e201d026b58de0c56aaf0e7fce87; lectura de los apartados sobre inmigración, sus notas metodológicas y el párrafo sobre salarios de nativos)
- Diseño e identificación: (a) descomposición contable del crecimiento 2022–2025; (b) MC2E provincia-año con la cuota inmigrante en la población en edad de trabajar instrumentada por un shift-share à la Card (2001) (asentamientos históricos por país de origen × choques nacionales por origen), efectos fijos de provincia y año, controles provinciales variables y, en algunas especificaciones, tendencias lineales provinciales; (c) ejercicio exploratorio provincial sobre salarios de nativos; (d) modelo de gravedad estructural (PPML) para contrafactuales de política migratoria.
- Datos, país y periodo: España; EPA 1999–2025 (empleo, actividad, paro y composición sectorial), padrón continuo (stock y flujos por provincia y país de origen), microdatos censales; gravedad con datos 2008–2019 (ONU, OCDE, OIT, MIPEX).
- Resultado principal (con su unidad, tal como lo da el autor): la población inmigrante habría explicado unos 1,7 pp (alrededor de la mitad) del crecimiento del PIB y algo más de dos tercios del crecimiento del empleo en 2022–2025, y 0,5 pp del crecimiento medio anual del PIB per cápita (2,7 %); sin efectos estadísticamente significativos sobre la tasa de empleo de los nativos, con reasignación de los nativos desde agricultura, industria y construcción hacia servicios; las provincias con más inmigración no muestran una evolución salarial nativa significativamente distinta (el propio informe advierte de que ello es compatible con presiones a la baja compensadas por cambios de composición); con una política migratoria más restrictiva (laxa) las entradas brutas serían en torno a un 20 % menores (mayores). El informe no publica coeficientes ni errores en el texto principal.
- Validez para España: directa y la más reciente; diseño muy próximo a P1. Pendiente: no se informa de inferencia AKM/BHJ, pesos de Rotemberg ni corrección de Jaeger, Ruist y Stuhler; la definición de origen (nacionalidad o nacimiento) no se precisa en la nota.
- Replicación pública: no hay paquete; datos de base públicos (EPA y padrón del INE): el diseño es reproducible en P1.
- Estado: VERIFICADA (Crossref)

## 3. Europa

### Dustmann, Frattini y Preston (2013). The effect of immigration along the distribution of wages
- DOI: 10.1093/restud/rds019 · Revista: Review of Economic Studies 80(1)
- Leído: resumen (https://api.openalex.org/works/doi:10.1093/restud/rds019)
- Diseño e identificación: efectos a lo largo de la distribución salarial de los nativos sin preasignar a los inmigrantes a celdas de cualificación (los sitúa por su posición observada en la distribución), con variación regional.
- Datos, país y periodo: Reino Unido (fuentes y años no detallados en el resumen).
- Resultado principal (con su unidad, tal como lo da el autor): fuerte «downgrading» de los inmigrantes al llegar; la inmigración reduce salarios por debajo del percentil 20 y los eleva ligeramente en la parte alta; efecto medio ligeramente positivo.
- Validez para España: alta como método (EES por percentiles y provincia/CC. AA.), dado el «downgrading» documentado en España.
- Replicación pública: paquete no localizado; datos de base (Labour Force Survey británica) distribuidos por el UK Data Service con registro y condiciones de uso: no cumplen con certeza la regla A, a comprobar.
- Estado: VERIFICADA (Crossref)

### Foged y Peri (2016). Immigrants' effect on native workers: new analysis on longitudinal data
- DOI: 10.1257/app.20150114 · Revista: American Economic Journal: Applied Economics 8(2)
- Leído: resumen (https://api.openalex.org/works/doi:10.1257/app.20150114)
- Diseño e identificación: cuasi experimento con la política danesa de dispersión de refugiados (1986–1998) entre municipios; seguimiento longitudinal de los trabajadores nativos poco cualificados.
- Datos, país y periodo: Dinamarca, registros administrativos del universo de trabajadores, 1991–2008.
- Resultado principal (con su unidad, tal como lo da el autor): la mayor oferta de inmigrantes de países de refugiados llevó a los nativos menos educados (sobre todo jóvenes y con poca antigüedad) a ocupaciones menos manuales, con efectos positivos sobre sus salarios, empleo y movilidad ocupacional (sin magnitudes en el resumen).
- Validez para España: media; el mecanismo de reasignación coincide con el del Banco de España (2026), pero la asignación cuasi aleatoria no tiene equivalente en España y el panel individual requeriría la MCVL (excluida): la versión longitudinal es NO ESTIMABLE con datos públicos.
- Replicación pública: programas públicos en openICPSR (proyecto 113642, https://doi.org/10.3886/E113642V1); datos administrativos daneses restringidos (Statistics Denmark): no reproducible.
- Estado: VERIFICADA (Crossref)

### Edo (2019). The impact of immigration on the labor market
- DOI: 10.1111/joes.12300 · Revista: Journal of Economic Surveys 33(3)
- Leído: resumen (https://api.openalex.org/works/doi:10.1111/joes.12300)
- Diseño e identificación: revisión de la literatura.
- Datos, país y periodo: no aplica (síntesis internacional).
- Resultado principal (con su unidad, tal como lo da el autor): el efecto de la inmigración sobre el salario y el empleo medios de los nativos es nulo o ligeramente positivo; las llegadas inesperadas pueden tener efectos inmediatos negativos porque el ajuste lleva tiempo; hay efectos distributivos: caen los salarios de los nativos con cualificaciones parecidas a las de los inmigrantes y suben los de los complementarios.
- Validez para España: marco para la fase 6 (distinguir efecto medio, efecto distributivo y corto frente a largo plazo).
- Replicación pública: no aplica (revisión).
- Estado: VERIFICADA (Crossref)

## Tabla de la pregunta

| trabajo | diseño | datos | resultado (unidad) | validez para España |
|---|---|---|---|---|
| Card (2001) | espacial, ciudad × ocupación; asentamientos previos | Censo EE. UU. 1990 | −1 a −3 pp en salario y tasa de empleo de nativos poco cualificados en ciudades de entrada; sin salida de nativos | alta como diseño; replicable con EPA + padrón |
| Borjas (2003) | celdas nacionales educación × experiencia | censos y CPS EE. UU. | elasticidad salarial −0,3 a −0,4 (10 % más oferta → −3/−4 % salario) | efecto relativo; sesgo por downgrading |
| Ottaviano y Peri (2012) | estructural CES anidada | EE. UU. 1990–2006 | +0,6 % a +1,7 % salario nativos sin secundaria; +0,6 % media nativa; −6,7 % inmigrantes previos (largo plazo) | depende de elasticidades y del capital |
| Peri y Sparber (2009) | especialización por tareas | censos EE. UU. + O*NET | nativos hacia tareas comunicativas; efecto salarial modesto (sin cifra en resumen) | relevante para P2; canal idioma más débil |
| Dustmann, Schönberg y Stuhler (2016) | revisión y modelo canónico | — | efectos relativos no comparables; preferir efecto total | guía del pre-registro |
| Jaeger, Ruist y Stuhler (2018) | shift-share con instrumentación múltiple | censos EE. UU. 1960–2010, áreas metropolitanas | impacto inicial más negativo y recuperación posterior de magnitud similar | crítica central; España tiene cambios de composición útiles |
| Goldsmith-Pinkham, Sorkin y Swift (2020) | econometría de Bartik (cuotas) | EE. UU. | pesos de Rotemberg (metodológico) | prueba obligatoria |
| Adão, Kolesár y Morales (2019) | inferencia shift-share | EE. UU., placebo | rechazo del nulo hasta 55 % con errores convencionales al 5 % | inferencia obligatoria |
| Borusyak, Hull y Jaravel (2022) | shift-share por choques | EE. UU. (ADH) | metodológico | exige muchos orígenes con peso disperso |
| Carrasco, Jimeno y Ortega (2008) | celdas región × ocupación | permisos de trabajo, EPA, censos 1991–2001 | elasticidad de la tasa de empleo nativa ≈ −0,17 (legales), no significativa (totales) | directa; periodo previo al auge |
| González y Ortega (2011) | IV regional, asentamientos de los ochenta | regiones españolas 2001–2006 | sin efecto en salarios ni empleo de poco cualificados; ajuste por intensidad de factores dentro de ramas | directa; réplica prevista |
| Amuedo-Dorantes y De la Rica (2007) | asimilación en sección cruzada | Censo 2001, EES 2002 | asimilación de empleo y ocupacional heterogénea (sin cifra en resumen) | directa |
| Amuedo-Dorantes y De la Rica (2011) | tareas por sexo y origen | España (cuota 4 %→13 %) | cambio de tareas nativas ≈ 2 veces el de EE. UU.; empleo nativo sin cambio | directa; P2 |
| Amuedo-Dorantes y De la Rica (2010) | elección regional y disparidades | EPA 1999–2007 | localización endógena; menor disparidad regional solo temporal | directa |
| Izquierdo, Lacuesta y Vegas (2009) | panel longitudinal | datos administrativos (probable MCVL) | −15 pp de brecha salarial en 5–6 años | directa; réplica NO ESTIMABLE si es MCVL |
| Simón, Sanromá y Ramos (2008) | descomposición de distribuciones | emparejados empresa-trabajador | brechas explicadas sobre todo por segregación ocupacional y de centro | directa; base de Oaxaca/DFL |
| Simón, Ramos y Sanromá (2014) | movilidad ocupacional origen-destino | encuesta longitudinal retrospectiva | downgrading inicial fuerte y movilidad lenta (asimilación segmentada) | directa |
| Fernández-Huertas Moraga, Ferrer-i-Carbonell y Saiz (2019) | cuasi experimento residencial | España 1998–2008 | desplazamiento leve de nativos; segregación agregada sin cambio | unidad geográfica de P1 |
| Fernández-Huertas Moraga (2021) | síntesis institucional | España hasta 2020 | 14,8 % nacidos fuera; entrada latinoamericana por tratados | contexto del instrumento |
| Gálvez-Iniesta (2025) | IV por celdas educación × experiencia | EPA 2005–2024 | coef. log-log empleo nativo: 0,038 (2005–24, 10 %), 0,191 (2005–13), −0,028 (2014–24) | directa, reproducible |
| Cuadrado, Gómez y Sastre (2024) | descriptivo comparado UE | Eurostat, INE hasta 2024 | actividad de extranjeros mayor que la de nacionales; 17,1 % extranjeros (2022) | hechos C1 |
| Cuadrado y Regil (2025) | descomposición contable | CN, EPA, EES 2022–2024 | 0,4–0,7 pp del 2,9 % anual de crecimiento del PIB per cápita | C2, no causal |
| Banco de España (2026) | MC2E provincia-año con shift-share de Card | EPA 1999–2025, padrón | empleo nativo: efecto no significativo; reasignación a servicios; salarios provinciales sin diferencia significativa; 1,7 pp del PIB 2022–2025 | directa; falta AKM/BHJ y JRS |
| Dustmann, Frattini y Preston (2013) | efectos por percentil | Reino Unido | caída bajo el percentil 20, ligera subida arriba; media ligeramente positiva | método aplicable con EES |
| Foged y Peri (2016) | dispersión de refugiados, panel | registros daneses 1991–2008 | efectos positivos en salario, empleo y movilidad de nativos poco cualificados | mecanismo sí; panel NO ESTIMABLE |
| Edo (2019) | revisión | internacional | efecto medio nulo o ligeramente positivo; distributivo y de corto plazo negativo posible | marco para fase 6 |

Reproducibles con datos públicos (candidatos a réplica en fase 5): Gálvez-Iniesta (2025) y el ejercicio del Banco de España (2026) (EPA + padrón), González y Ortega (2011) y Carrasco, Jimeno y Ortega (2008) (agregados públicos del INE y anuarios de permisos), Cuadrado y Regil (2025) (CN + EPA + EES). Paquetes de código públicos localizados: Goldsmith-Pinkham, Sorkin y Swift (openICPSR 117405), Borusyak, Hull y Jaravel (GitHub/Zenodo), Adão, Kolesár y Morales (ShiftShareSE en CRAN) y Foged y Peri (openICPSR 113642, solo código; datos restringidos).

## Qué esperamos en España y por qué

1. Efecto medio sobre la tasa de empleo nativa por provincia cercano a cero: lo encuentran González y Ortega (2011) para 2001–2006, Carrasco, Jimeno y Ortega (2008) para los noventa y el Banco de España (2026) para 1999–2025 con un diseño casi idéntico al de P1.
2. Efecto medio sobre salarios nativos pequeño y difícil de distinguir de cero; si aparece, negativo en la parte baja de la distribución y nulo o positivo arriba (Dustmann, Frattini y Preston 2013; Edo 2019), porque la inmigración española se ha concentrado en ocupaciones poco cualificadas.
3. Reasignación sectorial y por tareas de los nativos hacia servicios y tareas comunicativas, posiblemente más intensa que en EE. UU. (Amuedo-Dorantes y De la Rica 2011; Banco de España 2026).
4. Diferencias entre el corto y el largo plazo: con el instrumento convencional, la estabilidad de los asentamientos puede mezclar ajustes; España tiene cambios marcados de composición por origen entre olas, lo que permite aplicar la instrumentación múltiple de Jaeger, Ruist y Stuhler (2018). Hay que esperar efectos de corto plazo más negativos que los de largo plazo y que el signo dependa del periodo (Gálvez-Iniesta 2025: positivo en 2005–2013, ligeramente negativo en 2014–2024).
5. Inferencia: con unas 50 provincias y pocos orígenes de gran peso, los intervalos AKM/BHJ serán bastante más anchos que los convencionales (Adão, Kolesár y Morales 2019); lo más probable es que muchos resultados queden en SUGESTIVO y no en IDENTIFICADO.
6. Asimilación: brechas salariales brutas grandes, explicadas en buena parte por composición y segregación ocupacional (Simón, Sanromá y Ramos 2008), con convergencia parcial en los primeros años (≈ 15 pp en 5–6 años, Izquierdo, Lacuesta y Vegas 2009) y fuerte «downgrading» inicial (Simón, Ramos y Sanromá 2014); la réplica longitudinal es NO ESTIMABLE sin la MCVL y habrá que usar cohortes sintéticas con EPA/EES.
