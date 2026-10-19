"""M1-F2 · Normaliza el padrón continuo por provincia (1998-2022), sin red.

Entradas: data/raw/ine_padron/03006.px (país de nacimiento × nacionalidad española/extranjera) y 03005.px (extranjeros por
nacionalidad). Salidas:
- data/processed/padron_nacimiento.csv.gz: prov, anio, sexo, pais, grupo, nacionalidad (total | española | extranjera), valor;
- data/processed/padron_nacionalidad.csv.gz: prov, anio, sexo, pais, grupo, valor (solo extranjeros);
- data/processed/padron_grupos.csv.gz: prov, anio, origen_def, grupo, valor (ambos sexos), con «España» = nacidos en España
  (nacimiento) o españoles (nacionalidad).
Comprobaciones: la suma de países de cada grupo cuadra con los agregados del INE y la suma provincial con el total de España.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import PROC, RAW  # noqa: E402
from paises import grupo  # noqa: E402
from px import leer_px  # noqa: E402


def _prov(s: pd.Series) -> pd.Series:
    return s.str.extract(r"^(\d\d) ")[0]


def main() -> int:
    PROC.mkdir(parents=True, exist_ok=True)
    n = leer_px(RAW / "ine_padron" / "03006.px")
    n.columns = ["provincia", "pais", "nacionalidad", "sexo", "anio", "valor"]
    n["prov"] = _prov(n["provincia"])
    tot = n[(n.provincia == "TOTAL ESPAÑA")]
    n = n[n.prov.notna()].copy()
    n["grupo"] = n["pais"].map(grupo)
    n["nacionalidad"] = n["nacionalidad"].map({"TOTAL": "total", "Nacionalidad Española": "española",
                                               "Nacionalidad Extranjera": "extranjera"})
    n["sexo"] = n["sexo"].map({"Ambos sexos": "total", "Hombres": "hombres", "Mujeres": "mujeres"})
    n["anio"] = n["anio"].astype(int)
    paises = n[n.grupo.notna() & (n.pais != "NACIDOS EN ESPAÑA")]
    # comprobación: suma de países = nacidos en el extranjero
    a = paises[(paises.sexo == "total") & (paises.nacionalidad == "total")].groupby(["prov", "anio"]).valor.sum()
    b = n[(n.pais == "NACIDOS EN EL EXTRANJERO") & (n.sexo == "total") & (n.nacionalidad == "total")].set_index(["prov", "anio"]).valor
    dif = (a - b.reindex(a.index)).abs()
    # tolerancia: en 1998-2002 la suma de países difiere hasta en 13 personas del agregado (país no consta en el INE)
    assert (dif <= 20).all(), f"países no suman nacidos en el extranjero (máx. dif {dif.max()})"
    nt = tot[(tot.pais == "TOTAL POBLACIÓN") & (tot.sexo == "Ambos sexos") & (tot.nacionalidad == "TOTAL")]
    sp = n[(n.pais == "TOTAL POBLACIÓN") & (n.sexo == "total") & (n.nacionalidad == "total")].groupby("anio").valor.sum()
    assert (sp - nt.assign(anio=nt.anio.astype(int)).set_index("anio").valor).abs().max() < 1, "provincias no suman España"
    nac = n[n.grupo.notna()][["prov", "anio", "sexo", "pais", "grupo", "nacionalidad", "valor"]]
    nac.to_csv(PROC / "padron_nacimiento.csv.gz", index=False)

    x = leer_px(RAW / "ine_padron" / "03005.px")
    x.columns = ["pais", "provincia", "sexo", "anio", "valor"]
    x["prov"] = _prov(x["provincia"])
    x = x[x.prov.notna()].copy()
    x["grupo"] = x["pais"].map(grupo)
    x["sexo"] = x["sexo"].map({"Ambos sexos": "total", "Hombres": "hombres", "Mujeres": "mujeres"})
    x["anio"] = x["anio"].astype(int)
    xa = x[x.grupo.notna()]
    tx = x[x.pais == "TOTAL EXTRANJEROS"].set_index(["prov", "anio", "sexo"]).valor
    d2 = (xa.groupby(["prov", "anio", "sexo"]).valor.sum() - tx).abs().max()
    assert d2 <= 20, f"nacionalidades no suman el total de extranjeros (máx. dif {d2})"
    xa[["prov", "anio", "sexo", "pais", "grupo", "valor"]].to_csv(PROC / "padron_nacionalidad.csv.gz", index=False)

    # grupos (ambos sexos)
    g1 = nac[(nac.sexo == "total") & (nac.nacionalidad == "total")].groupby(["prov", "anio", "grupo"]).valor.sum().reset_index()
    g1["origen_def"] = "nacimiento"
    pt = n[(n.pais == "TOTAL POBLACIÓN") & (n.sexo == "total") & (n.nacionalidad == "total")].set_index(["prov", "anio"]).valor
    ext = xa[xa.sexo == "total"].groupby(["prov", "anio", "grupo"]).valor.sum().reset_index()
    esp = (pt - ext.groupby(["prov", "anio"]).valor.sum()).rename("valor").reset_index().assign(grupo="España")
    g2 = pd.concat([ext, esp])
    g2["origen_def"] = "nacionalidad"
    # nacionalizados: nacidos fuera con nacionalidad española
    g3 = nac[(nac.sexo == "total") & (nac.nacionalidad == "española") & (nac.grupo != "España")].groupby(
        ["prov", "anio", "grupo"]).valor.sum().reset_index().assign(origen_def="nacidos fuera con nacionalidad española")
    out = pd.concat([g1, g2, g3])[["prov", "anio", "origen_def", "grupo", "valor"]].sort_values(["origen_def", "prov", "anio", "grupo"])
    out.to_csv(PROC / "padron_grupos.csv.gz", index=False)
    print(f"f2_padron: {len(nac)} filas nacimiento, {len(xa)} nacionalidad, {len(out)} grupos; comprobaciones superadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
