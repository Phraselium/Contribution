ESTUDIO M1 · CONTRIBUCIÓN E IMPACTO ECONÓMICO DE LA POBLACIÓN SEGÚN SU ORIGEN: ESPAÑA POR PROVINCIA Y EUROPA POR PAÍS Y REGIÓN (SOLO INFORMACIÓN PÚBLICA)
Objetivo: solo con información pública y descargable sin solicitud, medir con estándar de Documento de Trabajo del Banco de España:
(A) la CONTRIBUCIÓN de cada grupo de origen (nacidos en España y por región de nacimiento o nacionalidad) al empleo, a los ingresos y gastos públicos, a la vivienda y a los salarios, en España por provincia y en Europa por país y región NUTS2 (NUTS3 donde haya datos);
(B) el IMPACTO causal de la inmigración sobre el empleo, los salarios, los servicios públicos y la vivienda de la población local, cuando el diseño lo permita.
Son dos preguntas distintas y nunca se mezclan: (A) es contabilidad; (B) requiere identificación.

PRIMER PASO: crea docs/plan.md con este mensaje completo, sin resumir, y un CLAUDE.md con las reglas de la sección A y la línea «Leer docs/plan.md y docs/estado.md al empezar o tras compactar». Commit y push.

══════════════════════════════════════
A. REGLAS
══════════════════════════════════════
- SOLO INFORMACIÓN PÚBLICA. Se usan únicamente:
  - datos y microdatos descargables libremente sin registro ni solicitud;
  - o, como máximo, con un registro gratuito y automático en la web de la fuente.
  Quedan excluidos: la Muestra Continua de Vidas Laborales, los microdatos de investigación de la EU-LFS y la EU-SILC, las solicitudes por transparencia y cualquier dato de acceso restringido.
  Cada fuente se documenta con su URL, su licencia, la fecha de descarga y su checksum. Si un dato necesario no es público, la pregunta queda NO ESTIMABLE o se imputa con supuestos explícitos, y se dice. No se generan tareas para pedir datos al autor.
- Idioma: español. Todo reproducible sin red con los datos versionados o con checksum; SEED=20261019 en todo lo aleatorio.
- Infraestructura de referencia: el repositorio público https://github.com/Phraselium/Econometr-a (rama claude/housing-price-spain-econometric-95dhj3). Clónalo en un directorio aparte, SOLO para lectura, y adapta de él lo que sirva: capas, clasificación de V18, hooks y guardas, subagentes de .claude/agents/, verificador de referencias, cifras_clave, Registry y check. No copies sus datos.
- Neutralidad y rigor en las dos direcciones:
  - se evalúan afirmaciones y políticas, nunca personas, partidos ni grupos como tales;
  - lo favorable y lo desfavorable a cualquier grupo se mide con el mismo estándar y se publica igual;
  - sin corrección política y sin sesgo de confirmación;
  - nunca se atribuyen rasgos a un grupo: se describen agregados y su variación interna.
- Comparaciones siempre en tres niveles: bruto; ajustado por edad y sexo; ajustado además por educación, años de residencia y región. Las diferencias brutas se descomponen (Oaxaca-Blinder o reponderación DFL) en composición y resto.
- Definiciones de origen fijadas antes de mirar datos:
  - país de nacimiento como principal; nacionalidad como sensibilidad;
  - grupos: nacidos en España; UE-14; UE-13 y otros de Europa; América Latina; Magreb; resto de África; Asia; resto;
  - nacionalizados y segunda generación se separan cuando los datos lo permitan.
  Se documenta qué permite cada fuente: muchas solo distinguen «española / extranjera» o grandes regiones.
- Protección de datos: solo agregados. Supresión de celdas con menos de 50 observaciones muestrales o con riesgo de identificación.
- Capas: C1 hechos (al menos dos fuentes independientes o dato oficial); C2 cotas con supuestos explícitos; C3 efectos identificados; C4 exploratorio.
- Clasificación de efectos:
  - IDENTIFICADO;
  - SUGESTIVO;
  - ASOCIACIÓN;
  - NO ESTIMABLE, indicando qué dato público faltaría o si solo existe con acceso restringido.
  Sin lenguaje causal fuera de IDENTIFICADO.
- Inferencia convencional:
  - errores agrupados al nivel del tratamiento;
  - wild cluster bootstrap (pesos de Webb) con menos de 40 clusters;
  - AKM o Borusyak-Hull-Jaravel en shift-share;
  - Conley en datos espaciales;
  - F efectivo e intervalos de Anderson-Rubin con instrumentos;
  - Holm para confirmatorias y BH para exploratorias.
  Con microdatos de encuesta, pesos muestrales y errores que respeten el diseño (estratos y conglomerados cuando la fuente los publique; si no, se dice).
- Pre-registro interno: antes de la fase 5 (efectos causales), plan fijado en docs/preregistro.md con la etiqueta local prereg-m1. Un hook bloquea las estimaciones causales sin ella. Si el proxy no deja subir la etiqueta, el hook acepta la etiqueta local con su commit en la rama remota. Se declara que no tiene sello externo.
- Referencias: VERIFICADA (DOI en Crossref) o NO VERIFICADA; nada no leído al menos en su resumen. PDFs solo de fuentes abiertas legítimas, en data/bib/pdf/ (ignorado por git) con checksum; al repositorio van fichas y enlaces, nunca el PDF ni párrafos copiados. Prensa solo para localizar originales.
- Excel: azul los datos introducidos (con su fuente en nota), negro lo calculado en la hoja, verde lo que viene de otra pestaña. Sin paneles inmovilizados. Maquetación limpia.
- Guardas: prohibido borrar datos crudos y rehacer todo sin orden del autor; ficheros con Write o heredoc entrecomillado; un solo make check a la vez; push solo a la rama de trabajo; ficheros de más de 50 MB a LFS o ignorados con checksum (si una fuente pública pesa mucho, se versionan el script de descarga y el checksum).
- Trabajo en docs/, src/, output/, tests/ y publicacion/ (generada, nunca a mano). Estado tras cada tarea en docs/estado.md. Commit por tarea. Si una fase supera 6 millones de tokens de subagentes, para y explícalo.

══════════════════════════════════════
B. INFRAESTRUCTURA
══════════════════════════════════════
- Makefile con objetivos m1_f0 … m1_f7, check, publicacion y web.
- Comandos /m1-fase0 … /m1-fase7 y /m1-estado.
- Subagentes adaptados de Econometr-a: bibliotecario, adquisidor-datos, ingeniero-datos, modelizador, montecarlo, replicador-ciego, replicador-estudio, abogado-del-diablo, arbitro-final, redactor y verificador-cifras. Como máximo 3 que escriban a la vez, en worktrees.
- Hooks: las guardas anteriores; bloqueo de la fase 5 sin prereg-m1; bloqueo de descargas desde dominios que exijan solicitud o credenciales no públicas. Tests que demuestren que bloquean.
- cifras_clave.csv como única fuente de cifras difundibles, con capa, fuente, periodo, ámbito y grupo de origen.

══════════════════════════════════════
C. FASES
══════════════════════════════════════
FASE 0 · Montaje e inventario de lo público
1. Infraestructura B.
2. docs/fuentes_publicas.md: para cada variable que necesita el estudio, qué fuente pública la da, con qué desagregación por origen (país, región, solo «española / extranjera»), territorial y temporal, y con qué limitaciones.
3. Lista de lo que NO es público y qué pregunta queda afectada. Esa lista no genera tareas; va a limitaciones.

FASE 1 · Bibliografía y métodos (en paralelo, hasta 3 bibliotecario)
Descarga, ficha y verificación de, al menos, las referencias siguientes. Lo que va entre paréntesis es un punto de partida a verificar, no un hecho.
- Impacto fiscal:
  - OCDE, International Migration Outlook 2021, capítulo sobre el impacto fiscal de la inmigración (método común para 25 países);
  - Dustmann y Frattini (2014), Economic Journal (Reino Unido);
  - Christl et al. (JRC, Comisión Europea, impacto fiscal de la inmigración en la UE);
  - estudios con datos administrativos de Países Bajos (CPB y van de Beek et al.) y Dinamarca (Ministerio de Finanzas), con su controversia metodológica;
  - estudios españoles (Banco de España, AIReF sobre pensiones y migración, FEDEA y otros).
- Mercado de trabajo:
  - Card (2001); Borjas (2003); Ottaviano y Peri (2012);
  - Dustmann, Schönberg y Stuhler (2016), Journal of Economic Perspectives, sobre por qué los estudios discrepan;
  - Jaeger, Ruist y Stuhler (2018), sobre el sesgo del instrumento de asentamientos;
  - España: Carrasco, Jimeno y Ortega (2008); González y Ortega (2011); Amuedo-Dorantes y De la Rica; Fernández-Huertas Moraga; documentos del Banco de España sobre inmigración y empleo de 2023-2026.
- Vivienda: González y Ortega (2013), Saiz (2007) y la bibliografía del estudio de vivienda de Econometr-a (docs/v18/bib si existe).
- Servicios públicos: congestión en sanidad y educación (localizar y verificar, en España y en Europa).
Una tabla por pregunta: diseño, datos, resultado con su unidad y validez para España. Reproducción solo de los estudios cuyo paquete de replicación y datos sean públicos.

FASE 2 · Datos públicos (en paralelo, hasta 3 adquisidor-datos; cada fuente con URL, licencia, edición, fecha y checksum)
España:
- Población y flujos (INE):
  - Estadística Continua de Población y padrón por país de nacimiento y nacionalidad, provincia, edad y sexo;
  - Estadística de Variaciones Residenciales y de Migraciones;
  - Censo 2021: tablas y microdatos públicos (educación, ocupación, vivienda por origen).
- Empleo:
  - EPA (microdatos trimestrales públicos; documentar qué variables de origen incluyen y con qué agrupación);
  - afiliación a la Seguridad Social por nacionalidad, régimen, sector y provincia (estadísticas públicas de la Seguridad Social);
  - paro registrado y contratos por nacionalidad (estadísticas públicas del SEPE).
- Salarios:
  - Encuesta de Estructura Salarial (microdatos públicos del INE; verificar qué variable de nacionalidad incluyen);
  - deciles salariales de la EPA;
  - Encuesta Anual de Coste Laboral si sirve.
- Ingresos públicos imputables:
  - cotizaciones con afiliación y bases medias publicadas;
  - IRPF imputado con la renta de la ECV (microdatos públicos) y un simulador fiscal documentado;
  - IVA e impuestos especiales imputados con la EPF (microdatos públicos);
  - IBI e impuestos sobre la vivienda según tenencia.
- Gasto público imputable:
  - educación: estadísticas públicas de alumnado extranjero del Ministerio de Educación y gasto por alumno;
  - sanidad: perfil público de gasto por edad y sexo (Ministerio de Sanidad o estudios publicados) aplicado a cada estructura de edad, con sensibilidad a diferencias de uso documentadas en la literatura;
  - pensiones y prestaciones: estadísticas públicas del INSS y la Seguridad Social por nacionalidad si existen, perfiles por edad si no;
  - desempleo: estadísticas públicas del SEPE por nacionalidad;
  - Ingreso Mínimo Vital y rentas mínimas: estadísticas públicas por nacionalidad si existen;
  - ayudas a la vivienda;
  - bienes públicos puros (defensa, deuda, administración general), con dos criterios: coste medio y coste marginal cero;
  - gasto público por funciones (IGAE, COFOG) y por comunidad.
- Vivienda: tenencia, hacinamiento, esfuerzo y tipo de hogar por origen (ECV, Censo 2021).
- Contexto provincial: PIB y renta (INE, Atlas de Distribución de Renta de los Hogares), estructura sectorial y precios de vivienda (la base pública de Econometr-a si su licencia lo permite).
Europa:
- Eurostat, agregados públicos:
  - población por país de nacimiento y ciudadanía por país y NUTS2;
  - empleo, paro y actividad por país de nacimiento y ciudadanía (tablas de la EU-LFS por país y NUTS2);
  - renta, pobreza, privación y vivienda por país de nacimiento (tablas de la EU-SILC);
  - flujos migratorios;
  - proyecciones de población.
- Microdatos de uso público de Eurostat (public microdata files de la EU-LFS y la EU-SILC): solo como complemento. Están anonimizados y su cobertura de países y años es limitada; se documenta y no se usan para inferencia fina por región.
- OCDE: International Migration Outlook, Indicators of Immigrant Integration (OCDE/UE) y resultados publicados de impacto fiscal por país.
- JRC: resultados publicados de impacto fiscal por país.

FASE 3 · Hechos descriptivos (contribución A, sin causalidad)
Por grupo de origen, en España (nacional, comunidad y provincia) y en Europa (país y NUTS2), en los tres niveles de la sección A, según lo que permita cada fuente pública:
1. Población y estructura por edad; flujos; años de residencia.
2. Empleo: tasas de actividad, empleo y paro; contribución de cada grupo al crecimiento del empleo y de las horas; sectores y ocupaciones; temporalidad y parcialidad; sobrecualificación.
3. Salarios: niveles y brechas por decil; descomposición de la brecha (composición frente a resto); convergencia con los años de residencia, con cohortes de llegada cuando la fuente lo permita y sin confundir cohorte y residencia.
4. Vivienda: tenencia, hacinamiento, esfuerzo y peso en la demanda de vivienda nueva por provincia.
5. Uso de prestaciones y servicios donde haya datos públicos, con la misma lectura bruta y ajustada.
Resultados con capa y supresión de celdas pequeñas.

FASE 4 · Contabilidad fiscal (contribución A)
1. Contribución fiscal neta estática anual por grupo de origen, en España y por comunidad (provincia si la imputación lo aguanta), con el método de la OCDE de 2021 adaptado: ingresos imputados menos gastos imputados; bienes públicos con coste medio y con coste marginal; intervalo por los supuestos de imputación. Cada partida indica si es dato observado o imputado y con qué fuente pública.
2. Contribución neta a lo largo del ciclo vital: valor actual por grupo y edad de llegada, con escenarios de convergencia de empleo y salarios, retorno al país de origen y tasas de descuento. Separa claramente el efecto «población joven hoy» del de las pensiones futuras.
3. Sensibilidad: qué supuestos cambian el signo y cuáles no.
4. Europa: comparación con los resultados publicados de la OCDE y del JRC por país; replicación aproximada con agregados de la EU-SILC donde sea posible.
5. Contribución a la sostenibilidad de las pensiones: proyección con y sin flujos migratorios, con las proyecciones públicas del INE (2026-2076) y de Eurostat, comparada con los informes públicos de la AIReF y el Ageing Report de la Comisión Europea.
Todo es contabilidad con supuestos (capa C2 o C4): no identifica efectos.

FASE 5 · Impacto causal (B), solo con prereg-m1
Pre-registro antes de estimar: preguntas, diseños, pruebas, multiverso y correcciones. Revisión de abogado-del-diablo; adenda; etiqueta.
Preguntas mínimas:
- P1 Salarios y empleo de la población local:
  - shift-share de llegadas por provincia y por celdas de educación y edad (Card, Borjas), con microdatos públicos de la EPA, la Estructura Salarial y el Censo, e inferencia AKM o BHJ;
  - corrección del sesgo de ajuste dinámico (Jaeger, Ruist y Stuhler);
  - efectos de corto y largo plazo;
  - réplica de Carrasco, Jimeno y Ortega y de González y Ortega con datos públicos ampliados.
- P2 Ocupaciones y movilidad de la población local (Peri y Sparber): ¿se desplaza hacia tareas más comunicativas o mejor pagadas?
- P3 Servicios públicos: congestión en sanidad y educación (listas de espera públicas, ratios de alumnado y de profesionales por provincia). Si no hay series públicas suficientes, NO ESTIMABLE.
- P4 Vivienda: enlace con el estudio de vivienda (réplica de González y Ortega 2013 de Econometr-a V18 si existe); no se duplica.
- P5 Europa: el mismo diseño por NUTS2 con agregados públicos de la EU-LFS, comparando países con instituciones distintas.
Pruebas mínimas:
- pretendencias del instrumento;
- pruebas de Rotemberg;
- exclusión de los orígenes de más peso;
- placebos;
- robustez a la definición de origen (nacimiento frente a nacionalidad);
- montecarlo para cada herramienta;
- replicador-ciego y abogado-del-diablo para todo lo que quede IDENTIFICADO o SUGESTIVO.

FASE 6 · Síntesis crítica
Para cada afirmación frecuente del debate público sobre inmigración y economía (localiza las más repetidas en ambos sentidos, sin atribuirlas a partidos), una ficha:
- qué dice la contabilidad;
- qué dice la evidencia causal;
- qué depende de supuestos;
- veredicto («se sostiene», «se sostiene con matices», «engañosa», «incorrecta», «no se puede saber») con su confianza.
Mismas reglas para las afirmaciones favorables y las desfavorables a la inmigración.

FASE 7 · Documento
publicacion/documento_m1/, generado con make, con formato de Documento de Trabajo del Banco de España:
- resumen ejecutivo de 1 página y resumen no técnico;
- 1. Introducción;
- 2. Datos públicos y definiciones;
- 3. Hechos (empleo, salarios, vivienda, prestaciones) en España por provincia y en Europa;
- 4. Contabilidad fiscal estática y de ciclo vital, con sus supuestos;
- 5. Impacto sobre la población local;
- 6. Pensiones y demografía;
- 7. Afirmaciones del debate y su veredicto;
- 8. Limitaciones, incluida una sección «Qué cambiaría con datos no públicos» (MCVL, microdatos de investigación de Eurostat, datos administrativos de uso de servicios).
Anexos: métodos, pruebas por estimación, supuestos fiscales, inventario de fuentes públicas con URL y fecha, bibliografía con estado de verificación y declaración de pre-registro interno.
Además: tablas_m1.xlsx con la convención de colores, figuras y mapas por provincia y NUTS2. arbitro-final como revisor de Documentos de Trabajo (ACEPTAR, REVISAR o REHACER). verificador-cifras comprueba cada número. make publicacion y make check limpios.

══════════════════════════════════════
D. PARADAS
══════════════════════════════════════
- Una guarda que no bloquea.
- Un resultado que solo se sostenga con un supuesto fiscal arbitrario: se documenta, se muestra la sensibilidad y se espera mi decisión antes de citarlo.
- Cualquier riesgo de identificar a personas en los agregados.
- Más de 6 millones de tokens de subagentes en una fase.

En cada parada y al final de cada fase, resumen de 250 palabras como máximo. Resumen final de 500 palabras como máximo:
- principales hechos por grupo y territorio;
- contribución fiscal neta (estática y de ciclo vital) con sus intervalos;
- efectos causales encontrados y su clasificación;
- veredictos de las afirmaciones;
- qué no se ha podido estimar por falta de datos públicos.

Empieza ahora: plan.md, CLAUDE.md, infraestructura B y fases 0 a 7 seguidas, deteniéndote solo en las paradas.
