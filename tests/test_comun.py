"""Tests de src/m1/comun.py, cifras.py y verificar_referencias.py."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "m1"))
import comun as C  # noqa: E402
import verificar_referencias as vr  # noqa: E402


@pytest.mark.parametrize("iso,g", [("ES", "España"), ("FR", "UE-14"), ("GB", "UE-14"), ("RO", "UE-13 y otros de Europa"),
                                   ("UA", "UE-13 y otros de Europa"), ("CO", "América Latina"), ("MA", "Magreb"),
                                   ("SN", "Resto de África"), ("EG", "Resto de África"), ("CN", "Asia"), ("US", "Resto"),
                                   (None, "Resto")])
def test_grupos(iso, g):
    assert C.grupo_iso2(iso) == g


def test_grupos_disjuntos():
    conj = [C.UE14, C.UE13 | C.OTROS_EUROPA, C.AMERICA_LATINA, C.MAGREB, C.ASIA, C.AFRICA_RESTO]
    for i, a in enumerate(conj):
        for b in conj[i + 1:]:
            assert not (a & b)


def test_suprimir():
    d = pd.DataFrame({"n_muestral": [10, 60], "valor": [1.0, 2.0]})
    s = C.suprimir(d)
    assert np.isnan(s.loc[0, "valor"]) and s.loc[1, "valor"] == 2.0 and s["suprimida"].tolist() == [True, False]


def test_holm_bh():
    p = {"a": 0.01, "b": 0.04, "c": 0.03}
    h = C.holm(p)
    assert h["a"] == pytest.approx(0.03) and h["c"] == pytest.approx(0.06) and h["b"] == pytest.approx(0.06)
    b = C.bh(p)
    assert b["a"] == pytest.approx(0.03) and b["b"] == pytest.approx(0.04) and b["c"] == pytest.approx(0.04)


def test_cuantil_media_pond():
    assert C.media_pond([1, 3], [1, 3]) == pytest.approx(2.5)
    assert C.cuantil_pond([1, 2, 3, 4], [1, 1, 1, 1], 0.5) == 2


def test_cifras_reglas():
    c = C.Cifras("prueba", "x.py")
    with pytest.raises(ValueError):
        c.add("x", 1, "u", "d", "C3", "f", "2024", "ES", clasificacion="SUGESTIVO")
    with pytest.raises(ValueError):
        c.add("x", 1, "u", "d", "C9", "f", "2024", "ES")


def test_verificador_estado():
    cr = {"existe": True, "registro": "Crossref", "titulo": "The fiscal effects of immigration to the UK", "primer_autor": "Dustmann",
          "anio": 2014}
    assert vr.estado("Dustmann, C. y Frattini, T. (2014). The fiscal effects of immigration to the UK", cr) == "VERIFICADA (Crossref)"
    assert vr.estado("Otro, A. (2014). The fiscal effects of immigration to the UK", cr).startswith("NO VERIFICADA (discrepa")
    assert vr.estado("X (2020). Informe", None) == "NO VERIFICADA (sin DOI)"
