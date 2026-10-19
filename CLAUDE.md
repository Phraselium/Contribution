# Estudio M1 · Contribución e impacto económico de la población según su origen (solo información pública)

Leer docs/plan.md y docs/estado.md al empezar o tras compactar.

## Reglas (sección A de docs/plan.md)

- **Solo información pública**: datos y microdatos descargables sin registro ni solicitud o, como máximo, con registro gratuito y automático. Excluidos: MCVL, microdatos de investigación de EU-LFS y EU-SILC, solicitudes por transparencia y cualquier dato restringido. Cada fuente con URL, licencia, fecha de descarga y checksum. Si un dato no es público: NO ESTIMABLE o imputación con supuestos explícitos, y se dice. No se generan tareas para pedir datos al autor.
- **Idioma** español. Reproducible sin red con datos versionados o con checksum. SEED=20261019 en todo lo aleatorio.
- **Referencia**: Econometr-a (rama claude/housing-price-spain-econometric-95dhj3) clonado aparte, SOLO lectura; se adapta su infraestructura, nunca sus datos.
- **Neutralidad en las dos direcciones**: se evalúan afirmaciones y políticas, nunca personas, partidos ni grupos; lo favorable y lo desfavorable con el mismo estándar y la misma difusión; sin corrección política ni sesgo de confirmación; nunca se atribuyen rasgos a un grupo: agregados y su variación interna.
- **Tres niveles** en toda comparación: bruto; ajustado por edad y sexo; ajustado además por educación, años de residencia y región. Las brechas brutas se descomponen (Oaxaca-Blinder o DFL) en composición y resto.
- **Origen** (fijado antes de mirar datos): país de nacimiento como principal, nacionalidad como sensibilidad. Grupos: nacidos en España; UE-14; UE-13 y otros de Europa; América Latina; Magreb; resto de África; Asia; resto. Nacionalizados y segunda generación por separado si los datos lo permiten. Se documenta qué permite cada fuente.
- **Protección de datos**: solo agregados; supresión de celdas con < 50 observaciones muestrales o con riesgo de identificación.
- **Capas**: C1 hechos (≥ 2 fuentes independientes o dato oficial); C2 cotas con supuestos explícitos; C3 efectos identificados; C4 exploratorio.
- **Efectos**: IDENTIFICADO, SUGESTIVO, ASOCIACIÓN, NO ESTIMABLE (con el dato público que faltaría o si solo existe restringido). Sin lenguaje causal fuera de IDENTIFICADO.
- **Inferencia**: errores agrupados al nivel del tratamiento; wild cluster bootstrap (Webb) con < 40 clusters; AKM o BHJ en shift-share; Conley en datos espaciales; F efectivo y Anderson-Rubin con instrumentos; Holm (confirmatorias) y BH (exploratorias). Microdatos de encuesta con pesos y diseño (estratos y conglomerados si se publican; si no, se dice).
- **Pre-registro interno**: docs/preregistro.md con etiqueta prereg-m1 antes de la fase 5; el hook bloquea lo causal sin ella (acepta la etiqueta local si su commit está en la rama remota). Sin sello externo, y se declara.
- **Referencias**: VERIFICADA (DOI en Crossref) o NO VERIFICADA; nada no leído al menos en su resumen. PDFs solo de fuentes abiertas en data/bib/pdf/ (ignorado) con checksum; al repositorio, fichas y enlaces, nunca PDFs ni párrafos copiados. Prensa solo para localizar originales.
- **Excel**: azul = dato introducido (fuente en nota); negro = calculado en la hoja; verde = de otra pestaña. Sin paneles inmovilizados.
- **Guardas**: prohibido borrar datos crudos y rehacer todo sin orden del autor; ficheros con Write o heredoc entrecomillado; un solo `make check` a la vez; push solo a la rama de trabajo (claude/m1-contribucion-origen); ficheros > 50 MB a LFS o ignorados con checksum (se versionan script de descarga y checksum).
- **Trabajo** en docs/, src/, output/, tests/ y publicacion/ (generada con make, nunca a mano). Estado tras cada tarea en docs/estado.md. Commit por tarea. Si una fase supera 6 millones de tokens de subagentes, parar y explicarlo.
- **Cifras**: output/cifras_clave.csv es la única fuente de cifras difundibles (capa, fuente, periodo, ámbito, grupo de origen).
- **Paradas** (sección D): guarda que no bloquea; resultado que solo se sostiene con un supuesto fiscal arbitrario; riesgo de identificar personas; > 6 M tokens de subagentes en una fase.
