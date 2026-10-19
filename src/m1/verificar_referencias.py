"""M1 · Verificador determinista de referencias (adaptado de Econometr-a, src/v15/verificar_referencias.py).

Fichas en docs/literatura/*.md con el formato:
    ### Autores (año). Título
    - DOI: 10.xxxx/… · Revista: …
    - Leído: resumen | texto completo (URL)
    - …
    - Estado: …
Para cada ficha con DOI: consulta Crossref (o DataCite si Crossref da 404) y guarda la respuesta reducida en la caché versionada
docs/literatura/crossref_cache.json; compara título (≥ 0,6 de palabras comunes), año (±1) y primer autor. Escribe:
- «VERIFICADA (Crossref)» o «VERIFICADA (DataCite)» si todo cuadra;
- «NO VERIFICADA (discrepa: …)» si el DOI existe pero no cuadra;
- «NO VERIFICADA (sin DOI)» si la ficha no trae DOI (informes institucionales, documentos sin DOI).
Falla si un DOI no existe o si, sin red, un DOI no está en la caché. Una ficha sin línea «Leído:» falla: nada no leído.
Uso: python3 src/m1/verificar_referencias.py [--red] [--solo-comprobar]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LIT = RAIZ / "docs" / "literatura"
CACHE = LIT / "crossref_cache.json"
FICHA = re.compile(r"^### (.+)$", re.M)
DOI = re.compile(r"^- DOI:\s*(10\.\d{4,9}/[^\s·]+)", re.M)
ESTADO = re.compile(r"^- Estado:.*$", re.M)
LEIDO = re.compile(r"^- Leído:\s*(resumen|texto completo)", re.M | re.I)
UA = {"User-Agent": "M1-estudio-publico (verificador de referencias; mailto:no-reply@example.org)"}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s).strip()


def _palabras(s: str) -> set[str]:
    return {w for w in _norm(s).split() if len(w) > 3}


def _get(url: str) -> dict:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:  # noqa: S310 (URL fija)
        return json.load(r)


def consultar(doi: str, cache: dict, red: bool) -> dict:
    if doi in cache:
        return cache[doi]
    if not red:
        raise SystemExit(f"verificar_referencias: DOI sin caché y sin red: {doi}")
    hoy = dt.date.today().isoformat()
    try:
        m = _get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
        a = m.get("author") or [{}]
        cache[doi] = {"existe": True, "registro": "Crossref", "titulo": (m.get("title") or [""])[0],
                      "primer_autor": a[0].get("family", a[0].get("name", "")),
                      "anio": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
                      "revista": (m.get("container-title") or [""])[0], "consulta": hoy}
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        try:
            m = _get("https://api.datacite.org/dois/" + urllib.parse.quote(doi))["data"]["attributes"]
            cr = (m.get("creators") or [{}])[0]
            cache[doi] = {"existe": True, "registro": "DataCite", "titulo": (m.get("titles") or [{}])[0].get("title", ""),
                          "primer_autor": cr.get("familyName") or cr.get("name", "").split(",")[0],
                          "anio": m.get("publicationYear"), "revista": m.get("publisher", ""), "consulta": hoy}
        except urllib.error.HTTPError as e2:
            if e2.code != 404:
                raise
            h = _get("https://doi.org/api/handles/" + urllib.parse.quote(doi))
            if h.get("responseCode") == 1:   # existe en doi.org con otra agencia (p. ej. Oficina de Publicaciones de la UE)
                ra = (_get("https://doi.org/ra/" + urllib.parse.quote(doi.split("/")[0])) or [{}])[0].get("RA", "otra agencia")
                cache[doi] = {"existe": True, "registro": ra, "consulta": hoy}
            else:
                cache[doi] = {"existe": False, "consulta": hoy}
    return cache[doi]


def estado(cab: str, cr: dict | None) -> str:
    if cr is None:
        return "NO VERIFICADA (sin DOI)"
    if not cr.get("existe"):
        return "NO VERIFICADA (el DOI no existe en Crossref ni en DataCite)"
    if cr.get("registro") not in ("Crossref", "DataCite"):
        return f"NO VERIFICADA (el DOI existe en doi.org, agencia {cr['registro']}, sin metadatos comparables)"
    problemas = []
    tit = cab.split(". ", 1)[1] if ". " in cab else cab
    ft, ct = _palabras(tit), _palabras(cr.get("titulo", ""))
    if ct and len(ft & ct) / max(1, min(len(ft), len(ct))) < 0.6:
        problemas.append("título")
    m = re.search(r"\((\d{4})", cab)
    if m and cr.get("anio") and abs(int(m.group(1)) - int(cr["anio"])) > 1:
        problemas.append(f"año ({m.group(1)} frente a {cr['anio']})")
    pa = cr.get("primer_autor") or ""
    if pa and _norm(pa).split() and re.sub(r"[^a-z]", "", _norm(pa).split()[-1]) not in re.sub(r"[^a-z]", "", _norm(cab.split("(")[0])):
        problemas.append(f"primer autor ({pa})")
    if problemas:
        return "NO VERIFICADA (discrepa: " + ", ".join(problemas) + ")"
    return f"VERIFICADA ({cr.get('registro', 'Crossref')})"


def procesar(red: bool, escribir: bool, solo: str = "*.md") -> tuple[dict, list[str]]:
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    errores, cuenta = [], {}
    for p in sorted(LIT.glob(solo)):
        partes = re.split(r"(?=^### )", p.read_text(encoding="utf-8"), flags=re.M)
        nuevas = []
        for b in partes:
            if not b.startswith("### "):
                nuevas.append(b)
                continue
            cab = FICHA.search(b).group(1)
            if not LEIDO.search(b):
                errores.append(f"{p.name}: ficha sin «- Leído: resumen|texto completo»: {cab[:70]}")
            md = DOI.search(b)
            cr = consultar(md.group(1).rstrip(".,;"), cache, red) if md else None
            if cr is not None and not cr.get("existe"):
                errores.append(f"{p.name}: DOI inexistente {md.group(1)} ({cab[:60]})")
            e = estado(cab, cr)
            clave = e.split(" (")[0] + (" (discrepa)" if "discrepa" in e else "")
            cuenta[clave] = cuenta.get(clave, 0) + 1
            b = ESTADO.sub(f"- Estado: {e}", b) if ESTADO.search(b) else b.rstrip("\n") + f"\n- Estado: {e}\n\n"
            nuevas.append(b)
        if escribir:
            p.write_text("".join(nuevas), encoding="utf-8")
    if escribir and red:
        CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return cuenta, errores


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--red", action="store_true")
    ap.add_argument("--solo-comprobar", action="store_true")
    ap.add_argument("--solo", default="*.md")
    a = ap.parse_args()
    cuenta, errores = procesar(red=a.red, escribir=not a.solo_comprobar, solo=a.solo)
    print("verificar_referencias:", cuenta)
    for e in errores:
        print("  ERROR", e)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
