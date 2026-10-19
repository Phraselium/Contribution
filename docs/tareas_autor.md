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
