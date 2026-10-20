"""M1-F3 · A POSTERIORI (verificación tras el cierre): desagregaciones de C1 que el plan pedía y no estaban publicadas, y la
composición por edad que explica la brecha de empleo. Sin red.

1. Empleo por provincia × grupo de nacimiento (EPA, 16-64 años, media de 2023-2025 para tener celdas suficientes): tasa de empleo y
   de paro; celdas con < 50 observaciones suprimidas. La EPA pública codifica el país de nacimiento por regiones (UE-14,
   UE-13 y otros de Europa, América Latina, África, Asia, resto): no separa el Magreb del resto de África, así que en empleo hay 7
   grupos y no 8. La población por provincia y 8 grupos (con Magreb) está en output/f3/poblacion_provincias.csv (padrón).
2. Composición por edad y sexo de la población de 16-64 años por nacimiento (EPA 2025), para leer la diferencia entre la brecha de
   empleo bruta y la ajustada por edad y sexo.
Salidas: output/f3/empleo_provincias_grupos.csv, output/f3/empleo_composicion_2025.csv; cifras F3_ALC_* (C1).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, PROC, Cifras  # noqa: E402

O = OUT / "f3"
EDADES = ["16-24", "25-34", "35-44", "45-54", "55-64"]


def main() -> int:
    cf = Cifras("f3_alcance", "src/m1/f3_alcance.py")
    c = pd.read_csv(PROC / "epa_celdas.csv.gz")
    c = c[(c.origen_def == "nacimiento") & c.edad6.isin(EDADES)]
    x = c[c.anio.between(2023, 2025)]
    p = x.groupby(["prov", "grupo"]).agg(pob=("pob", "sum"), act=("act", "sum"), ocu=("ocu", "sum"), par=("par", "sum"),
                                         n_muestral=("n_obs", "sum")).reset_index()
    p["tasa_empleo"] = 100 * p.ocu / p.pob
    p["tasa_paro"] = 100 * p.par / p.act
    p["pob_16_64_media"] = p.pob / 3
    p = p.drop(columns=["pob", "act", "ocu", "par"])
    p.loc[p.n_muestral < 50, ["tasa_empleo", "tasa_paro", "pob_16_64_media"]] = float("nan")
    p.to_csv(O / "empleo_provincias_grupos.csv", index=False)
    for g, r in p[p.grupo != "España"].groupby("grupo"):
        cf.add(f"F3_ALC_PROV_PUBLICABLES_{g.replace(' ', '_')}", int(r.tasa_empleo.notna().sum()), "provincias", f"Provincias (de 52) con "
               f"tasa de empleo publicable (≥ 50 observaciones en 2023-2025) para los nacidos en {g} (a posteriori)", "C1", "EPA (INE)",
               "2023-2025", "provincias", g)
    y = c[c.anio == 2025].assign(fuera=lambda d: d.grupo != "España")
    comp = y.groupby(["fuera", "edad6"]).agg(pob=("pob", "sum"), ocu=("ocu", "sum")).reset_index()
    comp["cuota"] = 100 * comp.pob / comp.groupby("fuera").pob.transform("sum")
    comp["tasa_empleo"] = 100 * comp.ocu / comp.pob
    comp.to_csv(O / "empleo_composicion_2025.csv", index=False)
    s = y.groupby(["fuera", "sexo"]).pob.sum()
    for f, nom in ((True, "FUERA"), (False, "España")):
        q = comp[comp.fuera == f].set_index("edad6")
        g = "nacidos fuera" if f else "España"
        cf.add(f"F3_ALC_CUOTA_25_54_{nom}_2025", round(float(q.loc[["25-34", "35-44", "45-54"], "cuota"].sum()), 1), "% de 16-64",
               f"Peso de 25-54 años en la población de 16-64 años, {g}", "C1", "EPA (INE)", "2025", "España", g)
        for e in ("16-24", "55-64"):
            cf.add(f"F3_ALC_CUOTA_{e.replace('-', '_')}_{nom}_2025", round(float(q.loc[e, "cuota"]), 1), "% de 16-64",
                   f"Peso de {e} años en la población de 16-64 años, {g}", "C1", "EPA (INE)", "2025", "España", g)
        cf.add(f"F3_ALC_CUOTA_MUJERES_{nom}_2025", round(float(100 * s[(f, "mujer")] / s[f].sum()), 1), "% de 16-64",
               f"Mujeres en la población de 16-64 años, {g}", "C1", "EPA (INE)", "2025", "España", g)
    # cruce nacimiento × nacionalidad (C1): nacidos fuera con y sin nacionalidad española, 16-64, 2025
    z = y[y.fuera]
    for nac, nom in ((True, "NACIONALIZADOS"), (False, "EXTRANJEROS")):
        q = z[z.nacionalizado == nac]
        cf.add(f"F3_ALC_EMP_FUERA_{nom}_2025", round(float(100 * q.ocu.sum() / q.pob.sum()), 1), "%", "Tasa de empleo 16-64 de los nacidos "
               f"fuera {'con' if nac else 'sin'} nacionalidad española ({int(q.n_obs.sum())} observaciones; a posteriori)", "C1", "EPA (INE)",
               "2025", "España", "nacidos fuera")
        cf.add(f"F3_ALC_CUOTA_25_54_FUERA_{nom}_2025", round(float(100 * q[q.edad6.isin(["25-34", "35-44", "45-54"])].pob.sum() / q.pob.sum()), 1),
               "% de 16-64", f"Peso de 25-54 años entre los nacidos fuera {'con' if nac else 'sin'} nacionalidad española", "C1", "EPA (INE)",
               "2025", "España", "nacidos fuera")
    cf.escribir()
    print(comp.round(1).to_string())
    print(p.groupby("grupo").tasa_empleo.apply(lambda s: s.notna().sum()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
