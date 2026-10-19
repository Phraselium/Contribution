"""M1-F5 · EXPLORATORIO A POSTERIORI (no pre-registrado): jackknife por comunidad autónoma de P1-H1, P1-H2 y P1-E3a con la
especificación principal (docs/desviaciones.md, desviación 14). No cambia ninguna clasificación. SOLO con la puerta prereg-m1.
Salidas: output/f5/x_jackknife/resultado.json, output/f5/x_jackknife.csv y cifras F5X_JK_* (capa C4).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import etiquetas  # noqa: E402
import f5_p1_shiftshare as p1  # noqa: E402
from comun import OUT, Cifras, escribir_resultado  # noqa: E402
from territorio import PROV  # noqa: E402

O = OUT / "f5"
HIP = {"P1-H1": "tasa_empleo", "P1-H2": "tasa_paro", "P1-E3a": "tasa_empleo_educ_baja"}


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    cf = Cifras("f5_x_jackknife", "src/m1/f5_x_jackknife.py")
    P, E, c = p1.padron(), p1.ecp(), p1.epa_nativos()
    Y = p1.resultados_nativos(c)
    ctrl0, bart, paro = p1.controles(c)
    d, S, g, grupos, _, _ = p1.panel(p1.PRINCIPAL, P, E, Y, (ctrl0, bart), paro)
    ccaa = d.prov.map(lambda p: PROV[p][1])
    filas = []
    for k in sorted(ccaa.unique()):
        m = (ccaa != k).to_numpy()
        for h, y in HIP.items():
            r = p1.estimar(d[m].reset_index(drop=True), S[m], g, grupos, p1.PRINCIPAL, y)
            filas.append({"ccaa_excluida": k, "hipotesis": h, "b": r["b"], "akm0_p": r["akm0_p"], "F_shock": r["F_shock"],
                          "acotado": r["akm0_acotado"]})
    jk = pd.DataFrame(filas)
    jk.to_csv(O / "x_jackknife.csv", index=False)
    resumen = jk.groupby("hipotesis").agg(b_min=("b", "min"), b_max=("b", "max"), neg=("b", lambda s: int((s < 0).sum())),
                                          rechaza=("akm0_p", lambda s: int((s < 0.05).sum())), n=("b", "size"),
                                          F_min=("F_shock", "min"), F_max=("F_shock", "max"))
    escribir_resultado(O / "x_jackknife" / "resultado.json", pregunta="Jackknife por comunidad autónoma (exploratorio, a posteriori)",
                       capa="C4", clasificacion="ASOCIACIÓN", datos="padrón, ECP, EPA (INE)", N=int(len(d)),
                       metodo="especificación principal de P1 excluyendo una comunidad cada vez", estimacion=None, ic95=[None, None],
                       p_ajustado=None, diagnosticos=resumen.to_dict("index"),
                       notas="No pre-registrado; no cambia ninguna clasificación (docs/desviaciones.md, 14).", prereg=f"prereg-m1 {commit}")
    for h, r in resumen.iterrows():
        k = h.replace("-", "_")
        cf.add(f"F5X_JK_{k}", round(float(jk[jk.hipotesis == h].b.median()), 2), "pp por pp", f"{h}: mediana de β al excluir una comunidad "
               f"autónoma cada vez ({int(r.n)} exclusiones; intervalo: mínimo y máximo; exploratorio, a posteriori)", "C4",
               "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España", clasificacion="ASOCIACIÓN",
               ic_inf=round(float(r.b_min), 2), ic_sup=round(float(r.b_max), 2))
        cf.add(f"F5X_JK_{k}_RECHAZA", int(r.rechaza), "especificaciones", f"{h}: exclusiones en las que AKM0 rechaza β = 0 al 5 % sin ajuste "
               f"(de {int(r.n)}; exploratorio, a posteriori)", "C4", "padrón, ECP, EPA (INE)", "2005-2022", "provincias", "nacidos en España")
    cf.escribir()
    print(resumen.round(3).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
