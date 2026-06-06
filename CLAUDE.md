# Contexto: Iglesia El Renuevo — MCyM

Este repositorio documenta todo el trabajo ministerial, técnico y creativo de **Misael Peloc** en la **Iglesia El Renuevo**, perteneciente al **Movimiento Cristiano y Misionero (MCyM)**. Está diseñado para que Claude tenga contexto completo al comenzar cualquier conversación, sin necesidad de re-explicar lo que ya se trabajó.

---

## 1. Quién soy y dónde estoy

- **Nombre**: Misael
- **Rol**: Pastor/Líder en Iglesia El Renuevo
- **Organización**: Movimiento Cristiano y Misionero (MCyM) — presente en Argentina, América Latina y Europa
- **Ubicación**: San Salvador de Jujuy, Argentina (NOA — Noroeste argentino)
- **Moneda de referencia**: Pesos argentinos (ARS)

---

## 2. La Iglesia — Contexto general

- **Nombre**: Iglesia El Renuevo
- **Organización paraguas**: Movimiento Cristiano y Misionero (MCyM) — miles de iglesias en América y Europa
- **Grupos ministeriales activos**:
  - Congregación general
  - Servidores / colaboradores (tiene reunión propia: "Reunión de Servidores")
  - Jóvenes
  - Adolescentes
- **Hebrón**: Otro local/iglesia de la organización MCyM con auditorio propio. Se trabajaron documentos para ese espacio (sillas para auditorio, programa de sostenimiento).

---

## 3. Infraestructura técnica del templo

### Audio / Video
- **Iluminación**: Consola DMX PLS Litúrgia 192
- **Proyectores**: Dos proyectores conectados simultáneamente por WiFi (se investigó cómo conectarlos)
- **Streaming**: La iglesia tiene capacidad de transmisión en vivo
- **Instrumento**: Batería Okto A Carlsbro (se investigaron conexiones externas)
- **Banda**: Usa separador de instrumentos con control de volumen independiente

### Obra / infraestructura
- **Proyecto de aislamiento acústico del templo** (activo a mayo 2025):
  - Paredes: ~240 m² — sistema trasdosado (lámina asfáltica + lana de roca 70 kg/m³ + estructura metálica + doble placa cartón yeso + caucho 2mm)
  - Techo: ~200 m² — falso techo con silent blocks
  - Costo estimado materiales solo paredes: $6.180.000 – $7.500.000 ARS
  - Costo total con mano de obra: $21.500.000 – $32.500.000 ARS
  - Nota: Los materiales en Jujuy son 15–25% más caros que en Buenos Aires por flete

---

## 4. Trabajo de predicación — Formato y preferencias

### 4.1 Estructura estándar del bosquejo

Misael usa un formato fijo para sus prédicas, desarrollado iterativamente con Claude. Siempre respetar este esquema:

```
Introducción
Punto 1
  a) Título | Versículo/s | Desarrollo
  b) Título | Versículo/s | Desarrollo
  c) Título | Versículo/s | Desarrollo
  → Aplicación (pregunta o desafío directo a la congregación)
Punto 2
  a/b/c (igual estructura)
  → Aplicación
Punto 3
  a/b/c (igual estructura)
  → Aplicación
Conclusión
Llamado Final
```

**Reglas estrictas**:
- Exactamente **3 puntos**. No más, no menos — "más de 3 confunde a la congregación"
- Cada punto: exactamente **3 subpuntos** ordenados en progresión lógica
- Los subpuntos deben llevar uno al siguiente hasta alcanzar el resultado del punto
- Títulos de puntos: **cortos y directos**
- El desarrollo de cada subpunto: **concreto y específico**, nunca genérico ni abstracto
- Cada punto cierra con **aplicación práctica**: pregunta directa o desafío a la congregación

### 4.2 Preguntas que Claude debe hacer ANTES de armar un bosquejo

1. ¿Cuánto tiempo tenés para el mensaje? (20-25 / 30-35 / 40-45 / más de 45 min)
2. ¿Qué tono querés que predomine? (Desafiante · Reflexivo · Celebratorio · Equilibrado)
3. ¿Hay algún momento personal o ilustración que quieras incluir?

### 4.3 Profundidad exegética

Misael valora y usa:
- **Análisis de palabras griegas** en los pasajes clave (con transliteración y significado en lenguaje simple)
- **Tablas visuales** de contrastes o conceptos para poder leer rápido mientras predica
- Cuando se usan términos griegos, incluir: _término griego (transliteración) — significado concreto_
- **Verificación bíblica estricta**: Misael detectó en una conversación que Claude inventó un versículo (Josué 14:14 parafraseado como cita directa). **Nunca inventar versículos**. Si la idea es una inferencia teológica del texto, decirlo explícitamente.

### 4.4 Formatos de salida para prédicas

**A) HTML personal (para el predicador)**
- Uso: Misael lo lee en su computadora mientras predica. No es para proyectar.
- Diseño: Fondo oscuro, texto blanco, **letras grandes**, alto contraste
- Estructura: Header fijo con botones de navegación por sección (Intro, Punto 1, 2, 3, Conclusión)
- Los títulos de sección deben aparecer en el header para cambiar rápido
- Cajas diferenciadas por color: versículos en rojo, aplicaciones en verde, preguntas en dorado

**B) DOCX/PDF "apunte" para la congregación** ← FORMATO FIJO, SIEMPRE IGUAL

Este formato se usa para TODAS las reuniones (generales, jóvenes, adolescentes, servidores). Sin excepción. El día de la reunión o el tipo de audiencia NO cambia el formato — solo cambia el contenido.

**Calendario de reuniones de referencia:**
| Día | Reunión |
|---|---|
| Martes | Reunión de Oración |
| Jueves | Reunión General (énfasis en líderes y colaboradores) |
| Sábado tarde | Reunión de Adolescentes |
| Sábado noche | Reunión de Jóvenes |
| Domingo | Reunión General (congregación completa) |

**Especificaciones del documento:**
- Tamaño: **Exactamente 2 páginas**, orientación vertical, tamaño carta o A4
- Fuente de títulos/cajas: **Montserrat** (SemiBold para cabecera, regular para el versículo)
- Fuente de cuerpo: Arial o sans-serif estándar, ~13pt
- Formato de entrega final: **DOCX** (que el usuario puede imprimir o convertir a PDF)

**Estructura visual — en este orden exacto:**

```
┌──────────────────────────────────────────────────┐
│ [HEADER DE PÁGINA: título pequeño, esquina sup.  │
│  izquierda, aparece en ambas páginas]            │
├──────────────────────────────────────────────────┤
│ ██████████████████████████████████████████████  │  ← BARRA NEGRA, ancho completo
│  TÍTULO DEL MENSAJE EN MAYÚSCULAS (blanco)       │    Montserrat SemiBold, ~18pt
├──────────────────────────────────────────────────┤
│ Texto base: LIBRO CAPÍTULO:VERSÍCULO             │  ← "Texto base:" en negrita
├──────────────────────────────────────────────────┤
│ ┌────────────────────────────────────────────┐   │  ← CAJA DEL VERSÍCULO
│ │ "Versículo completo en Montserrat,         │   │    Borde negro, fondo blanco
│ │  centrado, letra grande"                   │   │    Texto en Montserrat ~22pt
│ │                  Referencia SemiBold        │   │    Referencia en Montserrat SemiBold
│ └────────────────────────────────────────────┘   │
├──────────────────────────────────────────────────┤
│   [Introducción] Texto introductorio...          │  ← SIN NÚMERO. Etiqueta con
│                                                  │    highlight negro y texto blanco.
│ 1. [Título Punto 1] Texto del desarrollo...      │  ← PUNTOS CON NÚMEROS (1, 2, 3...)
│    a. Sub-punto con texto explicativo            │    La etiqueta del punto va con
│    b. Sub-punto con texto explicativo            │    highlight negro y texto blanco.
│    c. Sub-punto con texto explicativo            │    Los términos griegos/hebreos van
│       TÉRMINO: definición...                     │    en negrita subrayada + definición
│                                                  │
│ 2. [Título Punto 2] Texto...                     │
│    a. Sub-punto                                  │
│    b. Sub-punto                                  │
│    c. Sub-punto                                  │
│                                                  │
│ 3. [Título Punto 3] Texto...                     │
│    (continúa en página 2 si es necesario)        │
│                                                  │
│   [Conclusión] Texto de cierre... (si aplica)    │  ← SIN NÚMERO. Igual que Introducción.
├──────────────────────────────────────────────────┤
│ Ejemplos de la Biblia: (si aplica)               │  ← SECCIÓN OPCIONAL al final
│  [imagen bíblica]         [imagen bíblica]       │    Imágenes de personajes/escenas
│   Libro X:Y                Libro X:Y             │    con referencia del versículo
├──────────────────────────────────────────────────┤
│                                               1  │  ← NÚMERO DE PÁGINA
└──────────────────────────────────────────────────┘
```

**⚠️ REGLA CRÍTICA DE NUMERACIÓN — leer siempre antes de generar:**

```
Introducción  → SIN número ni letra. Solo etiqueta con highlight negro.
1. Punto 1    → NÚMERO (1, 2, 3...). Etiqueta con highlight negro.
   a. sub     → letra minúscula (a, b, c...)
   b. sub
2. Punto 2
3. Punto 3
Conclusión    → SIN número ni letra. Solo etiqueta con highlight negro (si aplica).
```

Esta estructura permite que los oyentes se ubiquen rápidamente cuando el predicador dice "vamos al punto 2".

**Reglas de formato detalladas:**

- **Barra de título negra**: Rectángulo de relleno negro, ancho total de la página, texto en blanco Montserrat SemiBold. Es el elemento más llamativo visualmente.
- **Caja del versículo**: Rectángulo con borde negro y fondo blanco. El versículo va centrado en Montserrat tamaño grande. La referencia (ej: "Mateo 5:3 NVI") va en Montserrat SemiBold debajo.
- **Introducción y Conclusión**: Sin número. Párrafo con etiqueta en highlight negro + texto blanco, seguido del contenido. Misma sangría que los puntos numerados.
- **Puntos principales (1, 2, 3...)**: Numeración arábiga. La etiqueta/título del punto va con highlight negro y texto blanco, seguida del contenido en la misma línea.
- **Sub-lista (a, b, c...)**: Sangría adicional, letras minúsculas. Los términos clave (ej: palabras griegas) van en **negrita + subrayado**, seguidos de su definición en texto normal.
- **Header de página**: El título del mensaje aparece en la esquina superior izquierda en ambas páginas (tamaño pequeño, discreto).
- **Número de página**: Pie de página, alineado a la derecha.
- **Imágenes bíblicas** (opcional): Si el mensaje lo justifica, al final de la página 2 se pueden incluir 2-3 ilustraciones de personajes o escenas bíblicas relevantes, con la referencia del versículo como pie de imagen.

**REGLA IMPORTANTE — siempre generar DOS archivos:**
Cada vez que se pida un apunte para la congregación, se generan automáticamente sin excepción:
1. `[titulo]_apunte.pdf` → Formato A4 para imprimir (el formato definido arriba)
2. `[titulo]_mobile.pdf` → Formato Liquid Mode para WhatsApp / celular (ver specs abajo)

---

**LIQUID MODE — Versión móvil del apunte**

**Por qué existe**: El PDF A4 es ideal para imprimir, pero cuando se comparte por WhatsApp los asistentes tienen que hacer zoom para leer. La versión Liquid Mode tiene el mismo contenido reformateado para leer en celular sin zoom.

**Especificaciones técnicas:**
- Tamaño de página: **105mm × 190mm** (formato apaisado de celular, aprox. 4" × 7.5")
- Orientación: vertical
- Márgenes: 8mm todos los lados
- Número de páginas: variable (4–6 páginas según el contenido)

**Tipografía escalada para pantalla:**
| Elemento | Formato A4 | Liquid Mode |
|---|---|---|
| Título (barra negra) | Montserrat SemiBold 18pt | Montserrat SemiBold 20pt |
| Versículo (caja) | Montserrat 22pt | Montserrat 18pt |
| Referencia del versículo | Montserrat SemiBold 13pt | Montserrat SemiBold 13pt |
| Texto base (A, B, C…) | Arial 13pt | Arial 14pt |
| Sub-puntos (a, b, c…) | Arial 12pt | Arial 13pt |
| Interlineado | 1.15 | 1.4 (más aireado para pantalla) |

**Estructura visual — igual al A4, adaptada al ancho reducido:**
- La **barra negra de título** ocupa el ancho completo de la página
- La **caja del versículo** con borde negro y fondo blanco, texto centrado
- Las **etiquetas de sección** (A, B, C…) mantienen el highlight negro y texto blanco
- Los **términos en negrita + subrayado** se mantienen igual
- Las imágenes bíblicas (si las hay) se muestran en columna simple, no en grilla

**Lo que cambia respecto al A4:**
- No hay columnas de 2 (todo en columna única)
- El contenido fluye en más páginas (por el texto más grande)
- No se fuerza a entrar en 2 páginas — fluye naturalmente

---

**C) Bosquejo en texto limpio** (para revisión antes de generar el HTML/PDF)
- Se hace primero en texto, Misael lo revisa (a veces con checkboxes para confirmar cada elemento), luego se genera el archivo final

---

## 5. Series y prédicas trabajadas

### Serie: El corazón del servidor
- **Mensaje 2**: "Sirviendo con el ejemplo" — Juan 13:12-15
  - Puntos: (1) El ejemplo que dejó Cristo, (2) El contra-modelo: servicio sin ejemplo, (3) El ejemplo que se multiplica
  - Contra-modelo: Marta, Diótrefes (3 Juan 9-10), discípulos discutiendo quién es el mayor
  - PDF apunte generado

### Mensajes sueltos trabajados
| Título | Texto base | Audiencia | Tono |
|---|---|---|---|
| "Agua inútil" | Apocalipsis 3:14-22 | Reunión de Servidores | Desafiante |
| "El amigo del novio" | Juan 3:25-30 | Reunión General | Reflexivo/Celebratorio |
| "Restaurado para servir" | Juan 21:15-17 · 1 Co 12:7 | — | — |
| "Dios te llamó ¿cómo respondes?" | Mateo 4:18-22 | — | — |
| "Dame este monte" | Josué 14 (Caleb) | — | — |

### Estudio bíblico: Jóvenes/Adolescentes
- **"Recordar a Dios en la juventud"** — Eclesiastés 12:1
  - Formato: Dos caminos comparados visualmente (Camino sin Dios / Camino con Dios), cada uno en tres etapas: Juventud → Vida adulta → Vejez → Resultado final
  - 18 versículos organizados por etapa y camino
  - Preparado para "clase esta noche" — indica que estos estudios son urgentes y frecuentes

---

## 6. Identidad visual — Logos y guía de uso

### 6.1 Iglesia El Renuevo

**Concepto**: Letra "R" con hojas/plantas entrelazadas en la base — evoca renovación y crecimiento.
**Color principal**: Verde lima `#5DBE2C` | Secundario: Negro y blanco
**Ruta**: `logos/` en la raíz del repositorio

| Archivo | Descripción | Cuándo usar |
|---|---|---|
| `LOGO-EL RENUEVO-R-1.png` | R blanca sobre círculo verde | Fondo oscuro, marca de agua en videos, redes sociales |
| `LOGO-EL RENUEVO-R-2.png` | R negra sobre círculo verde | Documentos impresos en color, fondo blanco |
| `LOGO-EL RENUEVO-R-3.png` | R verde sobre círculo negro | Fondos negros, slides oscuros |
| `LOGO-EL RENUEVO-R-4.png` | R verde sin círculo (solo ícono) | Header de apuntes, marca de agua discreta en documentos |
| `LOGO-EL RENUEVO-R-5.png` | R blanca sobre círculo negro (monocromático) | Impresión en blanco y negro |
| `LOGO-EL RENUEVO-R-6.png` | R negra sin círculo (monocromático) | Sellos, documentos formales en B/N |

**Regla de uso**: Para apuntes generales de la congregación usar **R-4** (discreta, sin fondo, solo el ícono verde) en el header o pie. Para material de redes usar **R-1** o **R-3** según el fondo.

---

### 6.2 Red de Jóvenes — "Raíces"

**Concepto**: Huella dactilar con una cruz en el centro (identidad + fe) + tipografía cursiva "Raíces".
**Colores**: Negro `#000000` + Naranja `#E8521A`
**Ruta**: `red_jovenes/logos/`

| Archivo | Descripción | Cuándo usar |
|---|---|---|
| `Principal.png` | Símbolo + "Raíces" cursiva + "RED DE JÓVENES" (vertical) | Portadas, redes sociales, material principal |
| `Horizontal.png` | Símbolo (izq) + nombre (der) con borde rectangular | Banners, encabezados web, presentaciones |
| `Identificador.png` | Solo el símbolo de la huella + cruz (naranja/negro) | Header de apuntes, ícono, marca de agua |
| `Logotipo.png` | Solo texto "Raíces" + "RED DE JÓVENES" sin símbolo | Cuando ya se muestra el ícono por separado |

**Regla de uso**: Para apuntes de Jóvenes usar **Identificador.png** en el header (esquina). Para material de convocatoria usar **Principal.png** o **Horizontal.png**.

---

### 6.3 Guía general de identidad por tipo de documento

| Tipo de documento | Logo a usar |
|---|---|
| Apunte congregación general (domingo/jueves) | `LOGO-EL RENUEVO-R-4.png` — header esquina superior derecha |
| Apunte Reunión de Jóvenes (sábado noche) | `red_jovenes/logos/Identificador.png` — header esquina superior derecha |
| Apunte Reunión de Adolescentes | Sin logo específico por ahora (pendiente logos red_adolescentes) |
| Video redes sociales general | `LOGO-EL RENUEVO-R-1.png` — watermark esquina superior |
| Video redes sociales Jóvenes | `red_jovenes/logos/Identificador.png` — watermark esquina |
| Documentos formales / propuestas | `LOGO-EL RENUEVO-R-2.png` o `R-4.png` — encabezado |
| Presentaciones de diapositivas | Logo según audiencia, esquina inferior derecha |

**Nota para Claude**: Cuando se genere cualquier documento, apunte, video o presentación, incluir siempre el logo correspondiente según esta tabla. Si el usuario no especifica logo, usar el de la iglesia general (R-4) por defecto. Si el contexto es Jóvenes, usar Raíces/Identificador.

---

## 7. Proyecto de software: App de proyección para iglesias

### Estado: En desarrollo / exploración (junio 2025)

**Qué es**: Alternativa a ProPresenter pensada para iglesias de MCyM y hispanohablantes en general. Similar a Reuna Presenter (competidor argentino analizado), pero con más potencial por conocimiento del dominio.

**Stack planeado**:
- Desktop: **Tauri** (Rust + frontend)
- Base de datos local: **SQLite** (fuente de verdad en uso diario)
- Sincronización en la nube: **Supabase** (opción recomendada) o PocketBase
- Sync: Manual PULL/PUSH (botón antes de cerrar o al abrir), no continuo

**Funcionalidades planeadas**:
- Canciones con letras
- Versiones bíblicas
- Temas visuales (themes) con CSS variables en runtime — definidos como objeto TypeScript
- Fondos animados / material audiovisual
- Control remoto, stage display
- Multi-pantalla

**Competidor analizado**:
- **Reuna Presenter** (reunapresenter.com): SaaS web argentino, v1.4 BETA, +200 iglesias, plan free (50 canciones, 1 pantalla), plan pro USD 12/mes. **Problema**: 100% web, depende de internet, 100 canciones es poco para iglesia activa, sin NDI ni video con capas.
- **Estrategia actual**: Usar Reuna en El Renuevo mientras se construye la propia solución

**Consideraciones de arquitectura**:
- Si es solo para El Renuevo: Supabase free tier alcanza
- Si es multi-iglesia (MCyM): necesita multi-tenancy, arquitectura más compleja
- Material audiovisual (videos de fondo) puede llegar a 2–10 GB → define el costo de cloud storage

---

## 8. Proyecto: Programa de sostenimiento / donaciones

- **Hebrón** tiene un programa de donaciones ("Programa de Sostenimiento") documentado en DOCX
- Se trabajó un documento sobre **sillas para el auditorio Hebrón**:
  - Referencia técnica: Bertolini Essentials V2 (sin mencionar la marca en el documento final — se llama "Sillas para Auditorio Hebrón")
  - Specs: altura 89cm, cojín 10cm espuma 900 g/m³, apilado x8, marco acero reciclable, vida útil 15-20 años
  - Formato: tipo catálogo con imágenes, tablas comparativas, diseño consistente con el doc de sostenimiento

---

## 9. Preferencias de trabajo con Claude

### Idioma
- **Siempre en español**. Claude responde en español con Misael.

### Estilo de respuesta
- **Directo y concreto**. Nada genérico ni abstracto.
- Misael hace revisiones iterativas: primero revisa en texto, luego pide el archivo final.
- Le gustan los **checkboxes** para revisar borradores y confirmar qué conservar.
- Aprecia cuando Claude **hace preguntas antes de trabajar** (especialmente en bosquejos).

### Verificación bíblica
- **Crítico**: Nunca inventar versículos ni parafrasear como si fuera cita directa.
- Si es una inferencia teológica, decirlo: "Esto no está en el texto en esas palabras, pero se infiere de..."
- Misael siempre verifica en su Biblia antes de predicar — lo espera de Claude también.

### Formatos preferidos de entrega
| Propósito | Formato |
|---|---|
| Bosquejo para predicar (personal) | HTML (fondo oscuro, letras grandes, nav fija) |
| Apunte para congregación | **2 archivos**: PDF A4 para imprimir + PDF Liquid Mode para WhatsApp |
| Documentos formales / propuestas | DOCX |
| Presupuestos / tablas de datos | DOCX o tabla en conversación |
| Estudio bíblico visual | HTML interactivo o tabla comparativa |

### Dónde guardar los archivos
- Carpeta del proyecto: `C:\Users\pmpel\projects\iglesia_el_renuevo\`

---

## 10. Vocabulario y términos usados

| Término | Significado |
|---|---|
| MCyM | Movimiento Cristiano y Misionero (organización de la iglesia) |
| El Renuevo | Nombre de la iglesia local de Misael en Jujuy |
| Hebrón | Otro local/iglesia de MCyM con auditorio (ciudad no confirmada) |
| Bosquejo | Outline/esquema de una prédica |
| Prédica | Sermón |
| Apunte | Handout de 2 páginas para que la congregación siga el mensaje |
| Servidores | Colaboradores/voluntarios del ministerio |
| Presbíteros | Líderes/ancianos de la iglesia a quienes se presentan propuestas |
| Reunión de Servidores | Reunión interna para el equipo de colaboradores |
| Reunión General | Servicio para toda la congregación |
| Reunión de Oración | Martes — énfasis en intercesión |
| Reunión de Adolescentes | Sábado tarde |
| Reunión de Jóvenes | Sábado noche |

---

## 11. Estado de proyectos activos (junio 2025)

| Proyecto | Estado | Notas |
|---|---|---|
| App de proyección (estilo ProPresenter) | En exploración/desarrollo | Stack: Tauri + SQLite + Supabase. Usando Reuna como puente mientras tanto |
| Aislamiento acústico del templo | En planificación | Presupuestando materiales, evaluando si hay hermanos con oficio construcción |
| Programa de donaciones Hebrón | Documentado | DOCX de sostenimiento + DOCX de sillas |
| Serie "El corazón del servidor" | En curso | Al menos 2 mensajes trabajados. Tiene formato PDF apunte. |
| Estudios para jóvenes/adolescentes | Recurrente | Uso de formatos visuales comparativos |

---

_Última actualización: junio 2025. Generado a partir del historial de conversaciones en Claude web._
