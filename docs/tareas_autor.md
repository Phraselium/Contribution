# Tareas del autor (fuera de esta sesión)

## Subir la etiqueta del pre-registro

El proxy de la sesión rechazó `git push origin prereg-m1` con HTTP 403 (la rama sí subió). La puerta de la fase 5 acepta la etiqueta local porque su commit está en `origin/claude/m1-contribucion-origen`, pero conviene que la etiqueta exista también en el remoto. Desde tu ordenador, con el repositorio clonado y la rama actualizada:

```
git fetch origin claude/m1-contribucion-origen
git tag -a prereg-m1 c247555d37e8d0dee45b87c3b959f35a47b762fb -m "Pre-registro interno M1, fijado en el commit c247555d37e8d0dee45b87c3b959f35a47b762fb; sin sello de tiempo externo"
git push origin prereg-m1
```

Comprobación: `git ls-remote origin refs/tags/prereg-m1` debe devolver la etiqueta, y `git rev-list -n1 prereg-m1` debe dar c247555d37e8d0dee45b87c3b959f35a47b762fb.

Nota: la etiqueta local original tiene fecha de etiquetado anterior a cualquier estimación de la fase 5; la que se cree desde tu ordenador tendrá la fecha de creación nueva. En ninguno de los dos casos hay sello de tiempo externo; la garantía es que el commit c247555 está en el historial remoto antes de los commits de la fase 5.

**Estado (19-10-2026, cierre autónomo):** la etiqueta prereg-m1 sigue pendiente de subir desde tu ordenador con las órdenes de arriba. El trabajo no se ha detenido por ello.

## Revisión a posteriori (verificación tras el cierre, 20-10-2026)

- **Commit al que debe apuntar la etiqueta:** `c247555d37e8d0dee45b87c3b959f35a47b762fb` (19-10-2026 15:19 UTC, «M1 F5: pre-registro
  interno y adenda fijados»). Es el commit en que se fijó el plan de análisis de la fase 5 (docs/preregistro.md y
  docs/preregistro_adenda.md); ninguno de los dos ficheros ha cambiado después (`git log c247555..HEAD -- docs/preregistro*.md` está
  vacío) y el primer commit con resultados de la fase 5 es posterior (ea10513, 16:31 UTC). No es HEAD. La etiqueta local ya apunta ahí
  (`git rev-list -n1 prereg-m1` = c247555…). El plan general del estudio (docs/plan.md, sin especificaciones econométricas) se fijó
  antes, en c0ceaac4e09945ad1021892eb730bd01d8199aae; no es el que acredita el análisis causal.
- **Orden exacta (desde tu ordenador; la sesión no crea ni empuja la etiqueta):**

```
git fetch origin claude/m1-contribucion-origen --tags
git tag -a prereg-m1 c247555d37e8d0dee45b87c3b959f35a47b762fb -m "Plan de análisis interno M1 (fase 5), fijado en c247555d37e8d0dee45b87c3b959f35a47b762fb"
git push origin refs/tags/prereg-m1
git rev-list -n1 prereg-m1   # debe dar c247555d37e8d0dee45b87c3b959f35a47b762fb
```

  Si ya tienes una etiqueta prereg-m1 local que apunte a otro commit, bórrala antes solo en local (`git tag -d prereg-m1`).
- **Nombre y alcance:** en el documento se llama «plan de análisis interno», no «pre-registro»: lo fijó y lo custodia el mismo equipo
  que lo ejecuta. Un sello externo (subir el fichero a OSF, AsPredicted o Zenodo, o sellar el hash del commit con OpenTimestamps)
  solo certificaría que el plan existía **desde la fecha de subida**, que ya es posterior a las estimaciones; no puede acreditar que
  existía antes de ellas. La única prueba de anterioridad disponible es el orden de los commits en el historial remoto de GitHub, que
  depende de la confianza en el repositorio.

## Congelación (a posteriori, 21-10-2026): comprobaciones previas y Release de GitHub

**Comprobaciones hechas en la sesión (solo lectura):**
- `git merge-base --is-ancestor c247555d37e8d0dee45b87c3b959f35a47b762fb origin/claude/m1-contribucion-origen` → sí es ancestro.
- `git log c247555..HEAD -- docs/preregistro.md docs/preregistro_adenda.md` → vacío: el plan y su adenda no han cambiado.
- `git ls-tree -r --name-only c247555` → no hay ningún fichero de output/f5 ni registro de estimaciones causales; los únicos
  `resultado.json` son los siete del Monte Carlo con datos simulados (output/montecarlo/{adenda_a5,bhj,conley,dfl,iv2sls,oaxaca,wcr_boot}).

**Orden completa, desde tu ordenador** (la sesión no crea, mueve ni empuja etiquetas):

```
git fetch origin claude/m1-contribucion-origen --tags
git tag -a prereg-m1 c247555d37e8d0dee45b87c3b959f35a47b762fb -m "Plan de análisis interno M1 (fase 5), fijado en c247555d37e8d0dee45b87c3b959f35a47b762fb"
git push origin refs/tags/prereg-m1
gh release create prereg-m1 --repo Phraselium/Contribution --verify-tag \
  --title "M1 · plan de análisis interno (fase 5)" \
  --notes "Plan de análisis interno de la fase 5 (docs/preregistro.md y docs/preregistro_adenda.md) fijado en el commit c247555d37e8d0dee45b87c3b959f35a47b762fb. La fecha de esta Release la pone el servidor de GitHub y solo certifica que la etiqueta existía en ese momento."
gh api repos/Phraselium/Contribution/releases/tags/prereg-m1 --jq '.created_at, .published_at'
```

(Sin gh: en GitHub, Releases → «Draft a new release» → «Choose a tag: prereg-m1» → «Publish release».)

**Por qué la fecha de la etiqueta no certifica nada por sí sola.** La fecha de una etiqueta anotada (tagger date) y la del commit las
pone el reloj de quien las crea y se pueden fijar a voluntad (`GIT_COMMITTER_DATE`); una etiqueta puede además crearse hoy sobre un
commit antiguo. La fecha de la Release (`created_at`/`published_at`) la pone el servidor de GitHub: certifica que la etiqueta existía
en esa fecha, pero esa fecha será posterior a las estimaciones de la fase 5. Lo único que indica que el plan es anterior a las
estimaciones es el orden de los commits en el historial remoto (c247555 antes de ea10513, el primer commit con resultados), que
depende de la confianza en el repositorio y en que no se haya reescrito el historial. Ni la etiqueta ni la Release convierten el
plan de análisis interno en un pre-registro externo.
