"""M1-F0 · Extrae las tablas de docs/fuentes_publicas.md a output/f0/inventario_fuentes.csv (una fila por variable o fuente) y
comprueba que existe la lista de lo no público. Sin red."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import DOCS, OUT  # noqa: E402


def main() -> int:
    t = (DOCS / "fuentes_publicas.md").read_text(encoding="utf-8")
    filas, seccion, cab = [], "", None
    for linea in t.splitlines():
        if linea.startswith("#"):
            seccion, cab = linea.lstrip("# ").strip(), None
            continue
        if linea.startswith("|"):
            celdas = [c.strip() for c in linea.strip("|").split("|")]
            if re.match(r"^-+$", celdas[0].replace(":", "")):
                continue
            if cab is None:
                cab = celdas
                continue
            filas.append({"seccion": seccion, **{cab[i] if i < len(cab) else f"c{i}": c for i, c in enumerate(celdas)}})
    df = pd.DataFrame(filas)
    if not any("NO es público" in s for s in df["seccion"]):
        print("falta la sección de lo no público")
        return 1
    (OUT / "f0").mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT / "f0" / "inventario_fuentes.csv", index=False)
    print(f"f0_inventario: {len(df)} filas; {sum('NO es público' in s for s in df['seccion'])} datos no públicos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
