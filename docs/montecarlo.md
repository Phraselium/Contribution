# Validación Monte Carlo de las herramientas econométricas (fase 5)

Generado por `src/m1/montecarlo/informe.py` a partir de `output/montecarlo/<herramienta>/resultado.json`. Solo datos simulados (nunca datos reales), SEED=20261019, R = 500 réplicas por diseño. Criterio común: **APTO** si la cobertura del IC95 está en [0,92; 0,98] y el tamaño al 5 % es ≤ 0,08; si no, **NO APTO** con la condición en que falla. Los procesos generadores se declararon en el docstring de cada script antes de simular. Error MC de una cobertura de 0,95 con R = 500: ≈ 0,01.

## Resumen de veredictos

| herramienta | veredicto | uso en M1 |
|---|---|---|
| `bhj` | NO APTO | No usar el IC de Wald de bhj como inferencia principal con la concentración de orígenes de M1. Usar AKM0 (nulo impuesto, invertido para el IC) o, en su defecto, informar bhj junto con 1/HHI y el apalancamiento máximo del shock. Nunca EE convencionales (HC1/CR1 por CCAA o provincia) en shift-share. AKM0 aún no está en econ.py: queda para el modelizador (el cálculo de referencia está en src/m1/montecarlo/bhj.py, función akm0_t2). |
| `wcr_boot` | APTO CON CONDICIÓN | APTO con G = 52, y con G = 17 si el regresor de interés no está dominado por pocos clusters de alto apalancamiento; con 17 clusters asimétricos sobre-rechaza (≈ 0,10), aunque mucho menos que CR1 con t(G-1). Informar siempre el apalancamiento por cluster; con G = 17 asimétrico, tratar p entre 0,05 y 0,10 como no significativo. Usar B = 9999 en la aplicación. |
| `iv2sls` | APTO CON CONDICIÓN | Wald (iv2sls con CR1 y t(G-1)) solo con F efectivo ≥ 10; con F < 10 informar el conjunto AR (puede ser no acotado). f_efectivo coincide con el F de primera etapa de iv2sls. AR con CR1 y 52 clusters heterogéneos queda al límite (≈ 0,92): para confirmatorias, complementar con wild bootstrap del test AR. |
| `conley` | NO APTO | NO APTO con 52 unidades y radio 200 km: infraestima la varianza (≈ 0,6-0,85 de la verdadera) y cubre 0,81-0,87, a veces peor que HC1. Con datos provinciales, usar clusters espaciales (CCAA) con wcr_boot o un núcleo más ancho con sensibilidad, y declarar la limitación. |
| `oaxaca` | APTO | APTO. Declarar que la referencia es la regresión agrupada con indicador de grupo: con rendimientos distintos por grupo no coincide con la descomposición con estructura de B (es otra cantidad, no un sesgo). Corregido: ahora añade constante si X no la trae. |
| `dfl` | APTO | APTO para media y cuantiles con logit bien especificado (covariables discretas). Con covariables continuas, comprobar el equilibrio de medias tras reponderar. |



## bhj · shift-share MC2E con EE robustos a la exposición (BHJ 2022)

**DGP**

```text
M1 · Monte Carlo de econ.bhj (MC2E shift-share con EE robustos a la exposición, BHJ 2022) frente a EE convencionales.

DGP (declarado antes de simular; cuotas FIJAS entre réplicas, como en el enfoque de diseño de BHJ/AKM; se redibujan shocks y errores):
- 52 provincias agrupadas en 17 «CCAA» contiguas; cada CCAA tiene uno de K=5 patrones de asentamiento (provincias de patrones
  iguales tienen cuotas parecidas aunque estén en CCAA distintas).
- O orígenes con mezcla nacional m ~ Dirichlet(a·1) (a pequeño: pocos orígenes dominantes); patrón k: m_k ~ Dirichlet(5·O·m);
  provincia l: pi_l ~ Dirichlet(60·m_k); exposición total e_l ~ U(0,04; 0,25); cuotas S_lo = e_l·pi_lo (suman e_l < 1).
- Shocks nacionales g_o ~ N(0, 1)/sigma_S i.i.d. (sigma_S² = media_l sum_o S_lo²: el instrumento z = S·g tiene DE ≈ 1).
- Problema de AKM: errores con componente de origen no observado nu_o: eps_l = sum_o S_lo nu_o + eta_l (provincias con cuotas
  parecidas tienen errores correlacionados); endogeneidad: mu_o = rho·nu_o + ..., v_l = rho·eta_l + ..., rho = 0,5.
- x_l = 2·z_l + sum_o S_lo mu_o + v_l (primera etapa fuerte); y_l = beta·x_l + eps_l (+ constante y e_l, que entran en los
  controles W = [1, e_l]).
- Apilado: 3 periodos con las mismas cuotas, shocks g_ot y nu_ot i.i.d. por (origen, periodo); W = efectos de periodo y periodo × e_l.
- beta = 0 (nulo) y beta = 0,5 (no nulo). Referencia adicional: test AKM0 (residuos con el nulo impuesto, al nivel del shock).
  Se compara el IC95 normal de bhj con MC2E de ubicación (econ.iv2sls) con EE robustos HC1 (normal) y agrupados CR1 por CCAA
  (corte) o por provincia (apilado), con t(G-1).
```

**Resultados**

| diseño | β | 1/HHI | F shock | sesgo | RMSE | cob. bhj | rech. β=0 bhj | cob. HC1 | rech. HC1 | cob. CR1 | rech. CR1 | cob. AKM0 | rech. AKM0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| corte_O40 | 0.000 | 21.552 | 21.261 | -0.012 | 0.169 | 0.864 | 0.136 | 0.806 | 0.194 | 0.810 | 0.190 | 0.958 | 0.042 |
| corte_O40 | 0.500 | 21.552 | 21.122 | -0.011 | 0.172 | 0.864 | 0.818 | 0.770 | 0.892 | 0.786 | 0.894 | 0.940 | 0.440 |
| corte_O20_10efectivos | 0.000 | 8.540 | 14.520 | -0.044 | 0.381 | 0.776 | 0.224 | 0.690 | 0.310 | 0.726 | 0.274 | 0.984 | 0.016 |
| corte_O20_10efectivos | 0.500 | 8.540 | 16.015 | -0.037 | 0.279 | 0.796 | 0.682 | 0.738 | 0.780 | 0.758 | 0.772 | 0.980 | 0.182 |
| apilado_3periodos_O40 | 0.000 | 70.357 | 56.877 | 0.002 | 0.094 | 0.918 | 0.082 | 0.790 | 0.210 | 0.788 | 0.212 | 0.952 | 0.048 |
| apilado_3periodos_O40 | 0.500 | 70.357 | 58.183 | -0.004 | 0.093 | 0.924 | 0.986 | 0.814 | 0.998 | 0.806 | 0.998 | 0.946 | 0.956 |

CR1 agrupado por CCAA (G = 17) en el corte y por provincia (G = 52) en el apilado. «rech. β=0» es el tamaño con β = 0 y la potencia con β = 0,5. bhj y iv2sls dan el mismo coeficiente (dif. máx. 1.7e-13).


**Veredicto: NO APTO.** corte_O40 (1/HHI≈22): cobertura bhj 0.864/0.864, tamaño 0.136 → falla; corte_O20_10efectivos (1/HHI≈9): cobertura bhj 0.776/0.796, tamaño 0.224 → falla; apilado_3periodos_O40 (1/HHI≈70): cobertura bhj 0.918/0.924, tamaño 0.082 → falla. El EE de bhj (tipo HC0 al nivel del shock) infra-cubre cuando pocos orígenes concentran la exposición (apalancamiento alto); solo se acerca al umbral con ~70 orígenes efectivos. EE convencionales HC1/CR1 sobre-rechazan en todos los diseños. AKM0 (nulo impuesto, referencia calculada en el MC) cumple en: corte_O40 β=0.0, corte_O40 β=0.5, corte_O20_10efectivos β=0.5, apilado_3periodos_O40 β=0.0, apilado_3periodos_O40 β=0.5.


*Uso:* No usar el IC de Wald de bhj como inferencia principal con la concentración de orígenes de M1. Usar AKM0 (nulo impuesto, invertido para el IC) o, en su defecto, informar bhj junto con 1/HHI y el apalancamiento máximo del shock. Nunca EE convencionales (HC1/CR1 por CCAA o provincia) en shift-share. AKM0 aún no está en econ.py: queda para el modelizador (el cálculo de referencia está en src/m1/montecarlo/bhj.py, función akm0_t2).


Script: `src/m1/montecarlo/bhj.py`; salida: `output/montecarlo/bhj/resultado.json` (3.9 s).


## wcr_boot · wild cluster bootstrap restringido (Webb)

**DGP**

```text
M1 · Monte Carlo de econ.wcr_boot (wild cluster bootstrap restringido, pesos de Webb) frente a CR1 con t(G-1).

DGP (declarado antes de simular; se redibuja todo en cada réplica salvo el número de clusters):
- G ∈ {17, 52} clusters (CCAA, provincias) de tamaños muy heterogéneos: N_g = redondeo(exp(N(log 40, 1))) acotado a [5, 400].
- Tratamiento al nivel del cluster: «asimetrico» (pocos clusters de alto apalancamiento) x_g = (exp(N(0,1)) - e^{1/2}) / DE, o
  «normal» x_g ~ N(0,1); x_ig = x_g + 0,3·N(0,1); un control individual c_ig ~ N(0,1).
- Error u_ig = a_g + e_ig con a_g ~ N(0, 1)·(0,5 + |x_g|) (heterocedasticidad ligada al apalancamiento) y e_ig ~ N(0, 1).
- y_ig = 1 + beta·x_ig + 0,5·c_ig + u_ig; beta = 0 (tamaño) y beta = 0,5 (potencia). H0: beta = 0 al 5 %.
- wcr_boot con B = 399 dentro del MC (con B = 9999 en la aplicación) y semilla distinta por réplica (SEED + r).
```

**Resultados**

| diseño | β | sesgo MCO | RMSE | rech. WCR (Webb) | rech. CR1 t(G-1) | cob. CR1 |
|---|---|---|---|---|---|---|
| G17_asimetrico | 0.000 | -0.025 | 0.659 | 0.102 | 0.354 | 0.646 |
| G17_asimetrico | 0.500 | -0.045 | 0.680 | 0.210 | 0.466 | 0.660 |
| G17_normal | 0.000 | -0.000 | 0.560 | 0.062 | 0.190 | 0.810 |
| G17_normal | 0.500 | 0.034 | 0.567 | 0.178 | 0.364 | 0.812 |
| G52_asimetrico | 0.000 | 0.000 | 0.553 | 0.074 | 0.274 | 0.726 |
| G52_asimetrico | 0.500 | -0.027 | 0.579 | 0.272 | 0.464 | 0.696 |
| G52_normal | 0.000 | -0.003 | 0.376 | 0.036 | 0.100 | 0.900 |
| G52_normal | 0.500 | -0.018 | 0.368 | 0.304 | 0.420 | 0.894 |

«rech.» es el tamaño con β = 0 y la potencia con β = 0,5 (B = 399 en el MC; EE MC del tamaño ≈ 0,01).


**Veredicto: APTO CON CONDICIÓN.** G17_asimetrico: tamaño WCR 0.102 (CR1 t(G-1) 0.354) → falla; G17_normal: tamaño WCR 0.062 (CR1 t(G-1) 0.190) → cumple; G52_asimetrico: tamaño WCR 0.074 (CR1 t(G-1) 0.274) → cumple; G52_normal: tamaño WCR 0.036 (CR1 t(G-1) 0.100) → cumple


*Uso:* APTO con G = 52, y con G = 17 si el regresor de interés no está dominado por pocos clusters de alto apalancamiento; con 17 clusters asimétricos sobre-rechaza (≈ 0,10), aunque mucho menos que CR1 con t(G-1). Informar siempre el apalancamiento por cluster; con G = 17 asimétrico, tratar p entre 0,05 y 0,10 como no significativo. Usar B = 9999 en la aplicación.


Script: `src/m1/montecarlo/wcr_boot.py`; salida: `output/montecarlo/wcr_boot/resultado.json` (278.3 s).


## iv2sls + f_efectivo + ar_conjunto · instrumento fuerte y débil

**DGP**

```text
M1 · Monte Carlo de econ.iv2sls + econ.f_efectivo + econ.ar_conjunto con instrumento fuerte y débil y 52 clusters.

DGP (declarado antes de simular; todo se redibuja en cada réplica):
- G = 52 clusters (provincias) con N_g ~ U{10, …, 60} observaciones.
- Instrumento z_ig = z_g + 0,5·N(0,1), z_g ~ N(0,1); control c_ig ~ N(0,1).
- Errores con componente de cluster y endogeneidad fuerte: (u, v) = (a_g, b_g) + (e_ig, f_ig), cada par N(0, [[1, 0,8], [0,8, 1]]).
- x = pi·z + 0,3·c + v; y = beta·x + 0,3·c + u; beta = 1 (cobertura y tamaño en el valor verdadero; potencia contra beta = 0).
- pi calibrado para un F efectivo (= F de Wald agrupado de la primera etapa) mediano ≈ 3, 10 y 50.
- Wald: IC b ± t(G-1)·EE CR1. AR: conjunto de econ.ar_conjunto (test agrupado con t(G-1)²); cobertura = el valor verdadero
  no se rechaza (rejilla de un punto); forma del conjunto (acotado/convexo/longitud) con una rejilla de 201 puntos en beta ± 5.
```

**Resultados**

| diseño | F efectivo (mediana) | sesgo MC2E (media) | sesgo (mediana) | cob. Wald | rech. β=0 Wald | cob. AR | rech. β=0 AR | AR acotado | AR convexo |
|---|---|---|---|---|---|---|---|---|---|
| F_objetivo_3 | 3.672 | -0.093 | 0.053 | 0.890 | 0.516 | 0.926 | 0.192 | 0.376 | 0.678 |
| F_objetivo_10 | 11.057 | -0.179 | 0.006 | 0.932 | 0.682 | 0.906 | 0.418 | 0.762 | 0.956 |
| F_objetivo_50 | 61.261 | -0.013 | 0.007 | 0.928 | 0.986 | 0.936 | 0.950 | 1.000 | 1.000 |

Cobertura AR agregada de los tres diseños: 0.923 ± 0.007. «rech. β=0» es potencia (β = 1). f_efectivo = F_primera de iv2sls (dif. máx. 2.8e-14).


**Veredicto: APTO CON CONDICIÓN.** Wald (iv2sls CR1): F≈3.7 cobertura 0.890; F≈11.1 cobertura 0.932; F≈61.3 cobertura 0.928. AR (ar_conjunto): F≈3.7 cobertura 0.926; F≈11.1 cobertura 0.906; F≈61.3 cobertura 0.936 (agregada 0.923 ± 0.007, idéntica en distribución en los tres diseños). Wald solo cumple con F efectivo ≥ 11; con F menor, usar el conjunto AR.


*Uso:* Wald (iv2sls con CR1 y t(G-1)) solo con F efectivo ≥ 10; con F < 10 informar el conjunto AR (puede ser no acotado). f_efectivo coincide con el F de primera etapa de iv2sls. AR con CR1 y 52 clusters heterogéneos queda al límite (≈ 0,92): para confirmatorias, complementar con wild bootstrap del test AR.


Script: `src/m1/montecarlo/iv2sls.py`; salida: `output/montecarlo/iv2sls/resultado.json` (94.4 s).


## conley · EE con dependencia espacial (núcleo uniforme, 200 km)

**DGP**

```text
M1 · Monte Carlo de econ.conley (MCO con varianza de Conley, núcleo uniforme, radio 200 km) frente a HC1.

DGP (declarado antes de simular):
- 52 puntos FIJOS (dibujados una vez) uniformes en el rectángulo lat 36-43,8, lon -9,3 a 3,3 (escala de las provincias).
- Regresor y error: campos gaussianos independientes con covarianza exp(-d/lambda) (d en km, gran círculo) más un 20 % de ruido
  propio (pepita): x = 0,9·F1 + 0,45·N(0,1), e = 0,9·F2 + 0,45·N(0,1). lambda ∈ {50, 100, 200} km.
- y = 1 + beta·x + e; beta = 0 (tamaño) y beta = 0,5 (potencia). IC95 normal b ± 1,96·EE.
```

**Resultados**

| λ (km) | β | sesgo | RMSE | cob. Conley | rech. β=0 Conley | cob. HC1 | rech. β=0 HC1 | V Conley / V MC | V HC1 / V MC | V<0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 50 | 0.000 | -0.004 | 0.153 | 0.870 | 0.128 | 0.922 | 0.078 | 0.815 | 0.861 | 0.002 |
| 50 | 0.500 | -0.000 | 0.144 | 0.872 | 0.922 | 0.916 | 0.934 | 0.855 | 0.909 | 0.008 |
| 100 | 0.000 | -0.002 | 0.172 | 0.828 | 0.168 | 0.846 | 0.154 | 0.682 | 0.647 | 0.004 |
| 100 | 0.500 | -0.003 | 0.162 | 0.862 | 0.898 | 0.890 | 0.918 | 0.797 | 0.740 | 0.006 |
| 200 | 0.000 | 0.019 | 0.202 | 0.808 | 0.190 | 0.782 | 0.218 | 0.617 | 0.487 | 0.002 |
| 200 | 0.500 | 0.009 | 0.190 | 0.836 | 0.858 | 0.814 | 0.912 | 0.672 | 0.527 | 0.002 |

Vecinos medios dentro de 200 km: 5.3.


**Veredicto: NO APTO.** lambda=50 km, beta=0.0: cobertura Conley 0.870 (HC1 0.922); lambda=50 km, beta=0.5: cobertura Conley 0.872 (HC1 0.916); lambda=100 km, beta=0.0: cobertura Conley 0.828 (HC1 0.846); lambda=100 km, beta=0.5: cobertura Conley 0.862 (HC1 0.890); lambda=200 km, beta=0.0: cobertura Conley 0.808 (HC1 0.782); lambda=200 km, beta=0.5: cobertura Conley 0.836 (HC1 0.814). Con 52 puntos y ~5 vecinos por radio el estimador infraestima la varianza (residuos estimados y núcleo truncado): no cumple en ningún diseño.


*Uso:* NO APTO con 52 unidades y radio 200 km: infraestima la varianza (≈ 0,6-0,85 de la verdadera) y cubre 0,81-0,87, a veces peor que HC1. Con datos provinciales, usar clusters espaciales (CCAA) con wcr_boot o un núcleo más ancho con sensibilidad, y declarar la limitación.


Script: `src/m1/montecarlo/conley.py`; salida: `output/montecarlo/conley/resultado.json` (1.0 s).


## oaxaca · Oaxaca-Blinder con coeficientes agrupados

**DGP**

```text
M1 · Monte Carlo de econ.oaxaca y econ.dfl: identidades contables exactas e insesgadez de la parte explicada (composición).

DGP (declarado antes de simular; composición conocida, todo se redibuja en cada réplica):
- n = 4000 con 30 % del grupo A y 70 % del grupo B (grupos genéricos; sin atribuir rasgos a ningún colectivo real).
- Covariables discretas independientes dentro de cada grupo: educación (3 niveles), edad (3 tramos), sexo.
  P(educ | A) = (0,45; 0,35; 0,20), P(educ | B) = (0,25; 0,45; 0,30); P(edad | A) = (0,50; 0,35; 0,15), P(edad | B) = (0,30; 0,40; 0,30);
  P(mujer | A) = 0,45, P(mujer | B) = 0,50. Con esta estructura el logit con efectos principales de DFL está bien especificado.
- «lineal»: y = 2 + 0,3·e2 + 0,7·e3 + 0,2·a2 + 0,35·a3 − 0,15·mujer − 0,10·A + error, error ~ N(0, (0,4 + 0,2·e3)²).
  Verdad: explicada = (E[x|A] − E[x|B])·b (poblacional); no explicada = −0,10.
- «lineal_pesos»: igual, pero la muestra sobrerrepresenta educación alta (probabilidad ×2) y se usan pesos 1/probabilidad.
- «heterogeneo»: A tiene la mitad de rendimiento educativo (0,15; 0,35). Verdad de composición con estructura de B:
  (E[x|A] − E[x|B])·b_B. DFL debe ser insesgado; Oaxaca con coeficientes agrupados estima otra cantidad (se informa, no se exige).
- Cuantiles de DFL: verdad por simulación grande (2·10⁶) de la distribución contrafactual (composición de A, estructura de B).
- Criterio (las herramientas no dan EE, así que no hay cobertura): identidades con error < 1e-10 y |sesgo| < max(3·EE_MC; 2 % de |verdad|).
```

**Resultados**

| diseño | verdad explicada | sesgo explicada | RMSE | sesgo no explicada | error máx. identidades | dif. sin/con constante |
|---|---|---|---|---|---|---|
| lineal | -0.155 | -0.000 | 0.011 | 0.000 | 0.0e+00 | 3.4e-15 |
| lineal_pesos | -0.155 | -0.000 | 0.011 | 0.000 | 0.0e+00 | 2.8e-15 |
| heterogeneo | -0.155 | 0.017 | 0.021 | -0.018 | 0.0e+00 | 2.8e-15 |


**Veredicto: APTO.** identidades exactas (error máx. 0.0e+00); parte explicada lineal: sesgo -0.0001 (verdad -0.1550); lineal_pesos: sesgo -0.0002 (verdad -0.1550); heterogeneo: sesgo +0.0172 (verdad -0.1550). Con rendimientos heterogéneos la referencia agrupada no coincide con la de B (sesgo frente a b_B +0.0172): no es error, es otra referencia; declararla. Sin constante en X ya no hay sesgo (corrección en econ.oaxaca; dif. máx. con/sin constante 3.4e-15).


*Uso:* APTO. Declarar que la referencia es la regresión agrupada con indicador de grupo: con rendimientos distintos por grupo no coincide con la descomposición con estructura de B (es otra cantidad, no un sesgo). Corregido: ahora añade constante si X no la trae.


Script: `src/m1/montecarlo/oaxaca_dfl.py`; salida: `output/montecarlo/oaxaca/resultado.json` (24.5 s).


## dfl · reponderación DiNardo-Fortin-Lemieux

**DGP**

```text
M1 · Monte Carlo de econ.oaxaca y econ.dfl: identidades contables exactas e insesgadez de la parte explicada (composición).

DGP (declarado antes de simular; composición conocida, todo se redibuja en cada réplica):
- n = 4000 con 30 % del grupo A y 70 % del grupo B (grupos genéricos; sin atribuir rasgos a ningún colectivo real).
- Covariables discretas independientes dentro de cada grupo: educación (3 niveles), edad (3 tramos), sexo.
  P(educ | A) = (0,45; 0,35; 0,20), P(educ | B) = (0,25; 0,45; 0,30); P(edad | A) = (0,50; 0,35; 0,15), P(edad | B) = (0,30; 0,40; 0,30);
  P(mujer | A) = 0,45, P(mujer | B) = 0,50. Con esta estructura el logit con efectos principales de DFL está bien especificado.
- «lineal»: y = 2 + 0,3·e2 + 0,7·e3 + 0,2·a2 + 0,35·a3 − 0,15·mujer − 0,10·A + error, error ~ N(0, (0,4 + 0,2·e3)²).
  Verdad: explicada = (E[x|A] − E[x|B])·b (poblacional); no explicada = −0,10.
- «lineal_pesos»: igual, pero la muestra sobrerrepresenta educación alta (probabilidad ×2) y se usan pesos 1/probabilidad.
- «heterogeneo»: A tiene la mitad de rendimiento educativo (0,15; 0,35). Verdad de composición con estructura de B:
  (E[x|A] − E[x|B])·b_B. DFL debe ser insesgado; Oaxaca con coeficientes agrupados estima otra cantidad (se informa, no se exige).
- Cuantiles de DFL: verdad por simulación grande (2·10⁶) de la distribución contrafactual (composición de A, estructura de B).
- Criterio (las herramientas no dan EE, así que no hay cobertura): identidades con error < 1e-10 y |sesgo| < max(3·EE_MC; 2 % de |verdad|).
```

**Resultados**

| diseño | sesgo media | RMSE media | sesgo q0.1 | sesgo q0.25 | sesgo q0.5 | sesgo q0.75 | sesgo q0.9 | error máx. identidades |
|---|---|---|---|---|---|---|---|---|
| lineal | -0.000 | 0.012 | 0.002 | -0.000 | -0.000 | 0.000 | -0.000 | 0.0e+00 |
| lineal_pesos | -0.000 | 0.012 | -0.002 | -0.000 | -0.000 | 0.000 | 0.001 | 0.0e+00 |
| heterogeneo | 0.000 | 0.013 | 0.001 | -0.000 | 0.001 | 0.002 | 0.002 | 0.0e+00 |


**Veredicto: APTO.** identidades exactas (error máx. 0.0e+00); composición en la media lineal: sesgo -0.0001; lineal_pesos: sesgo -0.0001; heterogeneo: sesgo +0.0000; cuantiles insesgados en todos los diseños. Logit bien especificado por construcción; con covariables continuas o interacciones omitidas hay que validar el logit.


*Uso:* APTO para media y cuantiles con logit bien especificado (covariables discretas). Con covariables continuas, comprobar el equilibrio de medias tras reponderar.


Script: `src/m1/montecarlo/oaxaca_dfl.py`; salida: `output/montecarlo/dfl/resultado.json` (24.5 s).


## Tests y correcciones

- `tests/test_econ.py`: `ols` = statsmodels OLS/WLS con CR1 y HC1; `iv2sls` = linearmodels IV2SLS (coeficientes y EE agrupado). econ aplica G/(G-1)·(n-1)/(n-k), igual que linearmodels con `debiased=True`; con su opción por defecto (`debiased=False`) linearmodels 7.1 no aplica ninguna corrección, de modo que V_econ = V_lm·G/(G-1)·(n-1)/(n-k). No se cambia econ (se mantiene la convención de Stata). También: f_efectivo = F_primera, bhj = MC2E de ubicación con W que incluye la suma de cuotas, e identidades de oaxaca y dfl.

- Corrección en `econ.oaxaca`: si X no traía constante, la regresión agrupada no tenía término independiente y la parte explicada quedaba sesgada (el indicador de grupo hacía de constante solo para A). Ahora se añade una constante cuando X no tiene ninguna columna constante; con constante el resultado no cambia.
