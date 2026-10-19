"""M1-F2 · Normaliza la Encuesta Nacional de Salud 2017 (INE/Ministerio de Sanidad, microdatos públicos) a un fichero de uso de
servicios sanitarios por persona, sin red. Sirve para repartir el gasto sanitario público (COFOG GF07) por edad, sexo y origen
con uso observado en lugar de suponer el mismo uso a igual edad (fase 4; sensibilidad del plan).

Adultos (15+): país de nacimiento E1_1 (1 España, 2 extranjero), nacionalidad E2_1a/b, consultas al médico de familia (N49) y al
especialista (N51) en 4 semanas, ingresos hospitalarios en 12 meses (O67) y días del último (O70), urgencias en 12 meses (O79),
medicamentos recetados en 2 semanas (P85). Menores (0-14): A1_1, G17, G18b, H34, H35 (sin urgencias ni medicamentos).
Posiciones del diseño de registro (disreg_ensalud17.zip). Salida: data/processed/ense_uso.csv.gz.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import PROC, RAW  # noqa: E402

# (nombre, inicio 1-based, fin) según el diseño de registro
ADULTO = [("CCAA", 1, 2), ("sexo", 13, 13), ("edad", 14, 16), ("nac", 28, 28), ("nacion_esp", 29, 29), ("nacion_ext", 30, 30),
          ("nivest", 37, 38), ("gp4", 222, 223), ("esp4", 225, 226), ("ing12", 284, 285), ("ingreso_si", 283, 283),
          ("dias_ult", 287, 289), ("urg_si", 300, 300), ("urg12", 301, 303), ("med2", 327, 327), ("factor", 567, 577)]
MENOR = [("CCAA", 1, 2), ("sexo", 13, 13), ("edad", 14, 16), ("nac", 25, 25), ("nacion_esp", 26, 26), ("nacion_ext", 27, 27),
         ("gp4", 116, 117), ("esp4", 119, 120), ("ing12", 170, 171), ("dias_ult", 172, 174), ("factor", 321, 331)]


def leer(z: zipfile.ZipFile, nombre: str, campos) -> pd.DataFrame:
    txt = z.read(nombre).decode("latin-1").splitlines()
    datos = {n: [linea[a - 1:b].strip() for linea in txt] for n, a, b in campos}
    return pd.DataFrame(datos).replace("", np.nan)


def main() -> int:
    with zipfile.ZipFile(RAW / "ense" / "datos_ensalud17_txt.zip") as z:
        a = leer(z, "MICRODAT.CA.txt", ADULTO)
        m = leer(z, "MICRODAT.CM.txt", MENOR)
    for d in (a, m):
        for c in d.columns:
            if c != "CCAA":
                d[c] = pd.to_numeric(d[c], errors="coerce")
        d["factor"] = d["factor"] / 1e4 if d["factor"].median() > 1e5 else d["factor"]
        # 98/99 y 998/999: no sabe / no contesta
        for c in ("gp4", "esp4", "ing12", "dias_ult", "urg12"):
            if c in d:
                d.loc[d[c] >= 97, c] = np.nan
    a.loc[a["ingreso_si"] == 2, ["ing12", "dias_ult"]] = 0
    a.loc[a["urg_si"] == 2, "urg12"] = 0
    a["med_receta"] = (a["med2"] == 1).astype(float).where(a["med2"].isin([1, 2]))
    a["poblacion"], m["poblacion"] = "adulto", "menor"
    d = pd.concat([a, m], ignore_index=True)
    d["nacido_fuera"] = d["nac"] == 2
    d["extranjero"] = d["nacion_ext"] == 1
    d["sexo"] = d["sexo"].map({1: "hombre", 2: "mujer"})
    # uso anual equivalente: consultas en 4 semanas × 13; días de hospital ≈ ingresos × días del último ingreso
    d["consultas_ap"] = d["gp4"] * 13
    d["consultas_esp"] = d["esp4"] * 13
    d["dias_hosp"] = d["ing12"] * d["dias_ult"]
    d["urgencias"] = d.get("urg12")
    cols = ["poblacion", "CCAA", "sexo", "edad", "nacido_fuera", "extranjero", "nivest", "factor", "consultas_ap", "consultas_esp",
            "dias_hosp", "urgencias", "med_receta"]
    d[cols].to_csv(PROC / "ense_uso.csv.gz", index=False)
    print(f"f2_ense: {len(a)} adultos, {len(m)} menores; nacidos fuera {d['nacido_fuera'].mean():.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
