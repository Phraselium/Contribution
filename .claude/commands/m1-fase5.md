---
description: M1 · Fase 5 · Impacto causal (B), solo con prereg-m1
---
0. Comprueba la puerta: `python3 src/m1/etiquetas.py` debe decir ABIERTA. Si no, redacta docs/preregistro.md, pásalo a abogado-del-diablo, escribe la adenda, haz commit, crea la etiqueta prereg-m1 y súbela (o súbe su commit a la rama remota si el proxy rechaza la etiqueta).
1. Lee docs/plan.md (sección C, fase 5) y docs/estado.md. Respeta las reglas A y las paradas D.
2. Ejecuta solo esta fase. Los scripts deterministas, con `make m1_f5`. Como máximo 3 subagentes que escriban a la vez, en worktrees; anota cada uno en docs/subagentes.csv con sus tokens.
3. Si la fase supera 6 millones de tokens de subagentes, para y explícalo.
4. Actualiza docs/estado.md (hecho, siguiente, subagentes y tokens) y docs/decisiones.md.
5. `make check` en solitario, commit por tarea y push solo a la rama de trabajo (`git push -u origin claude/m1-contribucion-origen`).
6. Resumen de 250 palabras como máximo.
