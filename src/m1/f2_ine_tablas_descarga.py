"""M1-F2 · Descarga de tablas públicas del INE (CON red): padrón continuo por país de nacimiento y nacionalidad por provincia
(1998-2022, PC-Axis), Estadística Continua de Población por provincia y región de nacimiento / nacionalidad (2002-), migraciones
por provincia y nacionalidad, proyecciones 2026-2075, Censo 2021, salarios por nacionalidad de la EPA y contexto provincial.
Licencia: INE, reutilización libre citando la fuente. Uso: python3 src/m1/f2_ine_tablas_descarga.py
"""
from __future__ import annotations

import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuentes  # noqa: E402

LIC = "INE: reutilización libre citando la fuente (https://www.ine.es/aviso_legal)"
PX = "https://www.ine.es/jaxi/files/_px/es/px/t20/e245/p08/l0/{}.px"
T3 = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/{}.csv"

PADRON = {
    "03005": "Población extranjera por nacionalidad, provincias, sexo y año (padrón, 1998-2022)",
    "03006": "Población por provincias, país de nacimiento, español/extranjero, sexo y año (padrón, 1998-2022)",
    "03002": "Población por provincias, edad quinquenal, españoles/extranjeros, sexo y año (padrón, 1998-2022)",
}
TEMPUS = {
    # Estadística Continua de Población
    "56948": "ECP: población por provincia, edad quinquenal, lugar de nacimiento (agrupación de países) y sexo",
    "56947": "ECP: población por provincia, edad quinquenal, nacionalidad (agrupación de países) y sexo",
    "56937": "ECP: población nacional por país de nacimiento, edad quinquenal y sexo",
    "56936": "ECP: población nacional por nacionalidad, edad quinquenal y sexo",
    # Estadística de Migraciones y Cambios de Residencia
    "69692": "Inmigraciones del extranjero por provincia, año, sexo, edad y país de nacimiento (España/extranjero)",
    "69693": "Inmigraciones del extranjero por provincia, año y nacionalidad",
    "69707": "Emigraciones al extranjero por provincia, año, sexo, edad y país de nacimiento (España/extranjero)",
    "69708": "Emigraciones al extranjero por provincia, año y nacionalidad",
    "69765": "Saldos migratorios por provincia, año, sexo, edad y país de nacimiento (España/extranjero)",
    # Proyecciones de población 2026-2075
    "36642": "Proyección: población a 1 de enero por lugar de nacimiento y año",
    "36776": "Proyección: flujos de inmigración por sexo, generación y lugar de nacimiento 2026-2075",
    "36777": "Proyección: flujos de emigración por lugar de nacimiento y sexo 2026-2075",
    # Censo 2021
    "66611": "Censo 2021: población de 15 y más por sexo, lugar de nacimiento y nivel de estudios",
    "66596": "Censo 2021: población de 15 y más por sexo, edad, lugar de nacimiento y nivel de estudios",
    "69947": "Censo 2021: ocupados por sexo, edad, nacionalidad y ocupación (3 dígitos)",
    # EPA, tablas
    "66240": "EPA: salarios medios por tipo de jornada, nacionalidad y decil",
    "66205": "EPA: asalariados por tipo de jornada, nacionalidad y decil",
    "65115": "EPA: ocupados extranjeros por zona, sexo y tiempo de residencia",
    "65336": "EPA: tasas de paro por nacionalidad, sexo y comunidad autónoma",
    "65310": "EPA: tasas de empleo por nacionalidad, sexo y comunidad autónoma",
    # ECV, tablas
    "9995": "ECV: hogares por régimen de tenencia y nacionalidad de la persona de referencia",
    "75484": "ECV: riesgo de pobreza o exclusión (AROPE 2030) por país de nacimiento",
}


def main() -> int:
    errores = 0
    for k, d in PADRON.items():
        url = PX.format(k)
        try:
            p = fuentes.ya_descargado(url) or fuentes.descargar(url, "ine_padron", f"{k}.px", LIC, "padrón 1998-2022 (ed. 2025)", d)
            print("ok", p.name)
        except urllib.error.HTTPError as e:
            print("FALLA", url, e.code)
            errores += 1
    for k, d in TEMPUS.items():
        url = T3.format(k)
        try:
            p = fuentes.ya_descargado(url) or fuentes.descargar(url, "ine_tablas", f"t{k}.csv", LIC, "consulta 2026-10", d)
            print("ok", p.relative_to(fuentes.RAIZ), p.stat().st_size)
        except urllib.error.HTTPError as e:
            print("FALLA", url, e.code)
            errores += 1
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
