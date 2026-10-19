"""M1 · make check: puertas de calidad. No escribe nada en el repositorio (git status igual antes y después).

1. ruff sobre src y tests.
2. pytest (tests/).
3. Fuentes: cada crudo registrado con URL, licencia, edición, fecha y sha256 coincidente; ningún crudo sin registrar; ningún fichero
   versionado de más de 50 MB.
4. Referencias: el estado de cada ficha coincide con el que da el verificador sin red (nadie marca VERIFICADA a mano).
5. cifras_clave: consolidada, ids únicos, capa y clasificación coherentes (C3 ⇔ IDENTIFICADO), campos obligatorios.
6. Lenguaje causal: ninguna frase causal en output/ ni publicacion/ fuera de líneas que citan un resultado IDENTIFICADO.
7. Supresión: en todo CSV de output/ con n_muestral, las celdas con n < 50 tienen el valor vacío.
8. Fase 5: todo resultado de output/f5 declara el commit de prereg-m1 y la puerta está abierta.
9. publicacion/: coincide con su MANIFIESTO.sha256 (generada, no editada a mano) y sin «[FALTA CIFRA».
10. Neutralidad: sin nombres de partidos en los entregables.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cifras  # noqa: E402
import etiquetas  # noqa: E402
import fuentes  # noqa: E402
import verificar_referencias as vr  # noqa: E402
from comun import RAIZ, UMBRAL_CELDA, sha256  # noqa: E402

LOCK = Path(os.environ.get("M1_LOCK_CHECK", "/tmp/m1_make_check.lock"))
CAUSAL = re.compile(r"\b(efecto causal|impacto causal|causa(n|ron|do)?\b|provoc(a|an|ó|aron)|caus(ó|aron)|se debe a|"
                    r"gracias a la inmigración|por culpa de)", re.I)
EXENTO = re.compile(r"IDENTIFICADO|NO ESTIMABLE|sin lenguaje causal|no (es|son|identifica|permite)|causal\w* (fuera|solo)|"
                    r"no causal|<!-- causal-ok -->|^#|pregunta|diseño|identificación|veredicto|afirmación|«", re.I)
PARTIDOS = re.compile(r"\b(PSOE|Partido Popular|\bPP\b|Vox|Sumar|Podemos|Ciudadanos|ERC|Junts|PNV|Bildu)\b")


def _git_status() -> str:
    return subprocess.run(["git", "status", "--porcelain"], cwd=RAIZ, capture_output=True, text=True).stdout


def paso(nombre, errores):
    print(("OK   " if not errores else "FALLA") + f" {nombre}" + ("" if not errores else f" ({len(errores)})"))
    for e in errores[:25]:
        print("       -", e)
    return not errores


def ruff() -> list[str]:
    r = subprocess.run(["ruff", "check", "src", "tests", "--quiet", "--no-cache"], cwd=RAIZ, capture_output=True, text=True)
    return [x for x in r.stdout.splitlines() if x.strip()] if r.returncode else []


def pytest_() -> list[str]:
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "M1_LOCK_SOLO_FICHERO": "1", "M1_LOCK_CHECK": "/tmp/m1_lock_tests"}
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests"], cwd=RAIZ, capture_output=True,
                       text=True, env=env)
    return [] if r.returncode == 0 else r.stdout.splitlines()[-15:]


def fuentes_() -> list[str]:
    e = fuentes.comprobar()
    r = subprocess.run(["git", "ls-files", "-z"], cwd=RAIZ, capture_output=True, text=True)
    for f in filter(None, r.stdout.split("\0")):
        p = RAIZ / f
        if p.exists() and p.stat().st_size > fuentes.GRANDE:
            e.append(f"fichero versionado de más de 50 MB: {f}")
    return e


def referencias() -> list[str]:
    e = []
    try:
        cache = json.loads(vr.CACHE.read_text(encoding="utf-8")) if vr.CACHE.exists() else {}
    except ValueError:
        return ["caché de Crossref ilegible"]
    for p in sorted(vr.LIT.glob("*.md")):
        for b in re.split(r"(?=^### )", p.read_text(encoding="utf-8"), flags=re.M):
            if not b.startswith("### "):
                continue
            cab = vr.FICHA.search(b).group(1)
            md = vr.DOI.search(b)
            doi = md.group(1).rstrip(".,;") if md else None
            if doi and doi not in cache:
                e.append(f"{p.name}: DOI sin caché {doi}")
                continue
            esperado = vr.estado(cab, cache.get(doi) if doi else None)
            m = vr.ESTADO.search(b)
            if not m or m.group(0) != f"- Estado: {esperado}":
                e.append(f"{p.name}: estado de «{cab[:50]}» no coincide con el verificador ({esperado})")
            if not vr.LEIDO.search(b):
                e.append(f"{p.name}: ficha sin «Leído»: {cab[:50]}")
    return e


def cifras_() -> list[str]:
    df = cifras.consolidar()
    e = cifras.errores(df)
    if cifras.DESTINO.exists():
        import pandas as pd
        actual = pd.read_csv(cifras.DESTINO, keep_default_na=False, na_values=[""])
        if set(actual["id"]) != set(df["id"]):
            e.append("output/cifras_clave.csv no está consolidada (python3 src/m1/cifras.py)")
    elif len(df):
        e.append("falta output/cifras_clave.csv")
    return e


def _textos():
    for base in ("output", "publicacion"):
        for p in (RAIZ / base).rglob("*.md"):
            yield p


def lenguaje() -> list[str]:
    e = []
    for p in _textos():
        for i, linea in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if CAUSAL.search(linea) and not EXENTO.search(linea):
                e.append(f"{p.relative_to(RAIZ)}:{i}: lenguaje causal fuera de IDENTIFICADO: «{linea.strip()[:90]}»")
    return e


def neutralidad() -> list[str]:
    e = []
    for p in _textos():
        for i, linea in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if PARTIDOS.search(linea):
                e.append(f"{p.relative_to(RAIZ)}:{i}: nombre de partido en un entregable")
    return e


def supresion() -> list[str]:
    import pandas as pd
    e = []
    for p in (RAIZ / "output").rglob("*.csv"):
        try:
            cab = pd.read_csv(p, nrows=0).columns
        except Exception:  # noqa: BLE001
            continue
        if "n_muestral" not in cab:
            continue
        d = pd.read_csv(p)
        vals = [c for c in d.columns if c.startswith(("valor", "tasa", "media", "brecha", "cuota", "p50", "d", "coef"))
                and c not in ("n_muestral",) and pd.api.types.is_numeric_dtype(d[c])]
        malos = d[(d["n_muestral"] < UMBRAL_CELDA) & d[vals].notna().any(axis=1)] if vals else d.iloc[0:0]
        if len(malos):
            e.append(f"{p.relative_to(RAIZ)}: {len(malos)} celdas con n < {UMBRAL_CELDA} sin suprimir")
    return e


def fase5() -> list[str]:
    res = list((RAIZ / "output" / "f5").rglob("resultado.json"))
    if not res:
        return []
    ok, motivo = etiquetas.estado()
    e = [] if ok else [f"hay resultados de la fase 5 pero la puerta está cerrada: {motivo}"]
    for p in res:
        d = json.loads(p.read_text(encoding="utf-8"))
        if not str(d.get("prereg", "")).startswith("prereg-m1"):
            e.append(f"{p.relative_to(RAIZ)}: no declara prereg-m1")
    return e


def publicacion() -> list[str]:
    base = RAIZ / "publicacion"
    man = base / "MANIFIESTO.sha256"
    ficheros = [p for p in base.rglob("*") if p.is_file() and p.name not in ("MANIFIESTO.sha256", ".gitkeep")]
    if not ficheros:
        return []
    if not man.exists():
        return ["publicacion/ sin MANIFIESTO.sha256 (genérela con make publicacion)"]
    esperado = dict(reversed(x.split("  ", 1)) for x in man.read_text(encoding="utf-8").splitlines() if x.strip())
    e = []
    for p in ficheros:
        rel = str(p.relative_to(base))
        if rel not in esperado:
            e.append(f"publicacion/{rel} no está en el manifiesto (¿escrito a mano?)")
        elif sha256(p) != esperado[rel]:
            e.append(f"publicacion/{rel} cambió tras generarse (¿editado a mano?)")
        if p.suffix in (".md", ".html", ".tex") and "[FALTA CIFRA" in p.read_text(encoding="utf-8", errors="ignore"):
            e.append(f"publicacion/{rel} contiene [FALTA CIFRA]")
    return e


def main() -> int:
    if LOCK.exists():
        try:
            os.kill(int(LOCK.read_text().split()[0]), 0)
            print("make check ya en marcha")
            return 1
        except (OSError, ValueError, IndexError):
            pass
    LOCK.write_text(f"{os.getpid()}\n")
    try:
        antes = _git_status()
        pasos = [("ruff", ruff), ("pytest", pytest_), ("fuentes y checksums", fuentes_), ("referencias", referencias),
                 ("cifras_clave", cifras_), ("lenguaje causal", lenguaje), ("neutralidad", neutralidad),
                 ("supresión de celdas", supresion), ("puerta de la fase 5", fase5), ("publicacion generada", publicacion)]
        ok = all([paso(n, f()) for n, f in pasos])
        ok = paso("git sin cambios tras el check", [] if _git_status() == antes else ["make check modificó el repositorio"]) and ok
        print("make check:", "LIMPIO" if ok else "CON FALLOS")
        return 0 if ok else 1
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
