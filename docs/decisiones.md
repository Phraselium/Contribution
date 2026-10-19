# Decisiones de M1

- D1 (fase 0). UE-14 = UE-15 sin España, con Reino Unido dentro en todo el periodo, para que el grupo no cambie de composición con el Brexit. UE-13 = ampliaciones de 2004, 2007 y 2013; «otros de Europa» incluye Turquía, Rusia, Ucrania, Balcanes no UE, Suiza, Noruega e Islandia.
- D2 (fase 0). Magreb = Marruecos, Argelia, Túnez, Libia, Mauritania y Sáhara Occidental; Egipto va a «resto de África».
- D3 (fase 0). Asia incluye Oriente Próximo y Cáucaso; «resto» = América del Norte, Oceanía y apátridas o no consta.
- D4 (fase 0). La rama de trabajo es claude/m1-contribucion-origen; el hook solo permite push a ella y a la etiqueta prereg-m1.
- D5 (fase 0, parada D «guarda que no bloquea»). Esta sesión arrancó en /home/user y no carga .claude/settings.json de M1, así que el hook no se aplica a los comandos del orquestador en esta sesión (se aplica al abrir el repositorio como proyecto). El autor decidió seguir con defensa en profundidad: las puertas críticas se comprueban también dentro del código (fuentes.descargar rechaza dominios no públicos; fase.py y cada f5_* exigen prereg-m1; check.py verifica checksums de crudos, cifras, lenguaje causal, supresión y publicación generada). Los 49 tests de tests/test_guardas.py demuestran que el hook bloquea.
