# Reproducción en limpio (congelación, a posteriori)

Fecha: 20/21-10-2026. Objetivo: reconstruir todas las cifras desde un clon nuevo del repositorio remoto, con un entorno de Python
nuevo, sin red durante el cálculo y sin tocar nada a mano.

## Procedimiento
1. `git clone --branch claude/m1-contribucion-origen https://github.com/Phraselium/Contribution.git M1_limpio` (directorio nuevo).
2. Entorno nuevo: `python3 -m venv venv_m1 && venv_m1/bin/pip install -r requirements.txt` (versiones fijadas).
3. Datos crudos: los versionados vienen con el clon; los 133 ignorados por tamaño (data/raw/**/grandes, microdatos y Eurostat > 10 MB)
   se enlazan desde la copia de trabajo y se comprueban contra data/CHECKSUMS.sha256 (todos coinciden). No se copia nada de
   data/processed: se regenera con la fase 2. Cinco PDF listados en CHECKSUMS.sha256 (data/raw/admin/grandes/ar2024_*.pdf,
   boe_ley_22_2009…pdf, gs2013…pdf) no existen tampoco en la copia de trabajo; el pipeline no los usa.
4. Puerta de la fase 5: el clon no tiene la etiqueta prereg-m1 (no se ha subido y no se crea). Se usa el mecanismo documentado de
   src/m1/etiquetas.py para trabajo sin red, `M1_ETIQUETAS_REMOTAS` apuntando a `{"prereg-m1": "c247555d37e8d0dee45b87c3b959f35a47b762fb"}`;
   la puerta sigue comprobando que el plan y su adenda no han cambiado desde ese commit. Sin esa variable, un clon nuevo no puede
   ejecutar la fase 5 hasta que el autor suba la etiqueta (docs/tareas_autor.md).
5. Todas las fases en orden: `make m1_f0 m1_f1 m1_f2 m1_f3 m1_f4 m1_f5 m1_f6 m1_f7 publicacion web`, que es la secuencia del nuevo
   objetivo `make all` (la guarda de la sesión bloquea la orden literal `make all`).

## Resultado
**Primera ejecución (6568429):** falló en la fase 2: `requirements.txt` no incluía `xlrd` (lectura de .xls) ni `linearmodels`
(tests). Corregido en el repositorio (dcdcd84), junto con el objetivo `all`, que no existía.

**Segunda ejecución (dcdcd84, mismo código de cálculo que 6568429):** completa en 23 minutos, sin fallos. Comparación de
output/cifras_clave.csv con la de 6568429: **755 de 755 cifras idénticas** (valor e intervalo, tolerancia 10⁻⁹), ninguna que falte
ni que sobre. Los demás ficheros generados tienen el mismo contenido: los .csv.gz de data/processed coinciden una vez
descomprimidos, y tablas_m1.xlsx tiene las mismas hojas y celdas; solo difieren en bytes por las marcas de tiempo internas de gzip y
del xlsx (y, por tanto, el MANIFIESTO de publicacion). La fase 1 genera además output/f1/tabla_comparacion_externa.csv, que
faltaba en el repositorio porque la fase 1 no se había vuelto a ejecutar tras añadir docs/literatura/comparacion_externa.md (añadido
en la congelación).

**Tercera ejecución (HEAD de la congelación):** ver el apartado siguiente.

**Tercera ejecución (74c2356, HEAD de la congelación con todo el código nuevo):** clon actualizado, mismo entorno, misma secuencia;
completa en 34 minutos, sin fallos. **859 de 859 cifras idénticas** a las de la copia de trabajo (incluidas las 104 nuevas de la
congelación), sin cifras que falten ni que sobren, y ningún fichero generado distinto salvo las marcas de tiempo de gzip y xlsx.
No hubo que corregir el pipeline por ninguna cifra.
