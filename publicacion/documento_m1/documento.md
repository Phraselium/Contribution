---
titulo: "Contribución e impacto económico de la población según su origen: España por provincia y Europa por país y región (solo información pública)"
serie: "Documento de trabajo M1 (formato de la serie Documentos de Trabajo del Banco de España; no es una publicación del Banco de España)"
fecha: "octubre de 2026"
---

# Contribución e impacto económico de la población según su origen

*España por provincia y Europa por país y región, solo con información pública*

Documento de trabajo M1 · octubre de 2026 · Formato de la serie Documentos de Trabajo del Banco de España; no es una publicación del Banco de España ni ha pasado por su revisión.

## Resumen ejecutivo

**Pregunta.** El estudio separa dos preguntas que no se mezclan. La primera es la **contribución**, una pregunta de contabilidad: cuánto aporta y recibe cada grupo de origen en empleo, salarios, vivienda y cuentas públicas. La segunda es el **impacto**, una pregunta de identificación: qué efecto tiene la inmigración sobre la población local. Solo se usan datos públicos descargables sin solicitud.

**Población.** La población nacida fuera de España era el 15,9 % en el padrón de 2022 y el 19,3 % en la Estadística Continua de Población de 2025. En 1998 era el 2,9 %. En la UE-27 la cifra es del 14,4 %. Es una población más joven: el 9,2 % tiene 65 o más años, frente al 23,5 % de los nacidos en España.

**Empleo.** En 2025 la tasa de empleo de 16 a 64 años es del 67,3 % entre los nacidos fuera y del 68,4 % entre los nacidos en España. La variación interna es amplia: África 50,8 %, UE-14 73,3 %. El paro es mayor entre los nacidos fuera: 14,0 % frente a 9,4 %. Al aumento de la ocupación entre 2014 y 2025, de 4,9 millones, los nacidos fuera aportan el 55,6 %. Es contabilidad: no dice qué habría ocurrido sin inmigración.

**Salarios.** Los extranjeros cobran por hora un -18,1 % menos que los españoles (Encuesta de Estructura Salarial, EES, 2022). A igual edad, sexo, estudios y región la diferencia baja al -6,2 %. Alrededor del 68,0 % de la brecha media es composición.

**Vivienda.** Vive en vivienda en propiedad el 81,9 % de los nacidos en España, frente al 32,9 % de los nacidos fuera de la UE. La sobrecarga del gasto en vivienda afecta al 26,1 % de los segundos y al 4,9 % de los primeros.

**Cuentas públicas.** Contribución neta estática en 2024, en euros por persona, con el intervalo de 64 combinaciones de supuestos:
- nacidos en España: entre -1.953 y -637;
- nacidos en el resto de la UE: entre 792 y 5.947;
- nacidos fuera de la UE: entre -2.089 y 2.822.

En el último grupo el signo depende del reparto de los bienes públicos y de la asignación de los hijos nacidos en España. Por eso solo se publica el intervalo (decisión del autor, D11). La contabilidad de ciclo vital da intervalos que contienen el cero para todos los grupos de llegada.

**Pensiones.** En una regla demográfica mecánica, sin migración el gasto en pensiones de 2050 sería 4,4 puntos de PIB mayor que en la proyección base de EUROPOP2023. Es una cota con supuestos, no una proyección del sistema.

**Impacto sobre la población local.** La estimación causal está pre-registrada, revisada y programada, pero **no se ha ejecutado**: la puerta del pre-registro interno exige que la etiqueta esté en un repositorio remoto, y en esta versión no lo está. Todas las preguntas causales quedan pendientes y se cita solo la literatura verificada.

**Afirmaciones del debate.** De las doce evaluadas, seis en cada sentido, tres son engañosas, cinco no se pueden saber con datos públicos y cuatro se sostienen con matices (sección 7).

## Resumen no técnico

Casi una de cada cinco personas que viven en España nació fuera. Trabajan en una proporción parecida a la de los nacidos en España, aunque con más paro y empleos más temporales. Cobran menos por hora, sobre todo porque son más jóvenes, tienen otros estudios y trabajan en otras ocupaciones. Viven mucho más de alquiler y dedican más parte de su renta a la vivienda.

En las cuentas públicas, los nacidos en otros países de la UE aportan más de lo que reciben en cualquier supuesto razonable. Para los nacidos fuera de la UE, el resultado depende de cómo se repartan gastos como la defensa o los intereses de la deuda, y de si la educación de sus hijos nacidos en España se les imputa a ellos.

Que la inmigración cambie el empleo o los salarios de los nacidos en España es otra pregunta. El estudio la deja preparada, pero sin resultados propios todavía.

## 1. Introducción

Este documento mide la contribución de cada grupo de origen al empleo, a los salarios, a la vivienda y a las cuentas públicas en España (nacional, comunidad y provincia) y en Europa (país y NUTS2). Además prepara, con un pre-registro interno, la estimación del impacto de la inmigración sobre la población local (pregunta B).

Las dos preguntas se responden por separado. La contribución (A) es contabilidad, capas C1 y C2. El impacto (B) exige identificación, capa C3, y solo se describe con lenguaje causal si queda IDENTIFICADO según reglas fijadas antes de estimar.

Reglas comunes a todo el documento:
- Las comparaciones se dan en tres niveles: bruto; ajustado por edad y sexo; ajustado además por educación, años de residencia (cuando la fuente los tiene) y región.
- Las diferencias brutas se descomponen en composición y resto.
- Se describen agregados y su variación interna; nunca se atribuyen rasgos a un grupo.
- Las afirmaciones favorables y desfavorables se evalúan con el mismo estándar.

## 2. Datos públicos y definiciones

**Origen.** El criterio principal es el país de nacimiento; la nacionalidad es la sensibilidad. Hay ocho grupos: nacidos en España; UE-14; UE-13 y otros de Europa; América Latina; Magreb; resto de África; Asia; resto.

**Qué permite cada fuente:**
- Padrón (1998-2022): ofrece los ocho grupos completos.
- EPA: los aproxima por región de nacimiento, sin separar Magreb y resto de África (decisión D6).
- Encuesta de Condiciones de Vida (ECV) y Eurostat: solo distinguen España, resto de la UE y resto del mundo.
- EES: solo nacionalidad.

Los nacionalizados son el 33,4 % de los nacidos fuera. La segunda generación solo se identifica si convive con sus padres (EPA, ECV).

El inventario de fuentes, con URL, licencia, fecha y sha256, está en el anexo D y en `data/fuentes.csv`. Lo que no es público, y qué pregunta afecta, está en la sección 8.

**Protección de datos.** Solo se publican agregados y se suprimen las celdas con menos de 50 observaciones muestrales. Las encuestas públicas no traen estratos ni conglomerados, salvo la EES (establecimiento), y los errores se agrupan en consecuencia (D7).

## 3. Hechos: población, empleo, salarios, vivienda y prestaciones

### 3.1 Población

La población nacida fuera pasó del 2,9 % en 1998 al 15,9 % en 2022. Por grupos, en 2022: América Latina 7,0 %, UE-13 y otros de Europa 2,4 %, UE-14 2,3 %, Magreb 2,3 %, Asia 1,1 % y resto de África 0,6 %.

Por provincias va del 3,9 % al 24,7 % (mapa 1).

Entre 2021 y 2024 el saldo migratorio exterior de los nacidos fuera fue de 2,3 millones, y el de los nacidos en España de -0,1 millones.

El 35,2 % de los nacidos fuera de 16 o más años lleva 20 años o más en España, y el 23,7 % menos de 5.

En Europa, España ocupa el puesto 12,0 por cuota de nacidos fuera (19,3 % según Eurostat).

![Mapa 1](figuras/mapa1_provincias_nacidos_fuera.png)

### 3.2 Empleo

Tasas de empleo de 16 a 64 años en 2025 (gráfico 1):
- nacidos en España: 68,4 %;
- UE-14: 73,3 %;
- UE-13 y otros de Europa: 69,4 %;
- América Latina: 71,7 %;
- África: 50,8 %;
- Asia: 68,4 %.

**Tres niveles.** La brecha de África con los nacidos en España es de -17,6 pp en bruto, -22,2 pp a igual edad y sexo, y -13,5 pp al añadir educación, residencia y provincia. La de América Latina pasa de 3,3 pp a 4,9 pp.

**Por provincias**, la brecha de empleo entre nacidos fuera y nacidos en España va de -16,6 a 3,0 pp. En 9,0 provincias los nacidos fuera tienen una tasa mayor (mapa 2).

**Crecimiento del empleo.** En 2014-2025 los nacidos fuera aportan el 55,6 % del aumento de la ocupación y el 71,8 % del de las horas.

**Europa.** La brecha de empleo de 20 a 64 años entre nacidos fuera y nativos es de -3,7 pp en España y de -6,4 pp en la UE-27 (mapa 3).

**Cohortes y generaciones.** El pseudopanel de cohortes de llegada indica que las cohortes llegadas después de 2008 tienen tasas de empleo menores que los nativos, más que las anteriores, a igual tiempo de residencia (C4). La segunda generación que convive con sus padres tiene, a igual tramo de edad, una tasa de empleo unos puntos menor que la de los nativos que también conviven con sus padres (output/f3/empleo_generaciones.csv).

![Gráfico 1](figuras/fig1_empleo.png)

![Mapa 2](figuras/mapa2_provincias_brecha_empleo.png)

![Mapa 3](figuras/mapa3_europa_nuts2.png)

### 3.3 Salarios

**Brecha de salario por hora** entre extranjeros y españoles (EES 2022, errores agrupados por establecimiento):
- bruta: -18,1 %;
- a igual edad y sexo: -15,5 %;
- además a igual estudios y región: -6,2 %;
- además a igual ocupación, sector, contrato y jornada: -3,0 % (informativo).

**Por percentiles**, la brecha es de -4,5 % en el 10, -19,4 % en la mediana y -26,5 % en el 90. La reponderación DFL atribuye a la composición en torno a dos tercios en cada percentil (gráfico 2).

**Segunda fuente.** Con la ECV, la mediana de los rendimientos del trabajo de los asalariados a jornada completa es un -29,5 % menor para los nacidos fuera de la UE.

**Convergencia salarial con los años de residencia: NO ESTIMABLE con datos públicos.** Ni la EES ni la ECV tienen años de residencia; haría falta la MCVL.

![Gráfico 2](figuras/fig2_salarios_dfl.png)

### 3.4 Vivienda

**Propiedad**, en la ECV 2021-2025:
- nacidos en España: 81,9 %;
- resto de la UE: 52,6 %;
- resto del mundo: 32,9 %.

Eurostat, como segunda fuente, da 84,1 % para los nativos y 38,7 % para los nacidos fuera. A igual edad, sexo, educación y región, la diferencia en propiedad de los nacidos fuera de la UE es de -45,3 pp.

**Sobrecarga del gasto en vivienda:** 26,1 % frente a 4,9 %.

**Hacinamiento** (Eurostat): 19,6 % frente a 5,6 %.

**Demanda de hogares** (C2). A tasa de jefatura constante, el aumento de población de 2015-2022 implica 477 mil hogares de nacidos fuera y -225 mil de nacidos en España. No incluye la formación de hogares por envejecimiento.

### 3.5 Prestaciones

Personas que perciben cada prestación o viven en un hogar que la percibe (ECV, media 2021-2025):

| Prestación | España | Resto UE | Resto del mundo |
|---|---|---|---|
| Desempleo (16-64) | 18,2 % | 22,9 % | 21,1 % |
| Jubilación (65+) | 72,5 % | 55,9 % | 44,1 % |
| Rentas mínimas e IMV | 5,5 % | 6,5 % | 11,9 % |
| Ayudas a la vivienda | 1,8 % | 2,2 % | 4,9 % |

A igual edad, sexo, educación y región, la diferencia en rentas mínimas de los nacidos fuera de la UE es de 6,0 pp, y en jubilación de -29,0 pp. Los registros administrativos (SEPE, IMV, pensionistas) solo distinguen nacionalidad y se usan como contraste (docs/fuentes/admin.md).

## 4. Contabilidad fiscal estática y de ciclo vital

**Método.** Se sigue la OCDE (2021) adaptada a datos públicos. Los ingresos y los gastos de las administraciones de 2024 se reparten entre las personas de la ECV 2025:
- impuestos sobre la renta, cotizaciones y prestaciones, observados en la encuesta y calibrados a las cuentas;
- IVA e impuestos especiales con la Encuesta de Presupuestos Familiares (EPF);
- sanidad con el perfil de uso de la Encuesta Nacional de Salud (ENSE);
- educación según matrícula;
- bienes públicos puros (servicios generales e intereses, defensa) a coste medio o a coste marginal cero.

Los ingresos no tributarios se reparten por persona, de modo que la suma cuadra con el saldo de las administraciones.

**Resultado estático (capa C2, gráfico 3).** Contribución neta por persona en 2024:
- **nacidos en España:** -1.367 € en el escenario principal; intervalo de supuestos [-1.953, -637];
- **resto de la UE:** [792, 5.947], positiva en todos los supuestos;
- **resto del mundo:** [-2.089, 2.822]; el signo depende de los bienes públicos y de los hijos nacidos en España, y por decisión D11 solo se publica el intervalo.

En prestaciones monetarias, los nacidos fuera de la UE reciben 1.927 € por persona y los nacidos en España 6.252 €, sobre todo por las pensiones.

**Ciclo vital (C2).** Valor actual de por vida según la edad de llegada, con supervivencia, retorno, convergencia, descuento y pensiones futuras ligadas a la carrera de cotización:
- llegada a los 30 años desde fuera de la UE: entre -174 y 98,0 miles de euros;
- desde la UE: entre -77,0 y 118.

Los dos intervalos contienen el cero. La parte hasta los 64 años («población joven hoy») se presenta separada de la de 65 y más años (pensiones y sanidad futuras) en output/f4/ciclo_vital.csv.

**Sensibilidad.** Lo que más mueve el resultado es la asignación de los hijos nacidos en España y el reparto de los bienes públicos; en el ciclo vital, también el retorno y la convergencia. Los impuestos indirectos, el uso sanitario observado frente a igual uso por edad, la calibración y el reparto del capital mueven menos (output/f4/sensibilidad_supuestos.csv).

**Europa.** No se replica: hacen falta los microdatos de investigación de la EU-SILC, que no son públicos. Se comparan los resultados publicados. Según el JRC (Fiorio et al. 2023), los inmigrantes en España muestran una contribución neta por persona mayor que la de los nativos en 2014-2018, y no hay diferencia significativa a igual composición demográfica. Este estudio coincide en la dirección para los nacidos en la UE y no para los nacidos fuera de ella, cuyo signo depende de los supuestos. Las cifras por país de la OCDE (2021) no se pudieron leer en el original (anexo XLS inaccesible) y no se citan.

![Gráfico 3](figuras/fig3_fiscal_intervalos.png)

## 5. Impacto sobre la población local

**Diseño pre-registrado** (docs/preregistro.md y su adenda, etiqueta local prereg-m1, pre-registro interno sin sello de tiempo externo):
- shift-share de Card por provincia con cuotas de 1998;
- inferencia AKM0 agrupada por origen, validada por Monte Carlo;
- ajuste dinámico de Jaeger, Ruist y Stuhler;
- pretendencia con la afiliación de 1999-2001, permutaciones, exclusión de los orígenes con mayor peso de Rotemberg y sensibilidad por nacionalidad.

**Estado: no ejecutado.** La puerta exige que el commit de la etiqueta esté en la rama de un repositorio remoto. Esta sesión no tuvo remoto y no pudo crearlo, así que la fase 5 queda pendiente y ninguna pregunta B tiene clasificación propia. En la literatura verificada sobre España (González y Ortega 2011; Carrasco, Jimeno y Ortega 2008; Banco de España 2025) no se encuentran efectos negativos significativos sobre el empleo de los nativos. Es literatura, no un resultado de M1.

**Situación de cada pregunta:**
- P3 (servicios públicos): pendiente, con techo ASOCIACIÓN. Las listas de espera solo se publican en PDF.
- P4 (vivienda): no se duplica; se remite a Econometr-a.
- P5 (Europa): pendiente, con techo SUGESTIVO.

## 6. Pensiones y demografía

Las pensiones de vejez y supervivencia suponen el 11,9 % del PIB en 2024. Tasa de dependencia de mayores de EUROPOP2023 en 2050, por cada 100 personas de 20 a 64 años (gráfico 4):
- variante base: 63,7;
- sin migración: 76,7;
- con un tercio más de migración: 59,5.

Con una regla mecánica que mantiene constantes el empleo, la cobertura y la pensión relativa, el gasto de 2050 sería del 21,7 % del PIB en la base y del 26,1 % sin migración. El Ageing Report 2024, que modeliza empleo y reformas, da 17,3 %, 16,1 % con más migración y 18,7 % con menos.

La regla mecánica es una cota: sobrestima el nivel, pero la dirección del efecto de la migración coincide. Las cotizaciones de hoy generan derechos futuros (sección 4).

![Gráfico 4](figuras/fig4_dependencia.png)

## 7. Afirmaciones del debate y su veredicto

Las fichas completas están en `afirmaciones.md`. Resumen:

| id | Afirmación | Veredicto |
|---|---|---|
| A1 | Los inmigrantes viven de las ayudas | engañosa (alta) |
| A2 | Quitan empleo a los españoles | engañosa (media) |
| A3 | Hunden los salarios | no se puede saber (media) |
| A4 | Colapsan la sanidad | engañosa (media) |
| A5 | Suponen un coste fiscal neto | no se puede saber (alta) |
| A6 | «Son la causa de la subida de la vivienda» | no se puede saber (media) |
| F1 | Pagan nuestras pensiones | se sostiene con matices (media) |
| F2 | Sin ellos no habría crecido el empleo | no se puede saber (media) |
| F3 | Aportan más de lo que reciben | no se puede saber (alta) |
| F4 | Trabajan tanto como los españoles | se sostiene con matices (alta) |
| F5 | Se les paga menos por el mismo trabajo | se sostiene con matices (media) |
| F6 | Hacen los trabajos que los españoles no quieren | se sostiene con matices (baja) |

## 8. Limitaciones

- La fase 5 no se ejecutó (sección 5).
- La agrupación de origen está limitada por las fuentes: tres grupos en la ECV y Eurostat, y la EPA sin Magreb.
- La ECV y la EPA públicas no traen el diseño muestral completo.
- La ENSE es de 2017.
- La contabilidad fiscal depende de supuestos de imputación, que se muestran como intervalos.
- No hay salarios provinciales por nacionalidad: la estadística de la AEAT no fue accesible.

### Qué cambiaría con datos no públicos

- **Muestra Continua de Vidas Laborales (MCVL).** Trayectorias individuales: convergencia salarial con los años de residencia, cotizaciones y pensiones futuras observadas, y retorno.
- **Microdatos de investigación de la EU-LFS y la EU-SILC.** País de nacimiento detallado por NUTS2, réplica del método de la OCDE en Europa y un shift-share europeo con cuotas anteriores a la llegada.
- **Datos administrativos de uso de servicios por origen** (historias clínicas, registros escolares, listas de espera por paciente). Congestión local y gasto en especie observado.
- **Paneles fiscales del IEF.** IRPF observado por origen.

## Anexos

- **A. Métodos:** docs/preregistro.md, docs/preregistro_adenda.md, src/m1/econ.py.
- **B. Pruebas por estimación y validación Monte Carlo:** docs/montecarlo.md.
- **C. Supuestos fiscales:** docstrings de src/m1/f4_fiscal.py y src/m1/f4_ciclo_vital.py, docs/supuestos/impuestos_indirectos_coicop.csv y output/f4/rejilla.csv.
- **D. Inventario de fuentes públicas:** docs/fuentes_publicas.md, docs/fuentes/*.md y data/fuentes.csv (URL, licencia, edición, fecha y sha256).
- **E. Bibliografía con estado de verificación:** output/f1/referencias.csv (VERIFICADA en Crossref o DataCite, o NO VERIFICADA).
- **F. Declaración de pre-registro interno.** El plan de la fase 5 se fijó en la etiqueta git local prereg-m1, antes de construir el instrumento y de estimar cualquier efecto. No tiene sello de tiempo externo. La etiqueta no está en un remoto, por lo que la puerta permanece cerrada.
- **Tablas:** tablas_m1.xlsx (azul: dato introducido con su fuente; negro: calculado; verde: de otra pestaña).
