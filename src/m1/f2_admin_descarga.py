"""M1-F2 · Registros administrativos de España (estadísticas públicas agregadas, sin microdatos), CON red.

Descarga con fuentes.descargar (URL, licencia, edición, fecha y sha256 en data/fuentes.csv y data/CHECKSUMS.sha256) a
data/raw/admin/. Solo descargas públicas y sin registro. Ficha: docs/fuentes/admin.md.

Bloques (uso: python3 src/m1/f2_admin_descarga.py [ss|ss_hist|sepe|imv|edu|san|todo]):
- ss       Seguridad Social, base PX-Web de la TGSS (w6.seg-social.es/PXWeb): afiliados medios extranjeros por país, provincia,
           régimen, sexo, edad y UE/no UE (2012-); afiliados medios totales por provincia, régimen, edad y sexo; afiliados
           último día por nacionalidad (españoles/extranjeros) y edad (2014-); cotizantes y base media de cotización del
           Régimen General por nacionalidad, provincia, edad, etc.; pensionistas (INSS, último mes).
- ss_hist  Seguridad Social, «Histórico de estadísticas de afiliación publicadas desde 1999» (Excel mensuales): afiliados
           extranjeros por provincia y régimen y por nacionalidad (2006-2011) y afiliados totales por provincia (1999-2011).
- sepe     SEPE: resúmenes mensuales «Avance» (paro registrado, contratos y beneficiarios de prestaciones de extranjeros por
           provincia y CCAA), diciembre de cada año 2005-2025 y todos los meses de 2026; contratos acumulados anuales
           (diciembre, 2006-2025) con contratos a extranjeros por provincia (comunitarios/extracomunitarios); series de paro.
- imv      Ingreso Mínimo Vital (INSS): dosier por CCAA y provincia con titulares por sexo y nacionalidad y nómina mensual.
- edu      Ministerio de Educación (EDUCAbase, ficheros PC-Axis): alumnado extranjero (series por CCAA y área de
           nacionalidad; provincia y país en el último curso), alumnado total, alumnos por grupo y por profesor (2015-16 a
           2024-25), gasto público en educación (series y último año) y «Las cifras de la educación en España» (xlsx).
- san      Ministerio de Sanidad: listas de espera SISLE-SNS por CCAA (todos los cortes publicados, PDF), profesionales de
           medicina y enfermería del SNS por CCAA (tablas «Sanidad en datos»); perfiles de gasto sanitario por edad: Ageing
           Report 2024 (Comisión Europea), Ley 22/2009 (ponderaciones por edad de la población protegida equivalente) y
           Blanco Moreno, Urbanos y Thuissard (Gac Sanit 2013) con la prestación real media por edad y sexo en España.

No transforma los crudos. Si una URL devuelve HTML en lugar del fichero esperado no se descarga (se informa).
"""
from __future__ import annotations

import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fuentes  # noqa: E402

FAM = "admin"
UA = fuentes.UA
HOY = time.strftime("%Y-%m-%d")

LIC_SS = ("Seguridad Social: reutilización autorizada (usos comerciales y no comerciales) citando la fuente y la fecha de "
          "última actualización, sin desnaturalizar (https://www.seg-social.es/wps/portal/wss/internet/AvisoLegal)")
LIC_SEPE = ("SEPE: reutilización según Ley 37/2007 y RD 1495/2011, condiciones generales de datos.gob.es, citando la fuente "
            "(https://www.sepe.es/HomeSepe/mas-informacion-contacto/aviso-legal.html; https://datos.gob.es/es/aviso-legal)")
LIC_EDU = ("Ministerio de Educación, FP y Deportes: reproducción autorizada manteniendo la integridad y citando al Ministerio "
           "como fuente; estadísticas públicas también en datos.gob.es (https://www.educacionfpydeportes.gob.es/comunes/"
           "aviso-legal.html)")
LIC_SAN = ("Ministerio de Sanidad: reutilización autorizada (usos comerciales y no comerciales) citando la fuente y la fecha "
           "de última actualización, sin desnaturalizar (https://www.sanidad.gob.es/avisoLegal/home.htm)")
LIC_CE = ("Comisión Europea: reutilización autorizada citando la fuente, Decisión 2011/833/UE, CC BY 4.0 "
          "(https://commission.europa.eu/legal-notice_en)")
LIC_BOE = "BOE: reutilización autorizada citando la fuente (https://www.boe.es/informacion/aviso_legal/)"
LIC_GS = ("Gaceta Sanitaria (SESPAS/Elsevier), acceso abierto; uso no comercial citando a los autores "
          "(https://www.gacetasanitaria.org)")

RESUMEN: list[tuple[str, str]] = []


# ── utilidades ───────────────────────────────────────────────────────────────────────────────────────────────────────────
def _get(url: str, rango: str | None = None, intentos: int = 5) -> bytes:
    h = {"User-Agent": UA}
    if rango:
        h["Range"] = rango
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=120) as r:  # noqa: S310
                return r.read()
        except urllib.error.HTTPError:
            raise
        except Exception:  # noqa: BLE001
            if i == intentos - 1:
                raise
            time.sleep(2 * (i + 1))
    return b""


def _texto(url: str) -> str:
    return _get(url).decode("utf-8", "replace")


def _q(url: str) -> str:
    """Codifica espacios, tildes y demás caracteres de una URL (mantiene la estructura)."""
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(urllib.parse.unquote(p.path), safe="/,+()"),
                                    p.query, p.fragment))


def _nombre(s: str) -> str:
    s = urllib.parse.unquote(s).replace("+", "_")
    s = re.sub(r"[^\w.\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s[:150]


def _es_html(url: str) -> bool:
    try:
        b = _get(url, "bytes=0-600").lstrip()[:200].lower()
    except urllib.error.HTTPError:
        return True
    return b.startswith((b"<!doctype", b"<html", b"error 404")) or b"<html" in b[:120]


def bajar(url: str, nombre: str, lic: str, edicion: str, desc: str, html_ok: bool = False, bib: bool = False) -> str:
    """bib=True: documento de referencia (informe o artículo en PDF). Por la regla de CLAUDE.md (PDFs de referencias nunca
    al repositorio) queda en data/raw/admin/grandes/ (no versionado) con URL y checksum registrados."""
    url = _q(url)
    if fuentes.ya_descargado(url):
        r = "ya"
    elif not html_ok and _es_html(url):
        r = "HTML (no es el fichero esperado)"
    else:
        try:
            fuentes.descargar(url, FAM, nombre, lic, edicion, desc, no_versionar=bib)
            r = "ok"
        except urllib.error.HTTPError as e:
            r = f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001
            r = f"error {type(e).__name__}: {str(e)[:80]}"
    print(f"{r:>6}  {nombre}", flush=True)
    RESUMEN.append((nombre, r))
    return r


# ── Seguridad Social: PX-Web de la TGSS ─────────────────────────────────────────────────────────────────────────────────
PXB = "https://w6.seg-social.es/PXWeb/Resources/PX/Databases/"
SS_PX = [
    ("Afiliados en alta laboral", "Afiliados Medios Extranjeros", [
        "1m. Afiliados Total Sistema por sexo, tramo de edad y pais.px",
        "2m. Afiliados Total Sistema por sexo, pais y regimen.px",
        "3m. Afiliados extranjeros por sexo, provincia, regimen y UEnoUE.px",
        "3mb.Afiliados extranjeros por sexo, CCAA, regimen y UEnoUE.px",
        "5m09. Afiliados extranjeros por RG y RETA, provincia, seccion CNAE 09 y UEnoUE (hasta dic-25).px",
        "5m25. Afiliados extranjeros por RG y RETA, provincia, seccion CNAE 25 y UEnoUE (desde ene-26).px"]),
    ("Afiliados en alta laboral", "Afiliados Medios", [
        "01m. Por sexo, edad y regimen.px",
        "03m. Por sexo, provincia y regimen.px",
        "03mb. Por sexo, CC.AA y regimen.px",
        "04m09. Por provincia, seccion de actividad CNAE 09 y regimen (RG y RETA) (hasta dic-25).px",
        "04m25. Por provincia, seccion de actividad CNAE 25 y regimen (RG y RETA) (desde ene-26).px",
        "11m. Por provincia, edad y sexo.px"]),
    ("Afiliados en alta laboral", "Afiliados Fin de mes", [
        "10f. Por edad, sexo, régimen, y nacionalidad (Ultimo dia).px"]),
    ("Bases de cotización y cotizantes", "Régimen General", [
        "01. Cotizantes y base media de cotizacion por sexo y edad.px",
        "02. Cotizantes y base media de cotizacion por sexo, tipo de contrato y tipo de jornada.px",
        "03_09. Cotizantes y base media de cotizacion por sexo y seccion de actividad CNAE 09 (hasta dic-25).px",
        "03_25. Cotizantes y base media de cotizacion por sexo y seccion de actividad CNAE 25 (desde ene-26).px",
        "04_09. Cotizantes y base media de cotizacion por sexo y actividad CNAE 09-2digitos (hasta dic-25).px",
        "04_25. Cotizantes y base media de cotizacion por sexo y actividad CNAE 25 - 2digitos (desde ene-26).px",
        "05. Cotizantes y base media de cotizacion por sexo y provincia.px",
        "05b. Cotizantes y base media de cotizacion por sexo y CCAA.px",
        "06. Cotizantes y base media de cotizacion por sexo y grupo de cotizacion.px",
        "07. Cotizantes y base media de cotizacion por sexo y nacionalidad.px"]),
]
SS_WEB = "https://www.seg-social.es"
SS_EST = SS_WEB + "/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas"


def _px_periodo(url: str) -> str:
    try:
        t = _get(url, "bytes=0-60000").decode("latin-1")
    except Exception:  # noqa: BLE001
        return f"consulta {HOY}"
    m = re.search(r'VALUES\("Per[ií]odo"\)=([^;]*);', t, re.S)
    lu = re.search(r'LAST-UPDATED="([^"]+)"', t)
    per = ""
    if m:
        v = re.findall(r'"([^"]+)"', m.group(1))
        if v:
            per = f"{v[0]}-{v[-1]}"
    return (per + (f"; actualizada {lu.group(1)}" if lu else f"; consulta {HOY}")).strip("; ")


def ss() -> None:
    for db, carpeta, tablas in SS_PX:
        for t in tablas:
            url = PXB + urllib.parse.quote(db) + "/" + urllib.parse.quote(carpeta) + "/" + urllib.parse.quote(t, safe=",")
            pref = "ss_px_ext" if "Extranjeros" in carpeta else ("ss_px_bases" if db.startswith("Bases") else "ss_px")
            bajar(url, _nombre(f"{pref}_{t}"), LIC_SS, _px_periodo(url),
                  f"TGSS PX-Web, {db} / {carpeta}: {t[:-3]}")
    # pensionistas (INSS), último informe mensual publicado
    h = _texto(SS_EST + "/EST23/26bce586-014b-4c4e-9484-009cee21e271")
    for f in dict.fromkeys(re.findall(r'href="(/wps/wcm/connect/wss/[0-9a-f-]{36}/(PTAS\d{6})\.xlsx)\?', h)):
        bajar(SS_WEB + f[0] + "?MOD=AJPERES", f"ss_pensionistas_{f[1]}.xlsx", LIC_SS, f[1][4:],
              "INSS, Pensionistas: por CCAA y provincia, sexo, edad, tramos de cuantía (sin nacionalidad)")


# ── Seguridad Social: histórico 1999-2011 (Excel mensuales) ─────────────────────────────────────────────────────────────
HIST = SS_EST[len(SS_WEB):] + "/EST8/EST167"   # ruta relativa al dominio
BLOQUES = ["434eb341-fdef-461c-8ed3-9850b39c4fd1", "7c6fe8ae-7cac-4209-91bb-d070c0a032af",
           "3eacb451-0430-4037-b468-125cc9785ea0", "4f9454a4-1ea8-43d1-a3ec-f984fc00ae1c"]


def _walk(ruta: str, titulos: list[str], prof: int, out: list) -> None:
    try:
        h = _texto(SS_WEB + ruta)
    except Exception:  # noqa: BLE001
        return
    for f in dict.fromkeys(re.findall(r'href="(/wps/wcm/connect/wss/[0-9a-f-]{36}/[^"?]+\.(?:xlsx?|XLSX?))\?', h)):
        out.append((titulos, f))
    if prof >= 4:
        return
    for s, t in dict.fromkeys(re.findall(r'href="(' + re.escape(ruta) + r'/[^"/]+)"[^>]*>([^<]{2,200})', h)):
        _walk(s, titulos + [html.unescape(t.strip())], prof + 1, out)


def _clase_hist(tit: list[str]) -> str | None:
    if len(tit) < 1 or not re.fullmatch(r"\d{4}", tit[0]):
        return None
    a, resto = int(tit[0]), " > ".join(tit[1:]).lower()
    if a > 2011:
        return None   # desde 2012 lo cubre la base PX-Web
    ext = "extranj" in resto or "afilados extranjeros" in resto
    if ext and "secci" not in resto:
        medios = "medi" in resto
        if (a <= 2008 and not medios) or (a >= 2009 and medios):
            return "ext_nac" if "nacionalidad" in resto else ("ext_prov" if "provincia" in resto else None)
        return None
    if a <= 2003:
        return "tot_prov_ud"   # 1999-2003: afiliados último día por régimen y provincia (un libro por mes)
    if a <= 2008:
        return "tot_prov_med" if re.fullmatch(r"(medios|afiliados medios|afiliación media mensual)", resto) else None
    return "tot_prov_med" if re.search(r"afiliados medios mes por cc\.?aa\.? y provincias seg[uú]n reg", resto) else None


def ss_hist() -> None:
    lista: list = []
    for b in BLOQUES:
        _walk(HIST + "/" + b, [], 0, lista)
    for tit, f in lista:
        c = _clase_hist(tit)
        if not c:
            continue
        base = f.rsplit("/", 1)[1]
        bajar(SS_WEB + f + "?MOD=AJPERES", _nombre(f"ss_hist_{tit[0]}_{c}_{base}"), LIC_SS, tit[0],
              "Seguridad Social, histórico de afiliación: " + " > ".join(tit))


# ── SEPE ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
SEPE = "https://www.sepe.es"


def sepe() -> None:
    h = _texto(SEPE + "/HomeSepe/que-es-el-sepe/estadisticas/datos-avance/datos.html")
    fic = dict.fromkeys(re.findall(r'href="(/SiteSepe/contenidos/que_es_el_sepe/estadisticas/datos_avance/datos/datos_'
                                   r'(\d{4})/(?:AV|Av|av)_(?:SISPE|sispe)_(\d{2})(\d{2})\.xls)"', h))
    ultimo = max(int(a) for _, a, _, _ in fic) if fic else 0
    for f, a, _, mm in fic:
        if mm == "12" or int(a) == ultimo:
            bajar(SEPE + f, f"sepe_avance_{a}{mm}.xls", LIC_SEPE, f"{a}-{mm}",
                  "SEPE, resumen mensual Avance: paro registrado, contratos y prestaciones (incluye extranjeros por "
                  "provincia/CCAA y zona de origen)")
    for a in range(2006, ultimo):
        try:
            hm = _texto(SEPE + f"/HomeSepe/que-es-el-sepe/estadisticas/contratos/estadisticas-nuevas/{a}/diciembre.html")
        except Exception as e:  # noqa: BLE001
            print("  sin página de contratos", a, e)
            continue
        for f in dict.fromkeys(re.findall(r'href="([^"]*contratos/datos/[^"]*ACUM[^"]*\.xls)"', hm, re.I)):
            bajar(urllib.parse.urljoin(SEPE + "/", f), f"sepe_contratos_acum_{a}12.xls", LIC_SEPE, f"{a} (acumulado anual)",
                  "SEPE, Estadística de contratos, acumulado anual a diciembre (contratos a extranjeros por provincia, "
                  "comunitarios/extracomunitarios, sexo, edad y sector)")
    av = SEPE + "/SiteSepe/contenidos/que_es_el_sepe/estadisticas/datos_avance/xls/empleo/"
    for f, d in [("paroprovsector.xls", "paro registrado total y de extranjeros por sector y provincia, último mes"),
                 ("evolparoseries2001.xls", "evolución mensual del paro registrado 2001-2016"),
                 ("evolparoseries.xls", "evolución mensual del paro registrado, últimos 10 años"),
                 ("evolprovsectores.xls", "evolución del paro registrado por provincia y sector")]:
        bajar(av + f, f"sepe_{f}", LIC_SEPE, f"consulta {HOY}", "SEPE, Avance: " + d)


# ── IMV ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
IMV = SS_EST + "/cbe2fda1-3ac7-4bc8-a5ec-06c178839e11"


def imv() -> None:
    for sec, pat, pref, d in [
        ("0e716715-d290-4745-a74a-28cc1c3bc9ea", r"(\d{6})\+COMPLETO\+Dossier[^\"?]*\.xlsx", "imv_dossier",
         "IMV, dosier por CCAA y provincia (titulares por sexo y nacionalidad: tabla 1.5)"),
        ("d1fee385-f3ad-4e58-a129-d8818d93ea4b", r"(\d{6})_IMV[^\"?]*N%C3%B3mina[^\"?]*\.xlsx", "imv_nomina",
         "IMV, nómina mensual por CCAA y provincia (prestaciones, beneficiarios, importes; sin nacionalidad)")]:
        h = _texto(IMV + "/" + sec)
        for anio_pag in dict.fromkeys(re.findall(r'href="(/wps/portal/[^"]*' + sec + r'/[0-9a-f-]{36})"', h)):
            ha = _texto(SS_WEB + anio_pag)
            fs = dict.fromkeys(re.findall(r'href="(/wps/wcm/connect/wss/[0-9a-f-]{36}/' + pat + r')\?', ha))
            if not fs:
                continue
            f, ym = max(fs, key=lambda x: x[1])   # último mes publicado de cada año
            bajar(SS_WEB + f + "?MOD=AJPERES", f"{pref}_{ym}.xlsx", LIC_SS, ym, d)


# ── Educación (EDUCAbase) ───────────────────────────────────────────────────────────────────────────────────────────────
EDU = "https://estadisticas.educacion.gob.es"
EDUPX = EDU + "/EducaJaxiPx/files/_px/es/px"
EDUWEB = "https://www.educacionfpydeportes.gob.es"


def _menu(path: str) -> list[tuple[str, str, str]]:
    h = _texto(f"{EDU}/EducaDynPx/educabase/index.htm?type=pcaxis&path={path}&file=pcaxis&l=s0")
    return [(p, f, html.unescape(t.strip())) for p, f, t in
            re.findall(r'Tabla\.htm\?path=([^&"]+)&amp;file=([^&"]+\.px)[^>]*>([^<]+)', h)]


def _edu_menu(path: str, filtro: str | None, pref: str, edicion: str) -> None:
    try:
        tablas = _menu(path)
    except Exception as e:  # noqa: BLE001
        print("  menú no disponible", path, e)
        return
    for p, f, t in tablas:
        if filtro and not re.search(filtro, t, re.I):
            continue
        bajar(EDUPX + p + f, _nombre(f"{pref}_{f}"), LIC_EDU, edicion, f"EDUCAbase {path}: {t}")


def edu() -> None:
    _edu_menu("/no-universitaria/alumnado/matriculado/series/extranjeros", None, "edu_series_extran", f"series, consulta {HOY}")
    _edu_menu("/no-universitaria/alumnado/matriculado/series/AlumnadoGen", r"Régimen General por (titularidad|sexo)",
              "edu_series_alumnado", f"series, consulta {HOY}")
    _edu_menu("/no-universitaria/alumnado/matriculado/2024-2025-rd/extran", None, "edu_2024-25_extran", "2024-2025 (resultados detallados)")
    _edu_menu("/no-universitaria/alumnado/matriculado/2025-2026-da/comunidad/extranjeros", None, "edu_2025-26da_extran",
              "2025-2026 (datos de avance)")
    for a in range(2015, 2025):
        c = f"{a}-{a + 1}-rd"
        _edu_menu(f"/no-universitaria/centros/centrosyunid/{c}/reggen",
                  r"^Número medio de alumnos por Unidades/Grupos por titularidad(/financiación)?(, | del centro, )comunidad "
                  r"autónoma/provincia y enseñanza$", f"edu_{a}-{(a + 1) % 100:02d}_alumnos_grupo", c)
        _edu_menu(f"/no-universitaria/profesorado/estadistica/{c}/resumen", r"^Número medio de alumnos por profesor",
                  f"edu_{a}-{(a + 1) % 100:02d}_alumnos_profesor", c)
        _edu_menu(f"/no-universitaria/profesorado/estadistica/{c}/reggen",
                  r"^Profesorado por titularidad del centro, comunidad autónoma/provincia, sexo y tipo de centro$",
                  f"edu_{a}-{(a + 1) % 100:02d}_profesorado", c)
    _edu_menu("/economicas/gasto/series", None, "edu_gasto_series", f"series desde 1992, consulta {HOY}")
    _edu_menu("/economicas/gasto/2024", None, "edu_gasto_2024", "2024")
    h = _texto(EDUWEB + "/servicios-al-ciudadano/estadisticas/indicadores/cifras-educacion-espana/2023-2024.html")
    for f, n in dict.fromkeys(re.findall(r'href="(/dam/jcr:[0-9a-f-]{36}/([a-z]\d{1,2})\.xlsx)"', h)):
        bajar(EDUWEB + f, f"edu_cifras_2023-24_{n}.xlsx", LIC_EDU, "Las cifras de la educación en España, curso 2023-2024 "
              "(edición 2026)", f"Las cifras de la educación en España 2023-2024, tabla {n.upper()}")
    # capítulo B4 (gasto en educación; tabla de gasto público por alumno y CCAA) de las ediciones anteriores
    for a in range(2008, 2023):
        c = f"{a}-{a + 1}"
        try:
            h = _texto(f"{EDUWEB}/servicios-al-ciudadano/estadisticas/indicadores/cifras-educacion-espana/{c}.html")
        except Exception as e:  # noqa: BLE001
            print("  sin edición", c, e)
            continue
        for f in dict.fromkeys(re.findall(r'href="(/dam/jcr:[0-9a-f-]{36}/b4(?:-xlsx)?\.xlsx?)"', h)):
            bajar(EDUWEB + f, f"edu_cifras_{a}-{(a + 1) % 100:02d}_b4.{f.rsplit('.', 1)[1]}", LIC_EDU,
                  f"Las cifras de la educación en España, curso {c}", f"Las cifras de la educación en España {c}, "
                  "capítulo B4 (gasto en educación; gasto público por alumno por CCAA)")


# ── Sanidad y perfiles de gasto por edad ─────────────────────────────────────────────────────────────────────────────────
SAN = "https://www.sanidad.gob.es/estadEstudios/estadisticas/inforRecopilaciones/"


def san() -> None:
    vistos = set()
    for pag in ("listaEspera.htm", "ListaEsperaInfAntCCAA.htm", "listaEsperaInfAnt.htm"):
        h = _texto(SAN + pag)
        for f in re.findall(r'href="([^"]*inforRecopilaciones/docs/[^"]+\.(?:pdf|xlsx?|csv))"', h, re.I):
            u = urllib.parse.urljoin(SAN + pag, f.strip())
            n = u.rsplit("/", 1)[1]
            if n in vistos or re.search(r"nota|real_decreto", n, re.I):
                continue
            vistos.add(n)
            bajar(u, _nombre(f"san_sisle_{n}"), LIC_SAN, n.rsplit(".", 1)[0],
                  "Ministerio de Sanidad, SISLE-SNS: listas de espera quirúrgica y de consultas externas (" +
                  ("por CCAA" if re.search(r"ccaa|comunidades", n, re.I) else "SNS") + ")")
    for t, d in [("tabla13", "profesionales de la medicina del SNS por CCAA (AP, hospital, urgencias, residentes)"),
                 ("tabla14", "profesionales de la enfermería del SNS por CCAA (AP, hospital, urgencias, residentes)")]:
        bajar(f"https://www.sanidad.gob.es/estadEstudios/sanidadDatos/tablas/{t}.htm", f"san_sanidad_en_datos_{t}.htm",
              LIC_SAN, f"consulta {HOY}", "Ministerio de Sanidad, Sanidad en datos: " + d, html_ok=True)
    ce = "https://economy-finance.ec.europa.eu/document/download/"
    for u, n, d in [
        (ce + "971dd209-41c2-425d-94f8-e3c3c3459af9_en?filename=ip279_en.pdf", "ar2024_ip279_informe.pdf",
         "Ageing Report 2024 (Institutional Paper 279): perfiles de gasto sanitario público por edad y sexo (agregados "
         "UE14/NMS/UE, gráfico I.2.2) y proyecciones por país"),
        (ce + "ea60b7c2-1b91-4e28-b651-2385d589e8c4_en?filename=ip257_en_1.pdf", "ar2024_ip257_metodologia.pdf",
         "Ageing Report 2024, supuestos y metodología (Institutional Paper 257): perfiles edad-coste"),
        (ce + "403cc04f-9487-406b-a48a-22538e0d461c_en?filename=2024_Ageing_Report-Statistical_annex_all_horizontal_tables.xlsx",
         "ar2024_anexo_tablas_horizontales.xlsx", "Ageing Report 2024, anexo estadístico (tablas horizontales)"),
        (ce + "e248db46-f876-4e72-8821-efae678e81ea_en?filename=2024_Ageing_Report-Statistical_annex_all_countryfiches.xlsx",
         "ar2024_anexo_fichas_pais.xlsx", "Ageing Report 2024, anexo estadístico (fichas por país)"),
        (ce + "392994f2-c025-4066-bea8-f65cf4bcd411_en?filename=2024-ageing-report-country-fiche-Spain.pdf",
         "ar2024_ficha_espana.pdf", "Ageing Report 2024, ficha de España")]:
        bajar(u, n, LIC_CE, "2024", d, bib=n.endswith(".pdf"))
    bajar("https://www.boe.es/boe/dias/2009/12/19/pdfs/BOE-A-2009-20375.pdf", "boe_ley_22_2009_financiacion_ccaa.pdf",
          LIC_BOE, "BOE núm. 305, 19-12-2009", "Ley 22/2009 (financiación autonómica): población protegida equivalente con "
          "ponderaciones de gasto sanitario por siete grupos de edad (art. 9)", bib=True)
    bajar("https://gacetasanitaria.org/es-download-pdf-S0213911112002701", "gs2013_blanco_urbanos_thuissard_prestacion_edad_sexo.pdf",
          LIC_GS, "Gac Sanit 2013;27(3):220-225", "Blanco Moreno, Urbanos Garrido y Thuissard Vasallo (2013): prestación "
          "real media (gasto sanitario público por persona) por edad y sexo en España, 1998, 2003 y 2008", bib=True)


BLOQ = {"ss": ss, "ss_hist": ss_hist, "sepe": sepe, "imv": imv, "edu": edu, "san": san}

if __name__ == "__main__":
    sel = sys.argv[1:] or ["todo"]
    for b in (list(BLOQ) if "todo" in sel else sel):
        print(f"== {b}", flush=True)
        BLOQ[b]()
    malos = [(n, r) for n, r in RESUMEN if r not in ("ok", "ya")]
    print(f"\nresumen: {len(RESUMEN)} ficheros, {len(RESUMEN) - len(malos)} ok/ya; fallos: {len(malos)}")
    for n, r in malos:
        print("  ", r, n)
