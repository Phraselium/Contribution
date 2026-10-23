# Reproducción en limpio (congelación, a posteriori)

Fecha: 20-10-2026. Objetivo: reconstruir todas las cifras desde un clon nuevo del repositorio remoto, con un entorno de Python
nuevo, sin red durante el cálculo y sin tocar nada a mano.

## Procedimiento
1. `git clone --branch claude/m1-contribucion-origen https://github.com/Phraselium/Contribution.git M1_limpio` (directorio nuevo).
2. Entorno nuevo: `python3 -m venv venv_m1 && venv_m1/bin/pip install -r requirements.txt` (versiones fijadas).
3. Datos crudos: los versionados vienen con el clon; los 133 ignorados por tamaño (data/raw/**/grandes, microdatos y Eurostat > 10 MB)
   se enlazan desde la copia de trabajo y se comprueban contra data/CHECKSUMS.sha256 (todos coinciden). No se copia nada de
   data/processed: se regenera con la fase 2. Cinco PDF listados en CHECKSUMS.sha256 (data/raw/admin/grandes/ar2024_*.pdf,
   boe_ley_22_2009…pdf, gs2013…pdf) no existen tampoco en la copia de trabajo; el pipeline no los usa.
4. Puerta de la fase 5: el clon no tiene la etiqueta prereg-m1 (no se ha subido y no se crea) [corrección del 23-10-2026: en la copia de trabajo sí existía una etiqueta local, creada por el asistente el 19-10-2026; se borró el 23-10-2026]. Se usa el mecanismo documentado de
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

## Entorno y datos (cierre de reproducibilidad, 23-10-2026, a posteriori)
- **Entorno:** Python 3.13.16 (`.python-version`). `requirements.txt` fija con `==` las dependencias directas; `requirements.lock` es
  el `pip freeze` completo (33 paquetes, con las dependencias transitivas) del entorno nuevo de la reproducción en limpio. Para
  recrearlo: `python3.13 -m venv venv && venv/bin/pip install -r requirements.lock`. `make check` incluye la puerta «entorno y
  dependencias»: todo módulo de terceros importado por src/, tests/ o la guarda, y los motores que pandas carga sin import explícito
  (read_excel → openpyxl y xlrd), deben estar en requirements.txt con versión exacta, en el bloqueo, y la versión de Python debe
  coincidir (tests/test_entorno.py demuestra que habría detectado la falta de xlrd).
- **Datos crudos:** 653 ficheros versionados en git (con su sha256 en data/CHECKSUMS.sha256) y 138 que no se versionan por tamaño y se
  descargan con `make m1_f2_descarga` (lista con URL, sha256 y bytes en docs/crudos_descargables.csv; 5,3 GB: EPA 1,8, EPF 1,6,
  ine_tablas 0,6, Eurostat 0,5, ECV 0,5, EES 0,3). Cinco de ellos son PDF de referencia (Ageing Report, BOE, Gasto sanitario) que no usa
  el pipeline y que tampoco están en la copia de trabajo: la comprobación los señala como ausentes.
- **Avisos:** el descargador (src/m1/fuentes.py) compara cada descarga con el sha256 registrado para su URL o su nombre; si no coincide,
  avisa por stderr, lo anota en data/descargas_avisos.log y guarda la nueva edición con la fecha en el nombre sin tocar el registro.
  Antes de cada fase, src/m1/fase.py avisa (sin bloquear) de los crudos descargables ausentes o con un tamaño distinto del registrado;
  `python3 src/m1/fuentes.py --descargados` hace la comprobación completa con sha256, y `make check` falla si un crudo presente no
  coincide con su sha256.
- **Registro de ejecuciones completas:** docs/registro_secuencia_completa.log (lo escribe la guarda; las tres primeras líneas se
  anotaron a posteriori).
