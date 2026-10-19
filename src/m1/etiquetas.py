"""M1 · Puerta del pre-registro interno prereg-m1 (sin sello de tiempo externo).

La fase 5 (efectos causales) solo corre si:
1. existe la etiqueta prereg-m1, en el remoto o en local; si solo está en local (el proxy no deja subir etiquetas), su commit
   tiene que estar en la rama remota de trabajo (origin/claude/m1-contribucion-origen);
2. los ficheros del pre-registro (docs/preregistro.md y su adenda) no han cambiado desde el commit de la etiqueta.

Para tests y trabajo sin red: M1_ETIQUETAS_REMOTAS apunta a un JSON {etiqueta: commit} que sustituye a la consulta al remoto, y
M1_FORZAR_PUERTA=cerrada fuerza el cierre.
Uso: python3 src/m1/etiquetas.py  → imprime el estado y sale con 0 (abierta) o 1 (cerrada).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ETIQUETA = "prereg-m1"
RAMA = "claude/m1-contribucion-origen"
FICHEROS = ["docs/preregistro.md", "docs/preregistro_adenda.md"]


def _git(args, raiz, timeout=25):
    try:
        r = subprocess.run(["git", *args], cwd=raiz, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r


def remota(raiz: Path = RAIZ) -> str | None:
    f = os.environ.get("M1_ETIQUETAS_REMOTAS")
    if f:
        try:
            return json.loads(Path(f).read_text(encoding="utf-8")).get(ETIQUETA)
        except (OSError, ValueError):
            return None
    r = _git(["ls-remote", "--tags", "origin", f"refs/tags/{ETIQUETA}", f"refs/tags/{ETIQUETA}^{{}}"], raiz)
    if r is None or r.returncode != 0:
        return None
    filas = dict(reversed(x.split("\t")) for x in r.stdout.strip().splitlines() if "\t" in x)
    return filas.get(f"refs/tags/{ETIQUETA}^{{}}") or filas.get(f"refs/tags/{ETIQUETA}")


def local(raiz: Path = RAIZ) -> str | None:
    r = _git(["rev-parse", "-q", "--verify", f"refs/tags/{ETIQUETA}^{{commit}}"], raiz)
    return r.stdout.strip() if r is not None and r.returncode == 0 and r.stdout.strip() else None


def estado(raiz: Path = RAIZ) -> tuple[bool, str]:
    if os.environ.get("M1_FORZAR_PUERTA") == "cerrada":
        return False, "puerta cerrada por M1_FORZAR_PUERTA"
    sha_r, sha_l = remota(raiz), local(raiz)
    if sha_r:
        commit, via = sha_r, "etiqueta en el remoto"
    elif sha_l:
        r = _git(["merge-base", "--is-ancestor", sha_l, f"origin/{RAMA}"], raiz)
        if r is None or r.returncode != 0:
            return False, f"{ETIQUETA} solo en local y su commit {sha_l[:7]} no está en origin/{RAMA}"
        commit, via = sha_l, f"etiqueta local con su commit en origin/{RAMA}"
    else:
        return False, f"no existe la etiqueta {ETIQUETA} (ni en el remoto ni en local): la fase 5 espera al pre-registro"
    existentes = [f for f in FICHEROS if (raiz / f).exists()]
    if "docs/preregistro.md" not in existentes:
        return False, "falta docs/preregistro.md"
    r = _git(["diff", "--quiet", commit, "HEAD", "--", *existentes], raiz)
    if r is None or r.returncode != 0:
        return False, f"los ficheros del pre-registro han cambiado desde {commit[:7]}"
    return True, f"{ETIQUETA} → {commit[:7]} ({via}); pre-registro interno sin sello de tiempo externo"


def exigir() -> str:
    """Para los scripts de la fase 5: aborta si la puerta está cerrada; devuelve el motivo (con el commit) si está abierta."""
    ok, motivo = estado()
    if not ok:
        raise SystemExit(f"Fase 5 bloqueada: {motivo}")
    return motivo


if __name__ == "__main__":
    ok, m = estado()
    print(("ABIERTA: " if ok else "CERRADA: ") + m)
    sys.exit(0 if ok else 1)
