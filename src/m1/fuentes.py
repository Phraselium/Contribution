"""M1 · Descargador de fuentes públicas con registro (URL, licencia, edición, fecha de descarga y sha256).

- Rechaza las URL de servicios que exigen solicitud o credenciales no públicas (src/m1/politica_fuentes.py).
- Nunca sobrescribe un crudo: si el fichero ya existe con el mismo sha256 no hace nada; si existe con otro contenido, guarda la
  nueva edición con la fecha en el nombre.
- Registra cada fichero en data/fuentes.csv y data/CHECKSUMS.sha256. Los ficheros de más de 50 MB quedan en data/raw pero
  ignorados por git (.gitignore: data/raw/**/grandes/); se versionan su URL, su checksum y el script que los descarga.
Uso como módulo: descargar(url, familia, nombre, licencia, edicion, descripcion).
"""
from __future__ import annotations

import csv
import datetime as dt
import shutil
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import RAIZ, RAW, sha256  # noqa: E402
from politica_fuentes import motivo_bloqueo  # noqa: E402

CATALOGO = RAIZ / "data" / "fuentes.csv"
CHECKSUMS = RAIZ / "data" / "CHECKSUMS.sha256"
COLS = ["ruta", "familia", "url", "licencia", "edicion", "fecha_descarga", "sha256", "bytes", "versionado", "descripcion"]
GRANDE = 50 * 1024 * 1024
VERSIONAR_MAX = 10 * 1024 * 1024   # D10: los crudos de más de 10 MB no se versionan
UA = "M1-estudio-publico/1.0 (investigacion; solo datos publicos)"


def _catalogo() -> list[dict]:
    if not CATALOGO.exists():
        return []
    with CATALOGO.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _guardar_catalogo(filas: list[dict]) -> None:
    CATALOGO.parent.mkdir(parents=True, exist_ok=True)
    filas = sorted({f["ruta"]: f for f in filas}.values(), key=lambda f: f["ruta"])
    with CATALOGO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(filas)
    CHECKSUMS.write_text("".join(f"{f['sha256']}  {f['ruta']}\n" for f in filas), encoding="utf-8")


def _ignorar(rel: str) -> None:
    gi = RAIZ / ".gitignore"
    texto = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if f"/{rel}\n" not in texto:
        if "# crudos > 10 MB" not in texto:
            texto = texto.rstrip("\n") + "\n# crudos > 10 MB (D10; generado por src/m1/fuentes.py)\n"
        gi.write_text(texto + f"/{rel}\n", encoding="utf-8")


def registrar(ruta: Path, familia: str, url: str, licencia: str, edicion: str, descripcion: str, fecha: str | None = None) -> dict:
    rel = str(ruta.relative_to(RAIZ))
    size = ruta.stat().st_size
    fila = dict(ruta=rel, familia=familia, url=url, licencia=licencia, edicion=edicion,
                fecha_descarga=fecha or dt.date.today().isoformat(), sha256=sha256(ruta), bytes=size,
                versionado="no (ignorado; checksum)" if ("/grandes/" in rel or size > VERSIONAR_MAX) else "sí",
                descripcion=descripcion)
    if size > VERSIONAR_MAX and "/grandes/" not in rel:
        _ignorar(rel)
    import fcntl
    with open(CATALOGO.with_suffix(".lock"), "w") as lk:   # varias descargas a la vez no pisan el catálogo
        fcntl.flock(lk, fcntl.LOCK_EX)
        filas = [f for f in _catalogo() if f["ruta"] != rel] + [fila]
        _guardar_catalogo(filas)
    return fila


def descargar(url: str, familia: str, nombre: str, licencia: str, edicion: str, descripcion: str,
              reintentos: int = 4, timeout: int = 300, no_versionar: bool = False) -> Path:
    """no_versionar=True deja el fichero en grandes/ (ignorado, con checksum) aunque pese menos de 50 MB: para series
    voluminosas (p. ej. 86 trimestres de la EPA) que se reconstruyen con el script de descarga."""
    m = motivo_bloqueo(url)
    if m:
        raise PermissionError(f"fuente no pública: {m} ({url})")
    destino_dir = RAW / familia
    destino_dir.mkdir(parents=True, exist_ok=True)
    tmp = destino_dir / f".{nombre}.part"
    espera = 2
    for intento in range(reintentos + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r, open(tmp, "wb") as fh:  # noqa: S310 (URL pública registrada)
                shutil.copyfileobj(r, fh, 1 << 20)
            break
        except Exception:  # noqa: BLE001
            if intento == reintentos:
                tmp.unlink(missing_ok=True)
                raise
            time.sleep(espera)
            espera *= 2
    destino = destino_dir / nombre
    if (destino_dir / "grandes" / nombre).exists():
        destino = destino_dir / "grandes" / nombre
    if tmp.stat().st_size > GRANDE or no_versionar:
        (destino_dir / "grandes").mkdir(exist_ok=True)
        destino = destino_dir / "grandes" / nombre
    if destino.exists():
        if sha256(destino) == sha256(tmp):
            tmp.unlink()
            if str(destino.relative_to(RAIZ)) not in {f["ruta"] for f in _catalogo()}:
                registrar(destino, familia, url, licencia, edicion, descripcion)
            return destino
        destino = destino.with_name(f"{destino.stem}_{dt.date.today():%Y%m%d}{destino.suffix}")
    tmp.rename(destino)
    registrar(destino, familia, url, licencia, edicion, descripcion)
    return destino


def ya_descargado(url: str) -> Path | None:
    """Ruta del crudo ya registrado para esa URL si existe en disco con su checksum (para reanudar descargas)."""
    for f in _catalogo():
        if f["url"] == url and (RAIZ / f["ruta"]).exists():
            return RAIZ / f["ruta"]
    return None


def comprobar() -> list[str]:
    """Errores de integridad: ficheros del catálogo ausentes (solo si son versionados) o con otro checksum, y crudos sin registrar."""
    errores, cat = [], {f["ruta"]: f for f in _catalogo()}
    for rel, f in cat.items():
        p = RAIZ / rel
        if not p.exists():
            if f["versionado"] == "sí":
                errores.append(f"falta el crudo versionado {rel}")
            continue
        if sha256(p) != f["sha256"]:
            errores.append(f"checksum distinto en {rel}")
        for c in ("url", "licencia", "fecha_descarga", "edicion"):
            if not f.get(c):
                errores.append(f"{rel}: falta {c}")
    for p in RAW.rglob("*"):
        if p.is_file() and not p.name.startswith(".") and str(p.relative_to(RAIZ)) not in cat:
            errores.append(f"crudo sin registrar en data/fuentes.csv: {p.relative_to(RAIZ)}")
    return errores


if __name__ == "__main__":
    e = comprobar()
    print("\n".join(e) or "fuentes: catálogo íntegro")
    sys.exit(1 if e else 0)
