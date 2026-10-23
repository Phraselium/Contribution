"""La puerta de entorno de make check (a posteriori) detecta dependencias que faltan en requirements.txt."""
from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src" / "m1"))
import check  # noqa: E402


def _repo(tmp_path: Path, req: str, codigo: str) -> Path:
    (tmp_path / "src" / "m1").mkdir(parents=True)
    (tmp_path / "tests").mkdir()
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    (tmp_path / ".claude" / "hooks" / "guardas_m1.py").write_text("import os\n", encoding="utf-8")
    (tmp_path / "src" / "m1" / "a.py").write_text(codigo, encoding="utf-8")
    (tmp_path / "requirements.txt").write_text(req, encoding="utf-8")
    (tmp_path / "requirements.lock").write_text(req, encoding="utf-8")
    (tmp_path / ".python-version").write_text(".".join(map(str, sys.version_info[:3])), encoding="utf-8")
    return tmp_path


def test_detecta_motor_de_excel_sin_declarar(tmp_path, monkeypatch):
    monkeypatch.setattr(check, "RAIZ", _repo(tmp_path, "pandas==3.0.5\nopenpyxl==3.1.5\n", "import pandas as pd\npd.read_excel('x.xls')\n"))
    assert any("xlrd" in x for x in check.entorno())


def test_detecta_import_sin_declarar_y_version_sin_fijar(tmp_path, monkeypatch):
    monkeypatch.setattr(check, "RAIZ", _repo(tmp_path, "numpy>=2\n", "import numpy\nimport scipy.stats\n"))
    e = check.entorno()
    assert any("scipy" in x for x in e) and any("no fijada" in x for x in e)


def test_repositorio_real_limpio():
    assert check.entorno() == []
