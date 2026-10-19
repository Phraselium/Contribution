"""M1-F5 · EXPLORATORIO A POSTERIORI (no pre-registrado): lectura de P1-E3a. No cambia ninguna clasificación pre-registrada
(docs/desviaciones.md, desviación 12). SOLO con la puerta prereg-m1 abierta.

Con la especificación principal de P1 (misma muestra, controles, pesos e instrumento):
1. MCO de P1-E3a, para ver cuánto se acerca el MC2E (con primera etapa débil, el MC2E se sesga hacia MCO).
2. Descomposición de Δ tasa de empleo de los nativos con educación baja en Δ log ocupados y Δ log población (EPA): si la
   población de nativos con estudios bajos crece más (o cae menos) en las provincias más expuestas, la tasa baja sin pérdida de
   empleo; si cae, puede haber salida geográfica. Se añade Δ log población nativa con educación media y alta.
3. Conversión a elasticidad (Δ log tasa / Δ log cuota de nacidos fuera) para compararla con la literatura.
4. Aritmética de la variante por nacionalidad: el efecto sobre la tasa total es la media de los efectos por nivel educativo
   ponderada por el peso de cada nivel en la población nativa.
Salidas: output/f5/x_e3a/resultado.json y cifras F5X_* (capa C4, rotuladas «exploratorio, a posteriori»).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import econ  # noqa: E402
import etiquetas  # noqa: E402
import f5_p1_shiftshare as p1  # noqa: E402
from comun import OUT, Cifras, escribir_resultado  # noqa: E402

O = OUT / "f5"
ROT = "exploratorio, a posteriori"


def extra(c: pd.DataFrame) -> pd.DataFrame:
    a = c[c.edad6 != "65+"]
    out = {}
    for e in ("baja", "media", "alta"):
        g = a[a.educ == e].groupby(["prov", "anio"])
        out[f"log_ocu_{e}"] = np.log(g.ocu.sum())
        out[f"log_pob_{e}"] = np.log(g.pob.sum())
    g = a[a.educ.isin(["media", "alta"])].groupby(["prov", "anio"])
    out["log_pob_media_alta"] = np.log(g.pob.sum())
    return pd.DataFrame(out)


def main() -> int:
    motivo = etiquetas.exigir()
    commit = motivo.split("→ ")[1].split(" ")[0] if "→ " in motivo else ""
    cf = Cifras("f5_x_e3a", "src/m1/f5_x_e3a_lectura.py")
    P, E, c = p1.padron(), p1.ecp(), p1.epa_nativos()
    Y = p1.resultados_nativos(c).join(extra(c))
    ctrl0, bart, paro = p1.controles(c)
    d, S, g, grupos, _, _ = p1.panel(p1.PRINCIPAL, P, E, Y, (ctrl0, bart), paro)
    res = {}
    for y in ("tasa_empleo_educ_baja", "log_ocu_baja", "log_pob_baja", "log_pob_media_alta"):
        r = p1.estimar(d, S, g, grupos, p1.PRINCIPAL, y)
        m = d[f"d_{y}"].notna()
        W = p1.W_de(d[m], p1.PRINCIPAL)
        o = econ.ols(d[m][f"d_{y}"].to_numpy(float), np.column_stack([d[m].x.to_numpy(float), W]), d[m].prov.to_numpy(),
                     d[m].pob0.to_numpy(float))
        res[y] = {"mc2e": r["b"], "akm0_p": r["akm0_p"], "akm0_conjunto": r["akm0_conjunto"], "mco": float(o["b"][0]),
                  "ee_mco_cluster": float(o["se"][0])}
    # pesos y niveles medios (nativos 16-64, años iniciales de los periodos)
    a = c[(c.edad6 != "65+") & c.anio.isin([2005, 2009, 2015])]
    tot = a.groupby("educ").pob.sum()
    w = (tot / tot[["baja", "media", "alta"]].sum())[["baja", "media", "alta"]]
    tasa_baja = float(a[a.educ == "baja"].ocu.sum() / a[a.educ == "baja"].pob.sum())
    s_fuera = float((E["Extranjero"] / E["Total"]).loc[(slice(None), [2005, 2009, 2015])].mean())
    eps = res["tasa_empleo_educ_baja"]["mc2e"] * s_fuera / tasa_baja
    # variante por nacionalidad para los tres niveles
    nac = {}
    for h in ("P1-E3a", "P1-E3b", "P1-E3c", "P1-H1"):
        r = json.loads((O / "p1" / h / "resultado.json").read_text())["diagnosticos"]["nacionalidad"]
        nac[h] = {"b": r["b"], "conjunto": r["akm0_conjunto"]}
    implicito = float(w["baja"] * nac["P1-E3a"]["b"] + w["media"] * nac["P1-E3b"]["b"] + w["alta"] * nac["P1-E3c"]["b"])
    diag = {"lineas": res, "peso_educ_baja_nativos": float(w["baja"]), "pesos": w.to_dict(), "tasa_empleo_baja_media": tasa_baja,
            "cuota_nacidos_fuera_15_64_media": s_fuera, "elasticidad_E3a": eps, "nacionalidad": nac,
            "tasa_total_implicita_por_niveles_nacionalidad": implicito}
    escribir_resultado(O / "x_e3a" / "resultado.json", pregunta="Lectura de P1-E3a (exploratorio, a posteriori)", capa="C4",
                       clasificacion="ASOCIACIÓN", datos="padrón, ECP, EPA (INE)", N=int(d.shape[0]),
                       metodo="misma especificación que P1; MCO y descomposición en ocupados y población", estimacion=None,
                       ic95=[None, None], p_ajustado=None, diagnosticos=diag,
                       notas="No pre-registrado; no cambia ninguna clasificación (docs/desviaciones.md, 12).", prereg=f"prereg-m1 {commit}")
    L = res
    fuente, per, amb, grp = "padrón, ECP, EPA (INE)", "2005-2022", "50 provincias", "nacidos en España con educación baja"
    cf.add("F5X_E3a_MCO", round(L["tasa_empleo_educ_baja"]["mco"], 2), "pp por pp", f"P1-E3a por MCO con la especificación principal ({ROT})",
           "C4", fuente, per, amb, grp)
    for y, k, dsc in (("log_ocu_baja", "OCU", "Δ log ocupados nacidos en España con educación baja"),
                      ("log_pob_baja", "POB", "Δ log población nacida en España de 16-64 con educación baja (EPA)"),
                      ("log_pob_media_alta", "POB_MA", "Δ log población nacida en España de 16-64 con educación media o alta (EPA)")):
        cf.add(f"F5X_E3a_{k}", round(L[y]["mc2e"], 2), "log por pp", f"{dsc} por punto de tratamiento, MC2E ({ROT}; p AKM0 sin ajustar = "
               f"{L[y]['akm0_p']:.2f})", "C4", fuente, per, amb, grp)
        cf.add(f"F5X_E3a_{k}_p", round(L[y]["akm0_p"], 3), "p ajustado", f"p AKM0 sin ajustar de {dsc} ({ROT})", "C4", fuente, per, amb, grp)
    cf.add("F5X_E3a_ELAST", round(eps, 2), "elasticidad", "P1-E3a expresada como elasticidad de la tasa de empleo respecto a la cuota "
           f"de nacidos fuera, con medias de los años iniciales ({ROT})", "C4", fuente, per, amb, grp)
    cf.add("F5X_PESO_BAJA", round(100 * float(w["baja"]), 1), "% de los nativos de 16-64", "Peso de la educación baja entre los nacidos en "
           "España de 16-64 (EPA, años iniciales de los periodos)", "C1", "EPA (INE)", "2005, 2009, 2015", "España", "nacidos en España")
    cf.add("F5X_NAC_IMPLICITO", round(implicito, 2), "pp por pp", "Media ponderada por educación de las estimaciones por nacionalidad de "
           f"P1-E3a, E3b y E3c ({ROT})", "C4", fuente, per, amb, "nacidos en España")
    cf.add("F5X_E3b_NAC", round(nac["P1-E3b"]["b"], 2), "pp por pp", f"P1-E3b (educación media), variante por nacionalidad ({ROT})", "C4",
           fuente, per, amb, "nacidos en España con educación media")
    cf.add("F5X_E3c_NAC", round(nac["P1-E3c"]["b"], 2), "pp por pp", f"P1-E3c (educación alta), variante por nacionalidad ({ROT})", "C4",
           fuente, per, amb, "nacidos en España con educación alta")
    cf.escribir()
    print(json.dumps(diag, indent=1, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
