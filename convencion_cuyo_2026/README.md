# Convención Regional Cuyo 2026 — Mendoza

Proyecto de ayuda a los organizadores de la Convención Regional Cuyo (Mendoza).
Estado: **prototipo v2** con la identidad oficial y los pedidos de Camila (12/10/2026). Menús y pastores siguen siendo de ejemplo.

Datos oficiales: **12 al 15 de noviembre de 2026**, Godoy Cruz (Mendoza). Lema: *Creciendo en su Gracia* (2 Pedro 3:18). Web: convencionregionalcuyo.com.ar

## Links

| Qué | Link | Archivo local |
|---|---|---|
| Design System (colores, tipografías, logos, componentes) | https://claude.ai/artifact/QzDvnQvKqUZ5UqcUEDQqvu | `assets/` (SVG de Canva + `assets/png/` recortes) |
| Lienzo de desarrollo (mobile + escritorio por página, estados, panel, impresos, UI Kit) | https://claude.ai/artifact/AH1ui7ZxBZdKqjeNwjLo6i | `desarrollo/` |
| Prototipo funcional (menú + comidas + info + apuntes + bienvenida + panel) | https://claude.ai/artifact/L5C3BLcuE5finWyxL6wUUu | `prototipo/menu_convencion_prototipo.html` |
| Lienzo de diseño v1 (identidad provisoria, reemplazado por el de desarrollo) | https://claude.ai/artifact/MJipHLNJJSdBjQEdWrgpiH | `diseno/` |
| Sugerencias para los organizadores | https://claude.ai/artifact/Ji41mHCk12NwzkEox2Qaeu | `sugerencias.html` (detalle en `sugerencias.md`) |

Los links son privados: hay que compartirlos desde el menú **Compartir** de cada página.

## Pedido 1 — Menú del día por QR (audio 1)

- Escanean un QR y ven **solo el menú del día en curso** (el jueves solo el del jueves; nada de "spoiler" de los días siguientes). Si no se pudiera, no es problema.
- El menú puede cambiar en el día: se agrega algo, se saca algo o se cambia la guarnición. Quieren poder **modificarlo en el momento**.

Cómo lo resuelve el prototipo:
- Vista del asistente filtrada por día. Antes y después de la convención muestra un mensaje en lugar del menú.
- Panel de cocina: editar, agregar ("Nuevo"), quitar solo por hoy ("Hoy no hay") y volver al original.
- Los cambios se muestran con el plato anterior tachado y la hora de la última actualización.
- Aviso del día opcional (ej.: cambio de salón).

## Pedido 2 — Bienvenida de los pastores (audio 2)

- Idea del pastor: originalmente un video, pero se prefiere **texto** (el audio no siempre se escucha bien).
- Aprox. **18 pastores** de Mendoza, cada uno con un texto de bienvenida y una **foto del matrimonio pastoral**.
- Podrían salir de forma aleatoria (uno por comida/día) o **todos juntos**. Ellos prefieren **todos juntos**, siempre visibles.

Cómo lo resuelve el prototipo:
- Pestaña "Bienvenida" junto al menú, con los 18 mensajes en tarjetas (foto + nombre + iglesia + texto).
- Encabezado con Salmos 133:1 (RVR1960).

## Piezas de diseño (lienzo)

1. Asistente · Menú de hoy (celular)
2. Asistente · Bienvenida de los pastores (celular)
3. Panel de cocina (celular)
4. Cartel de mesa con QR, 10 × 15 cm
5. Historia para redes, 1080 × 1920

## Pedido 3 — Feedback de Camila (12/10/2026)

- **Info práctica:** solo Wi‑Fi y objetos perdidos (como aviso). Hecho: pestaña "Wi‑Fi y avisos"; cocina/organización carga y marca "Entregado" desde el panel.
- **Apuntes:** solo si son privados. Hecho: se guardan únicamente en el celular de cada persona (nadie más los ve). Se pierden si borran datos del navegador o cambian de celular.
- **Confirmar almuerzo y cena (sí o sí):** los 4 almuerzos y 4 cenas visibles; "Voy / No voy"; cada día se confirma hasta el día anterior a las 20:00 (hora a confirmar con ellos); mensaje de confirmar con anticipación. Panel con el conteo por comida.

## Identidad visual (oficial)

- Colores: #083d6b azul marino · #f4e7d1 naranja claro (crema) · #b3defa celeste claro.
- Tipografías: Tan Meringue (títulos; archivo en `assets/fonts/`, provisto por la organización) y League Spartan (Google Fonts).

## Datos ficticios a reemplazar

- Horarios, menús y salones. Red y clave de Wi‑Fi. Conteos de confirmaciones.
- Nombres, iglesias, textos y fotos de los 18 matrimonios pastorales (se usaron los 18 departamentos de Mendoza).
- El QR del cartel es decorativo.

## Versión real — stack y decisiones (12/10/2026)

Stack: **Next.js en Vercel Hobby** + **Supabase Free** (Postgres, Auth y Storage).

| Tema | Decisión |
|---|---|
| Apuntes | Solo en el celular (localStorage) + botón "Compartir". Nunca pasan por el servidor. |
| Identidad del asistente | Ingreso anónimo de Supabase + nombre e iglesia. No hay acceso a la lista de inscriptos. |
| Cierre de confirmaciones | 20:00 (hora de Mendoza) del día anterior, controlado por la base (RLS). |
| Escala | ~200 asistentes y ~50 de cocina/organización. Menú por consulta periódica, sin Realtime (límite de 200 conexiones). |
| Supabase | Plan gratis. Un cron diario de Vercel lo consulta para que no se pause. |
| Dominio | Gratuito de Vercel (`*.vercel.app`). Ese es el link del QR. |
| Fotos de pastores | Consentimiento confirmado. Bucket público, escritura solo staff. |

## Pendiente para la versión real

- Plazo para borrar nombres y confirmaciones después del evento (propuesta: 30 días).
- Quiénes de los 50 entran al panel y con qué rol (cocina u organización).
- Logos vectoriales (los SVG de Canva traen las texturas como imágenes).
- QR real apuntando al link definitivo.
- Preguntas para los organizadores: qué comidas hay por día (¿desayuno, merienda?), opciones sin TACC o vegetarianas.
