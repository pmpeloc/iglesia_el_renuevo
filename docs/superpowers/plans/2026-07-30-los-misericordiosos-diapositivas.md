# Los misericordiosos — Diapositivas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear 20 diapositivas PNG 16:9 con texto integrado para acompañar la prédica «Bienaventurados los misericordiosos».

**Architecture:** Cada diapositiva se generará como una imagen completa mediante ImageGen, usando como referencia visual la serie «Hambre y sed de justicia». Los resultados aprobados se copiarán a la carpeta final, se normalizarán a 1920 × 1080 px y se verificarán individualmente y como secuencia.

**Tech Stack:** ImageGen integrado, herramientas locales de inspección y normalización de imágenes.

## Global Constraints

- Respetar los cuatro puntos y doce subpuntos del bosquejo existente.
- Entregar 20 archivos PNG en `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/`.
- Resolución final exacta: 1920 × 1080 px.
- Ilustración bíblica editorial cálida, consistente con «Hambre y sed de justicia».
- Paleta crema, naranja intenso, negro y verde.
- Texto enorme, de alto contraste y principalmente a la izquierda.
- Una escena dominante a la derecha.
- Logo `logos/LOGO-EL RENUEVO-R-4.png` pequeño y discreto.
- Una idea por diapositiva; sin párrafos.
- Solo los puntos principales usarán `PUNTO PRINCIPAL` y su número.
- Los subpuntos usarán únicamente `a)`, `b)` o `c)` y nunca `PUNTO 1`, `PUNTO 2`, `PUNTO 3` o `PUNTO 4`.
- No aceptar palabras deformadas, inventadas, cortadas ni errores ortográficos.

---

### Task 1: Generar portada e introducción

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/01_portada.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/02_intro.png`

**Interfaces:**
- Consumes: estilo visual de `predicas/SERIE_LAS_BIENAVENTURANZAS/HAMBRE_Y_SED_DE_JUSTICIA/diapositivas/`.
- Produces: apertura visual que fija la identidad del resto de la serie.

- [ ] **Step 1: Generar la portada**

Texto exacto:

```text
LAS BIENAVENTURANZAS
BIENAVENTURADOS LOS MISERICORDIOSOS
MATEO 5:7
```

Escena: Jesús en un camino de Judea acercándose con compasión a personas heridas y necesitadas; amanecer cálido; composición abierta, esperanzadora y celebratoria.

- [ ] **Step 2: Generar la introducción**

Texto exacto:

```text
LA MISERICORDIA
NO SOLO MIRA.
ACTÚA.
MATEO 5:7
```

Escena: una mano fuerte levantando a otra persona desde el suelo; acción concreta, cercanía y dignidad; entorno bíblico.

- [ ] **Step 3: Validar el bloque**

Comprobar texto exacto, legibilidad, continuidad visual, logo y proporción 16:9. Regenerar cualquier pieza que falle.

- [ ] **Step 4: Normalizar y guardar**

Copiar los resultados aprobados a sus rutas finales y convertirlos a PNG de 1920 × 1080 px sin deformar la composición.

- [ ] **Step 5: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/01_portada.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/02_intro.png'
git commit -m "feat: agregar apertura de los misericordiosos"
```

---

### Task 2: Generar el punto 1

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/03_punto_1.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/04_subpunto_1a.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/05_subpunto_1b.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/06_subpunto_1c.png`

**Interfaces:**
- Consumes: identidad aprobada en las diapositivas 01 y 02.
- Produces: desarrollo visual de la misericordia como compasión activa.

- [ ] **Step 1: Generar el punto principal**

```text
PUNTO PRINCIPAL
1.
AMOR EN
MOVIMIENTO
```

Escena: Jesús avanzando decididamente hacia una persona caída mientras otros observan desde lejos.

- [ ] **Step 2: Generar el subpunto 1a**

```text
a)
COMPASIÓN Y ACCIÓN
EFESIOS 2:1, 4–5
```

Escena: Cristo extendiendo su mano hacia una persona que sale de oscuridad y ruinas hacia la luz.

- [ ] **Step 3: Generar el subpunto 1b**

```text
b)
VESTIDOS DE
MISERICORDIA
COLOSENSES 3:12–13
```

Escena: una persona colocando un manto sobre los hombros de otra que tiene frío; gesto continuo de cuidado.

- [ ] **Step 4: Generar el subpunto 1c**

```text
c)
SIN ENTENDER
LA MISERICORDIA
MATEO 18:23–35
```

Escena: el siervo perdonado sujetando con dureza a su consiervo; contraste visual entre una gran deuda cancelada al fondo y la falta de misericordia en primer plano.

- [ ] **Step 5: Validar, normalizar y guardar**

Revisar las cuatro piezas individualmente, corregir cualquier error de texto y guardar cada PNG a 1920 × 1080 px.

- [ ] **Step 6: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/03_punto_1.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/04_subpunto_1a.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/05_subpunto_1b.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/06_subpunto_1c.png'
git commit -m "feat: agregar punto uno de los misericordiosos"
```

---

### Task 3: Generar el punto 2

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/07_punto_2.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/08_subpunto_2a.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/09_subpunto_2b.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/10_subpunto_2c.png`

**Interfaces:**
- Consumes: identidad aprobada en las diapositivas 01 y 02.
- Produces: desarrollo visual de la dirección que produce la misericordia recibida.

- [ ] **Step 1: Generar el punto principal**

```text
PUNTO PRINCIPAL
2.
HACIA DÓNDE
NOS DIRIGE LA
MISERICORDIA
```

Escena: Cristo guiando a varias personas por un camino hacia alguien que necesita ayuda.

- [ ] **Step 2: Generar el subpunto 2a**

```text
a)
NOS LLEVA
A SERVIR
FILIPENSES 2:3
```

Escena: Jesús lavando los pies de un discípulo; servidores en segundo plano; sin tronos ni gestos triunfalistas.

- [ ] **Step 3: Generar el subpunto 2b**

```text
b)
NOS LLEVA A
IMITAR A DIOS
LUCAS 6:36
```

Escena: el padre abrazando al hijo pródigo mientras Cristo aparece como referencia luminosa y compasiva en la composición.

- [ ] **Step 4: Generar el subpunto 2c**

```text
c)
NOS RECUERDA QUE
FUIMOS PERDONADOS
1 SAMUEL 12:24
```

Escena: una familia o pequeño grupo arrodillado al amanecer, recordando con gratitud la ayuda recibida de Dios.

- [ ] **Step 5: Validar, normalizar y guardar**

Revisar las cuatro piezas individualmente, corregir cualquier error de texto y guardar cada PNG a 1920 × 1080 px.

- [ ] **Step 6: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/07_punto_2.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/08_subpunto_2a.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/09_subpunto_2b.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/10_subpunto_2c.png'
git commit -m "feat: agregar punto dos de los misericordiosos"
```

---

### Task 4: Generar el punto 3

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/11_punto_3.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/12_subpunto_3a.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/13_subpunto_3b.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/14_subpunto_3c.png`

**Interfaces:**
- Consumes: identidad aprobada en las diapositivas 01 y 02.
- Produces: tres ámbitos concretos donde se cultiva la misericordia.

- [ ] **Step 1: Generar el punto principal**

```text
PUNTO PRINCIPAL
3.
CÓMO LA
CULTIVAMOS
```

Escena: manos sembrando y regando una planta de olivo que comienza a crecer en tierra seca.

- [ ] **Step 2: Generar el subpunto 3a**

```text
a)
ESTANDO CON LOS
QUE MALTRATAN
MATEO 5:44
```

Escena: una persona bendiciendo y orando por quienes la hostigan, con postura firme y serena.

- [ ] **Step 3: Generar el subpunto 3b**

```text
b)
ESTANDO CON LOS
QUE SUFREN
1 JUAN 3:17
```

Escena: el buen samaritano atendiendo las heridas del hombre caído junto al camino.

- [ ] **Step 4: Generar el subpunto 3c**

```text
c)
ESTANDO CON LOS
QUE TROPIEZAN
FILIPENSES 1:9–10
```

Escena: Jesús restaurando a Pedro junto al lago; cercanía, verdad y ternura sin condenación.

- [ ] **Step 5: Validar, normalizar y guardar**

Revisar las cuatro piezas individualmente, corregir cualquier error de texto y guardar cada PNG a 1920 × 1080 px.

- [ ] **Step 6: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/11_punto_3.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/12_subpunto_3a.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/13_subpunto_3b.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/14_subpunto_3c.png'
git commit -m "feat: agregar punto tres de los misericordiosos"
```

---

### Task 5: Generar el punto 4

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/15_punto_4.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/16_subpunto_4a.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/17_subpunto_4b.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/18_subpunto_4c.png`

**Interfaces:**
- Consumes: identidad aprobada en las diapositivas 01 y 02.
- Produces: desarrollo visual de la promesa presente, final y personal.

- [ ] **Step 1: Generar el punto principal**

```text
PUNTO PRINCIPAL
4.
LA RECOMPENSA
```

Escena: una persona que sembró misericordia contempla un campo iluminado al amanecer; manos abiertas, esperanza y paz.

- [ ] **Step 2: Generar el subpunto 4a**

```text
a)
UNA PROMESA
PARA HOY
MATEO 6:14–15
```

Escena: dos personas reconciliándose y abrazándose después de un conflicto, con una comunidad cercana celebrando la restauración.

- [ ] **Step 3: Generar el subpunto 4b**

```text
b)
UNA PROMESA
PARA MAÑANA
SANTIAGO 2:13
```

Escena simbólica: la luz de la misericordia vence a la sombra del juicio; una balanza antigua queda bañada en luz cálida.

- [ ] **Step 4: Generar el subpunto 4c**

```text
c)
UNA PROMESA
QUE HACE BIEN
PROVERBIOS 11:17
```

Escena: la misma persona que ayudó a un necesitado camina luego en paz, rodeada de una comunidad restaurada.

- [ ] **Step 5: Validar, normalizar y guardar**

Revisar las cuatro piezas individualmente, corregir cualquier error de texto y guardar cada PNG a 1920 × 1080 px.

- [ ] **Step 6: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/15_punto_4.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/16_subpunto_4a.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/17_subpunto_4b.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/18_subpunto_4c.png'
git commit -m "feat: agregar punto cuatro de los misericordiosos"
```

---

### Task 6: Generar conclusión y llamado

**Files:**
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/19_conclusion.png`
- Create: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/20_llamado_final.png`

**Interfaces:**
- Consumes: narrativa visual completa de las diapositivas 01 a 18.
- Produces: cierre celebratorio y aplicación final.

- [ ] **Step 1: Generar la conclusión**

```text
CONCLUSIÓN
NO LLEGAMOS MOSTRANDO
QUE FUIMOS JUSTOS.
LLEGAMOS CELEBRANDO
QUE FUIMOS PERDONADOS.
MATEO 5:7
```

Escena: Jesús rodeado por personas restauradas que celebran juntas al atardecer; alegría reverente, no espectáculo.

- [ ] **Step 2: Generar el llamado final**

```text
LLAMADO FINAL
¿A QUIÉN PODEMOS
MOSTRARLE HOY
LA MISERICORDIA
QUE YA RECIBIMOS?
```

Escena: una persona extendiendo la mano a otra en primer plano, mientras una comunidad se dispone a servir al fondo.

- [ ] **Step 3: Validar, normalizar y guardar**

Revisar ambas piezas individualmente, corregir cualquier error de texto y guardar cada PNG a 1920 × 1080 px.

- [ ] **Step 4: Commit**

```powershell
git add -- 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/19_conclusion.png' 'predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/20_llamado_final.png'
git commit -m "feat: cerrar diapositivas de los misericordiosos"
```

---

### Task 7: Verificación integral

**Files:**
- Inspect: `predicas/SERIE_LAS_BIENAVENTURANZAS/LOS_MISERICORDIOSOS/diapositivas/*.png`

**Interfaces:**
- Consumes: las 20 imágenes finales.
- Produces: secuencia lista para proyectar.

- [ ] **Step 1: Verificar cantidad, nombres y dimensiones**

Comprobar que existan exactamente 20 archivos numerados del `01` al `20` y que todos midan 1920 × 1080 px.

- [ ] **Step 2: Revisar cada diapositiva a tamaño completo**

Verificar texto, ortografía, cortes, contraste, escena, logo y legibilidad. Regenerar cualquier imagen defectuosa.

- [ ] **Step 3: Revisar la secuencia completa**

Crear una vista de conjunto y comprobar coherencia de paleta, jerarquía, ritmo visual y progresión narrativa.

- [ ] **Step 4: Comprobar correspondencia con el bosquejo**

Confirmar que los cuatro puntos y doce subpuntos aparecen una sola vez, en el orden correcto, seguidos de conclusión y llamado.

- [ ] **Step 5: Ejecutar comprobación final del repositorio**

```powershell
git status --short
```

Resultado esperado: solo cambios conocidos del usuario, sin archivos temporales de generación añadidos por error.
