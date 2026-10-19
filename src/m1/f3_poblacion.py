"""M1-F3 · Población, estructura por edad, flujos y años de residencia por grupo de origen (descriptivo, C1). Sin red.

Fuentes: padrón continuo (1998-2022, ocho grupos por país de nacimiento y nacionalidad), Estadística Continua de Población
(t56948, provincia × edad × región de nacimiento, hasta el último 1 de enero), Estadística de Migraciones y Cambios de Residencia
(t69692, t69707: 2021-2024), EPA (años de residencia) y Eurostat (migr_pop3ctb). Salidas en output/f3/poblacion_*.csv.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import OUT, PROC, RAW, Cifras  # noqa: E402

O = OUT / "f3"
PAD = "Padrón continuo (INE)"
ECP = "Estadística Continua de Población (INE)"


def _num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")


def ecp_enero() -> pd.DataFrame:
    p = RAW / "ine_tablas" / "grandes" / "t56948.csv"
    trozos = []
    for ch in pd.read_csv(p, sep=";", dtype=str, chunksize=2_000_000, encoding="utf-8-sig"):
        ch = ch[ch["Periodo"].str.startswith("1 de enero") & (ch["Sexo"] == "Total")]
        trozos.append(ch)
    d = pd.concat(trozos)
    d["anio"] = d["Periodo"].str[-4:].astype(int)
    d["valor"] = _num(d["Total"])
    d["prov"] = d["Provincias"].str.extract(r"^(\d\d) ")[0]
    return d.rename(columns={"Grupo quinquenal de edad": "edad", "País de nacimiento": "nacimiento"})


def main() -> int:
    O.mkdir(parents=True, exist_ok=True)
    cf = Cifras("f3_poblacion", "src/m1/f3_poblacion.py")
    g = pd.read_csv(PROC / "padron_grupos.csv.gz", dtype={"prov": str})
    # 1. series nacionales (padrón)
    nac = g.groupby(["origen_def", "anio", "grupo"]).valor.sum().reset_index()
    tot = nac[nac.origen_def != "nacidos fuera con nacionalidad española"].groupby(["origen_def", "anio"]).valor.transform("sum")
    nac.loc[nac.origen_def != "nacidos fuera con nacionalidad española", "cuota"] = nac.valor / tot
    nac.to_csv(O / "poblacion_padron_nacional.csv", index=False)
    a = 2022
    n = nac[(nac.origen_def == "nacimiento") & (nac.anio == a)].set_index("grupo")
    fuera = 1 - n.loc["España", "cuota"]
    cf.add(f"F3_POB_FUERA_PADRON_{a}", round(100 * fuera, 1), "% de la población", "Población nacida fuera de España (padrón)",
           "C1", PAD, f"1-1-{a}", "España", "nacidos fuera")
    for gr, r in n.iterrows():
        cf.add(f"F3_POB_CUOTA_{gr}_{a}", round(100 * r.cuota, 2), "% de la población", f"Cuota de población del grupo {gr}", "C1",
               PAD, f"1-1-{a}", "España", gr)
    n98 = nac[(nac.origen_def == "nacimiento") & (nac.anio == 1998)].set_index("grupo")
    cf.add("F3_POB_FUERA_PADRON_1998", round(100 * (1 - n98.loc["España", "cuota"]), 1), "% de la población",
           "Población nacida fuera de España (padrón)", "C1", PAD, "1-1-1998", "España", "nacidos fuera")
    nz = nac[(nac.origen_def == "nacidos fuera con nacionalidad española") & (nac.anio == a)].valor.sum()
    tf = n.valor.sum() - n.loc["España", "valor"]
    cf.add(f"F3_POB_NACIONALIZADOS_{a}", round(100 * nz / tf, 1), "% de los nacidos fuera",
           "Nacidos fuera con nacionalidad española (incluye hijos de españoles nacidos fuera)", "C1", PAD, f"1-1-{a}", "España",
           "nacidos fuera")
    # 2. provincias
    pr = g[(g.origen_def == "nacimiento") & g.anio.isin([2002, 2008, 2014, a])]
    pr = pr.assign(cuota=pr.valor / pr.groupby(["prov", "anio"]).valor.transform("sum"))
    pr.to_csv(O / "poblacion_provincias.csv", index=False)
    f = pr[(pr.anio == a) & (pr.grupo != "España")].groupby("prov").cuota.sum()
    cf.add(f"F3_POB_FUERA_PROV_MAX_{a}", round(100 * f.max(), 1), "%", f"Provincia con mayor cuota de nacidos fuera ({f.idxmax()})",
           "C1", PAD, f"1-1-{a}", f"provincia {f.idxmax()}", "nacidos fuera")
    cf.add(f"F3_POB_FUERA_PROV_MIN_{a}", round(100 * f.min(), 1), "%", f"Provincia con menor cuota de nacidos fuera ({f.idxmin()})",
           "C1", PAD, f"1-1-{a}", f"provincia {f.idxmin()}", "nacidos fuera")
    # 3. ECP: último 1 de enero, segunda fuente y estructura por edad
    e = ecp_enero()
    ult = e.anio.max()
    en = e[(e.Provincias == "Total Nacional") & (e.anio == ult)]
    tot_n = en[(en.nacimiento == "Total") & (en.edad == "Todas las edades")].valor.iloc[0]
    ext_n = en[(en.nacimiento == "Extranjero") & (en.edad == "Todas las edades")].valor.iloc[0]
    cf.add(f"F3_POB_FUERA_ECP_{ult}", round(100 * ext_n / tot_n, 1), "% de la población",
           "Población nacida fuera de España (ECP, segunda fuente)", "C1", ECP, f"1-1-{ult}", "España", "nacidos fuera")
    edad = en[en.edad != "Todas las edades"].copy()
    edad["ini"] = edad.edad.str.extract(r"(\d+)")[0].astype(int)
    filas = []
    for nombre in ("España", "Extranjero", "África", "Sudamérica", "UE27_2020 sin España", "Asia"):
        x = edad[edad.nacimiento == nombre].sort_values("ini")
        if x.empty:
            continue
        w = x.valor / x.valor.sum()
        filas.append({"nacimiento": nombre, "anio": ult, "pct_0_15": 100 * w[x.ini < 15].sum(),
                      "pct_16_64": 100 * w[(x.ini >= 15) & (x.ini < 65)].sum(), "pct_65_mas": 100 * w[x.ini >= 65].sum(),
                      "edad_media_aprox": float((w * (x.ini + 2.5)).sum())})
    est = pd.DataFrame(filas)
    est.to_csv(O / "poblacion_estructura_edad.csv", index=False)
    s = est.set_index("nacimiento")
    for nm, grp in (("España", "España"), ("Extranjero", "nacidos fuera")):
        cf.add(f"F3_POB_65MAS_{grp}_{ult}", round(s.loc[nm, "pct_65_mas"], 1), "% del grupo", "Población de 65 y más años", "C1", ECP,
               f"1-1-{ult}", "España", grp)
        cf.add(f"F3_POB_EDADMEDIA_{grp}_{ult}", round(s.loc[nm, "edad_media_aprox"], 1), "años",
               "Edad media aproximada (marcas de clase quinquenales)", "C1", ECP, f"1-1-{ult}", "España", grp)
    # provincias con la ECP (segunda fuente)
    ep = e[(e.prov.notna()) & (e.anio == ult) & (e.edad == "Todas las edades") & e.nacimiento.isin(["Total", "Extranjero"])]
    ep = ep.pivot_table(index="prov", columns="nacimiento", values="valor", aggfunc="sum")
    ep["cuota_fuera"] = ep["Extranjero"] / ep["Total"]
    ep.reset_index().to_csv(O / "poblacion_provincias_ecp.csv", index=False)
    # 4. flujos 2021-2024
    fl = flujos()
    fl.to_csv(O / "poblacion_flujos.csv", index=False)
    s = fl[fl.prov.isna()].groupby(["nacimiento"])[["inmigraciones", "emigraciones", "saldo"]].sum()
    cf.add("F3_POB_SALDO_EXTERIOR_FUERA_2021_2024", round(s.loc["Extranjero", "saldo"] / 1e6, 2), "millones",
           "Saldo migratorio con el extranjero de nacidos fuera, acumulado 2021-2024", "C1", "Estadística de Migraciones (INE)",
           "2021-2024", "España", "nacidos fuera")
    cf.add("F3_POB_SALDO_EXTERIOR_ESPANA_2021_2024", round(s.loc["España", "saldo"] / 1e6, 3), "millones",
           "Saldo migratorio con el extranjero de nacidos en España, acumulado 2021-2024", "C1", "Estadística de Migraciones (INE)",
           "2021-2024", "España", "España")
    # 5. años de residencia (EPA, 16+, último año completo)
    c = pd.read_csv(PROC / "epa_celdas.csv.gz", usecols=["anio", "origen_def", "grupo", "resid", "pob", "n_obs"])
    r = c[(c.origen_def == "nacimiento") & (c.grupo != "España") & (c.anio == 2025)].groupby(["grupo", "resid"])[["pob", "n_obs"]].sum()
    r["cuota"] = r.pob / r.groupby(level=0).pob.transform("sum")
    r = r.reset_index().rename(columns={"n_obs": "n_muestral"})
    r.loc[r.n_muestral < 50, "cuota"] = np.nan
    r.to_csv(O / "poblacion_residencia.csv", index=False)
    rt = c[(c.origen_def == "nacimiento") & (c.grupo != "España") & (c.anio == 2025)].groupby("resid").pob.sum()
    cf.add("F3_POB_RESID_20MAS_2025", round(100 * rt.get("20+", 0) / rt.sum(), 1), "% de los nacidos fuera de 16+",
           "Nacidos fuera con 20 o más años de residencia en España", "C1", "EPA (INE)", "2025", "España", "nacidos fuera")
    cf.add("F3_POB_RESID_0A4_2025", round(100 * rt.get("0-4", 0) / rt.sum(), 1), "% de los nacidos fuera de 16+",
           "Nacidos fuera con menos de 5 años de residencia en España", "C1", "EPA (INE)", "2025", "España", "nacidos fuera")
    # 6. Europa
    eu = pd.read_csv(RAW / "eurostat" / "migr_pop3ctb.csv.gz", low_memory=False)
    eu = eu[(eu.age == "TOTAL") & (eu.sex == "T") & eu.c_birth.isin(["TOTAL", "FOR", "NAT", "EU27_2020_FOR", "NEU27_2020_FOR"])]
    w = eu.pivot_table(index=["geo", "TIME_PERIOD"], columns="c_birth", values="OBS_VALUE").reset_index()
    w["cuota_fuera"] = w["FOR"] / w["TOTAL"]
    w.to_csv(O / "poblacion_europa.csv", index=False)
    u = w[w.TIME_PERIOD == w.TIME_PERIOD.max()].set_index("geo")
    au = int(w.TIME_PERIOD.max())
    if "EU27_2020" in u.index:
        cf.add(f"F3_POB_FUERA_UE27_{au}", round(100 * u.loc["EU27_2020", "cuota_fuera"], 1), "% de la población",
               "Población nacida fuera del país de residencia, UE-27", "C1", "Eurostat migr_pop3ctb", f"1-1-{au}", "UE-27",
               "nacidos fuera")
    cf.add(f"F3_POB_FUERA_ES_EUROSTAT_{au}", round(100 * u.loc["ES", "cuota_fuera"], 1), "% de la población",
           "Población nacida fuera, España (Eurostat)", "C1", "Eurostat migr_pop3ctb", f"1-1-{au}", "España", "nacidos fuera")
    paises = u[u.index.str.len() == 2].cuota_fuera.dropna().sort_values(ascending=False)
    cf.add(f"F3_POB_FUERA_ES_RANKING_{au}", int(list(paises.index).index("ES") + 1), "posición",
           f"Posición de España por cuota de nacidos fuera entre {len(paises)} países europeos con dato", "C1", "Eurostat migr_pop3ctb",
           f"1-1-{au}", "Europa", "nacidos fuera")
    cf.escribir()
    print("f3_poblacion: hecho;", len(cf.filas), "cifras")
    return 0


def flujos() -> pd.DataFrame:
    out = []
    for t, v in (("t69692", "inmigraciones"), ("t69707", "emigraciones")):
        d = pd.read_csv(RAW / "ine_tablas" / f"{t}.csv", sep=";", dtype=str, encoding="utf-8-sig")
        d = d[(d.Edad == "Total") & (d.Sexo == "Ambos sexos") & (d["País de nacimiento"] != "Total")]
        d = d[d["Comunidades y Ciudades Autónomas"].isna() | d.Provincias.notna()]
        d["prov"] = d.Provincias.str.extract(r"^(\d\d) ")[0]
        d[v] = _num(d.Total)
        out.append(d[["prov", "País de nacimiento", "Periodo", v]].rename(columns={"País de nacimiento": "nacimiento", "Periodo": "anio"}))
    f = out[0].merge(out[1], on=["prov", "nacimiento", "anio"], how="outer")
    f["saldo"] = f.inmigraciones - f.emigraciones
    return f


if __name__ == "__main__":
    sys.exit(main())
