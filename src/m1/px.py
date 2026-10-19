"""M1 · Lector mínimo de ficheros PC-Axis (.px) del INE a DataFrame largo (una columna por dimensión y `valor`)."""
from __future__ import annotations

import itertools
import re
from pathlib import Path

import numpy as np
import pandas as pd


def leer_px(ruta: Path, codificacion: str = "iso-8859-15") -> pd.DataFrame:
    t = Path(ruta).read_bytes().decode(codificacion)

    def lista(clave):
        m = re.search(r'%s=(.*?);' % re.escape(clave), t, re.S)
        return re.findall(r'"([^"]*)"', m.group(1)) if m else []

    dims = lista("STUB") + lista("HEADING")
    valores = [lista(f'VALUES("{d}")') for d in dims]
    datos = t.split("DATA=", 1)[1].rsplit(";", 1)[0]
    nums = [np.nan if x.strip('"') in ("", ".", "..", "...", "-") else float(x) for x in re.findall(r'"[^"]*"|[^\s"]+', datos)]
    n = int(np.prod([len(v) for v in valores]))
    if len(nums) != n:
        raise ValueError(f"{ruta}: {len(nums)} datos frente a {n} celdas")
    filas = list(itertools.product(*valores))
    df = pd.DataFrame(filas, columns=dims)
    df["valor"] = nums
    return df
