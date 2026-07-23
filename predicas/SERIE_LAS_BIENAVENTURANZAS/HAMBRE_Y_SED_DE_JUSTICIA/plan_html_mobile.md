# HTML personal y PDF Liquid Mode - Plan de implementación

> **Para agentes:** HABILIDAD REQUERIDA: usar `superpowers:subagent-driven-development` o `superpowers:executing-plans` para ejecutar este plan paso a paso. Los pasos usan casillas (`- [ ]`) para su seguimiento.

**Objetivo:** Crear un HTML personal para predicar y un PDF Liquid Mode para compartir por WhatsApp.

**Arquitectura:** El bosquejo Markdown aprobado será la única fuente de contenido. El HTML reutilizará el patrón oscuro de la prédica anterior; el PDF se generará directamente en 105 × 190 mm y se verificará mediante imágenes renderizadas.

**Tecnologías:** HTML, CSS, JavaScript mínimo, Python, ReportLab y pypdfium2.

## Restricciones globales

- Crear solo los dos archivos solicitados.
- Mantener exactamente tres puntos y tres subpuntos por punto.
- No agregar palabras griegas o hebreas.
- HTML oscuro, tipografía grande y navegación fija.
- PDF móvil con márgenes de 8 mm, logo R-4 y contenido en columna única.
- Versículos antes de cada explicación.
- Aplicaciones en primera persona plural.

---

### Tarea 1: HTML personal

**Archivo:**
- Crear: `predicas/SERIE_LAS_BIENAVENTURANZAS/HAMBRE_Y_SED_DE_JUSTICIA/hambre_y_sed_de_justicia.html`

- [ ] Crear la navegación fija con seis destinos.
- [ ] Incorporar introducción, tres puntos, conclusión y llamado.
- [ ] Presentar versículos en rojo, aplicaciones en verde y preguntas en dorado.
- [ ] Verificar que los seis enlaces de navegación apunten a secciones existentes.
- [ ] Abrir el archivo en navegador y comprobar que no haya texto cortado.

### Tarea 2: PDF Liquid Mode

**Archivo:**
- Crear: `predicas/SERIE_LAS_BIENAVENTURANZAS/HAMBRE_Y_SED_DE_JUSTICIA/hambre_y_sed_de_justicia_mobile.pdf`

- [ ] Configurar páginas de 105 × 190 mm con márgenes de 8 mm.
- [ ] Registrar Montserrat y una fuente sans-serif de respaldo.
- [ ] Añadir logo R-4, encabezado discreto y número de página.
- [ ] Maquetar título, texto base, versículos, puntos, subpuntos y aplicaciones.
- [ ] Permitir que el contenido fluya sin forzar una cantidad exacta de páginas.

### Tarea 3: Verificación

**Archivos:**
- Revisar: `hambre_y_sed_de_justicia.html`
- Revisar: `hambre_y_sed_de_justicia_mobile.pdf`

- [ ] Confirmar por conteo: tres puntos, nueve subpuntos y tres aplicaciones.
- [ ] Renderizar todas las páginas del PDF a PNG.
- [ ] Inspeccionar visualmente cada página.
- [ ] Confirmar que no haya texto cortado, solapado, páginas vacías o referencias incorrectas.
