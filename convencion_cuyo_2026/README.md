# Convención Regional Cuyo 2026 — Mendoza

Proyecto de ayuda a los organizadores de la Convención Regional Cuyo (Mendoza).
Estado: **prototipo con datos ficticios**, esperando feedback. Después se refina con datos e identidad oficiales.

## Links

| Qué | Link | Archivo local |
|---|---|---|
| Prototipo funcional (menú + bienvenida + panel de cocina) | https://claude.ai/artifact/L5C3BLcuE5finWyxL6wUUu | `prototipo/menu_convencion_prototipo.html` |
| Lienzo de diseño (pantallas, cartel QR, historia) | https://claude.ai/artifact/MJipHLNJJSdBjQEdWrgpiH | `diseno/` |

Los dos links son privados: hay que compartirlos desde el menú **Compartir** de cada página.

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

## Datos ficticios a reemplazar

- Fechas (12 al 14 de noviembre de 2026), horarios, menús y salones.
- Nombres, iglesias, textos y fotos de los 18 matrimonios pastorales (se usaron los 18 departamentos de Mendoza).
- Colores y tipografías: provisorios (malbec + gris andino). Falta la identidad oficial de la convención.
- El QR del cartel es decorativo.

## Pendiente para la versión real

- Base de datos compartida, para que cocina edite y todos vean el cambio al instante (hoy el prototipo guarda en el navegador).
- Clave o acceso restringido al panel de cocina.
- QR real apuntando al link definitivo.
- Preguntas para los organizadores: qué comidas hay por día (¿desayuno, merienda?), opciones sin TACC o vegetarianas, si confirman que la bienvenida va toda junta.
