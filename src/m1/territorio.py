"""M1 · Correspondencia versionada de códigos territoriales: provincia INE → CCAA, NUTS2 y NUTS3 (NUTS 2021).
Baleares (07) y las dos provincias canarias (35, 38) tienen varias NUTS3 (islas); se listan todas para los mapas."""
from __future__ import annotations

import pandas as pd

# prov INE: (nombre, CCAA INE, NUTS2, [NUTS3])
PROV = {
    "01": ("Araba/Álava", "16", "ES21", ["ES211"]), "02": ("Albacete", "08", "ES42", ["ES421"]),
    "03": ("Alicante/Alacant", "10", "ES52", ["ES521"]), "04": ("Almería", "01", "ES61", ["ES611"]),
    "05": ("Ávila", "07", "ES41", ["ES411"]), "06": ("Badajoz", "11", "ES43", ["ES431"]),
    "07": ("Illes Balears", "04", "ES53", ["ES531", "ES532", "ES533"]), "08": ("Barcelona", "09", "ES51", ["ES511"]),
    "09": ("Burgos", "07", "ES41", ["ES412"]), "10": ("Cáceres", "11", "ES43", ["ES432"]),
    "11": ("Cádiz", "01", "ES61", ["ES612"]), "12": ("Castellón/Castelló", "10", "ES52", ["ES522"]),
    "13": ("Ciudad Real", "08", "ES42", ["ES422"]), "14": ("Córdoba", "01", "ES61", ["ES613"]),
    "15": ("A Coruña", "12", "ES11", ["ES111"]), "16": ("Cuenca", "08", "ES42", ["ES423"]),
    "17": ("Girona", "09", "ES51", ["ES512"]), "18": ("Granada", "01", "ES61", ["ES614"]),
    "19": ("Guadalajara", "08", "ES42", ["ES424"]), "20": ("Gipuzkoa", "16", "ES21", ["ES212"]),
    "21": ("Huelva", "01", "ES61", ["ES615"]), "22": ("Huesca", "02", "ES24", ["ES241"]),
    "23": ("Jaén", "01", "ES61", ["ES616"]), "24": ("León", "07", "ES41", ["ES413"]),
    "25": ("Lleida", "09", "ES51", ["ES513"]), "26": ("La Rioja", "17", "ES23", ["ES230"]),
    "27": ("Lugo", "12", "ES11", ["ES112"]), "28": ("Madrid", "13", "ES30", ["ES300"]),
    "29": ("Málaga", "01", "ES61", ["ES617"]), "30": ("Murcia", "14", "ES62", ["ES620"]),
    "31": ("Navarra", "15", "ES22", ["ES220"]), "32": ("Ourense", "12", "ES11", ["ES113"]),
    "33": ("Asturias", "03", "ES12", ["ES120"]), "34": ("Palencia", "07", "ES41", ["ES414"]),
    "35": ("Las Palmas", "05", "ES70", ["ES704", "ES705", "ES708"]), "36": ("Pontevedra", "12", "ES11", ["ES114"]),
    "37": ("Salamanca", "07", "ES41", ["ES415"]), "38": ("Santa Cruz de Tenerife", "05", "ES70", ["ES703", "ES706", "ES707", "ES709"]),
    "39": ("Cantabria", "06", "ES13", ["ES130"]), "40": ("Segovia", "07", "ES41", ["ES416"]),
    "41": ("Sevilla", "01", "ES61", ["ES618"]), "42": ("Soria", "07", "ES41", ["ES417"]),
    "43": ("Tarragona", "09", "ES51", ["ES514"]), "44": ("Teruel", "02", "ES24", ["ES242"]),
    "45": ("Toledo", "08", "ES42", ["ES425"]), "46": ("Valencia/València", "10", "ES52", ["ES523"]),
    "47": ("Valladolid", "07", "ES41", ["ES418"]), "48": ("Bizkaia", "16", "ES21", ["ES213"]),
    "49": ("Zamora", "07", "ES41", ["ES419"]), "50": ("Zaragoza", "02", "ES24", ["ES243"]),
    "51": ("Ceuta", "18", "ES63", ["ES630"]), "52": ("Melilla", "19", "ES64", ["ES640"]),
}


def tabla() -> pd.DataFrame:
    return pd.DataFrame([{"prov": k, "nombre": v[0], "ccaa": v[1], "nuts2": v[2], "nuts3": ";".join(v[3])} for k, v in PROV.items()])


def nombre(prov: str) -> str:
    return PROV.get(str(prov).zfill(2), (str(prov),))[0]
