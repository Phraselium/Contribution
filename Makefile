# M1 · Contribución e impacto económico de la población según su origen (solo información pública).
# Todo objetivo es reproducible sin red con data/raw (versionado o con checksum), salvo los *_descarga.
# Prohibidos sin orden del autor: make clean, make all (guardas en .claude/hooks/guardas_m1.py).
PY := python3
SEED := 20261019
export PYTHONHASHSEED := 0

.PHONY: m1_f0 m1_f1 m1_f2 m1_f2_descarga m1_f3 m1_f4 m1_f5 m1_f6 m1_f7 check publicacion web cifras estado prereg

m1_f0:                ## Montaje e inventario de lo público (sin red)
	$(PY) src/m1/fase.py 0

m1_f1:                ## Bibliografía: verificación sin red con la caché de Crossref
	$(PY) src/m1/verificar_referencias.py --solo-comprobar
	$(PY) src/m1/fase.py 1

m1_f2_descarga:       ## Descarga de fuentes públicas (CON red; registra URL, licencia, fecha y sha256)
	$(PY) src/m1/fase.py 2 --red

m1_f2:                ## Normalización de los crudos a data/processed (sin red)
	$(PY) src/m1/fase.py 2

m1_f3:                ## Hechos descriptivos (contribución A)
	$(PY) src/m1/fase.py 3

m1_f4:                ## Contabilidad fiscal (contribución A)
	$(PY) src/m1/fase.py 4

m1_f5:                ## Impacto causal (B): solo con prereg-m1
	$(PY) src/m1/etiquetas.py
	$(PY) src/m1/fase.py 5

m1_f6:                ## Síntesis crítica de afirmaciones
	$(PY) src/m1/fase.py 6

m1_f7:                ## Documento de trabajo
	$(PY) src/m1/fase.py 7

cifras:
	$(PY) src/m1/cifras.py

publicacion:          ## Genera publicacion/documento_m1 y su manifiesto
	$(PY) src/m1/publicar.py

web:                  ## Página HTML estática del documento en publicacion/web
	$(PY) src/m1/publicar.py --web

prereg:               ## Estado de la puerta del pre-registro interno
	$(PY) src/m1/etiquetas.py

estado:
	@sed -n '1,40p' docs/estado.md

check:                ## Puertas de calidad (un solo make check a la vez; no escribe en el repositorio)
	$(PY) src/m1/check.py
