"""Pruebas de cuadre contable de la contabilidad fiscal (C2) y del ciclo vital. A posteriori: añadidas en la verificación tras el
cierre (docs/cuadre.md); no formaban parte del plan de análisis interno.

Referencia pública: Eurostat, cuentas anuales de las AAPP (sector S13, millones de euros corrientes): gov_10a_main (TR, TE, B9),
gov_10a_taxag (impuestos y cotizaciones por partida) y gov_10a_exp (gasto por función COFOG y prestaciones D62). Ficheros en
data/raw/eurostat con checksum en el inventario de fuentes.

Tolerancia: 1 millón de euros en cada total (la unidad de publicación de Eurostat, que redondea a millones). Las contribuciones de
C2 son repartos de esos mismos totales, así que la identidad debe cumplirse hasta el redondeo de la fuente; cualquier diferencia
mayor es un error de cálculo (así se detectó la omisión del D62 sanitario, 1.735 M€). Se comprueban el principal de 2022, 2023 y
2024 y las 32 combinaciones calibradas de la rejilla; las 32 sin calibrar usan los importes de la ECV sin llevarlos a las cuentas
y no tienen por qué cuadrar (se informa de su desviación en docs/cuadre.md, no se prueba).
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src" / "m1"))
EU = RAIZ / "data" / "raw" / "eurostat"
F4 = Path(__import__("os").environ.get("M1_F4_DIR", RAIZ / "output" / "f4"))   # M1_F4_DIR: probar salidas antiguas
TOL = 1.0   # millones de euros

pytestmark = pytest.mark.skipif(not (F4 / "neta_por_grupo_2024.csv").exists() or not (EU / "gov_10a_main.csv.gz").exists(),
                                reason="faltan las salidas de la fase 4 o los crudos de Eurostat")


@lru_cache(maxsize=None)
def _leer(nombre: str, usecols: tuple | None = None) -> pd.DataFrame:
    return pd.read_csv(EU / nombre, usecols=list(usecols) if usecols else None, low_memory=False)


def _main(a: int) -> pd.Series:
    m = _leer("gov_10a_main.csv.gz")
    return m[(m.geo == "ES") & (m.unit == "MIO_EUR") & (m.sector == "S13") & (m.TIME_PERIOD == a)].set_index("na_item").OBS_VALUE


def _tax(a: int) -> pd.Series:
    t = _leer("gov_10a_taxag.csv.gz")
    return t[(t.geo == "ES") & (t.unit == "MIO_EUR") & (t.sector == "S13") & (t.TIME_PERIOD == a)].set_index("na_item").OBS_VALUE


def _exp(a: int) -> tuple[pd.Series, pd.Series]:
    e = _leer("grandes/gov_10a_exp.csv.gz", ("geo", "sector", "unit", "na_item", "cofog99", "TIME_PERIOD", "OBS_VALUE"))
    e = e[(e.geo == "ES") & (e.sector == "S13") & (e.unit == "MIO_EUR") & (e.TIME_PERIOD == a)]
    return e[e.na_item == "TE"].set_index("cofog99").OBS_VALUE, e[e.na_item == "D62"].set_index("cofog99").OBS_VALUE


def _totales(n: pd.DataFrame) -> pd.Series:
    cols = [c for c in n.columns if c.startswith(("ing_", "gas_"))] + ["ingresos", "gastos", "neta"]
    return n[cols].multiply(n.poblacion, axis=0).sum() / 1e6


# a) suma ponderada por población de las contribuciones netas = saldo de las AAPP (B9) ─────────────────────────────────────────
@pytest.mark.parametrize("anio", [2022, 2023, 2024])
def test_saldo_principal(anio):
    n = pd.read_csv(F4 / "neta_por_grupo_anios.csv")
    tot = _totales(n[n.anio_cuentas == anio])
    m = _main(anio)
    assert abs(tot["neta"] - m["B9"]) <= TOL, f"{anio}: suma {tot['neta']:.0f} M€ frente a B9 {m['B9']:.0f} M€"
    assert abs(tot["ingresos"] - m["TR"]) <= TOL
    assert abs(tot["gastos"] - m["TE"]) <= TOL


def test_saldo_rejilla_calibrada():
    r = pd.read_csv(F4 / "rejilla.csv")
    r = r[r.calibrar]
    sup = ["sanidad", "bienes", "educ_hijos", "indirectos", "capital"]
    s = r.assign(t=r.neta_pc * r.poblacion / 1e6).groupby(sup).t.sum()
    assert len(s) == 32
    b9 = _main(2024)["B9"]
    malos = s[(s - b9).abs() > TOL]
    assert malos.empty, f"combinaciones que no cuadran con B9 = {b9:.0f} M€:\n{malos}"


# b) por partida, frente a la Contabilidad Nacional ──────────────────────────────────────────────────────────────────────────
def _partidas_cn(a: int) -> dict[str, float]:
    """Definición de cada partida del modelo en códigos SEC 2010 (la que usa src/m1/f4_fiscal.py)."""
    t, (te, d62) = _tax(a), _exp(a)
    return {
        "ing_irpf_cotiz_trab": t["D51A_C1"] + t["D613"], "ing_cotiz_empresa": t["D611"], "ing_iva": t["D211"],
        "ing_especiales": t["D214"], "ing_vivienda_ibi": t["D29A"] + t["D59"],
        "ing_sociedades_capital": t["D51B_C2"] + t["D29"] - t["D29A"] + t["D91"],
        "pensiones": d62["GF1002"] + d62["GF1003"],
        "otras_prest_monetarias": d62["GF10"] - d62["GF1002"] - d62["GF1003"],
        "gas_sanidad": te["GF07"], "gas_educacion": te["GF09"],
        "gas_prot_social_especie": te["GF10"] - d62["GF10"], "gas_bienes_publicos_puros": te["GF01"] + te["GF02"],
        "gas_resto_servicios": sum(te[f] for f in ("GF03", "GF04", "GF05", "GF06", "GF08")),
    }


def _partidas_modelo(n: pd.DataFrame) -> dict[str, float]:
    tot = _totales(n)
    otras = ["gas_desempleo", "gas_enfermedad_incapacidad", "gas_familia", "gas_exclusion_social", "gas_vivienda", "gas_otras_prestaciones"]
    m = {k: tot[k] for k in ("ing_irpf_cotiz_trab", "ing_cotiz_empresa", "ing_iva", "ing_especiales", "ing_vivienda_ibi",
                             "ing_sociedades_capital", "gas_sanidad", "gas_educacion", "gas_prot_social_especie",
                             "gas_bienes_publicos_puros", "gas_resto_servicios")}
    m["pensiones"] = tot["gas_vejez"] + tot["gas_supervivencia"]
    m["otras_prest_monetarias"] = sum(tot[k] for k in otras)
    return m


@pytest.mark.parametrize("anio", [2022, 2023, 2024])
def test_partidas(anio):
    n = pd.read_csv(F4 / "neta_por_grupo_anios.csv")
    mod, cn = _partidas_modelo(n[n.anio_cuentas == anio]), _partidas_cn(anio)
    malos = {k: (round(mod[k]), round(cn[k])) for k in cn if abs(mod[k] - cn[k]) > TOL}
    assert not malos, f"{anio}: partidas (modelo, CN) que no cuadran: {malos}"


@pytest.mark.parametrize("anio", [2022, 2023, 2024])
def test_resto_ingresos(anio):
    """El resto de ingresos repartido por persona es exactamente TR menos los impuestos y cotizaciones imputados, y no es negativo."""
    n = pd.read_csv(F4 / "neta_por_grupo_anios.csv")
    tot, cn, m = _totales(n[n.anio_cuentas == anio]), _partidas_cn(anio), _main(anio)
    imputados = sum(cn[k] for k in cn if k.startswith("ing_"))
    assert tot["ing_otros_ingresos"] > 0
    assert abs(tot["ing_otros_ingresos"] - (m["TR"] - imputados)) <= TOL


# c) ciclo vital: los perfiles por edad, agregados con la pirámide de 2024, reproducen los totales de C2 ──────────────────────
def test_ciclo_vital_reproduce_c2():
    import f4_ciclo_vital as cv
    if cv.SUPR.empty:
        pytest.fail("falta data/processed/perfil_suprimidos_2024.csv: ejecute make m1_f4")
    P = cv.perfiles(True)
    pir = pd.read_csv(F4 / "piramide_ecv_2024.csv")
    n = pd.read_csv(F4 / "neta_por_grupo_2024.csv").set_index("grupo")
    cols = [c for c in n.columns if c.startswith(("ing_", "gas_"))] + ["ingresos", "gastos", "neta"]
    malos = []
    for g, p in P.items():
        tramo = p.groupby((p.index.to_series().clip(upper=85) // 5) * 5).first()
        w = pir[pir.grupo == g].set_index("e").poblacion
        agg = tramo[cols].multiply(w, axis=0).sum() / 1e6
        c2 = n.loc[g, cols].astype(float) * n.loc[g, "poblacion"] / 1e6
        assert np.isclose(w.sum(), n.loc[g, "poblacion"], rtol=1e-9)
        malos += [f"{g} {k}: {agg[k]:.1f} frente a {c2[k]:.1f}" for k in cols if abs(agg[k] - c2[k]) > TOL]
    assert not malos, "\n".join(malos)


def test_piramide_es_la_de_c2():
    pir = pd.read_csv(F4 / "piramide_ecv_2024.csv")
    n = pd.read_csv(F4 / "neta_por_grupo_2024.csv").set_index("grupo")
    assert np.allclose(pir.groupby("grupo").poblacion.sum().reindex(n.index), n.poblacion, rtol=1e-9)
