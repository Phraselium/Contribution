"""M1-F1 · Extrae la tabla final de cada fichero de docs/literatura (una por pregunta) a output/f1/tabla_<pregunta>.csv y resume el
estado de verificación de las referencias en output/f1/referencias.csv. Sin red."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import DOCS, OUT  # noqa: E402


def tabla_final(texto: str) -> pd.DataFrame:
    bloques, actual = [], []
    for linea in texto.splitlines():
        if linea.startswith("|"):
            actual.append([c.strip() for c in linea.strip().strip("|").split("|")])
        elif actual:
            bloques.append(actual)
            actual = []
    if actual:
        bloques.append(actual)
    if not bloques:
        return pd.DataFrame()
    b = [f for f in bloques[-1] if not re.match(r"^:?-+:?$", f[0].replace(" ", ""))]
    return pd.DataFrame(b[1:], columns=b[0][: len(b[1])] if b[1:] else b[0])


def main() -> int:
    (OUT / "f1").mkdir(parents=True, exist_ok=True)
    refs = []
    for p in sorted((DOCS / "literatura").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        tabla_final(t).to_csv(OUT / "f1" / f"tabla_{p.stem}.csv", index=False)
        for b in re.split(r"(?=^### )", t, flags=re.M)[1:]:
            cab = b.splitlines()[0][4:]
            est = re.search(r"^- Estado: (.*)$", b, re.M)
            doi = re.search(r"^- DOI:\s*(10\.\S+)", b, re.M)
            refs.append({"pregunta": p.stem, "referencia": cab, "doi": doi.group(1) if doi else "",
                         "estado": est.group(1) if est else ""})
    r = pd.DataFrame(refs)
    r.to_csv(OUT / "f1" / "referencias.csv", index=False)
    print("f1_tablas:", r.groupby("pregunta").size().to_dict(), r["estado"].str.split(" \\(").str[0].value_counts().to_dict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
