# Literatura · Impacto fiscal de la inmigración y pensiones (M1, fase 1)

Preparado por el subagente bibliotecario el 2026-10-19. Fichas sin estado: la línea «Estado» la rellena `src/m1/verificar_referencias.py`.

Notas de método de esta búsqueda:
- DOI comprobados uno a uno en api.crossref.org (título, autores, revista y año). Cuando Crossref no tiene el DOI se dice en la ficha.
- Los PDF abiertos se descargaron solo al scratchpad de la sesión (por instrucción, en esta tarea solo se escribe este fichero). Se anota su sha256 para que `adquisidor-datos` o el verificador puedan volver a guardarlos en `data/bib/pdf/` y comprobar que son los mismos.
- Bloqueos de acceso durante la búsqueda (2026-10-19): oecd.org y oecd-ilibrary.org devolvieron 403, airef.es devolvió 503 (y además su cadena TLS no valida con el proxy), y los PDF de publications.jrc.ec.europa.eu y Wiley quedaron bloqueados por su cortafuegos. Por eso las cifras por país de la OCDE 2021 y las de la AIReF 2025 no se leyeron en el original (ver la sección «Pendientes»).
- Las cifras van con la unidad que da cada autor. Ninguna se ha recalculado.

---

## 1. Estudios internacionales con método común

### Damas de Matos, A. (OCDE) (2021). The fiscal impact of immigration in OECD countries since the mid-2000s (International Migration Outlook 2021, cap. 4)
- DOI: 10.1787/29f23e9d-en (libro, en Crossref); el DOI del capítulo, 10.1787/4ccb6899-en, lo resuelve Crossref como alias del DOI del libro (respuesta 301) · Revista: International Migration Outlook (OCDE, serie anual)
- Leído: resumen (resumen del capítulo en OpenAlex, https://api.openalex.org/works/doi:10.1787/4ccb6899-en, y página de la OCDE https://www.oecd.org/en/publications/international-migration-outlook-2021_29f23e9d-en.html, vista a través del buscador; el texto completo devolvió 403)
- Diseño e identificación: contabilidad fiscal estática anual. Ingresos y gastos públicos se reparten entre nacidos en el país y nacidos fuera con un método común para todos los países. Desglose por partida de gasto e ingreso y análisis de los determinantes socioeconómicos de la posición fiscal. Escenarios con y sin bienes públicos (coste medio frente a marginal) y una simulación contrafactual en la que los inmigrantes en edad central tienen la tasa de empleo de los nativos del mismo sexo y nivel educativo. Es contabilidad: no identifica efectos causales.
- Datos, país y periodo: 25 países de la OCDE, cada año de 2006 a 2018. Encuestas de hogares (EU-SILC en los países europeos) combinadas con cuentas públicas por funciones. Colaboraron Chojnicki, Ragot y Sakthivel.
- Resultado principal (con su unidad, tal como lo da el autor): según el resumen, la contribución fiscal neta total de los inmigrantes fue pequeña en todo el periodo, entre −1 % y +1 % del PIB en la mayoría de los países. Los impuestos y cotizaciones que pagan los inmigrantes superan en promedio el gasto en su protección social, sanidad y educación. Al incluir todo el gasto público, la contribución es positiva en alrededor de un tercio de los países. El factor que más explica las diferencias con los nativos es el peso de la edad central de trabajo (25-54 años). Si se imputa a los inmigrantes el coste educativo de sus hijos nacidos en el país, la contribución baja en promedio unos 0,5 puntos de PIB. Las cifras por país (España incluida) están en un anexo XLS de la OCDE que no se pudo descargar. La prensa atribuye a este capítulo, para España en 2006-2018, alrededor de −0,15 % del PIB para los inmigrantes frente a −5,2 % para los nativos. Esa cifra NO se ha leído en el original y no debe usarse hasta comprobarla.
- Validez para España: alta. España está entre los 25 países y el método está pensado para compararlos; es la referencia que la fase 4 adapta. Límites: es una foto anual que depende del ciclo (2008-2015 fue de crisis en España) y de cómo se reparten los bienes públicos.
- Replicación pública: no público como paquete. El método está documentado en el capítulo y sus anexos, y los datos de entrada (EU-SILC agregada y COFOG) son públicos en parte; la EU-SILC en microdatos de investigación es restringida.
- Estado: NO VERIFICADA (discrepa: primer autor (OECD))

### Christl, M., Bélanger, A., Conte, A., Mazza, J. y Narazani, E. (2021). The fiscal impact of immigration in the EU
- DOI: sin DOI · Revista: JRC Working Papers on Taxation and Structural Reforms n.º 01/2021 (JRC124744); también GLO Discussion Paper n.º 814
- Leído: texto completo (versión GLO DP 814, https://www.econstor.eu/bitstream/10419/232517/1/GLO-DP-0814.pdf; ficha JRC https://publications.jrc.ec.europa.eu/repository/handle/JRC124744). PDF local: sha256 e731ddb43e53e5fd3316ef1c9575eb84cdf75380d16aa2250e8a5181ef716b77
- Diseño e identificación: microsimulación estática con EUROMOD. A los impuestos directos, cotizaciones y prestaciones monetarias se suman el IVA imputado (con la Encuesta de Presupuestos Familiares de Eurostat de 2010) y las prestaciones en especie (educación, sanidad, vivienda social). Hay dos indicadores. El impacto fiscal neto medio (ANFI) es una media de corte transversal. El déficit de ciclo vital (LCD) suma los perfiles por edad de 0 a 80 años, con sensibilidad a 75 y 85, y elimina las diferencias de estructura por edad. No incluye bienes públicos puros. Es contabilidad, no identificación.
- Datos, país y periodo: EU-SILC 2015 a través de EUROMOD, 27 Estados miembros más el Reino Unido. Origen definido por país de nacimiento: nativos, nacidos en otro país de la UE y nacidos fuera de la UE. Se reponderan las muestras para corregir la infrarrepresentación de inmigrantes.
- Resultado principal (con su unidad, tal como lo da el autor): en la media de la UE en 2015 el ANFI, en euros por persona y año, es −476 para nativos, −208 para nacidos en la UE y −219 para nacidos fuera; los inmigrantes aportan unos 250 € al año más que los nativos. Con el LCD de 0 a 80 años el orden se invierte: −723 € nativos, −1.106 € UE y −2.600 € fuera de la UE (cifras de la tabla 1; el texto da −2.411 en un lugar, una discrepancia interna). En España el ANFI de los nacidos en otro país de la UE es mayor que el de los nativos. Las cifras por país solo vienen en gráficos, no en tabla numérica. Los autores advierten que el LCD imputa al país de acogida una educación que muchos inmigrantes recibieron en origen.
- Validez para España: alta y directa (España está en la muestra y el método es común). Límites: un solo año (2015, con paro aún alto), sin bienes públicos y sin cifras numéricas por país. La comparación de la fase 4 tendrá que leer los gráficos o pedir los valores al JRC, y lo segundo queda fuera de las reglas.
- Replicación pública: no público. EUROMOD es de acceso libre con registro, pero sus datos de entrada EU-SILC son microdatos de investigación restringidos.
- Estado: NO VERIFICADA (sin DOI)

### Christl, M., Bélanger, A., Conte, A., Mazza, J. y Narazani, E. (2022). Projecting the fiscal impact of immigration in the European Union
- DOI: 10.1111/1475-5890.12314 · Revista: Fiscal Studies 43(4), 365-385
- Leído: resumen (Crossref, https://api.crossref.org/works/10.1111/1475-5890.12314; el PDF abierto de Wiley devolvió 403)
- Diseño e identificación: la contabilidad estática del documento de 2021, más un modelo demográfico de microsimulación dinámica que proyecta el impacto fiscal neto de la inmigración hacia el futuro (la versión JRC de 2020, JRC121937, llega hasta 2035).
- Datos, país y periodo: EU-SILC y EUROMOD, UE-27; proyección desde mediados de la década de 2010.
- Resultado principal (con su unidad, tal como lo da el autor): de nuevo, los inmigrantes aportan en promedio más que los nativos en la foto anual, pero menos con perfiles de edad (ciclo vital); los nacidos fuera de la UE, menos que los nacidos en la UE. En la proyección, la migración dentro de la UE suaviza el efecto fiscal negativo del envejecimiento pero no basta para compensarlo. El resumen no da cifras por país.
- Validez para España: media-alta. Es útil para separar el efecto «población joven hoy» del de las pensiones futuras, que la fase 4 pide separar. Hay que leer el texto completo para extraer las cifras de España.
- Replicación pública: no público (el modelo de proyección no está publicado y los microdatos EU-SILC son restringidos).
- Estado: VERIFICADA (Crossref)

### Fiorio, C. V., Frattini, T., Riganti, A. y Christl, M. (2023). Migration and public finances in the EU
- DOI: 10.1007/s10797-023-09787-9 · Revista: International Tax and Public Finance 31(3), 635-684 (en línea en 2023; número de 2024). Versión previa: JRC Working Papers on Taxation and Structural Reforms n.º 05/2022
- Leído: texto completo (https://sites.unimi.it/tommasofrattini/wp-content/uploads/2023/12/s10797-023-09787-9.pdf, acceso abierto). PDF local: sha256 5d512988ddecc4bcd37e4b6242093ab5c9ef1b54d138103bbfe2a5cd425d6700
- Diseño e identificación: contabilidad estática anual con EUROMOD, sumando impuestos indirectos y prestaciones en especie (educación, sanidad, vivienda social). Las brechas entre migrantes y nativos se comparan en bruto y condicionadas a variables demográficas y a la situación laboral, una descomposición de composición. No se incluyen bienes públicos puros, impuestos especiales ni impuesto de sociedades. La cobertura del gasto es menor que la del ingreso, y los autores avisan de que importa la comparación entre grupos, no el nivel.
- Datos, país y periodo: EU-SILC con EUROMOD y agregados de Eurostat, UE-14, 2014-2018; detalle para Francia, Alemania, Italia, España y Suecia. Origen por país de nacimiento. En España el modelo cubre alrededor del 70 % del gasto y el 84 % del ingreso agregados.
- Resultado principal (con su unidad, tal como lo da el autor): contribución fiscal neta (NFC) media en € de 2018 por persona y año, 2014-2018. UE-14: nativos +32, migrantes +1.510. España: nativos −814, migrantes +793, es decir, unos 1.600 € más por migrante. Italia: nativos −16, migrantes unos 2.870 € más. Alemania: nativos +439, migrantes +3.705. Francia: nativos +341, migrantes −1.167. Suecia: nativos +1.816, migrantes +623. En España, con la misma composición por edad y sexo, la NFC de los migrantes no difiere significativamente de la de los nativos en ningún año; al añadir la situación laboral, la brecha se aplana. La ventaja bruta es por tanto de composición.
- Validez para España: muy alta. Usa la misma fuente pública agregada que la fase 4 (EU-SILC), aplica la descomposición que exigen las reglas y da cifras de España.
- Replicación pública: no público (microdatos de investigación EU-SILC, restringidos). Es aproximable con los ficheros de uso público de la EU-SILC y con agregados.
- Estado: VERIFICADA (Crossref)

### Boffi, G., Suari-Andreu, E. y van Vliet, O. (2024). The net fiscal position of migrants in Europe: trends and insights
- DOI: sin DOI · Revista: TransEuroWorkS Working Paper 2/2024 (Horizonte Europa, n.º 101061198)
- Leído: texto completo (https://transeuroworks.eu/wp-content/uploads/2024/05/The-net-fiscal-position-of-migrants-in-Europe_WP.pdf). PDF local: sha256 df05c186c04de14060c77487130ce7c5db787fc503d385896a808b3759431fab
- Diseño e identificación: contabilidad estática individual de abajo arriba: impuestos sobre la renta y cotizaciones, simulados con los parámetros fiscales de la OCDE, menos prestaciones monetarias contributivas y no contributivas. No incluye IVA, gasto en especie ni bienes públicos. Analiza tendencias en el tiempo. Es descriptivo.
- Datos, país y periodo: EU-SILC transversal, 15 países de la UE, 2007-2018; nativos, nacidos en la UE y nacidos fuera de la UE.
- Resultado principal (con su unidad, tal como lo da el autor): posición fiscal neta media en €, ajustada por inflación y PPA, 2007-2018. España: nativos −1.756, nacidos en la UE −242, nacidos fuera −161. Media de los países: −1.585, −469 y −493. Con esta definición estrecha, los tres grupos reciben en neto en casi todos los países. La crisis de 2008-2011 empeora a todos; hacia 2017 los migrantes recuperan su nivel previo y los nativos no. En el sur de Europa (Grecia, Italia, Portugal, España) la diferencia a favor de los migrantes es más clara, y se debe sobre todo a que los nativos reciben más pensiones contributivas.
- Validez para España: media. Es útil como cota con solo partidas monetarias directas y por la serie temporal que cruza la crisis. No es comparable en nivel con la OCDE o el JRC, porque omite IVA y gasto en especie.
- Replicación pública: no público (EU-SILC de investigación). Los parámetros fiscales de la OCDE (Taxing Wages) son públicos.
- Estado: NO VERIFICADA (sin DOI)

## 2. Reino Unido

### Dustmann, C. y Frattini, T. (2014). The fiscal effects of immigration to the UK
- DOI: 10.1111/ecoj.12181 · Revista: The Economic Journal 124(580), F593-F643
- Leído: texto completo de la versión de documento de trabajo (Centro Studi Luca d'Agliano WP n.º 359, noviembre de 2013, https://www.dagliano.unimi.it//media/WP2013_359.pdf; el resumen coincide con el de la revista según OpenAlex). PDF local: sha256 24bb551892a5f5db340008259d75f6d43ddf1c93e1595c00ffa5af8b43e85305
- Diseño e identificación: contabilidad fiscal estática anual y acumulada (en £ de 2011). Los ingresos y gastos públicos se imputan por grupo con encuestas. Los bienes públicos puros (alrededor del 23 % del gasto: defensa, órganos ejecutivos y legislativos, etc.) se tratan con dos criterios, coste medio y coste marginal cero. Los autores eligen supuestos prudentes que, dicen, tienden a sobreestimar el coste neto de los inmigrantes; por ejemplo, imputan a los padres inmigrantes la educación de todos sus hijos.
- Datos, país y periodo: Reino Unido, 1995-2011/12; Labour Force Survey y otras encuestas, cuentas públicas. Grupos: nativos, inmigrantes del EEE y de fuera del EEE, y «recientes» (llegados desde 2000).
- Resultado principal (con su unidad, tal como lo da el autor): en 1995-2011 los inmigrantes del EEE aportaron en neto unos 8.800 M£ y pagaron un 4 % más de lo que recibieron, mientras que los nativos tuvieron un saldo de unos −604.500 M£ y pagaron el 93 % de lo que recibieron. Los de fuera del EEE tuvieron un saldo acumulado negativo, explicado en parte por su mayor número de hijos y la imputación de su educación. Los inmigrantes recientes, en 2001-2011: EEE +22.100 M£ (un 34 % más pagado que recibido), fuera del EEE +2.900 M£ (un 2 % más) y nativos −624.100 M£ (el 89 %). La versión publicada en 2014 puede diferir algo en las cifras; hay que comprobarlas en la revista.
- Validez para España: media. El método (dos criterios para los bienes públicos, separar a los llegados recientemente) se puede trasladar. La composición de la inmigración y el sistema de pensiones del Reino Unido difieren mucho de los de España.
- Replicación pública: no público como paquete. La LFS británica está disponible en el UK Data Service con registro y licencia de usuario final, lo que la deja fuera del criterio de M1.
- Estado: VERIFICADA (Crossref)

## 3. Países Bajos y Dinamarca: datos administrativos y controversia metodológica

### van de Beek, J., Roodenburg, H., Hartog, J. y Kreffer, G. (2023). Borderless Welfare State: The Consequences of Immigration for Public Finances (2.ª edición revisada; original neerlandés «Grenzeloze verzorgingsstaat», 2021)
- DOI: sin DOI · Revista: libro, Uitgeverij Demo-Demo, Zeist (ISBN 9789083334820 / 9789083334837, PDF de libre descarga)
- Leído: texto completo, consulta parcial: resumen, glosario, cap. 4 (comparación con el CPB de 2003), cap. 6 (sensibilidad), cap. 7 (1995-2019) y cap. 8.13 (bienes públicos), en https://media.joomeo.com/original/656de2ca9bdbb.pdf (copia del PDF que los autores distribuyen en https://demo-demo.nl/en/). PDF local: sha256 9cb3ea689d663e4d19b24866ff310a1ed843f0c24c4f796f132f164dd6cfe187
- Diseño e identificación: contabilidad generacional con perfiles por edad de impuestos, cotizaciones, prestaciones y gasto en especie. Calcula el valor actual neto de la contribución de por vida de cada inmigrante desde su llegada hasta la emigración o la muerte, con una tasa real de descuento del 2,5 % como en el CPB y variantes. Separa por motivo de entrada, por 42 u 87 regiones de origen y por generación. Los bienes públicos (unos 94.000 M€) se reparten a partes iguales por persona, no según el PIB. Hay variantes para la tasa de descuento, la edad de la pensión pública y el reparto de los bienes públicos, y un escenario restrictivo de política migratoria. Es contabilidad.
- Datos, país y periodo: microdatos administrativos anonimizados de Statistics Netherlands (CBS) de toda la población, con perfiles de 2016; flujos de 1995-2019.
- Resultado principal (con su unidad, tal como lo da el autor): contribución neta de por vida, en valor actual (€): de media, unos +42.000 € por inmigrante occidental y unos −167.000 € por inmigrante no occidental. Como referencia, un nativo nacido en 2016 sale en unos −3.000 € y un residente medio nacido en 2016 en unos −65.000 €. Por motivo: inmigración laboral positiva; estudio, reagrupación familiar y asilo negativas, con unos −400.000 € para el asilo en edades de llegada de hasta unos 70 años. El coste neto acumulado de los llegados en 1995-2019 sería de unos 400.000 M€. El coste estático anual realizado en 2016 sería de unos 17.000 M€, y crecería hasta unos 50.000 M€ al año si continúan los flujos de 2015-2019. Con el escenario restrictivo, la inmigración sigue sin ser neutral para el presupuesto. Para la segunda generación, la contribución sigue de cerca a la de los padres.
- Validez para España: media-baja como cifra y alta como método. Las estructuras institucionales (prestaciones generosas, vivienda social amplia) y la composición de los flujos son distintas. Los supuestos que los autores muestran decisivos (reparto de bienes públicos, tasa de descuento, segunda generación) son los que la fase 4 debe someter a sensibilidad.
- Replicación pública: no público (los microdatos del CBS son de acceso restringido para investigadores autorizados).
- Estado: NO VERIFICADA (sin DOI)

### van de Beek, J., Hartog, J., Kreffer, G. y Roodenburg, H. (2024). The long-term fiscal impact of immigrants in the Netherlands, differentiated by motive, source region and generation
- DOI: sin DOI · Revista: IZA Discussion Paper n.º 17569 (diciembre de 2024)
- Leído: resumen (https://www.iza.org/publications/dp/17569/the-long-term-fiscal-impact-of-immigrantsin-the-netherlands-differentiated-by-motive-source-region-and-generation; PDF descargado de https://docs.iza.org/dp17569.pdf, solo se leyó el resumen). PDF local: sha256 31a78ba222062199d58992cc01ffdb0f2f407949aaa03ec7cbae229e38e5c253
- Diseño e identificación: es la versión de documento de trabajo del libro anterior: contribución neta de por vida descontada de la población inmigrante presente en 2016, por motivo y por hasta 87 regiones de origen. Añade un análisis de la segunda generación con las notas del examen Cito a los 12 años, el nivel educativo y los ingresos. Asocia las diferencias por región con un índice de distancia cultural respecto a la «Europa protestante»; es una correlación, no un efecto identificado.
- Datos, país y periodo: microdatos del CBS (población completa), Países Bajos, 2016.
- Resultado principal (con su unidad, tal como lo da el autor): según el resumen, la contribución neta de los inmigrantes laborales es positiva y la de los de estudio, familia y asilo es negativa. Para la segunda generación, las notas a los 12 años y el nivel educativo alcanzado son similares a los de nativos de origen social parecido, pero con la misma educación los ingresos son menores, y también su contribución neta. Los autores atribuyen la brecha a un menor rendimiento de la educación, no a menos educación. El resumen no da cifras en euros.
- Validez para España: media. Aporta la distinción por motivo de entrada y la segunda generación, que España solo puede aproximar con datos públicos (el padrón y la EPA no recogen el motivo de entrada).
- Replicación pública: no público (CBS restringido).
- Estado: NO VERIFICADA (sin DOI)

### Finansministeriet (Ministerio de Finanzas de Dinamarca) (2019). Indvandreres nettobidrag til de offentlige finanser i 2016 (Økonomisk Analyse)
- DOI: sin DOI · Revista: Økonomisk Analyse, Finansministeriet, Center for holdbarhed og strukturpolitik (ISBN 978-87-93531-63-5), abril de 2019
- Leído: texto completo (https://fm.dk/media/18011/indvandreres_nettobidrag_til_de_offentlige_finanser_i_2016_a.pdf). PDF local: sha256 5e70c2511f32bcbf7ca33f672be2e07d3c9f7d7286f94ca2a63c4c6c2f10b252. Las ediciones de 2018 (datos de 2018, publicada en 2021) y 2019 (publicada en 2023) devolvieron 404 en las URL encontradas.
- Diseño e identificación: contabilidad estática anual sobre registros administrativos individuales (base del modelo legal «Lovmodellen»). Se reparten todos los ingresos y gastos públicos: impuestos y transferencias individuales directamente; educación, sanidad y guarderías por actividad y coste unitario; impuesto de sociedades, impuestos sobre la producción y parte del consumo colectivo con claves de reparto. Grupos de Danmarks Statistik: personas de origen danés, inmigrantes y descendientes (segunda generación), occidentales o no occidentales; en otras ediciones, también MENAPT. Variante con el saldo corregido de partidas especiales.
- Datos, país y periodo: Dinamarca, 2016 (y 2015 revisado); 5,7 millones de residentes.
- Resultado principal (con su unidad, tal como lo da el autor): contribución neta en miles de millones de coronas (mia. kr.) de 2016. Personas de origen danés +28. Inmigrantes y descendientes −30 en total: no occidentales −35 (inmigrantes −18, descendientes −17) y occidentales +5 (inmigrantes +7, descendientes −2). Por persona, en miles de coronas: origen danés +6, inmigrantes no occidentales −56, descendientes no occidentales −118, inmigrantes occidentales +29. El 38 % de los inmigrantes no occidentales de 25 a 64 años aporta en neto; entre los ocupados, todos los motivos de residencia aportan en promedio. El saldo negativo de los descendientes se explica sobre todo porque son mayoritariamente niños y jóvenes. Al corregir partidas especiales (PAL-skat, impuesto de sociedades), la contribución de los de origen danés baja en 11 mia. kr.
- Validez para España: media. Es el caso de referencia con datos administrativos completos y método transparente, y muestra el peso de la estructura por edad (descendientes) y de las claves de reparto. España no tiene datos públicos equivalentes a este nivel individual.
- Replicación pública: no público (registros individuales de Danmarks Statistik con acceso restringido); el informe publica la metodología.
- Estado: NO VERIFICADA (sin DOI)

**Controversia metodológica (Países Bajos y Dinamarca).** En lo leído hay cuatro puntos de desacuerdo, y todos cambian la magnitud y a veces el signo:
1. *Bienes públicos.* Según van de Beek et al. (2023, cap. 4), el CPB en 2003 («Immigration and the Dutch economy», Roodenburg, Euwals y ter Rele, no leído en el original: la URL del CPB devolvió 404) repartía los bienes públicos en proporción a la contribución al PIB, lo que estrecha las diferencias entre grupos. van de Beek et al. los reparten a partes iguales por persona, lo que las agranda, y su sensibilidad muestra que el criterio cambia los niveles pero no el orden de los grupos. Dustmann y Frattini y la OCDE presentan las dos variantes (coste medio y coste marginal cero). Christl et al. y Fiorio et al. no los incluyen.
2. *Ciclo vital frente a foto anual.* La foto anual favorece a los grupos concentrados en edades de trabajo (OCDE; Fiorio et al.). Los perfiles de ciclo vital (Christl et al. LCD; van de Beek et al.) penalizan a los grupos con menos empleo e incluyen las pensiones futuras. El signo puede invertirse entre los dos enfoques (Christl et al. 2021).
3. *Segunda generación.* Dinamarca cuenta a los descendientes como grupo propio (negativo por su edad); van de Beek et al. los siguen de por vida; la OCDE estima que asignarlos a los padres resta unos 0,5 puntos de PIB, pero advierte que así no se cuentan los impuestos que pagarán de adultos.
4. *Imputación de la educación.* Dustmann y Frattini y Christl et al. señalan que imputar al país de acogida la educación de los hijos (y, en el ciclo vital, la de los propios inmigrantes) sesga contra los inmigrantes: la educación recibida en origen no le cuesta nada al país de acogida.
Hay además una disputa política: van de Beek et al. dicen que el Gobierno neerlandés declaró no necesitar ese tipo de información, y algunos economistas neerlandeses han cuestionado el estudio según la prensa (prensa usada solo para localizar). Se documenta como desacuerdo de método, sin tomar partido.

## 4. España

### Conde-Ruiz, J. I., Jimeno, J. F. y Valera, G. (2008). Inmigración y pensiones: ¿qué sabemos?
- DOI: 10.32796/cice.2008.75.5940 · Revista: Cuadernos Económicos de ICE n.º 75, 249-272
- Leído: texto completo (https://www.revistasice.com/index.php/CICE/article/download/5940/5940). PDF local: sha256 817286cea99ac3475eaa8dcd835d7b3cf4e611689c046f6d5fd068ce102cdf44
- Diseño e identificación: revisión de la literatura teórica y empírica sobre los canales por los que la inmigración afecta a un sistema de pensiones de reparto y prestación definida: tasa de dependencia, tasa de empleo, educación y economía política de la redistribución. No estima.
- Datos, país y periodo: no aplica (revisión, con referencias a España hasta 2007).
- Resultado principal (con su unidad, tal como lo da el autor): la llegada de inmigrantes en edad de trabajar retrasa la subida de la tasa de dependencia y mejora el saldo a medio plazo. Pero esos inmigrantes generan derechos a pensión, de modo que el problema pasa a la generación siguiente. A largo plazo, si los inmigrantes adoptan los patrones demográficos de los nativos, la inmigración no resuelve los desequilibrios financieros del sistema. Es una conclusión cualitativa.
- Validez para España: alta (escrita para España). Fija la distinción entre «población joven hoy» y pensiones futuras que pide la fase 4.
- Replicación pública: no aplica (revisión).
- Estado: VERIFICADA (Crossref)

### Jiménez-Ridruejo Ayuso, Z., Borondo Arribas, C., López Díaz, J., Lorenzo Lago, C. y Rodríguez Sumaza, C. (2009). El efecto de la inmigración en la sostenibilidad a largo plazo del sistema de pensiones en España
- DOI: sin DOI · Revista: Hacienda Pública Española / Review of Public Economics 188(1), 74-121
- Leído: resumen (https://ideas.repec.org/a/hpe/journl/y2009v1881p74-121.html)
- Diseño e identificación: modelo socioeconómico de simulación («Carrión») que proyecta hasta 2060 el gasto en pensiones de jubilación, las cotizaciones y el PIB. La conducta de los inmigrantes actuales y futuros (permanencia, fecundidad, salarios, empleo) se calibra con estimaciones econométricas. Es proyección con supuestos, no identificación.
- Datos, país y periodo: España, base hacia 2007, proyección a 2060.
- Resultado principal (con su unidad, tal como lo da el autor): la ratio de solvencia de los inmigrantes (cotizaciones sobre pensiones) es claramente mayor que la de los nativos hasta alrededor de 2055. Después, la de ambos grupos cae muy por debajo de los niveles actuales. El resumen no da valores numéricos.
- Validez para España: alta en el diseño. Los supuestos son anteriores a la Gran Recesión y a las reformas de 2011, 2013, 2021 y 2023, así que las cifras están desfasadas.
- Replicación pública: no público.
- Estado: NO VERIFICADA (sin DOI)

### Moreno Fuentes, F. J. y Bruquetas Callejo, M. (2011). Inmigración y Estado de bienestar en España (ed. inglesa: Immigration and the Welfare State in Spain)
- DOI: sin DOI · Revista: Colección Estudios Sociales n.º 31, Obra Social «la Caixa», Barcelona
- Leído: texto completo (edición inglesa, consulta parcial de la presentación, cap. 2 y cap. 6, https://documentation.lastradainternational.org/lsidocs/immigration%20and%20welfare%20in%20spain.pdf). PDF local: sha256 b267c30ea930a6d571d01284843d0c62af3a554318443173e84a344ac2af5b3d
- Diseño e identificación: estudio institucional y descriptivo del acceso y uso de prestaciones y servicios (sanidad, educación, servicios sociales, pensiones, desempleo) por los inmigrantes y de su contribución a la financiación. Para el saldo fiscal revisa estimaciones ajenas; no estima las suyas.
- Datos, país y periodo: España, hasta 2010 (padrón, afiliación, encuestas, informes oficiales).
- Resultado principal (con su unidad, tal como lo da el autor): recoge, de la Oficina Económica del Presidente (2006), que en 2005 los inmigrantes absorbieron el 5,4 % del gasto público (18.600 M€) y aportaron el 6,6 % de los ingresos (23.400 M€): un saldo neto de unos 4.780 M€, la mitad del superávit de ese año. De Dolado y Vázquez (2008) recoge un saldo positivo de unos 2.000 M€ en 2008, que se esperaba llegara a 3.000 M€ hacia 2010 y bajara a unos 1.500 M€ al año a finales de la década siguiente. Concluye que, por su estructura por edad, los inmigrantes serían contribuyentes netos durante al menos dos décadas, y que la crisis reduciría ese saldo por su concentración en sectores cíclicos.
- Validez para España: alta como síntesis anterior a la crisis. Las cifras de 2005-2008 vienen del auge y no se pueden extrapolar. Las fuentes originales (OEP 2006; Dolado y Vázquez, FEDEA 2008) no se han leído aquí.
- Replicación pública: no aplica (síntesis).
- Estado: NO VERIFICADA (sin DOI)

### Muñoz de Bustillo Llorente, R. y Grande Martín, R. (2017). Inmigración y Estado de bienestar en España
- DOI: 10.24241/AnuarioCIDOBInmi.2017.206 · Revista: Anuario CIDOB de la Inmigración 2017, 206-229
- Leído: resumen (página de CIDOB con el resumen y las conclusiones, https://www.cidob.org/publicaciones/inmigracion-estado-bienestar-espana)
- Diseño e identificación: análisis descriptivo con regresiones de la probabilidad de recibir prestaciones y de su cuantía, controlando por características observables, más una revisión del «efecto imán». Es ajuste por composición; no hay identificación causal. Nota: el encargo citaba a «Muñoz de Bustillo y Antón»; el trabajo localizado con este título es con Grande. Muñoz de Bustillo y Antón tienen trabajos afines (p. ej., sobre uso sanitario, 10.1007/s10198-009-0204-z) que corresponden a la pregunta de servicios públicos.
- Datos, país y periodo: ECV 2015, Encuesta Nacional de Salud y otras fuentes; España, hacia 2014-2015.
- Resultado principal (con su unidad, tal como lo da el autor): con controles, la probabilidad de recibir prestaciones monetarias es 4,7 puntos menor para los inmigrantes (16 sin controles), y reciben unos 1.400 € menos de cuantía (unos 320 € sin pensiones ni desempleo). El texto da también 1.500 y 400 €, una discrepancia interna. Rechazan la hipótesis de sobreuso. El uso sanitario es similar o menor, salvo urgencias hospitalarias (6 % frente a 3,5 %). Los inmigrantes eran el 52,5 % del empleo en servicio doméstico y cuidados en 2014. No encuentran un efecto imán apreciable.
- Validez para España: alta (datos españoles públicos: ECV y ENS). Sirve para el lado del gasto de la fase 4 y para los tres niveles de comparación.
- Replicación pública: datos públicos (microdatos ECV y ENS del INE, https://www.ine.es); no hay paquete de código.
- Estado: NO VERIFICADA (discrepa: primer autor (Catedrático de Economía Aplicada, Departamento de Economía Aplicada, Universidad de Salamanca))

### Hernández de Cos, P., Jimeno, J. F. y Ramos, R. (2017). El sistema público de pensiones en España: situación actual, retos y alternativas de reforma
- DOI: sin DOI · Revista: Banco de España, Documentos Ocasionales n.º 1701
- Leído: texto completo (consulta parcial: secc. 3, https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/DocumentosOcasionales/17/Fich/do1701.pdf)
- Diseño e identificación: descomposición contable del gasto en pensiones sobre PIB en cuatro factores (tasa de dependencia, inversa de la tasa de empleo, tasa de sustitución y participación de los salarios) y extrapolación ilustrativa. Revisión de modelos más completos.
- Datos, país y periodo: España; proyecciones del INE y de la Comisión de entonces (horizonte 2060-2066).
- Resultado principal (con su unidad, tal como lo da el autor): la tasa de dependencia dependerá sobre todo de la inmigración y de los cambios legales en la edad de jubilación, que fijan el tamaño de la población en edad de trabajar. Las proyecciones de entonces preveían una entrada neta pequeña hasta 2020, muy por debajo de la del auge. La inmigración entra como un factor más de la identidad contable; el documento no cuantifica un saldo fiscal de los inmigrantes.
- Validez para España: alta como marco contable para la proyección con y sin flujos de la fase 4 (punto 5). Los supuestos migratorios están superados.
- Replicación pública: la identidad es replicable con datos públicos (INE, Seguridad Social, Contabilidad Nacional); no hay paquete de código.
- Estado: NO VERIFICADA (sin DOI)

### Banco de España (2024). Informe Anual 2023, capítulo 2: Retos estructurales de la economía española
- DOI: sin DOI · Revista: Banco de España, Informe Anual 2023
- Leído: texto completo (sección de demografía y flujos migratorios, https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/PublicacionesAnuales/InformesAnuales/23/Fich/InfAnual_2023_Cap2.pdf). PDF local: sha256 97ca4245643745fab9e1e6de8629f8f34685296f846fa55e8928fb597ec15f61
- Diseño e identificación: análisis descriptivo y ejercicio contable sobre las proyecciones de población del INE de 2022: cuánto tendría que crecer la población nacida fuera en edad de trabajar para mantener constante la tasa de dependencia.
- Datos, país y periodo: España; INE (proyecciones 2022-2072), Eurostat; horizonte 2053.
- Resultado principal (con su unidad, tal como lo da el autor): la capacidad de la inmigración para frenar el envejecimiento es limitada. Para mantener la tasa de dependencia en su nivel actual durante 30 años, la población nacida fuera en edad de trabajar tendría que ser tres veces la que prevé el INE. Las proyecciones del INE ya suponen una ganancia neta acumulada por migración de casi 10 millones de personas hasta 2053. La prensa difundió la cifra de unos 24,7 millones de inmigrantes adicionales en edad de trabajar, que corresponde a este ejercicio; es un stock, no un flujo, y aquí no se ha comprobado el número en el texto.
- Validez para España: alta. Es la referencia oficial más reciente del Banco de España sobre demografía e inmigración. No es un cálculo de saldo fiscal: solo ofrece la cota demográfica.
- Replicación pública: datos públicos (proyecciones del INE, https://www.ine.es); el ejercicio se puede replicar con supuestos explícitos.
- Estado: NO VERIFICADA (sin DOI)

### García Díaz, M. Á. (2023). Nota sobre la evolución del sistema público de pensiones en la Opinión de la AIReF sobre la sostenibilidad de las Administraciones Públicas a largo plazo: la incidencia de la demografía
- DOI: sin DOI · Revista: FEDEA, Apuntes 2023/09 (abril de 2023)
- Leído: texto completo (copia en https://institutosantalucia.es/wp-content/uploads/2024/04/ap2023-09.pdf). PDF local: sha256 2cf9b4edd08e33c1f570c89e1d9792286066f040dc6cefa3c78b0ac94d1e5fc8
- Diseño e identificación: nota crítica que resume y discute los escenarios demográficos y de pensiones de la Opinión 1/23 de la AIReF y los compara con los supuestos del Ministerio de Inclusión. Contiene los escenarios migratorios de la AIReF tal como los cita el autor. Es proyección con supuestos.
- Datos, país y periodo: España, horizonte 2050 y 2070 (escenarios de la AIReF de 2023).
- Resultado principal (con su unidad, tal como lo da el autor): según esta nota, el escenario base de la AIReF supone un saldo migratorio neto medio de unas 235.000 personas al año (239.000 en otro pasaje) y una población de 50,3 millones en 2050; la proporción de extranjeros pasaría del 11,4 % en 2022 al 16 % en 2050 y al 20,1 % en 2070. Con flujos menores (206.000 al año) el gasto en pensiones subiría unas 3 décimas de PIB, y con flujos mayores (271.000) bajaría. Más crecimiento del PIB (+0,3 puntos al año) reduciría el gasto en pensiones en 1,2 puntos de PIB en 2050. Estas cifras de la AIReF NO se han leído en el original de la AIReF (inaccesible el 2026-10-19).
- Validez para España: alta como lectura de los escenarios de la AIReF. Hay que contrastarla con la Opinión original y con la de 2025.
- Replicación pública: no aplica (nota); el modelo de la AIReF no es público.
- Estado: NO VERIFICADA (sin DOI)

### Carrasco, R. (2026). Análisis de algunos efectos económicos de la inmigración en España
- DOI: sin DOI · Revista: Instituto Santalucía, informe (marzo de 2026)
- Leído: texto completo (secc. 5, impacto fiscal, https://institutosantalucia.es/wp-content/uploads/2026/03/informe-efectos-economicos-inmigracion-espana.pdf). PDF local: sha256 95d90f2bfac7cddd68c0673398ff3d99d2d9270ee275fe06c55a37ff6fbd1c51
- Diseño e identificación: síntesis de la evidencia sobre demografía, crecimiento, impacto fiscal, regularización, vivienda, servicios públicos y mercado de trabajo. No hace estimación propia del saldo fiscal.
- Datos, país y periodo: España y la UE; literatura hasta 2025.
- Resultado principal (con su unidad, tal como lo da el autor): el impacto fiscal medio de la inmigración es modesto y depende de la integración laboral temprana y del empleo formal. Recoge los valores del JRC para la media de la UE en 2015 (−476 € nativos, −208 € UE y −219 € fuera de la UE), las estimaciones españolas de 2005-2008 (OEP 2006: +4.784 M€ en 2005; Dolado y Vázquez 2008: unos +2.000 M€ al año) y un estudio FIPROS de la Seguridad Social (2006/97) que califica de «limitados y transitorios» los efectos beneficiosos sobre la solvencia de las pensiones.
- Validez para España: alta como síntesis reciente. No aporta cifras nuevas.
- Replicación pública: no aplica (síntesis).
- Estado: NO VERIFICADA (sin DOI)

## 5. Pensiones y envejecimiento: proyecciones oficiales europeas

### Comisión Europea (DG ECFIN) y Comité de Política Económica (2024). 2024 Ageing Report: Economic and budgetary projections for the EU Member States (2022-2070)
- DOI: 10.2765/022983 (impreso en el informe; resuelve en doi.org pero no consta en Crossref ni DataCite, así que el verificador lo marcará NO VERIFICADA si solo consulta Crossref) · Revista: European Economy, Institutional Paper 279 (ISSN 2443-8014; ISBN 978-92-68-13780-2)
- Leído: texto completo (resumen, supuestos y tablas estadísticas II.1.6, II.1.64, II.1.86 y II.1.87, https://economy-finance.ec.europa.eu/publications/2024-ageing-report-economic-and-budgetary-projections-eu-member-states-2022-2070_en). PDF local: sha256 952ee30dededf74d3c260c9442202515542ca24b4f4e7f17ff549585af97f930
- Diseño e identificación: proyecciones de gasto en pensiones, sanidad, cuidados de larga duración y educación con supuestos comunes (población de Eurostat EUROPOP2023; supuestos en el Institutional Paper 257). Incluye sensibilidad con migración un 33 % mayor o menor. Son escenarios, no efectos identificados.
- Datos, país y periodo: UE-27, 2022-2070.
- Resultado principal (con su unidad, tal como lo da el autor): la migración neta media en la UE es de alrededor del 0,3 % de la población al año en 2022-2070. España: saldo migratorio neto de 677.200 personas en 2022, 221.200 en 2030, 196.200 en 2050 y 193.700 en 2070. Gasto público bruto en pensiones de España, en % del PIB: escenario base 13,1 (2022), 17,3 (2050) y 16,7 (2070); con migración +33 %, 16,1 (2050) y 15,7 (2070); con migración −33 %, 18,7 (2050) y 18,1 (2070). La diferencia entre los dos escenarios de sensibilidad llega a unos 2,6 puntos de PIB en 2050. UE en el base: 11,4, 12,1 y 11,8. En la UE, más migración se asocia a un menor crecimiento del gasto; menos migración lo eleva, porque reduce el PIB y la población activa.
- Validez para España: muy alta. Es la referencia oficial para la fase 4 (punto 5). Los supuestos migratorios de España (unos 200.000 al año a largo plazo) son inferiores a los de la AIReF y el INE, y eso pesa mucho en el resultado.
- Replicación pública: proyecciones y supuestos públicos (tablas por país en el informe y en la web de la DG ECFIN); los modelos nacionales de pensiones no son públicos.
- Estado: NO VERIFICADA (el DOI existe en doi.org, agencia OP, sin metadatos comparables)

## 6. Contabilidad generacional y modelos de ciclo vital

### Auerbach, A. J. y Oreopoulos, P. (1999). Generational accounting and immigration in the United States
- DOI: 10.3386/w7041 · Revista: NBER Working Paper n.º 7041
- Leído: resumen (https://www.nber.org/papers/w7041)
- Diseño e identificación: contabilidad generacional adaptada a la inmigración: perfiles por edad de impuestos y transferencias, con los descendientes incluidos y distintas reglas para cerrar la restricción presupuestaria intertemporal.
- Datos, país y periodo: Estados Unidos, base a finales de la década de 1990, horizonte indefinido.
- Resultado principal (con su unidad, tal como lo da el autor): como los nuevos inmigrantes pesan más entre las generaciones futuras, si el desequilibrio fiscal recae en ellas, la inmigración alivia la carga de los nativos. Con una política de «responsabilidad fiscal», el signo depende de cuánto crezca el gasto en compras públicas con la población inmigrante. En todo caso, el efecto es muy pequeño frente al desequilibrio total: la inmigración no lo causa ni lo resuelve.
- Validez para España: media. El método se puede trasladar (pensiones de reparto, envejecimiento); las magnitudes no. Hay una versión breve en AER Papers & Proceedings 89(2), 1999, 176-180, DOI 10.1257/aer.89.2.176 (verificado en Crossref), no fichada porque no tiene resumen que leer.
- Replicación pública: no público.
- Estado: VERIFICADA (Crossref)

### Auerbach, A. J. y Oreopoulos, P. (2000). The fiscal effect of U.S. immigration: a generational-accounting perspective
- DOI: 10.1086/654705 · Revista: Tax Policy and the Economy 14, 123-156
- Leído: resumen (OpenAlex, https://api.openalex.org/works/doi:10.1086/654705)
- Diseño e identificación: contabilidad generacional; critica el enfoque estático transversal porque ignora el impacto futuro de los inmigrantes actuales y de sus hijos.
- Datos, país y periodo: Estados Unidos, proyecciones de finales de la década de 1990.
- Resultado principal (con su unidad, tal como lo da el autor): la mejora fiscal de Estados Unidos de finales de los noventa reduce el beneficio potencial de la inmigración. El efecto de cambiar el volumen de inmigración tiene signo incierto, según los parámetros, y es pequeño frente al desequilibrio total. Pesa más la composición, sobre todo el nivel educativo.
- Validez para España: media (es un argumento de método: volumen frente a composición, y descendientes).
- Replicación pública: no público.
- Estado: VERIFICADA (Crossref)

### Storesletten, K. (2000). Sustaining fiscal policy through immigration
- DOI: 10.1086/262120 · Revista: Journal of Political Economy 108(2), 300-323 (el encargo lo situaba en la AER; Crossref confirma que es la JPE)
- Leído: resumen (Crossref y OpenAlex, https://api.openalex.org/works/doi:10.1086/262120)
- Diseño e identificación: modelo de equilibrio general de generaciones solapadas, calibrado, con inmigrantes y nativos diferenciados; calcula la ganancia fiscal descontada de admitir un inmigrante más según su edad y cualificación.
- Datos, país y periodo: Estados Unidos, calibración de la década de 1990.
- Resultado principal (con su unidad, tal como lo da el autor): hay políticas migratorias que por sí solas resolverían el problema fiscal del envejecimiento del baby boom; consisten en más entradas de inmigrantes cualificados en edad de trabajar. Un ejemplo factible: admitir cada año 1,6 millones de inmigrantes muy cualificados de 40 a 44 años.
- Validez para España: media-baja en cifra; alta como herramienta (valor actual neto por edad de llegada y cualificación, que es lo que pide la fase 4, punto 2).
- Replicación pública: no público.
- Estado: VERIFICADA (Crossref)

### Storesletten, K. (2003). Fiscal implications of immigration—a net present value calculation
- DOI: 10.1111/1467-9442.t01-2-00009 · Revista: Scandinavian Journal of Economics 105(3), 487-506
- Leído: resumen (Crossref, https://api.crossref.org/works/10.1111/1467-9442.t01-2-00009)
- Diseño e identificación: valor actual neto de los impuestos futuros menos el gasto por inmigrante, con precios y conducta constantes (sin equilibrio general).
- Datos, país y periodo: Suecia, estado de bienestar con gasto y presión fiscal altos.
- Resultado principal (con su unidad, tal como lo da el autor): el valor actual neto llega a +23.500 USD por inmigrante joven en edad de trabajar, pero el inmigrante medio nuevo supone −20.500 USD. Pesan sobre todo el empleo y la edad. Para los jóvenes en edad de trabajar, la tasa de participación que deja el saldo en cero es del 60 %, muy por debajo de la observada en ese grupo.
- Validez para España: media. Es la referencia para un estado de bienestar europeo; ofrece el concepto de tasa de empleo de equilibrio para los escenarios de convergencia.
- Replicación pública: no público.
- Estado: VERIFICADA (Crossref)

### Rowthorn, R. (2008). The fiscal impact of immigration on the advanced economies
- DOI: 10.1093/oxrep/grn025 · Revista: Oxford Review of Economic Policy 24(3), 560-580
- Leído: resumen (Crossref y OpenAlex, https://api.openalex.org/works/doi:10.1093/oxrep/grn025)
- Diseño e identificación: revisión de la evidencia internacional y de los problemas de medición, con secciones sobre el Reino Unido y los países de baja fecundidad.
- Datos, país y periodo: economías avanzadas, Europa y Norteamérica, literatura hasta 2008.
- Resultado principal (con su unidad, tal como lo da el autor): la mayoría de los estudios dan una contribución fiscal neta del conjunto de los inmigrantes pequeña, normalmente dentro de ±1 % del PIB, porque lo que aportan unos lo compensan otros. Los inmigrantes muy cualificados aportan mucho. Los poco cualificados que se asientan tienden a suponer un coste neto, salvo que retornen y usen poco el gasto. Las excepciones con grandes beneficios corresponden a países en colapso demográfico y se apoyan en supuestos poco realistas sobre el reparto intergeneracional. Conclusión: en general no hay un argumento fiscal fuerte a favor ni en contra de la inmigración a gran escala.
- Validez para España: alta como marco de expectativas y como guía de los supuestos que hay que poner a prueba (retorno, cualificación, reparto intergeneracional).
- Replicación pública: no aplica (revisión).
- Estado: VERIFICADA (Crossref)

---

## Pendientes y no localizados (sin ficha porque no se leyeron)

- **OCDE 2021, resultados por país**: anexo XLS del capítulo 4 (contribución neta de nacidos fuera y nativos en % del PIB, 2006-2018, con y sin bienes públicos). oecd.org devolvió 403. Hay que descargarlo en la fase 2 (adquisidor-datos) desde la página del capítulo o sus StatLinks y comprobar la cifra de España que circula en prensa (−0,15 % del PIB inmigrantes, −5,2 % nativos).
- **AIReF**: Opinión 2/25 sobre la sostenibilidad de las AAPP a largo plazo (31-3-2025) y su recuadro 5 «Impacto fiscal de la inmigración»; Opinión 1/23 (2023); documento técnico de proyecciones demográficas 2024-2070 (septiembre de 2025). airef.es devolvió 503 y la cadena TLS no valida con el proxy. Sus escenarios de 2023 solo se conocen aquí a través de García Díaz (FEDEA 2023). Hay que reintentarlo.
- **CPB (2003)**, Roodenburg, Euwals y ter Rele, «Immigration and the Dutch economy»: la URL del CPB devolvió 404; solo se conoce a través de van de Beek et al. (2023).
- **Finansministeriet**, ediciones de 2018 (publicada en 2021) y 2019 (publicada en 2023), y la proyección de 2018 a 2100: las URL encontradas devolvieron 404.
- **Oficina Económica del Presidente (2006)**, «Inmigración y economía española: 1996-2006», y **Dolado y Vázquez (eds.) (2008)**, «Ensayos sobre los efectos económicos de la inmigración en España» (FEDEA): citados por terceros, no leídos.
- **Hernando de Frutos (IBEI, c. 2017)**, «El impacto fiscal de la inmigración en España durante la crisis económica»: localizado solo por el título; no se pudo acceder al texto.
- **Banco de España**: no se encontró ningún Documento Ocasional o de Trabajo dedicado al saldo fiscal de los inmigrantes. Los trabajos del Banco que se usan son marcos de pensiones y demografía (DO 1701, Informe Anual 2023).
- **Christl et al. (2021)**, valores numéricos por país: solo están en los gráficos 5 y 6. Si la fase 4 los necesita, habrá que digitalizarlos con un error de lectura declarado.

## Tabla de la pregunta

| trabajo | diseño | datos | resultado (unidad) | validez para España |
|---|---|---|---|---|
| OCDE / Damas de Matos (2021) | contabilidad estática anual, método común; bienes públicos con coste medio y marginal | 25 países OCDE, 2006-2018 (EU-SILC y COFOG) | contribución neta de los inmigrantes entre −1 % y +1 % del PIB en la mayoría de países; −0,5 pp de PIB si se imputan los hijos (% PIB) | alta; cifras de España pendientes de verificar en el anexo |
| Christl et al. (2021, JRC) | microsimulación EUROMOD; ANFI estático y LCD de ciclo vital; sin bienes públicos | EU-SILC 2015, UE-27 y RU | ANFI UE: −476 nativos, −208 UE, −219 fuera UE; LCD: −723, −1.106, −2.600 (€/persona/año) | alta; España solo en gráficos |
| Christl et al. (2022, Fiscal Studies) | estático más proyección demográfica dinámica | EU-SILC/EUROMOD, UE-27 | la migración UE suaviza el efecto fiscal del envejecimiento pero no lo compensa (cualitativo) | media-alta |
| Fiorio et al. (2023, ITPF) | contabilidad estática EUROMOD con IVA y gasto en especie; descomposición por composición | EU-SILC, UE-14, 2014-2018 | España: nativos −814, migrantes +793; UE-14: +32 frente a +1.510 (€ de 2018/persona/año); sin diferencia en España a igual composición | muy alta |
| Boffi et al. (2024, TEW) | estático de abajo arriba, solo partidas monetarias directas | EU-SILC, 15 países, 2007-2018 | España: nativos −1.756, UE −242, fuera UE −161 (€ PPA/persona/año) | media (cota estrecha) |
| Dustmann y Frattini (2014, EJ) | contabilidad estática anual y acumulada; bienes públicos con coste medio y marginal | Reino Unido, 1995-2011, LFS | recientes 2001-2011: EEE +22.100, no EEE +2.900, nativos −624.100 (M£ de 2011) | media (método) |
| van de Beek et al. (2023, libro) | contabilidad generacional; VAN de por vida; bienes públicos por persona | CBS, Países Bajos, perfiles de 2016, flujos 1995-2019 | occidental medio +42.000, no occidental medio −167.000 (€ VAN/persona); 400.000 M€ acumulados 1995-2019 | media-baja en cifra, alta en método |
| van de Beek et al. (2024, IZA) | contabilidad generacional por motivo y región; segunda generación | CBS, Países Bajos, 2016 | laboral positivo; estudio, familia y asilo negativos (cualitativo en el resumen) | media |
| Finansministeriet (2019) | contabilidad estática con registros; claves de reparto para lo colectivo | registros, Dinamarca, 2016 | origen danés +28; inmigrantes y descendientes −30; no occidentales −35; occidentales +5 (mil M DKK) | media |
| Conde-Ruiz, Jimeno y Valera (2008) | revisión teórica y empírica | España, literatura hasta 2007 | alivio a medio plazo, el problema se traslada a largo plazo (cualitativo) | alta |
| Jiménez-Ridruejo et al. (2009) | microsimulación «Carrión» hasta 2060 | España, base hacia 2007 | ratio cotizaciones/pensiones de los inmigrantes mayor que la de los nativos hasta hacia 2055 (ratio) | alta en diseño, cifras desfasadas |
| Moreno Fuentes y Bruquetas (2011) | estudio institucional y revisión | España, hasta 2010 | recoge saldo neto 2005 de +4.780 M€ (OEP) y 2008 de +2.000 M€ (Dolado y Vázquez) | alta para antes de la crisis |
| Muñoz de Bustillo y Grande (2017) | regresiones de recepción y cuantía de prestaciones con controles | ECV 2015 y ENS, España | −4,7 pp probabilidad de recibir prestaciones; unos −1.400 €/año de cuantía (pp; €) | alta (datos públicos) |
| Hernández de Cos, Jimeno y Ramos (2017, BdE DO 1701) | descomposición contable del gasto en pensiones | España, proyecciones INE y CE | la inmigración determina la dependencia; sin cifra fiscal | alta (marco) |
| Banco de España (2024, IA 2023, cap. 2) | ejercicio contable de tasa de dependencia constante | INE 2022-2072, España | haría falta triplicar la población nacida fuera en edad de trabajar prevista por el INE (múltiplo) | alta (cota demográfica) |
| García Díaz (2023, FEDEA) | nota sobre los escenarios de la AIReF de 2023 | AIReF, España, 2050-2070 | flujos de 206.000 en vez de 239.000 al año suben el gasto en pensiones unas 0,3 pp de PIB (pp PIB) | alta; contrastar con la AIReF |
| Carrasco (2026, Inst. Santalucía) | síntesis | España y UE | impacto fiscal medio modesto, ligado al empleo formal (cualitativo) | alta (síntesis) |
| CE y EPC (2024, Ageing Report) | proyección con supuestos comunes; migración ±33 % | EUROPOP2023, UE-27, 2022-2070 | España, pensiones en % PIB 2050: base 17,3; +33 % migración 16,1; −33 % migración 18,7 (% PIB) | muy alta |
| Auerbach y Oreopoulos (1999, NBER) | contabilidad generacional | EE. UU., década de 1990 | efecto muy pequeño frente al desequilibrio total (cualitativo) | media |
| Auerbach y Oreopoulos (2000, TPE) | contabilidad generacional | EE. UU. | el volumen tiene signo incierto y pequeño; la composición educativa importa más (cualitativo) | media |
| Storesletten (2000, JPE) | OLG de equilibrio general calibrado | EE. UU. | 1,6 millones al año de inmigrantes muy cualificados de 40-44 años sostendrían la política fiscal (personas/año) | media-baja en cifra, alta en herramienta |
| Storesletten (2003, SJE) | VAN por inmigrante, equilibrio parcial | Suecia | +23.500 USD joven en edad de trabajar; −20.500 USD inmigrante medio; participación de equilibrio del 60 % (USD; %) | media |
| Rowthorn (2008, OxREP) | revisión | economías avanzadas | contribución neta normalmente dentro de ±1 % del PIB (% PIB) | alta (expectativas) |

## Qué esperamos en España y por qué

1. En la foto estática anual, lo esperable es una contribución neta de los nacidos fuera pequeña en proporción al PIB (del orden de ±1 %) y quizá mayor por persona que la de los nacidos en España. Así lo apuntan Fiorio et al. (España: migrantes +793 frente a nativos −814 € por persona), Boffi et al. y la OCDE. El motivo es la composición: más peso en edades de trabajo y pocas pensiones contributivas, que concentran el gasto de los nativos.
2. Esa ventaja debería desaparecer o casi al ajustar por edad y sexo: Fiorio et al. no hallan diferencia significativa en España a igual composición. Por eso la descomposición en tres niveles es imprescindible antes de difundir ninguna brecha bruta.
3. En el ciclo vital el signo puede invertirse (Christl et al.). Dependerá de los supuestos sobre convergencia de empleo y salarios, retorno al país de origen, tasa de descuento y derechos de pensión futuros. Estos son los supuestos que, según las reglas, hay que mostrar con su sensibilidad y, si cambian el signo, señalar como parada.
4. El resultado depende mucho del ciclo: positivo en el auge de 2005-2008, negativo en la crisis de 2008-2015 según lo que se atribuye a la OCDE. Conviene medir varios años y no uno solo.
5. Tres decisiones de imputación mueven el nivel tanto como el grupo de origen: los bienes públicos (coste medio frente a marginal), la educación de los hijos (asignada a los padres o a ellos mismos) y la segunda generación.
6. En pensiones, la inmigración sostenida reduce el gasto sobre PIB (Ageing Report 2024: unos 2,6 puntos de diferencia en 2050 entre migración −33 % y +33 %). Pero no resuelve el envejecimiento por sí sola (Banco de España, IA 2023) y traslada parte del problema a cuando esos cotizantes se jubilen (Conde-Ruiz et al.; Jiménez-Ridruejo et al.). Ese efecto «población joven hoy» y el de las pensiones futuras deben presentarse por separado.
