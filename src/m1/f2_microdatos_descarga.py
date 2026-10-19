"""M1-F2 · Descarga de microdatos públicos del INE (CON red): EPA trimestral 2005T1-último, ECV 2008-último, EPF 2016-último
y Encuesta de Estructura Salarial 2010-2022. Libres, sin registro (https://www.ine.es/prodyser/microdatos.htm).

Los ficheros quedan en data/raw/<familia>/grandes/ (ignorados por git) con URL, licencia, fecha y sha256 en data/fuentes.csv;
se reconstruyen con este script. Uso: python3 src/m1/f2_microdatos_descarga.py [epa|ecv|epf|ees]
"""
from __future__ import annotations

import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuentes  # noqa: E402

LIC = "INE: reutilización libre citando la fuente (https://www.ine.es/aviso_legal)"
BASE = "https://www.ine.es/ftp/microdatos"


def _bajar(url, familia, nombre, edicion, desc):
    if fuentes.ya_descargado(url):
        return "ya"
    try:
        fuentes.descargar(url, familia, nombre, LIC, edicion, desc, no_versionar=True)
        return "ok"
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}"


def epa():
    for a in range(2005, 2027):
        for t in range(1, 5):
            r = _bajar(f"{BASE}/epa/datos_{t}t{a % 100:02d}.zip", "epa", f"datos_{t}t{a % 100:02d}.zip", f"{a}T{t}",
                       f"EPA microdatos trimestrales {a}T{t}")
            print("epa", a, t, r, flush=True)
            if r.startswith("HTTP") and a >= 2026:
                return
    for d in ("dr_EPA_2005.xlsx", "dr_EPA_2021.xlsx", "dr_EPA_2026.xlsx"):
        print("epa diseño", d, _bajar(f"{BASE}/epa/{d}", "epa", d, d[7:11], "EPA diseño de registro"))


def ecv():
    for a in range(2008, 2026):
        r = _bajar(f"{BASE}/ecv/ecv_b2013/datos_{a}.zip", "ecv", f"datos_{a}.zip", str(a), f"ECV transversal {a} (base 2013)")
        if r.startswith("HTTP"):
            r = _bajar(f"{BASE}/ecv/ecv_b2004/ecvb04_{a}.zip", "ecv", f"ecvb04_{a}.zip", str(a), f"ECV transversal {a} (base 2004)")
        print("ecv", a, r, flush=True)


def epf():
    for a in range(2016, 2026):
        print("epf", a, _bajar(f"{BASE}/epf2006/epf_{a}.zip", "epf", f"epf_{a}.zip", str(a), f"EPF microdatos {a}"), flush=True)
    print("epf diseño", _bajar(f"{BASE}/epf2006/disreg_epf.zip", "epf", "disreg_epf.zip", "2006-", "EPF diseños de registro"))


def ees():
    for a in (2010, 2014, 2018, 2022):
        print("ees", a, _bajar(f"{BASE}/salarial/datos_{a}.zip", "ees", f"datos_{a}.zip", str(a), f"EES microdatos {a}"), flush=True)


if __name__ == "__main__":
    que = sys.argv[1:] or ["ecv", "epf", "ees", "epa"]
    for q in que:
        globals()[q]()
