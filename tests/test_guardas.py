"""Tests que demuestran que las guardas de M1 bloquean (y que no bloquean lo permitido)."""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]
HOOK = RAIZ / ".claude" / "hooks" / "guardas_m1.py"
spec = importlib.util.spec_from_file_location("guardas_m1", HOOK)
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)


def bash(cmd):
    return G.evaluar({"tool_name": "Bash", "tool_input": {"command": cmd}}, RAIZ)


@pytest.fixture(autouse=True)
def _sin_check_en_marcha(monkeypatch, tmp_path):
    monkeypatch.setattr(G, "LOCK", tmp_path / "lock")
    monkeypatch.setenv("M1_LOCK_SOLO_FICHERO", "1")


@pytest.mark.parametrize("cmd", [
    "cat > x.py <<EOF\nprint(1)\nEOF",
    "python3 - <<PY\nprint(1)\nPY",
])
def test_heredoc_sin_comillas_bloquea(cmd):
    assert bash(cmd).startswith("(a)")


def test_heredoc_entrecomillado_pasa():
    assert bash("cat > x.py <<'EOF'\nprint(`date`)\nEOF") is None


def test_un_solo_make_check(tmp_path, monkeypatch):
    lock = tmp_path / "lock"
    lock.write_text(f"{os.getpid()}\n")
    monkeypatch.setattr(G, "LOCK", lock)
    assert bash("make check").startswith("(b)")
    lock.write_text("999999999\n")
    assert bash("make check") is None


@pytest.mark.parametrize("cmd", ["make m1_f5", "make m1_f5_p1", "python3 src/m1/f5_p1_shiftshare.py"])
def test_fase5_sin_prereg_bloquea(cmd, monkeypatch):
    monkeypatch.setenv("M1_FORZAR_PUERTA", "cerrada")
    assert bash(cmd).startswith("(c)")


def test_fase5_con_prereg_remota_pasa(monkeypatch, tmp_path):
    """Con la etiqueta en el remoto apuntando a HEAD y el pre-registro sin cambios, la puerta se abre."""
    monkeypatch.delenv("M1_FORZAR_PUERTA", raising=False)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
    if not (RAIZ / "docs" / "preregistro.md").exists():
        pytest.skip("sin docs/preregistro.md todavía")
    f = tmp_path / "et.json"
    f.write_text(json.dumps({"prereg-m1": head}))
    monkeypatch.setenv("M1_ETIQUETAS_REMOTAS", str(f))
    dif = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", "docs/preregistro.md"], cwd=RAIZ).returncode
    if dif:
        pytest.skip("pre-registro con cambios sin commit")
    assert bash("make m1_f5") is None


@pytest.mark.parametrize("cmd", [
    "rm data/raw/ine/ecp.json", "rm -f ./data/raw/eurostat/x.tsv", "git rm -r data/raw/epa", "mv data/raw/a.csv /tmp/",
    "find data/raw -name '*.zip' -delete", "truncate -s0 data/raw/ine/x.csv", "git clean -fdx",
])
def test_borrar_crudos_bloquea(cmd):
    assert bash(cmd).startswith("(d)")


@pytest.mark.parametrize("cmd", [
    "make clean", "make all", "git push --force origin claude/m1-contribucion-origen", "git push -f origin x",
    "git filter-repo --path data", "git reset --hard HEAD~3", "rm -rf data", "rm -rf output/",
])
def test_destructivos_bloquean(cmd):
    assert bash(cmd).startswith("(e)")


@pytest.mark.parametrize("cmd", ["git push origin main", "git push -u origin master", "git push", "git push origin HEAD",
                                 "git push --tags origin otra"])
def test_push_a_otra_rama_bloquea(cmd):
    assert bash(cmd).startswith("(f)")


@pytest.mark.parametrize("cmd", ["git push -u origin claude/m1-contribucion-origen",
                                 "git push origin HEAD:claude/m1-contribucion-origen", "git push origin prereg-m1",
                                 "git push origin refs/tags/prereg-m1"])
def test_push_rama_de_trabajo_pasa(cmd):
    assert bash(cmd) is None


@pytest.mark.parametrize("url", [
    "https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST211/MCVL",
    "https://sede.seg-social.gob.es/wps/portal/sede/sede/Ciudadanos",
    "https://circabc.europa.eu/ui/group/abc/library/lfs",
    "https://ec.europa.eu/eurostat/web/microdata/scientific-use-files",
    "https://transparencia.gob.es/transparencia/es/ejercicio-derecho/solicitud.html",
    "https://www.ine.es/servicios/laboratorio/solicitud",
    "https://international.ipums.org/international/",
    "https://www.lisdatacenter.org/data-access/",
])
def test_descargas_restringidas_bloquean(url):
    assert bash(f"curl -sSLo /tmp/x '{url}'").startswith("(g)")
    assert G.evaluar({"tool_name": "WebFetch", "tool_input": {"url": url, "prompt": "x"}}, RAIZ).startswith("(g)")


@pytest.mark.parametrize("url", [
    "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/56936",
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_ergacob",
    "https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8",
    "https://ec.europa.eu/eurostat/web/microdata/public-microdata",
])
def test_descargas_publicas_pasan(url):
    assert bash(f"curl -sSLo /tmp/x '{url}'") is None


def test_no_editar_crudos_existentes(tmp_path):
    crudo = next((p for p in (RAIZ / "data" / "raw").rglob("*") if p.is_file()), None)
    if crudo is None:
        crudo = RAIZ / "data" / "raw" / ".prueba_guarda"
        crudo.parent.mkdir(parents=True, exist_ok=True)
        crudo.write_text("x")
    try:
        for h in ("Write", "Edit"):
            assert G.evaluar({"tool_name": h, "tool_input": {"file_path": str(crudo)}}, RAIZ).startswith("(h)")
        assert G.evaluar({"tool_name": "Write", "tool_input": {"file_path": str(RAIZ / "data/raw/nueva/x.csv")}}, RAIZ) is None
    finally:
        if crudo.name == ".prueba_guarda":
            crudo.unlink()


def test_publicacion_no_a_mano():
    r = G.evaluar({"tool_name": "Write", "tool_input": {"file_path": str(RAIZ / "publicacion/documento_m1/x.md")}}, RAIZ)
    assert r.startswith("(i)")


def test_hook_por_stdin_sale_con_2():
    d = json.dumps({"tool_name": "Bash", "tool_input": {"command": "make clean"}})
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(RAIZ)}
    r = subprocess.run([sys.executable, str(HOOK)], input=d, capture_output=True, text=True, env=env)
    assert r.returncode == 2 and "Guarda M1" in r.stderr


def test_descargador_rechaza_restringidas():
    sys.path.insert(0, str(RAIZ / "src" / "m1"))
    import fuentes
    with pytest.raises(PermissionError):
        fuentes.descargar("https://circabc.europa.eu/x", "prueba", "x", "", "", "")


def test_fases_6_7_bloqueadas_si_hay_resultados_causales(monkeypatch, tmp_path):
    monkeypatch.setenv("M1_FORZAR_PUERTA", "cerrada")
    (tmp_path / "output" / "f5").mkdir(parents=True)
    (tmp_path / "src" / "m1").mkdir(parents=True)
    import shutil
    shutil.copy(RAIZ / "src" / "m1" / "etiquetas.py", tmp_path / "src" / "m1" / "etiquetas.py")
    shutil.copy(RAIZ / "src" / "m1" / "politica_fuentes.py", tmp_path / "src" / "m1" / "politica_fuentes.py")
    assert G.evaluar({"tool_name": "Bash", "tool_input": {"command": "make m1_f7"}}, tmp_path).startswith("(c)")


def test_secuencia_completa_se_registra(tmp_path, monkeypatch):
    log = tmp_path / "reg.log"
    monkeypatch.setattr(G, "REGISTRO", log)
    assert G.registrar_secuencia("make PY=x m1_f0 m1_f1 m1_f2 m1_f3 m1_f4 m1_f5 m1_f6 m1_f7 publicacion web", RAIZ)
    assert not G.registrar_secuencia("make m1_f4", RAIZ)
    assert log.read_text(encoding="utf-8").count("m1_f0") == 1
