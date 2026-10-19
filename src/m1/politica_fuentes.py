"""M1 · Política de fuentes: solo información pública (docs/plan.md, sección A).

`motivo_bloqueo(url)` devuelve el motivo si la URL pertenece a un servicio que exige solicitud, acreditación o credenciales no
públicas (MCVL, microdatos de investigación de Eurostat, laboratorios seguros, sedes con certificado, solicitudes de
transparencia, paneles fiscales bajo petición), o None si no está en la lista. La usan el hook de descargas
(.claude/hooks/guardas_m1.py), el descargador (src/m1/fuentes.py) y los tests (tests/test_guardas.py).
"""
from __future__ import annotations

import re

BLOQUEADAS: list[tuple[str, str]] = [
    (r"mcvl|muestra[-_ %20]*continua[-_ %20]*de[-_ %20]*vidas", "Muestra Continua de Vidas Laborales: acceso por solicitud"),
    (r"sede\.seg-social\.gob\.es|sede-tu\.seg-social", "sede electrónica de la Seguridad Social: exige certificado o Cl@ve"),
    (r"circabc\.europa\.eu", "CIRCABC: distribución de microdatos de investigación de Eurostat a entidades acreditadas"),
    (r"eurostat[^\s]*/(microdata/)?(scientific-use|access-to-microdata|research-entities|application-form)",
     "microdatos de investigación de Eurostat (EU-LFS, EU-SILC): acceso por solicitud"),
    (r"(transparencia\.gob\.es|sede\.transparencia)[^\s]*(solicitud|ejercicio-derecho|derecho-acceso)",
     "solicitud de acceso por transparencia"),
    (r"sede\.agenciatributaria\.gob\.es", "sede de la AEAT: exige identificación"),
    (r"ief\.es[^\s]*(panel|muestra)[^\s]*(irpf|declarantes)", "paneles de IRPF del IEF: acceso por solicitud"),
    (r"ine\.es[^\s]*(laboratorio|acceso[-_ ]?seguro|investigadores/solicitud)", "laboratorio de microdatos del INE: acceso por solicitud"),
    (r"bde\.es[^\s]*belab", "BELab del Banco de España: acceso por solicitud"),
    (r"ipums\.org", "IPUMS: registro con aprobación manual"),
    (r"lisdatacenter\.org", "LIS: registro con aprobación manual"),
    (r"ukdataservice\.ac\.uk[^\s]*(safeguarded|controlled)", "datos restringidos del UK Data Service"),
]
_PATS = [(re.compile(p, re.I), m) for p, m in BLOQUEADAS]
URL = re.compile(r"https?://[^\s'\"<>)]+", re.I)


def motivo_bloqueo(url: str) -> str | None:
    for p, m in _PATS:
        if p.search(url):
            return m
    return None


def urls_en(texto: str) -> list[str]:
    return URL.findall(texto or "")
