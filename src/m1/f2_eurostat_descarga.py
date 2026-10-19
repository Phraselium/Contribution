"""M1-F2 · Descarga de tablas públicas de Eurostat (CON red), API de difusión SDMX 2.1 en SDMX-CSV comprimido.
Licencia: Eurostat, reutilización libre citando la fuente (Decisión 2011/833/UE; CC BY 4.0).
Uso: python3 src/m1/f2_eurostat_descarga.py
"""
from __future__ import annotations

import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuentes  # noqa: E402

LIC = "Eurostat: CC BY 4.0, reutilización citando la fuente (https://ec.europa.eu/eurostat/about-us/policies/copyright)"
API = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/{}?format=SDMX-CSV&compressed=true"

TABLAS = {
    # población y flujos
    "migr_pop3ctb": "Población a 1 de enero por grupo de edad, sexo y país de nacimiento",
    "migr_pop1ctz": "Población a 1 de enero por grupo de edad, sexo y ciudadanía",
    "migr_imm3ctb": "Inmigración por grupo de edad, sexo y país de nacimiento",
    "migr_emi4ctb": "Emigración por grupo de edad, sexo y país de nacimiento",
    "proj_23np": "EUROPOP2023: población proyectada a 1 de enero por edad y sexo",
    "proj_23nanmig": "EUROPOP2023: supuestos de migración neta por edad y sexo",
    # censos (cuotas de asentamiento para P5)
    "cens_11cob_n": "Censo 2011: población por país de nacimiento (nacional)",
    "cens_11arco_r2": "Censo 2011: población por periodo de llegada, país de nacimiento y NUTS2",
    "cens_21cob_r3": "Censo 2021: población por país de nacimiento, grupo de edad y NUTS3",
    # EU-LFS por país
    "lfsa_ergacob": "Tasas de empleo por país de nacimiento",
    "lfsa_urgacob": "Tasas de paro por país de nacimiento",
    "lfsa_argacob": "Tasas de actividad por país de nacimiento",
    "lfsa_ergaedcob": "Tasas de empleo por nivel educativo y país de nacimiento",
    "lfsa_etpgacob": "Asalariados temporales por país de nacimiento (%)",
    "lfsa_eppgacob": "Empleo a tiempo parcial por país de nacimiento (%)",
    "lfsa_eoqgac": "Tasas de sobrecualificación por país de nacimiento",
    "lfsa_pgacws": "Población en hogares privados por país de nacimiento y situación laboral",
    "lfsa_pgaccpm": "Población por estatus migratorio, país de nacimiento y país de nacimiento de los padres",
    # EU-LFS regional (NUTS2)
    "lfst_r_lfsd2pwc": "Población en hogares privados por país de nacimiento, situación laboral y NUTS2",
    "lfst_r_lfe2emprc": "Tasas de empleo por nivel educativo, país de nacimiento y NUTS2",
    "lfst_r_lfur2gac": "Tasas de paro por país de nacimiento y NUTS2",
    "lfst_r_lfp2actrc": "Tasas de actividad por nivel educativo, país de nacimiento y NUTS2",
    "lfst_r_lfsd2pwn": "Población en hogares privados por ciudadanía, situación laboral y NUTS2",
    # EU-SILC
    "ilc_di16": "Renta media y mediana por grupo de país de nacimiento",
    "ilc_li32": "Tasa de riesgo de pobreza por grupo de país de nacimiento",
    "ilc_li09c": "Tasa de riesgo de pobreza antes de transferencias por país de nacimiento",
    "ilc_li80": "Impacto de las transferencias sociales en la pobreza por país de nacimiento",
    "ilc_peps06n": "AROPE por grupo de país de nacimiento",
    "ilc_mdsd05": "Privación material y social por país de nacimiento",
    "ilc_lvho16": "Hacinamiento por grupo de país de nacimiento",
    "ilc_lvho26": "Sobrecarga del coste de la vivienda por país de nacimiento",
    "ilc_lvps16": "Distribución por grupo de país de nacimiento y tenencia de la vivienda",
    "ilc_iw16": "Pobreza en el trabajo por país de nacimiento",
    # finanzas públicas
    "gov_10a_exp": "Gasto de las AAPP por función (COFOG)",
    "gov_10a_taxag": "Impuestos y cotizaciones por tipo (cuentas nacionales)",
    "gov_10a_main": "Principales agregados de las AAPP",
    "nama_10_gdp": "PIB y principales componentes",
    "nama_10r_2gdp": "PIB regional NUTS2",
}


GISCO = {
    "NUTS_RG_20M_2021_4326.geojson": "GISCO: polígonos NUTS 2021 (1:20M) para mapas",
    "NUTS_LB_2021_4326.geojson": "GISCO: puntos de etiqueta NUTS 2021 (coordenadas para errores de Conley)",
}
LIC_GISCO = ("GISCO/EuroGeographics: uso permitido citando «© EuroGeographics para los límites administrativos» "
             "(https://ec.europa.eu/eurostat/web/gisco/geodata/administrative-units)")


def main() -> int:
    err = 0
    for k, d in GISCO.items():
        url = f"https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/{k}"
        try:
            p = fuentes.ya_descargado(url) or fuentes.descargar(url, "gisco", k, LIC_GISCO, "NUTS 2021", d)
            print("ok", k, p.stat().st_size, flush=True)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            print("FALLA", k, e, flush=True)
            err += 1
    for k, d in TABLAS.items():
        url = API.format(k)
        try:
            p = fuentes.ya_descargado(url) or fuentes.descargar(url, "eurostat", f"{k}.csv.gz", LIC, "consulta 2026-10", d)
            print("ok", k, p.stat().st_size, flush=True)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            print("FALLA", k, e, flush=True)
            err += 1
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
