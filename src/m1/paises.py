"""M1 · Correspondencia versionada de los nombres de país del INE (padrón, ECP) con los ocho grupos de origen del plan.
Las filas agregadas (en mayúsculas) no se asignan. Decisiones D1-D3 de docs/decisiones.md."""
from __future__ import annotations

UE14 = ["Alemania", "Austria", "Bélgica", "Dinamarca", "Finlandia", "Francia", "Grecia", "Irlanda", "Italia", "Luxemburgo",
        "Países Bajos", "Portugal", "Suecia", "Reino Unido"]
UE13_OTROS_EUROPA = ["Bulgaria", "Chipre", "Croacia", "Eslovenia", "Estonia", "Hungría", "Letonia", "Lituania", "Malta", "Polonia",
                     "República Checa", "República Eslovaca", "Rumanía", "Albania", "Andorra", "Armenia", "Belarús",
                     "Bosnia y Herzegovina", "Georgia", "Islandia", "Liechtenstein", "Macedonia del Norte", "Moldavia", "Noruega",
                     "Rusia", "Serbia y Montenegro (Antigua Yugoslavia)", "Serbia", "Suiza", "Turquía", "Ucrania",
                     "Resto de Países Europeos", "Resto de Nacionalidades Europeas"]
MAGREB = ["Argelia", "Marruecos", "Mauritania", "Túnez"]
RESTO_AFRICA = ["Angola", "Benin", "Burkina Faso", "Cabo Verde", "Camerún", "Congo", "Costa de Marfil", "Egipto", "Etiopía",
                "Gambia", "Ghana", "Guinea", "Guinea Ecuatorial", "Guinea-Bissau", "Kenia", "Liberia", "Mali", "Nigeria",
                "República Democrática del Congo", "Senegal", "Sierra Leona", "Sudáfrica", "Togo", "Resto de Países Africanos",
                "Resto de África"]
AMERICA_LATINA = ["Costa Rica", "Cuba", "Dominica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panamá",
                  "República Dominicana", "Resto de América Central y Caribe", "México", "Argentina", "Bolivia", "Brasil", "Chile",
                  "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela", "Resto de América del Sur"]
ASIA = ["Arabia Saudí", "Bangladesh", "China", "Corea", "Filipinas", "India", "Indonesia", "Irán", "Iraq", "Israel", "Japón",
        "Jordania", "Kazajstán", "Líbano", "Nepal", "Pakistán", "Siria", "Tailandia", "Vietnam", "Resto de Asia",
        "Resto de Países Asiáticos"]
RESTO = ["Canadá", "Estados Unidos de América", "Australia", "Nueva Zelanda", "Resto de Oceanía", "Resto de Países de Oceanía", "APÁTRIDAS",
         "Resto de América del Norte"]

GRUPO_DE_PAIS: dict[str, str] = {}
for _lista, _g in ((UE14, "UE-14"), (UE13_OTROS_EUROPA, "UE-13 y otros de Europa"), (MAGREB, "Magreb"),
                   (RESTO_AFRICA, "Resto de África"), (AMERICA_LATINA, "América Latina"), (ASIA, "Asia"), (RESTO, "Resto")):
    for _p in _lista:
        GRUPO_DE_PAIS[_p] = _g


def grupo(nombre: str) -> str | None:
    if nombre in ("NACIDOS EN ESPAÑA", "España"):
        return "España"
    return GRUPO_DE_PAIS.get(nombre)
