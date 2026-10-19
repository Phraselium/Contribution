"""M1 · Genera docs/montecarlo.md a partir de output/montecarlo/<herramienta>/resultado.json (sin simular nada).

Orden de ejecución: bhj.py, wcr_boot.py, iv2sls.py, conley.py, oaxaca_dfl.py y después este script.
"""

from __future__ import annotations

import json

import _mc

ORDEN = ["bhj", "wcr_boot", "iv2sls", "conley", "oaxaca", "dfl"]
TITULOS = {
    "bhj": "bhj · shift-share MC2E con EE robustos a la exposición (BHJ 2022)",
    "wcr_boot": "wcr_boot · wild cluster bootstrap restringido (Webb)",
    "iv2sls": "iv2sls + f_efectivo + ar_conjunto · instrumento fuerte y débil",
    "conley": "conley · EE con dependencia espacial (núcleo uniforme, 200 km)",
    "oaxaca": "oaxaca · Oaxaca-Blinder con coeficientes agrupados",
    "dfl": "dfl · reponderación DiNardo-Fortin-Lemieux",
}
USO = {
    "bhj": "No usar el IC de Wald de bhj como inferencia principal con la concentración de orígenes de M1. Usar AKM0 (nulo "
    "impuesto, invertido para el IC) o, en su defecto, informar bhj junto con 1/HHI y el apalancamiento máximo del shock. Nunca "
    "EE convencionales (HC1/CR1 por CCAA o provincia) en shift-share. AKM0 aún no está en econ.py: queda para el modelizador "
    "(el cálculo de referencia está en src/m1/montecarlo/bhj.py, función akm0_t2).",
    "wcr_boot": "APTO con G = 52, y con G = 17 si el regresor de interés no está dominado por pocos clusters de alto apalancamiento; "
    "con 17 clusters asimétricos sobre-rechaza (≈ 0,10), aunque mucho menos que CR1 con t(G-1). Informar siempre el apalancamiento "
    "por cluster; con G = 17 asimétrico, tratar p entre 0,05 y 0,10 como no significativo. Usar B = 9999 en la aplicación.",
    "iv2sls": "Wald (iv2sls con CR1 y t(G-1)) solo con F efectivo ≥ 10; con F < 10 informar el conjunto AR (puede ser no acotado). "
    "f_efectivo coincide con el F de primera etapa de iv2sls. AR con CR1 y 52 clusters heterogéneos queda al límite (≈ 0,92): "
    "para confirmatorias, complementar con wild bootstrap del test AR.",
    "conley": "NO APTO con 52 unidades y radio 200 km: infraestima la varianza (≈ 0,6-0,85 de la verdadera) y cubre 0,81-0,87, "
    "a veces peor que HC1. Con datos provinciales, usar clusters espaciales (CCAA) con wcr_boot o un núcleo más ancho con "
    "sensibilidad, y declarar la limitación.",
    "oaxaca": "APTO. Declarar que la referencia es la regresión agrupada con indicador de grupo: con rendimientos distintos por grupo "
    "no coincide con la descomposición con estructura de B (es otra cantidad, no un sesgo). Corregido: ahora añade constante si X no "
    "la trae.",
    "dfl": "APTO para media y cuantiles con logit bien especificado (covariables discretas). Con covariables continuas, comprobar el "
    "equilibrio de medias tras reponderar.",
}


def f3(v):
    return "—" if v is None else (f"{v:.3f}" if isinstance(v, float) else str(v))


def tabla(cab, filas):
    s = "| " + " | ".join(cab) + " |\n|" + "|".join("---" for _ in cab) + "|\n"
    return s + "".join("| " + " | ".join(f3(x) for x in f) + " |\n" for f in filas)


def rech(d):
    return d.get("tamano", d.get("potencia"))


def sec_bhj(d):
    cab = [
        "diseño",
        "β",
        "1/HHI",
        "F shock",
        "sesgo",
        "RMSE",
        "cob. bhj",
        "rech. β=0 bhj",
        "cob. HC1",
        "rech. HC1",
        "cob. CR1",
        "rech. CR1",
        "cob. AKM0",
        "rech. AKM0",
    ]
    filas = []
    for f in d["disenos"]:
        cr1 = next(v for k, v in f.items() if k.startswith("iv2sls_CR1"))
        filas.append(
            [
                f["diseno"],
                f["beta"],
                f["orígenes_efectivos_1/HHI"],
                f["F_shock_mediana"],
                f["bhj"]["sesgo"],
                f["bhj"]["rmse"],
                f["bhj"]["cobertura95"],
                rech(f["bhj"]),
                f["iv2sls_HC1"]["cobertura95"],
                rech(f["iv2sls_HC1"]),
                cr1["cobertura95"],
                rech(cr1),
                f["akm0_referencia"]["cobertura95"],
                rech(f["akm0_referencia"]),
            ]
        )
    return (
        tabla(cab, filas) + "\nCR1 agrupado por CCAA (G = 17) en el corte y por provincia (G = 52) en el apilado. «rech. β=0» es el "
        "tamaño con β = 0 y la potencia con β = 0,5. bhj y iv2sls dan el mismo coeficiente (dif. máx. "
        f"{max(f['max_dif_b_bhj_vs_iv2sls'] for f in d['disenos']):.1e}).\n"
    )


def sec_wcr(d):
    cab = ["diseño", "β", "sesgo MCO", "RMSE", "rech. WCR (Webb)", "rech. CR1 t(G-1)", "cob. CR1"]
    filas = [
        [f["diseno"], f["beta"], f["mco"]["sesgo"], f["mco"]["rmse"], rech(f["wcr_webb"]), rech(f["cr1_t(G-1)"]), f["mco"]["cobertura95"]]
        for f in d["disenos"]
    ]
    return tabla(cab, filas) + "\n«rech.» es el tamaño con β = 0 y la potencia con β = 0,5 (B = 399 en el MC; EE MC del tamaño ≈ 0,01).\n"


def sec_iv(d):
    cab = [
        "diseño",
        "F efectivo (mediana)",
        "sesgo MC2E (media)",
        "sesgo (mediana)",
        "cob. Wald",
        "rech. β=0 Wald",
        "cob. AR",
        "rech. β=0 AR",
        "AR acotado",
        "AR convexo",
    ]
    filas = [
        [
            f["diseno"],
            f["F_efectivo_mediana"],
            f["wald_iv2sls_CR1"]["sesgo"],
            f["wald_iv2sls_CR1"]["mediana_sesgo"],
            f["wald_iv2sls_CR1"]["cobertura95"],
            f["wald_iv2sls_CR1"]["potencia_vs_0"],
            f["ar_conjunto"]["cobertura95"],
            f["ar_conjunto"]["potencia_vs_0"],
            f["ar_conjunto"]["frac_acotado_en_beta±5"],
            f["ar_conjunto"]["frac_convexo"],
        ]
        for f in d["disenos"]
    ]
    return tabla(cab, filas) + (
        f"\nCobertura AR agregada de los tres diseños: {d['dgp']['ar_cobertura_agregada']:.3f} ± "
        f"{d['dgp']['ar_cobertura_agregada_ee']:.3f}. «rech. β=0» es potencia (β = 1). f_efectivo = F_primera "
        f"de iv2sls (dif. máx. {max(f['max_dif_f_efectivo_vs_F_primera'] for f in d['disenos']):.1e}).\n"
    )


def sec_conley(d):
    cab = [
        "λ (km)",
        "β",
        "sesgo",
        "RMSE",
        "cob. Conley",
        "rech. β=0 Conley",
        "cob. HC1",
        "rech. β=0 HC1",
        "V Conley / V MC",
        "V HC1 / V MC",
        "V<0",
    ]
    filas = [
        [
            f["lambda_km"],
            f["beta"],
            f["conley"]["sesgo"],
            f["conley"]["rmse"],
            f["conley"]["cobertura95"],
            rech(f["conley"]),
            f["hc1"]["cobertura95"],
            rech(f["hc1"]),
            f["var_conley_media/var_mc_b"],
            f["var_hc1_media/var_mc_b"],
            f["frac_var_conley_negativa"],
        ]
        for f in d["disenos"]
    ]
    return tabla(cab, filas) + f"\nVecinos medios dentro de 200 km: {d['dgp']['vecinos_medios_en_radio']:.1f}.\n"


def sec_oaxaca(d):
    cab = [
        "diseño",
        "verdad explicada",
        "sesgo explicada",
        "RMSE",
        "sesgo no explicada",
        "error máx. identidades",
        "dif. sin/con constante",
    ]
    filas = [
        [
            f["diseno"],
            f["explicada"]["verdad"],
            f["explicada"]["sesgo"],
            f["explicada"]["rmse"],
            f["no_explicada"]["sesgo"],
            f"{f['max_error_identidades']:.1e}",
            f"{f['max_dif_sin_vs_con_constante']:.1e}",
        ]
        for f in d["disenos"]
    ]
    return tabla(cab, filas)


def sec_dfl(d):
    qs = list(d["disenos"][0]["composicion_cuantiles"])
    cab = ["diseño", "sesgo media", "RMSE media"] + [f"sesgo q{q}" for q in qs] + ["error máx. identidades"]
    filas = [
        [f["diseno"], f["composicion_media"]["sesgo"], f["composicion_media"]["rmse"]]
        + [f["composicion_cuantiles"][q]["sesgo"] for q in qs]
        + [f"{f['max_error_identidades']:.1e}"]
        for f in d["disenos"]
    ]
    return tabla(cab, filas)


SECCION = {"bhj": sec_bhj, "wcr_boot": sec_wcr, "iv2sls": sec_iv, "conley": sec_conley, "oaxaca": sec_oaxaca, "dfl": sec_dfl}


def main():
    docs = {h: json.loads((_mc.OUT_MC / h / "resultado.json").read_text(encoding="utf-8")) for h in ORDEN}
    s = [
        "# Validación Monte Carlo de las herramientas econométricas (fase 5)\n",
        "Generado por `src/m1/montecarlo/informe.py` a partir de `output/montecarlo/<herramienta>/resultado.json`. Solo datos "
        f"simulados (nunca datos reales), SEED={_mc.SEED}, R = 500 réplicas por diseño. Criterio común: **APTO** si la cobertura "
        "del IC95 está en [0,92; 0,98] y el tamaño al 5 % es ≤ 0,08; si no, **NO APTO** con la condición en que falla. Los "
        "procesos generadores se declararon en el docstring de cada script antes de simular. Error MC de una cobertura de 0,95 con "
        "R = 500: ≈ 0,01.\n",
        "## Resumen de veredictos\n",
        tabla(["herramienta", "veredicto", "uso en M1"], [[f"`{h}`", docs[h]["veredicto"], USO[h]] for h in ORDEN]),
        "\n",
    ]
    for h in ORDEN:
        d = docs[h]
        s += [
            f"## {TITULOS[h]}\n",
            "**DGP**\n",
            "```text\n" + d["dgp"]["descripcion"].strip() + "\n```\n",
            "**Resultados**\n",
            SECCION[h](d),
            f"\n**Veredicto: {d['veredicto']}.** {d['condicion']}\n",
            f"\n*Uso:* {USO[h]}\n",
            f"\nScript: `src/m1/montecarlo/{'oaxaca_dfl' if h in ('oaxaca', 'dfl') else h}.py`; salida: "
            f"`output/montecarlo/{h}/resultado.json` ({d['segundos']} s).\n\n",
        ]
    s += [
        "## Tests y correcciones\n",
        "- `tests/test_econ.py`: `ols` = statsmodels OLS/WLS con CR1 y HC1; `iv2sls` = linearmodels IV2SLS (coeficientes y EE "
        "agrupado). econ aplica G/(G-1)·(n-1)/(n-k), igual que linearmodels con `debiased=True`; con su opción por defecto "
        "(`debiased=False`) linearmodels 7.1 no aplica ninguna corrección, de modo que V_econ = V_lm·G/(G-1)·(n-1)/(n-k). No se "
        "cambia econ (se mantiene la convención de Stata). También: f_efectivo = F_primera, bhj = MC2E de ubicación con W que "
        "incluye la suma de cuotas, e identidades de oaxaca y dfl.\n",
        "- Corrección en `econ.oaxaca`: si X no traía constante, la regresión agrupada no tenía término independiente y la parte "
        "explicada quedaba sesgada (el indicador de grupo hacía de constante solo para A). Ahora se añade una constante cuando X no "
        "tiene ninguna columna constante; con constante el resultado no cambia.\n",
    ]
    p = _mc.RAIZ / "docs" / "montecarlo.md"
    p.write_text("\n".join(s), encoding="utf-8")
    print(p)


if __name__ == "__main__":
    main()
