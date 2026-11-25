# Cómo armar el turno del miércoles (Casa de Oración)

Checklist para cada miércoles. Armado después del primer turno (25/11/2026) con lo que se corrigió ese día.

## 1. Formato del turno

- **Para toda la iglesia El Renuevo** (no solo jóvenes). En flyers y guías: "Iglesia El Renuevo", logo R-4.
- **20:30–20:50 · Tiempo libre**: la gente local no llega puntual. Cada uno ora con la guía, piano grabado, nadie dirige. No cuenta dentro de la hora.
- **20:50–21:50 · Turno guiado de 1 hora.** Por ahora, un solo turno por semana.
- Se anuncia como "20:30 a 22:00" (incluye el tiempo libre y el margen).

## 2. Cronograma: tabla corta, estilo Betania

Se entrega como **tabla** (hora · momento · música). Nada de indicaciones minuto a minuto: el 25/11 la versión larga confundía.

| Hora | Momento | Duración |
|---|---|---|
| 20:30 | Tiempo libre | 20' |
| 20:50 | Adoración + oración de entrada con el versículo central de la guía | 10' |
| 21:00 | Ciclo 1 · Bloque 1 de la guía | 15' |
| 21:15 | Ciclo 2 · Bloque 2 | 15' |
| 21:30 | Ciclo 3 · Bloque 3 (todos a la vez o en grupos de 3 personas) | 15' |
| 21:45 | Cierre: "nombre para no soltar" + cuaderno de pedidos | 5' |

Cada ciclo: canción (4') → el líder lee la frase del bloque y ora con los versículos a/b sobre el fondo (4') → oraciones de una frase de los presentes (5') → coro para cerrar (2').

**Cómo lo hace Betania** (turno del 25/11/2026 en YouTube, canal MiSion CEM): la música no se corta en todo el turno; el líder no lee la guía como lista, toma un versículo y un motivo y los ora sobre el fondo; después vuelve el canto con un coro repetido y empieza el ciclo siguiente. Las oraciones de una frase de los presentes son un agregado nuestro.

## 3. Música

- **Solo canciones lentas o de tempo medio**: tienen que poder bajar a fondo mientras alguien ora. El 25/11 se habían elegido "Eres Fiel" (Coalo Zamorano) y "Que todos los pueblos te alaben" (Marco Barrientos) por el tema; son rápidas y se cambiaron.
- **Elegir por tempo primero y por tema después.** Si hay dudas sobre el tempo con el que las toca la banda, preguntarle a Misael antes de publicar.
- **No repetir** la misma canción en dos momentos del turno.
- Base: repertorio de Renuevo Music (✓), más una sugerida nueva por momento para aprender. Toma Tu Lugar suele funcionar porque compone para casas de oración.
- Coro comodín: "Al que está sentado en el trono".

## 4. Qué se publica en Netlify (casadeoracion-elrenuevo.netlify.app)

Todo dentro de `sitio/`. Deploy: `npx -y netlify-cli deploy --prod --dir sitio --site b88c1933-7a8d-4230-96ee-30b84c9825d2`.

- `tN/`: página para la gente con la **guía del miércoles** en PDF (celular y A4). Es el link del flyer.
- `taller-N/cronograma-DD-MM.html`: cronograma en tabla, para el que dirige.
- `taller-N/musicos.html`: sección del miércoles con los mismos horarios y canciones que el cronograma.
- `taller-N/index.html`: sección "Guía del miércoles" con la tabla resumida y los links al cronograma y a la hoja de músicos.

**Cuando se cambia algo** (una canción, un horario), revisar que coincida en los tres: cronograma, musicos.html e index.html del taller. Buscar con grep el nombre viejo en `sitio/` y en `flyers/`.

## 5. Flyer para WhatsApp

- Vertical 1080×1920, HTML → PNG con Chrome headless, en `flyers/`.
- Título = título de la guía; arriba "HOY · CASA DE ORACIÓN"; versículo central; recuadro con día y horario; "Rep. de Siria 255, Perico · ¡Toda la iglesia!"; link a `casadeoracion-elrenuevo.netlify.app/tN`.
- Imagen: ilustraciones de estilo plano de la serie (`video_loop/*/assets/`). Paleta distinta a la de los otros anuncios en circulación.
- Texto para WhatsApp en `flyers/copys.md`, con el link directo al PDF de la guía para celular.

## 6. Orden de trabajo

1. Guía del miércoles (sale del taller del sábado) → confirmar contenido con Misael.
2. Cronograma en tabla + música (por tempo) → confirmar.
3. Hoja de músicos e index del taller con los mismos datos.
4. Flyer + texto para WhatsApp.
5. Deploy y comprobar que los links den 200.
