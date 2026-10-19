"""M1 · make publicacion / make web: genera publicacion/documento_m1/ desde docs/documento/documento.md sustituyendo cada marcador
{{id}} (o {{id:inf}}, {{id:sup}}) por su valor de output/cifras_clave.csv, copia figuras, tablas_m1.xlsx y las fichas de
afirmaciones, y escribe publicacion/MANIFIESTO.sha256 (make check comprueba que nada se edite a mano). Con --web genera además
publicacion/web/index.html. Sin red. Falla si queda algún «[FALTA CIFRA».
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cifras as cmod  # noqa: E402
from comun import DOCS, OUT, RAIZ, sha256  # noqa: E402
from f6_afirmaciones import render  # noqa: E402

PUB = RAIZ / "publicacion"
DOC = PUB / "documento_m1"


def md_a_html(md: str) -> str:
    out, lista, tabla = [], False, []

    def inline(s):
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    def cerrar_tabla():
        if tabla:
            filas = [f for f in tabla if not re.match(r"^\|[-| ]+\|$", f)]
            h = "".join(f"<th>{inline(c.strip())}</th>" for c in filas[0].strip("|").split("|"))
            cuerpo = "".join("<tr>" + "".join(f"<td>{inline(c.strip())}</td>" for c in f.strip("|").split("|")) + "</tr>" for f in filas[1:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{cuerpo}</tbody></table>")
            tabla.clear()
    cuerpo = md.split("---", 2)[2] if md.startswith("---") else md
    for linea in cuerpo.splitlines():
        if linea.startswith("|"):
            tabla.append(linea)
            continue
        cerrar_tabla()
        if linea.startswith("- "):
            if not lista:
                out.append("<ul>")
                lista = True
            out.append(f"<li>{inline(linea[2:])}</li>")
            continue
        if lista:
            out.append("</ul>")
            lista = False
        m = re.match(r"^(#{1,4}) (.*)$", linea)
        img = re.match(r"^!\[(.*?)\]\((.*?)\)$", linea)
        if m:
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif img:
            out.append(f'<figure><img src="../documento_m1/{img.group(2)}" alt="{html.escape(img.group(1))}"><figcaption>'
                       f"{html.escape(img.group(1))}</figcaption></figure>")
        elif linea.strip():
            out.append(f"<p>{inline(linea)}</p>")
    cerrar_tabla()
    if lista:
        out.append("</ul>")
    estilo = ("body{font-family:Georgia,serif;max-width:860px;margin:0 auto;padding:16px;line-height:1.5;color:#222;background:#fff}"
              "table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #ccc;padding:4px 6px;text-align:left}"
              "img{max-width:100%}h1{font-size:26px}h2{border-bottom:1px solid #ddd;margin-top:32px}code{font-size:13px}"
              "@media (prefers-color-scheme: dark){body{background:#151515;color:#ddd}td,th{border-color:#444}}")
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>Documento M1</title><style>{estilo}</style></head><body>{''.join(out)}</body></html>")


def main() -> int:
    web = "--web" in sys.argv
    c = cmod.consolidar()
    texto = render((DOCS / "documento" / "documento.md").read_text(encoding="utf-8"), c)
    faltan = re.findall(r"\[FALTA CIFRA: [^\]]+\]", texto)
    if faltan:
        print("faltan cifras:", faltan)
        return 1
    if DOC.exists():
        shutil.rmtree(DOC)
    (DOC / "figuras").mkdir(parents=True)
    (DOC / "documento.md").write_text(texto, encoding="utf-8")
    for p in sorted((OUT / "f7" / "figuras").glob("*.png")):
        shutil.copy2(p, DOC / "figuras" / p.name)
    shutil.copy2(OUT / "f7" / "tablas_m1.xlsx", DOC / "tablas_m1.xlsx")
    shutil.copy2(OUT / "f6" / "afirmaciones.md", DOC / "afirmaciones.md")
    shutil.copy2(OUT / "cifras_clave.csv", DOC / "cifras_clave.csv")
    if web or (PUB / "web").exists():
        (PUB / "web").mkdir(exist_ok=True)
        (PUB / "web" / "index.html").write_text(md_a_html(texto), encoding="utf-8")
    man = [f"{sha256(p)}  {p.relative_to(PUB)}" for p in sorted(PUB.rglob("*")) if p.is_file() and p.name not in ("MANIFIESTO.sha256", ".gitkeep")]
    (PUB / "MANIFIESTO.sha256").write_text("\n".join(man) + "\n", encoding="utf-8")
    print(f"publicar: {len(man)} ficheros en publicacion/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
