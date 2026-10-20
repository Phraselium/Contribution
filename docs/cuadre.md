# Cuadre contable de C2 y del ciclo vital (a posteriori)

Añadido en la verificación tras el cierre (punto 1 del encargo). Pruebas en `tests/test_cuadre_fiscal.py`, que `make check` ejecuta
con el resto de pytest. No formaban parte del plan de análisis interno.

## Referencia y tolerancia
- Saldo y totales: Eurostat `gov_10a_main` (S13, MIO_EUR): España 2024, TR = 673.734 M€, TE = 725.001 M€, **B9 = −51.267 M€**
  (también 2022: −63.105; 2023: −50.027). Partidas: `gov_10a_taxag` (impuestos y cotizaciones) y `gov_10a_exp` (COFOG, TE y D62).
  Ficheros en data/raw/eurostat con checksum.
- **Tolerancia: 1 M€ por total**, la unidad de publicación de Eurostat. Las contribuciones de C2 son repartos de esos mismos
  totales, por lo que la identidad debe cumplirse hasta el redondeo de la fuente. No se ha ampliado tras ver resultados.

## Resultados
| prueba | antes de corregir | después |
|---|---|---|
| a) Σ población × contribución neta = B9, principal 2022, 2023, 2024 | **FALLA**: −49.532 frente a −51.267 M€ en 2024 (diferencia 1.735 M€; 1.742 y 1.741 en 2022 y 2023) | pasa (diferencia < 0,001 M€) |
| a) ídem, 32 combinaciones calibradas de la rejilla | FALLA en las 32 (misma diferencia) | pasa |
| a) 32 combinaciones sin calibrar | no se prueba: usan importes de la ECV sin llevarlos a las cuentas | se desvían +11.578 M€ de B9 (todas igual) |
| b) cada partida frente a su definición SEC 2010 (13 partidas, 3 años) | **FALLA** sanidad: 101.207 frente a 102.942 M€ (TE de GF07) | pasa |
| b) resto de ingresos = TR − impuestos imputados, ≥ 0 | pasa | pasa (89.396 M€ en 2024) |
| c) perfiles del ciclo vital × pirámide de la ECV 2024 = totales de C2, por grupo y partida | **FALLA**: resto de la UE, neta 4.637 frente a 5.836 M€ (−20,5 %; gastos +9,0 %); resto del mundo, neta −1.645 frente a −1.392 M€ | pasa |

**Error 1 (a, b).** La sanidad restaba las prestaciones monetarias D62 de la función GF07 (reembolsos; 1.735 M€ en 2024) y no las
imputaba en ninguna partida. Corrección: se imputa el TE completo de GF07 con el perfil de cada subfunción (src/m1/f4_fiscal.py).

**Error 2 (c).** En los tramos de edad suprimidos del perfil (n < 50: resto de la UE 0-24 y 70+; resto del mundo 0-4 y 85+) el ciclo
vital usaba el perfil nativo escalado por bloques con el tramo observado más próximo, que no reproduce lo que la contabilidad
estática atribuye a esas edades. Corrección: forma por edad nativa, partida a partida, reescalada al total del grupo en esos tramos
(totales agrupados por segmento, de uso interno en data/processed, no publicados; mismo criterio que la estandarización: el umbral se
aplica a lo publicado, no a los términos de un agregado). La variante «sin escalar» se mantiene como sensibilidad.

**Convención que la prueba c) no cubre (declarada, no corregida).** `vida()` usa para el gasto en especie por edad (sanidad, educación,
protección social en especie) el perfil de los nacidos en España para todos (D12, criterio OCDE). Frente al perfil propio del grupo,
eso añade por persona y año +13 € al resto de la UE y +36 € al resto del mundo en gasto (educación +24 y +53; sanidad −8 y −13;
protección social en especie −3 y −4). Es la única diferencia entre los flujos del ciclo vital en 2024 y los de C2.

## Cifras que cambian (antes → después)
Las 86 cifras de output/cifras_clave.csv que cambian con las dos correcciones (euros por persona y año, % del PIB o miles de euros de
valor actual). Ningún intervalo D11 cambia de contener a excluir el cero salvo uno: **F4_NETA_EST_PC_Resto_del_mundo_2024**
(contribución a igual edad y sexo del resto del mundo) pasa de [−3.184, 25] a [−3.223, −12], negativa en las 64 combinaciones. Y
una sensibilidad cambia de signo: **F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_40** pasa de +2 a −8 miles de euros (sin salidas, llegada a los
40 años, resto de la UE).

| id | antes | después | IC antes | IC después |
|---|---|---|---|---|
| F4_NETA_DIF_NAT_FUERA_2024 | 1892 | 1897 | [-643, 5061] | [-638, 5066] |
| F4_NETA_DIF_NAT_Resto_UE_2024 | 4799 | 4801 | [1764, 7601] | [1766, 7603] |
| F4_NETA_DIF_NAT_Resto_del_mundo_2024 | 1207 | 1213 | [-1215, 4552] | [-1209, 4557] |
| F4_NETA_EQUILIBRADA_PC_España_2024 | -350 | -351 | [-936, 146] | [-937, 144] |
| F4_NETA_EQUILIBRADA_PC_Resto_UE_2024 | 4449 | 4450 | [1778, 6729] | [1779, 6730] |
| F4_NETA_EQUILIBRADA_PC_Resto_del_mundo_2024 | 857 | 862 | [-1070, 3615] | [-1065, 3620] |
| F4_NETA_EST_DIF_NAT_MUESTREO_Resto_UE | 239 | 240 | [-655, 1133] | [-654, 1133] |
| F4_NETA_EST_DIF_NAT_Resto_UE_2024 | 239 | 240 | [16, 3009] | [14, 3010] |
| F4_NETA_EST_DIF_NAT_Resto_del_mundo_2024 | -1708 | -1708 | [-1973, 1668] | [-1976, 1668] |
| F4_NETA_EST_PC_Resto_UE_2024 | -1128 | -1164 | [-1284, 1428] | [-1322, 1391] |
| F4_NETA_EST_PC_Resto_del_mundo_2024 | -3075 | -3111 | [-3184, 25] | [-3223, -12] |
| F4_NETA_FUERA_MARGINAL_HIJO | 3339 | 3307 | [2651, 3339] | [2618, 3307] |
| F4_NETA_FUERA_MARGINAL_PADRES | 1032 | 1001 | [187, 1032] | [155, 1001] |
| F4_NETA_FUERA_MEDIO_HIJO | 1146 | 1115 | [458, 1146] | [425, 1115] |
| F4_NETA_FUERA_MEDIO_PADRES | -670 | -700 | [-1515, -670] | [-1546, -700] |
| F4_NETA_PC_España_2024 | -1367 | -1404 | [-1591, -1115] | [-1627, -1151] |
| F4_NETA_PC_FUERA_2024 | 525 | 493 | [-1515, 3339] | [-1546, 3307] |
| F4_NETA_PC_RANGO_SUPUESTOS_España_2024 | -1367 | -1404 | [-1953, -636] | [-1990, -673] |
| F4_NETA_PC_RANGO_SUPUESTOS_Resto_UE_2024 | 3432 | 3398 | [761, 5949] | [726, 5915] |
| F4_NETA_PC_RANGO_SUPUESTOS_Resto_del_mundo_2024 | -160 | -191 | [-2087, 2823] | [-2118, 2792] |
| F4_NETA_PC_Resto_UE_2024 | 3432 | 3398 | [2479, 4342] | [2444, 4307] |
| F4_NETA_PC_Resto_del_mundo_2024 | -160 | -191 | [-534, 290] | [-565, 259] |
| F4_NETA_TOTAL_PIB_España_2024 | -3.39 | -3.49 | [-4.85, -1.50] | [-4.94, -1.59] |
| F4_NETA_TOTAL_PIB_Resto_del_mundo_2024 | -0.07 | -0.09 | [-1.16, 1.29] | [-1.18, 1.27] |
| F4_VA_65MAS_Resto_UE_LLEGADA_20 | -24 | -25 |  |  |
| F4_VA_65MAS_Resto_UE_LLEGADA_30 | -26 | -27 |  |  |
| F4_VA_65MAS_Resto_UE_LLEGADA_40 | -25 | -26 |  |  |
| F4_VA_65MAS_Resto_UE_LLEGADA_50 | -25 | -27 |  |  |
| F4_VA_CONJUNTA_Resto_UE_30 | 26 | 23 |  |  |
| F4_VA_CONVERG_Resto_UE_LLEGADA_0 | -57 | -57 | [-145, 21] | [-145, 24] |
| F4_VA_CONVERG_Resto_UE_LLEGADA_20 | 44 | 42 | [6, 181] | [4, 178] |
| F4_VA_CONVERG_Resto_UE_LLEGADA_30 | 62 | 61 | [17, 168] | [10, 167] |
| F4_VA_CONVERG_Resto_UE_LLEGADA_40 | 58 | 57 | [-4, 129] | [-11, 128] |
| F4_VA_CONVERG_Resto_UE_LLEGADA_50 | 21 | 19 | [-63, 52] | [-71, 51] |
| F4_VA_CONVERG_Resto_del_mundo_LLEGADA_0 | -65 | -61 | [-186, 26] | [-185, 27] |
| F4_VA_CONVERG_Resto_del_mundo_LLEGADA_20 | 29 | 29 | [-28, 162] | [-30, 161] |
| F4_VA_CONVERG_Resto_del_mundo_LLEGADA_30 | 47 | 46 | [-29, 148] | [-31, 147] |
| F4_VA_CONVERG_Resto_del_mundo_LLEGADA_40 | 34 | 34 | [-47, 103] | [-48, 102] |
| F4_VA_CONVERG_Resto_del_mundo_LLEGADA_50 | -2 | -2 | [-110, 29] | [-112, 29] |
| F4_VA_DIF_NAT_CONV_Resto_UE_LLEGADA_20 | -34 | -35 | [-86, 133] | [-87, 132] |
| F4_VA_DIF_NAT_CONV_Resto_UE_LLEGADA_30 | -19 | -19 | [-84, 116] | [-83, 116] |
| F4_VA_DIF_NAT_CONV_Resto_UE_LLEGADA_40 | 61 | 61 | [-11, 171] | [-10, 171] |
| F4_VA_DIF_NAT_CONV_Resto_UE_LLEGADA_50 | 133 | 134 | [52, 230] | [48, 231] |
| F4_VA_DIF_NAT_CONV_Resto_del_mundo_LLEGADA_20 | -56 | -55 | [-103, 119] | [-103, 119] |
| F4_VA_DIF_NAT_CONV_Resto_del_mundo_LLEGADA_30 | -33 | -33 | [-99, 101] | [-98, 101] |
| F4_VA_DIF_NAT_CONV_Resto_del_mundo_LLEGADA_50 | 112 | 112 | [13, 211] | [13, 212] |
| F4_VA_DIF_NAT_Resto_UE_LLEGADA_20 | -87 | -88 | [-90, 47] | [-92, 36] |
| F4_VA_DIF_NAT_Resto_UE_LLEGADA_30 | -72 | -72 | [-89, 40] | [-89, 33] |
| F4_VA_DIF_NAT_Resto_UE_LLEGADA_40 | 15 | 15 | [-23, 122] | [-28, 122] |
| F4_VA_DIF_NAT_Resto_UE_LLEGADA_50 | 118 | 117 | [30, 211] | [22, 209] |
| F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_20 | -112 | -111 | [-176, -38] | [-176, -37] |
| F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_30 | -94 | -93 | [-150, 2] | [-150, 3] |
| F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_40 | -12 | -11 | [-82, 88] | [-82, 89] |
| F4_VA_DIF_NAT_Resto_del_mundo_LLEGADA_50 | 93 | 94 | [-22, 181] | [-22, 182] |
| F4_VA_EQUILIBRADO_Resto_del_mundo_0 | -63 | -59 |  |  |
| F4_VA_España_EDAD_0 | -87 | -88 | [-142, -82] | [-144, -83] |
| F4_VA_España_EDAD_20 | 97 | 96 | [41, 105] | [39, 104] |
| F4_VA_España_EDAD_30 | 99 | 98 | [31, 121] | [29, 120] |
| F4_VA_España_EDAD_40 | 13 | 12 | [-62, 50] | [-64, 49] |
| F4_VA_HASTA64_Resto_UE_LLEGADA_20 | 34 | 32 |  |  |
| F4_VA_HASTA64_Resto_UE_LLEGADA_30 | 54 | 53 |  |  |
| F4_VA_IMPUT_UE_Resto_UE_30 | 30 | 29 |  |  |
| F4_VA_MITAD_SALIDA_Resto_UE_LLEGADA_20 | 20 | 16 |  |  |
| F4_VA_MITAD_SALIDA_Resto_UE_LLEGADA_30 | 32 | 29 |  |  |
| F4_VA_MITAD_SALIDA_Resto_UE_LLEGADA_40 | 23 | 19 |  |  |
| F4_VA_MITAD_SALIDA_Resto_del_mundo_LLEGADA_20 | -25 | -26 |  |  |
| F4_VA_MITAD_SALIDA_Resto_del_mundo_LLEGADA_40 | -17 | -18 |  |  |
| F4_VA_Resto_UE_LLEGADA_0 | -59 | -59 | [-186, -34] | [-189, -34] |
| F4_VA_Resto_UE_LLEGADA_20 | 10 | 8 | [-16, 121] | [-29, 115] |
| F4_VA_Resto_UE_LLEGADA_30 | 27 | 26 | [-22, 117] | [-34, 112] |
| F4_VA_Resto_UE_LLEGADA_40 | 29 | 27 | [-38, 81] | [-51, 75] |
| F4_VA_Resto_UE_LLEGADA_50 | 4 | 2 | [-95, 33] | [-110, 31] |
| F4_VA_Resto_del_mundo_LLEGADA_0 | -74 | -71 | [-273, -47] | [-271, -43] |
| F4_VA_Resto_del_mundo_LLEGADA_20 | -15 | -15 | [-111, 44] | [-113, 44] |
| F4_VA_Resto_del_mundo_LLEGADA_30 | 6 | 5 | [-98, 52] | [-99, 51] |
| F4_VA_Resto_del_mundo_LLEGADA_40 | 1 | 1 | [-107, 36] | [-109, 36] |
| F4_VA_Resto_del_mundo_LLEGADA_50 | -20 | -20 | [-162, 5] | [-163, 5] |
| F4_VA_SIN_MIN15_Resto_UE_30 | 20 | 18 |  |  |
| F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_20 | 35 | 27 |  |  |
| F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_30 | 30 | 22 |  |  |
| F4_VA_SIN_SALIDA_Resto_UE_LLEGADA_40 | 2 | -8 |  |  |
| F4_VA_SIN_SALIDA_Resto_del_mundo_LLEGADA_20 | -51 | -52 |  |  |
| F4_VA_SIN_SALIDA_Resto_del_mundo_LLEGADA_30 | -41 | -42 |  |  |
| F4_VA_SIN_SALIDA_Resto_del_mundo_LLEGADA_40 | -63 | -64 |  |  |
| F4_VA_SIN_SUELO_Resto_UE_30 | 27 | 26 |  |  |
| F4_VA_SIN_SUELO_Resto_del_mundo_30 | 6 | 5 |  |  |
