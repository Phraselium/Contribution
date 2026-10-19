"""M1 · Ejecuta los scripts deterministas de una fase (src/m1/f<N>_*.py, en orden alfabético) y consolida cifras_clave.

Uso: python3 src/m1/fase.py <N> [patrón]. Los scripts de descarga (sufijo _descarga.py) solo corren con --red.
La fase 5 exige la puerta prereg-m1 (src/m1/etiquetas.py); cada script f5_* la vuelve a comprobar.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SRC = RAIZ / "src" / "m1"


def main() -> int:
    n = sys.argv[1]
    patron = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "*"
    red = "--red" in sys.argv
    if n in ("5", "6", "7"):
        sys.path.insert(0, str(SRC))
        import etiquetas
        if n == "5" or (RAIZ / "output" / "f5").exists():
            etiquetas.exigir()
    scripts = sorted(p for p in SRC.glob(f"f{n}_{patron}.py") if red == p.stem.endswith("_descarga"))
    for s in scripts:
        print(f"── {s.relative_to(RAIZ)}", flush=True)
        r = subprocess.run([sys.executable, str(s)], cwd=RAIZ)
        if r.returncode:
            print(f"FALLA {s.name} (código {r.returncode})")
            return r.returncode
    return subprocess.run([sys.executable, str(SRC / "cifras.py")], cwd=RAIZ).returncode


if __name__ == "__main__":
    sys.exit(main())
