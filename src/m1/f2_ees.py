"""M1-F2 · Normaliza la Encuesta de Estructura Salarial (INE, microdatos públicos 2010, 2014, 2018, 2022), sin red.

Origen: solo TIPOPAIS (nacionalidad: 1 España, 2 resto del mundo); no hay país de nacimiento ni años de residencia (limitación
declarada). Territorio: NUTS1. Ganancia por hora del mes de octubre (definición INE): (salario base + complementos salariales
+ pagos por horas extraordinarias) / horas del mes (jornada semanal pactada × 4,345 + horas extraordinarias), solo para
trabajadores sin días de situación especial en el mes (SIESPM1 = 6). Ganancia anual: retribución bruta del año más especie
(RETRINOIN + RETRIIN + VESPNOIN + VESPIN, o SALBRUTO + VESP en 2010), anualizada con los días de alta (DRELABAM, DRELABAD).
Salida: data/processed/ees.csv.gz (una fila por trabajador con FACTOTAL).
"""
from __future__ import annotations

import io
import re
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import PROC, RAW  # noqa: E402


def leer(a: int) -> pd.DataFrame:
    with zipfile.ZipFile(RAW / "ees" / "grandes" / f"datos_{a}.zip") as z:
        n = [x for x in z.namelist() if re.match(r"(?i)^csv/ees_\d{4}\.(csv|tab)$", x)][0]
        d = pd.read_csv(io.BytesIO(z.read(n)), sep="\t", dtype=str, keep_default_na=False)
    d = d.apply(lambda s: s.str.strip())
    num = lambda c: pd.to_numeric(d[c].str.replace(",", "."), errors="coerce") if c in d else pd.Series(0.0, index=d.index)  # noqa: E731
    mens = num("SALBASE") + num("COMSAL") + num("COMSALTT") + num("PHEXTRA")
    horas = (num("JSP1") + num("JSP2") / 60) * 4.345 + num("HEXTRA")
    hora = (mens / horas).where((d["SIESPM1"] == "6") & (horas > 0))
    if "RETRINOIN" in d:
        anual = num("RETRINOIN") + num("RETRIIN") + num("VESPNOIN") + num("VESPIN")
    else:
        anual = num("SALBRUTO") + num("VESP")
    dias = num("DRELABAM") * 30.4 + num("DRELABAD")
    anual_eq = (anual * 365 / dias).where(dias >= 30)
    return pd.DataFrame({
        "anio": a, "nuts1": d["NUTS1"], "sexo": d["SEXO"].map({"1": "hombre", "6": "mujer"}),
        "extranjero": d["TIPOPAIS"].eq("2"), "edad": d["ANOS2"], "estudios": d["ESTU"], "cno1": d["CNO1"].str[0],
        "cnace": d["CNACE"].str[0], "jornada": d["TIPOJOR"].map({"1": "completa", "2": "parcial"}),
        "contrato": d["TIPOCON"].map({"1": "indefinido", "2": "temporal"}),
        "antig": num("ANOANTI"), "control": d["CONTROL"], "salario_hora": hora, "salario_anual": anual,
        "salario_anual_eq": anual_eq, "factor": num("FACTOTAL")})


def main() -> int:
    df = pd.concat([leer(a) for a in (2010, 2014, 2018, 2022)], ignore_index=True)
    df.to_csv(PROC / "ees.csv.gz", index=False)
    r = df.groupby(["anio", "extranjero"]).apply(lambda g: np.average(g.salario_hora.fillna(0), weights=g.factor *
                                                                      g.salario_hora.notna()), include_groups=False)
    print("f2_ees:", len(df), "trabajadores; ganancia media por hora:", r.round(2).to_dict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
