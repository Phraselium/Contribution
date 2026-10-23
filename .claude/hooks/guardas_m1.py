#!/usr/bin/env python3
"""M1 · Guardas PreToolUse (adaptadas de Econometr-a V15-V16). Lee el JSON del hook por la entrada estándar; sale con código 2
(bloquea, motivo en stderr) si:

Bash
  (a) heredoc sin comillas («<<EOF» en lugar de «<<'EOF'»);
  (b) `make check` cuando ya hay uno en marcha (cerrojo /tmp/m1_make_check.lock con PID vivo, o proceso `make check`);
  (c) fase 5 sin la etiqueta prereg-m1: `make m1_f5*`, `make m1_f6`/`m1_f7` (dependen de la 5) o `python … src/m1/f5_*`;
  (d) borrar o sobrescribir datos crudos: rm/mv/truncate/git rm/git clean sobre data/raw, redirección > a data/raw;
  (e) rehacer todo o destruir: make clean, make all, git push --force/-f, git filter-repo, git reset --hard, rm -rf data|output;
  (f) push a una rama que no es la de trabajo (claude/m1-contribucion-origen) ni la etiqueta prereg-m1;
  (g) descargas (curl, wget, python, git clone…) desde dominios que exigen solicitud o credenciales no públicas
      (src/m1/politica_fuentes.py).
WebFetch
  (g) la misma lista de dominios.
Write / Edit / NotebookEdit
  (h) sobrescribir o editar un fichero ya existente de data/raw (los crudos solo se añaden);
  (i) escribir a mano en publicacion/ (se genera con `make publicacion`).
Registro (sin bloquear, a posteriori): (j) toda orden make con la secuencia completa m1_f0 … m1_f7 (equivalente a `make all`) se
anota en docs/registro_secuencia_completa.log.
Uso como función: `evaluar(datos_hook, raiz) -> motivo | None` (tests/test_guardas.py).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path

RAMA = "claude/m1-contribucion-origen"
LOCK = Path(os.environ.get("M1_LOCK_CHECK", "/tmp/m1_make_check.lock"))
HEREDOC_SIN_COMILLAS = re.compile(r"(?<!<)<<-?\s*([A-Za-z_][A-Za-z0-9_]*)\b")
CUERPO = re.compile(r"(?m)^([^\n]*?)<<-?\s*(['\"])([A-Za-z_][A-Za-z0-9_]*)\2[^\n]*\n(.*?)^\3\s*$", re.S)
RAW = r"(\./)?data/raw(/|\s|$|['\"])"
PROHIBIDOS = [
    (re.compile(r"\bmake\b[^;&|\n]*\s(clean|all)(\s|$|;|&|\|)"), "(e) make clean / make all están prohibidos sin orden del autor"),
    (re.compile(r"\bgit\s+push\b[^;&|\n]*\s(--force\S*|-f)(\s|$)"), "(e) git push --force está prohibido"),
    (re.compile(r"\bgit\s+filter-repo\b"), "(e) git filter-repo está prohibido"),
    (re.compile(r"\bgit\s+reset\s+--hard\b"), "(e) git reset --hard está prohibido sin orden del autor"),
    (re.compile(r"\brm\s+(-\S+\s+)*(\./)?(data|output)(/?\s|/?$)"), "(e) rm de data/ u output/ completos está prohibido"),
    (re.compile(r"\b(rm|unlink|shred|truncate)\b[^;&|\n]*" + RAW), "(d) prohibido borrar datos crudos (data/raw)"),
    (re.compile(r"\bmv\s+[^;&|\n]*" + RAW), "(d) prohibido mover datos crudos (data/raw)"),
    (re.compile(r"\bgit\s+(rm|clean)\b[^;&|\n]*" + RAW), "(d) prohibido borrar datos crudos (data/raw)"),
    (re.compile(r"\bgit\s+clean\s+-\S*[fdx]"), "(d) git clean está prohibido (borraría datos crudos ignorados)"),
    (re.compile(r"\bfind\b[^;&|\n]*data/raw[^;&|\n]*-delete"), "(d) prohibido borrar datos crudos (data/raw)"),
]


def _politica(raiz: Path):
    spec = importlib.util.spec_from_file_location("politica_fuentes", raiz / "src" / "m1" / "politica_fuentes.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _etiquetas(raiz: Path):
    spec = importlib.util.spec_from_file_location("etiquetas_m1", raiz / "src" / "m1" / "etiquetas.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _sin_cuerpos(cmd: str, solo_texto: bool = False) -> str:
    def rep(m):
        if solo_texto and not re.search(r"\b(cat|tee)\b", m.group(1)):
            return m.group(0)
        return m.group(1) + "<<'cuerpo'\n"
    return CUERPO.sub(rep, cmd)


def _vivo(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        return False


def make_check_en_marcha() -> bool:
    if LOCK.exists():
        try:
            if _vivo(int(LOCK.read_text().split()[0])):
                return True
        except (ValueError, IndexError):
            pass
    if os.environ.get("M1_LOCK_SOLO_FICHERO"):
        return False
    for p in Path("/proc").glob("[0-9]*/cmdline"):
        try:
            c = p.read_bytes().replace(b"\0", b" ").decode(errors="ignore").strip()
        except OSError:
            continue
        if re.match(r"^make\s+(-\S+\s+)*check(\s|$)", c):
            return True
    return False


def _puerta_abierta(raiz: Path) -> tuple[bool, str]:
    try:
        return _etiquetas(raiz).estado(raiz)
    except Exception as e:  # noqa: BLE001 (sin módulo o sin git: la puerta queda cerrada)
        return False, f"no se pudo comprobar la etiqueta ({e})"


def _push_mal(cmd: str) -> str | None:
    for m in re.finditer(r"\bgit\s+push\b([^;&|\n]*)", cmd):
        args = [a for a in m.group(1).split() if not a.startswith("-")]
        refs = args[1:] if args else []
        if not refs:
            return "(f) git push sin refspec explícito: use git push -u origin " + RAMA
        for r in refs:
            dest = r.split(":")[-1].replace("refs/heads/", "").replace("refs/tags/", "")
            if dest not in (RAMA, "prereg-m1"):
                return f"(f) push solo a la rama de trabajo {RAMA} (o la etiqueta prereg-m1), no a «{dest}»"
    return None


FASES = {f"m1_f{i}" for i in range(8)}
REGISTRO = Path(os.environ.get("M1_REGISTRO_SECUENCIA", "")) if os.environ.get("M1_REGISTRO_SECUENCIA") else None


def registrar_secuencia(cmd: str, raiz: Path) -> bool:
    """(j) registro, sin bloquear (a posteriori): toda orden make que contenga la secuencia completa m1_f0 … m1_f7 (la equivalente a
    `make all`, que (e) bloquea) se anota con fecha, directorio y orden en docs/registro_secuencia_completa.log."""
    hit = False
    for m in re.finditer(r"\bmake\b([^;&|\n]*)", cmd):
        if FASES <= set(re.findall(r"\bm1_f[0-7]\b", m.group(1))):
            hit = True
    if hit:
        import datetime as dt
        log = REGISTRO or (raiz / "docs" / "registro_secuencia_completa.log")
        try:
            log.parent.mkdir(parents=True, exist_ok=True)
            with open(log, "a", encoding="utf-8") as fh:
                fh.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%dT%H:%M:%SZ}\tcwd={os.getcwd()}\t{' '.join(cmd.split())[:500]}\n")
        except OSError:
            pass
    return hit


def evaluar_bash(cmd: str, raiz: Path) -> str | None:
    registrar_secuencia(cmd, raiz)
    if HEREDOC_SIN_COMILLAS.search(_sin_cuerpos(cmd)):
        return "(a) heredoc sin comillas: use <<'EOF' (el shell expandiría `…` y $(…))"
    if re.search(r"\bmake\b[^;&|\n]*\scheck(\s|$|;|&|\|)", cmd) and make_check_en_marcha():
        return "(b) ya hay un make check en marcha: un solo make check a la vez"
    # m1_f6 y m1_f7 dependen de la fase 5 solo si hay resultados causales (output/f5); m1_f5 y src/m1/f5_* siempre
    causal = (re.search(r"\bmake\b[^;&|\n]*\sm1_f5\w*", cmd) or re.search(r"src/m1/f5_\w+\.py", cmd) or
              (re.search(r"\bmake\b[^;&|\n]*\sm1_f[67]\w*", cmd) and (raiz / "output" / "f5").exists()))
    if causal:
        ok, motivo = _puerta_abierta(raiz)
        if not ok:
            return f"(c) fase 5 (y las que dependen de ella) bloqueada: {motivo}"
    orden = _sin_cuerpos(cmd, solo_texto=True)
    for pat, motivo in PROHIBIDOS:
        if pat.search(orden):
            return motivo
    if re.search(r">>?\s*(\./)?data/raw/\S+", orden) and not re.search(r">>\s*(\./)?data/raw/\S*CHECKSUMS", orden):
        destino = re.search(r">>?\s*((\./)?data/raw/\S+)", orden).group(1)
        if (raiz / destino).exists():
            return "(d) prohibido sobrescribir datos crudos existentes (data/raw)"
    p = _push_mal(orden)
    if p:
        return p
    pol = _politica(raiz)
    for u in pol.urls_en(cmd):
        m = pol.motivo_bloqueo(u)
        if m:
            return f"(g) descarga bloqueada: {m} ({u[:80]})"
    return None


def evaluar(datos: dict, raiz: Path) -> str | None:
    herr = datos.get("tool_name")
    ent = datos.get("tool_input") or {}
    if herr == "Bash":
        return evaluar_bash(ent.get("command", ""), raiz)
    if herr == "WebFetch":
        m = _politica(raiz).motivo_bloqueo(ent.get("url", ""))
        return f"(g) descarga bloqueada: {m}" if m else None
    if herr in ("Write", "Edit", "NotebookEdit", "MultiEdit"):
        ruta = ent.get("file_path") or ent.get("notebook_path") or ""
        rel = ruta[len(str(raiz)) + 1:] if ruta.startswith(str(raiz) + "/") else re.sub(r"^\./", "", ruta)
        if rel.startswith("data/raw/") and (raiz / rel).exists():
            return "(h) los datos crudos no se editan ni se sobrescriben (data/raw solo admite ficheros nuevos)"
        if rel.startswith("publicacion/"):
            return "(i) publicacion/ se genera con make publicacion, nunca a mano"
    return None


def main() -> int:
    try:
        datos = json.load(sys.stdin)
    except ValueError:
        return 0
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))
    motivo = evaluar(datos, raiz)
    if motivo:
        print(f"Guarda M1: {motivo}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
