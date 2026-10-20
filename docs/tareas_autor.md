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
