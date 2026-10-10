# La Palabra que transforma — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redactar un bosquejo celebratorio de 30 minutos basado en Salmo 19:7-11, con exactamente tres puntos y tres subpuntos por punto.

**Architecture:** Un único archivo Markdown contendrá el mensaje completo. La progresión irá desde la restauración interior, pasando por la dirección cotidiana, hasta el deleite y valor permanente de la Palabra.

**Tech Stack:** Markdown y verificación textual con PowerShell/Ripgrep.

## Global Constraints

- Duración objetivo: 30 minutos.
- Tono predominante: celebratorio.
- Texto base: Salmo 19:7-11.
- Exactamente 3 puntos principales y 3 subpuntos por punto.
- Cada punto termina con una aplicación práctica inclusiva.
- Aplicaciones y llamado final en primera persona plural.
- Sin ilustración personal.
- No inventar versículos ni presentar inferencias como citas directas.
- No generar todavía HTML, DOCX ni PDF.

---

### Task 1: Verificar el fundamento bíblico

**Files:**
- Read: `predicas/LA_IMPORTANCIA_DE_LA_BIBLIA/la_suficiencia_de_las_escrituras_Sugel_Michelen.md`
- Read: `docs/superpowers/specs/2026-07-26-la-palabra-que-transforma-design.md`

**Interfaces:**
- Consumes: Salmo 19:7-11 y el diseño aprobado.
- Produces: referencias y términos bíblicos confirmados para la redacción.

- [ ] **Step 1: Confirmar el contenido de Salmo 19:7-11**

Verificar las seis descripciones de la Palabra y sus efectos:

```text
perfecta → convierte el alma
fiel → hace sabio al sencillo
rectos → alegran el corazón
puro → alumbra los ojos
limpio → permanece para siempre
verdad y justos → advertencia y recompensa
```

- [ ] **Step 2: Limitar el análisis léxico**

Usar solamente los términos que ayuden a predicar el pasaje:

```text
torá — instrucción
néfesh — vida interior / ser entero
```

- [ ] **Step 3: Registrar inferencias como explicación**

No entrecomillar como texto bíblico expresiones tales como «traza nuestro camino» o «es nuestro mayor tesoro»; presentarlas como explicación derivada de Salmo 19:8-10.

### Task 2: Redactar el bosquejo completo

**Files:**
- Create: `predicas/LA_IMPORTANCIA_DE_LA_BIBLIA/la_palabra_que_transforma_bosquejo.md`

**Interfaces:**
- Consumes: estructura y referencias verificadas en Task 1.
- Produces: bosquejo listo para revisión de Misael.

- [ ] **Step 1: Redactar introducción y tesis**

La introducción debe contrastar tener una Biblia con permitir que su Palabra obre en nosotros. Debe cerrar con esta tesis:

```text
David celebra la Palabra de Dios porque restaura nuestro interior,
ilumina nuestro camino y se convierte en nuestro mayor tesoro.
```

- [ ] **Step 2: Desarrollar el punto 1**

```text
1. La Palabra nos restaura — Salmo 19:7
   a. Es perfecta y completa.
   b. Convierte y restaura el alma.
   c. Su testimonio fiel hace sabio al sencillo.
```

Cerrar con una pregunta o desafío inclusivo sobre las áreas interiores que necesitamos exponer a la Palabra.

- [ ] **Step 3: Desarrollar el punto 2**

```text
2. La Palabra nos ilumina — Salmo 19:8
   a. Sus mandamientos trazan un camino recto.
   b. Ese camino alegra el corazón.
   c. Su precepto puro alumbra nuestros ojos.
```

Cerrar celebrando que no necesitamos caminar a oscuras y preguntando qué decisiones debemos someter a la Palabra.

- [ ] **Step 4: Desarrollar el punto 3**

```text
3. La Palabra es nuestro tesoro — Salmo 19:9-11
   a. Es limpia y permanece para siempre.
   b. Sus juicios son verdaderos y justos.
   c. Es más valiosa que el oro y más dulce que la miel.
```

Cerrar confrontando con tono esperanzador qué lugar ocupa la Biblia entre nuestros deseos y prioridades.

- [ ] **Step 5: Redactar conclusión y llamado**

Recapitular los tres movimientos y llamar a la congregación a recibir, abrir, escuchar, creer y obedecer juntos la Palabra. Mantener primera persona plural y evitar órdenes dirigidas desde el predicador hacia la congregación.

### Task 3: Verificar estructura, tono y duración

**Files:**
- Test: `predicas/LA_IMPORTANCIA_DE_LA_BIBLIA/la_palabra_que_transforma_bosquejo.md`

**Interfaces:**
- Consumes: bosquejo completo.
- Produces: versión limpia para revisión previa a cualquier archivo final.

- [ ] **Step 1: Auditar la estructura**

Confirmar manualmente:

```text
1 introducción
3 puntos principales
3 subpuntos en cada punto
3 aplicaciones
1 conclusión
1 llamado final
```

- [ ] **Step 2: Auditar el lenguaje inclusivo**

Run:

```powershell
rg -n 'Dejá|Pedile|Tenés que|Abrí|Leé|Obedecé' predicas/LA_IMPORTANCIA_DE_LA_BIBLIA/la_palabra_que_transforma_bosquejo.md
```

Expected: sin imperativos en segunda persona dirigidos a la congregación.

- [ ] **Step 3: Auditar referencias bíblicas**

Revisar cada cita y distinguir claramente entre texto bíblico, paráfrasis y explicación.

- [ ] **Step 4: Auditar duración**

Mantener el cuerpo del mensaje entre 2.600 y 3.000 palabras para dejar espacio a la lectura bíblica, pausas y oración dentro de los 30 minutos.

