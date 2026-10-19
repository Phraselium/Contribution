"""M1-F3 · Uso de prestaciones monetarias por origen (descriptivo; C1 bruto, C4 ajustado). Sin red.

ECV 2021-2025 (renta del año anterior): perceptores y cuantías medias de desempleo (PY090G), jubilación (PY100G), supervivencia
(PY110G), incapacidad (PY130G), rentas mínimas e IMV («exclusión social», HY060G, del hogar), ayudas a la vivienda (HY070G, del
hogar) y prestaciones familiares (HY050G, del hogar). Las del hogar se atribuyen a todos sus miembros (la persona «vive en un
hogar que percibe»). Tres niveles (bruto; edad y sexo; además educación y región). Errores agrupados por hogar (la ECV pública
no trae estratos ni UPM). El contraste con los registros administrativos por nacionalidad (SEPE, IMV, pensiones) no está
hecho (mejora futura, docs/mejoras_futuras.md).
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, Cifras  # noqa: E402
from f3_vivienda import cargar_ecv, niveles_ecv  # noqa: E402

O = OUT / "f3"
ECV = "ECV (INE, microdatos)"
PREST = {"desempleo": ("PY090G", "16-64"), "jubilacion": ("PY100G", "65+"), "supervivencia": ("PY110G", "todas"),
         "incapacidad": ("PY130G", "16-64"), "rentas_minimas_IMV": ("HY060G", "todas"), "ayuda_vivienda": ("HY070G", "todas"),
         "familia_hijos": ("HY050G", "todas")}


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f3_prestaciones", "src/m1/f3_prestaciones.py")
    d = cargar_ecv()
    tabs, medias = [], []
    for nombre, (v, edades) in PREST.items():
        x = d.copy()
        if edades == "16-64":
            x = x[x.edad.between(16, 64)]
        elif edades == "65+":
            x = x[x.edad >= 65]
        if v.startswith("PY"):
            x = x[x.edad >= 16]
        x[f"perceptor_{nombre}"] = (x[v].fillna(0) > 0).astype(float)
        hog = v.startswith("HY")
        x[f"importe_{nombre}"] = x[v].fillna(0) / (x.n_hogar if hog else 1)
        t = niveles_ecv(x, f"perceptor_{nombre}")
        t["poblacion"] = edades
        tabs.append(t)
        m = x.groupby("nacimiento3").apply(lambda g: pd.Series({
            "tasa_perceptores": np.average(g[f"perceptor_{nombre}"], weights=g.RB050),
            "importe_medio_por_persona": np.average(g[f"importe_{nombre}"], weights=g.RB050),
            "importe_medio_perceptores": np.average(g.loc[g[v] > 0, v], weights=g.loc[g[v] > 0, "RB050"]) if (g[v] > 0).any() else np.nan,
            "n_muestral": int((g[v] > 0).sum())}), include_groups=False).reset_index()
        m["prestacion"], m["poblacion"] = nombre, edades
        medias.append(m)
    tn = pd.concat(tabs)
    tn.to_csv(O / "prestaciones_tres_niveles.csv", index=False)
    md = pd.concat(medias)
    md.loc[md.n_muestral < 50, ["tasa_perceptores", "importe_medio_por_persona", "importe_medio_perceptores"]] = np.nan
    md.to_csv(O / "prestaciones_medias.csv", index=False)
    for _, r in md.iterrows():
        cf.add(f"F3_PRE_{r.prestacion}_{r.nacimiento3.replace(' ', '_')}", round(100 * r.tasa_perceptores, 1), "% de personas",
               f"Personas ({r.poblacion}) que perciben {r.prestacion.replace('_', ' ')} (o viven en un hogar que la percibe), media de las ECV 2021-2025 (rentas de 2020-2024)",
               "C1", ECV, "2020-2024 (renta)", "España", r.nacimiento3)
    for _, r in tn[tn.nivel_ajuste.isin(["edad y sexo", "completo"])].iterrows():
        cf.add(f"F3_PRE_BRECHA_{r.variable}_{r.grupo.replace(' ', '_')}_{r.nivel_ajuste.replace(' ', '_')}", round(100 * r.brecha, 1), "pp",
               f"Diferencia en la probabilidad de percibir ({r.variable.replace('perceptor_', '')}) frente a nacidos en España ({r.nivel_ajuste})",
               "C4", ECV, "2020-2024 (renta)", "España", r.grupo, nivel_ajuste=r.nivel_ajuste,
               ic_inf=round(100 * (r.brecha - 1.96 * r.ee), 1), ic_sup=round(100 * (r.brecha + 1.96 * r.ee), 1))
    cf.escribir()
    print("f3_prestaciones: hecho;", len(cf.filas), "cifras")
    return 0


if __name__ == "__main__":
    sys.exit(main())
