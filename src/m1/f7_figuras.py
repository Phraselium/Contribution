"""M1-F7 · Figuras y mapas del documento (PNG en output/f7/figuras/). Sin red. Solo lee salidas de las fases 3 y 4 y la geometría
GISCO NUTS 2021 (© EuroGeographics para los límites administrativos)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.collections import PatchCollection  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import territorio  # noqa: E402
from comun import OUT, RAW  # noqa: E402

F = OUT / "f7" / "figuras"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 150})
COLORES = ["#2b5c8a", "#c4702b", "#5a9a5a", "#8e5a9a", "#b84a4a", "#7a7a7a", "#c9a227", "#3aa0a8"]


def _geo() -> list[dict]:
    return json.loads((RAW / "gisco" / "NUTS_RG_20M_2021_4326.geojson").read_text(encoding="utf-8"))["features"]


def _poligonos(geom) -> list[np.ndarray]:
    coords = geom["coordinates"]
    if geom["type"] == "Polygon":
        coords = [coords]
    return [np.array(p[0]) for p in coords]


def mapa(valores: dict, nivel: int, titulo: str, fichero: str, etiqueta: str, extent=None, cmap="viridis", canarias=False):
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    pats, vals = [], []
    for f in _geo():
        p = f["properties"]
        if p["LEVL_CODE"] != nivel or p["NUTS_ID"] not in valores or pd.isna(valores[p["NUTS_ID"]]):
            continue
        for pol in _poligonos(f["geometry"]):
            if canarias and pol[:, 1].mean() < 30:
                pol = pol + np.array([5.5, 7.0])   # Canarias desplazadas para el mapa
            pats.append(Polygon(pol, closed=True))
            vals.append(valores[p["NUTS_ID"]])
    from matplotlib.colors import TwoSlopeNorm
    norma = TwoSlopeNorm(vcenter=0, vmin=min(min(vals), -1e-6), vmax=max(max(vals), 1e-6)) if cmap == "RdBu" else None
    pc = PatchCollection(pats, cmap=cmap, edgecolor="white", linewidth=0.3, norm=norma)
    pc.set_array(np.array(vals))
    ax.add_collection(pc)
    ax.autoscale_view()
    if extent:
        ax.set_xlim(extent[0], extent[1])
        ax.set_ylim(extent[2], extent[3])
    ax.set_aspect(1.25)
    ax.axis("off")
    fig.colorbar(pc, ax=ax, shrink=0.7, label=etiqueta)
    ax.set_title(titulo)
    fig.text(0.01, 0.01, "Límites: © EuroGeographics (GISCO NUTS 2021).", fontsize=6)
    fig.savefig(F / fichero, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    F.mkdir(parents=True, exist_ok=True)
    # 1. empleo por grupo
    e = pd.read_csv(OUT / "f3" / "empleo_nacional.csv")
    e = e[e.origen_def == "nacimiento"]
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
    for i, g in enumerate(["España", "UE-14", "UE-13 y otros de Europa", "América Latina", "África", "Asia"]):
        x = e[e.grupo == g].sort_values("anio")
        ax[0].plot(x.anio, 100 * x.tasa_empleo, color=COLORES[i], label=g)
        ax[1].plot(x.anio, 100 * x.tasa_paro, color=COLORES[i])
    ax[0].set_title("Tasa de empleo 16-64 (%)")
    ax[1].set_title("Tasa de paro (%)")
    ax[0].legend(fontsize=7, frameon=False)
    fig.text(0.01, -0.02, "Fuente: EPA (INE), microdatos 2005-2026; grupo por región de nacimiento (aproximación D6).", fontsize=7)
    fig.savefig(F / "fig1_empleo.png", bbox_inches="tight")
    plt.close(fig)
    # 2. brecha salarial por cuantil
    d = pd.read_csv(OUT / "f3" / "salarios_deciles_dfl.csv")
    d = d[(d.anio == 2022) & (d.cuantil != "media")].copy()
    d["q"] = d.cuantil.astype(float)
    fig, ax = plt.subplots(figsize=(5, 3.2))
    ax.bar(d.q * 100 - 2, 100 * (np.exp(d.composicion) - 1), width=4, color=COLORES[0], label="composición")
    ax.bar(d.q * 100 + 2, 100 * (np.exp(d.resto) - 1), width=4, color=COLORES[1], label="resto")
    ax.axhline(0, color="black", lw=0.5)
    ax.set_xlabel("percentil")
    ax.set_ylabel("% del salario por hora")
    ax.set_title("Brecha salarial extranjeros − españoles (EES 2022), DFL")
    ax.legend(frameon=False)
    fig.savefig(F / "fig2_salarios_dfl.png", bbox_inches="tight")
    plt.close(fig)
    # 3. contribución fiscal: componentes y rango
    r = pd.read_csv(OUT / "f4" / "neta_por_grupo_2024.csv").set_index("grupo")
    rej = pd.read_csv(OUT / "f4" / "rejilla.csv")
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    for i, g in enumerate(r.index):
        x = rej[rej.grupo == g].neta_pc
        ax.plot([x.min(), x.max()], [i, i], color=COLORES[i], lw=6, alpha=0.4)
        ax.plot(r.loc[g, "neta"], i, "o", color=COLORES[i])
    ax.axvline(0, color="black", lw=0.5)
    ax.set_yticks(range(len(r.index)), ["Nacidos en " + g if g == "España" else g for g in r.index])
    ax.set_xlabel("€ por persona y año (2024)")
    ax.set_title("Contribución fiscal neta estática: principal e intervalo de 64 supuestos")
    fig.savefig(F / "fig3_fiscal_intervalos.png", bbox_inches="tight")
    plt.close(fig)
    # 4. pensiones: dependencia por variante
    p = pd.read_csv(OUT / "f4" / "pensiones_demografia.csv")
    p = p[p.geo == "ES"]
    fig, ax = plt.subplots(figsize=(5, 3.2))
    for i, v in enumerate(["BSL", "HMIGR", "LMIGR", "NMIGR"]):
        x = p[p.projection == v].sort_values("TIME_PERIOD")
        ax.plot(x.TIME_PERIOD, 100 * x.tasa_dependencia, color=COLORES[i], label={"BSL": "base", "HMIGR": "+33 % migración",
                                                                               "LMIGR": "−33 % migración", "NMIGR": "sin migración"}[v])
    ax.set_title("Tasa de dependencia 65+/20-64, EUROPOP2023 (España)")
    ax.legend(frameon=False)
    fig.savefig(F / "fig4_dependencia.png", bbox_inches="tight")
    plt.close(fig)
    # 5. mapa provincial: población nacida fuera (padrón 2022)
    pr = pd.read_csv(OUT / "f3" / "poblacion_provincias.csv", dtype={"prov": str})
    pr = pr[(pr.anio == 2022) & (pr.grupo != "España")].groupby("prov").cuota.sum()
    val = {}
    for prov, v in pr.items():
        for n3 in territorio.PROV[prov.zfill(2)][3]:
            val[n3] = 100 * v
    mapa(val, 3, "Población nacida fuera de España, 2022 (%)", "mapa1_provincias_nacidos_fuera.png", "%", extent=(-10, 5, 34, 44.5),
         canarias=True)
    # 6. mapa provincial: brecha de tasa de empleo (EPA 2025)
    ep = pd.read_csv(OUT / "f3" / "empleo_provincias.csv", dtype={"prov": str})
    w = ep[ep.anio == 2025].pivot(index="prov", columns="origen2", values="tasa_empleo")
    gap = 100 * (w["Nacidos fuera"] - w["España"])
    val = {n3: v for prov, v in gap.items() for n3 in territorio.PROV[prov.zfill(2)][3]}
    mapa(val, 3, "Tasa de empleo 16-64: nacidos fuera − nacidos en España, 2025 (pp)", "mapa2_provincias_brecha_empleo.png", "pp",
         extent=(-10, 5, 34, 44.5), cmap="RdBu", canarias=True)
    # 7. Europa NUTS2: brecha de empleo nativos / nacidos fuera
    eu = pd.read_csv(OUT / "f3" / "empleo_europa_nuts2.csv")
    eu = eu[eu.anio == eu.anio.max()].pivot_table(index="geo", columns="c_birth", values="valor")
    if {"NAT", "FOR"} <= set(eu.columns):
        g2 = (eu["FOR"] - eu["NAT"]).dropna().to_dict()
        mapa(g2, 2, "Tasa de empleo 20-64: nacidos fuera − nativos, NUTS2 (pp)", "mapa3_europa_nuts2.png", "pp", extent=(-12, 35, 34, 71),
             cmap="RdBu")
    print("f7_figuras:", sorted(p.name for p in F.glob("*.png")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
