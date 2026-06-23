# El Menú de Mi Semana — Instrucciones de configuración

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `Code.gs` | Backend (Google Apps Script) — recibe y guarda votos |
| `vote.html` | Página que escanean los chicos (celular) |
| `results.html` | Pantalla del proyector (resultados en vivo) |

---

## PASO 1 — Configurar el backend (5 min)

1. Abrí [Google Sheets](https://sheets.google.com) → creá una hoja nueva
2. Menú **Extensiones → Apps Script**
3. Borrá el código que aparece y pegá el contenido de `Code.gs`
4. Guardá (💾 o Ctrl+S)
5. Hacé clic en **Implementar → Nueva implementación**
   - Tipo: **Aplicación web**
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona**
6. Hacé clic en **Implementar** → copiá la URL que aparece (empieza con `https://script.google.com/macros/s/...`)

---

## PASO 2 — Pegar la URL en los archivos HTML

En **vote.html** y en **results.html**, buscá esta línea y reemplazá el texto:

```javascript
const SCRIPT_URL = 'TU_URL_DE_APPS_SCRIPT_ACÁ';
```

En **results.html** también reemplazá la URL del sitio (para el QR):

```javascript
const VOTE_URL = 'https://TU-APP.vercel.app/vote.html';
```

---

## PASO 3 — Subir a Vercel / Netlify / GitHub Pages

Los tres archivos HTML son estáticos. Cualquier plataforma funciona:

**Vercel / Netlify:** Arrastrar la carpeta `dinamica_menu_semana/` al dashboard → Deploy automático.

**GitHub Pages:** Subir los archivos a un repositorio → Settings → Pages → Branch main.

---

## Durante el evento

| Pantalla | Quién la ve |
|----------|-------------|
| `results.html` | El proyector (abrilo en el navegador del proyector antes de empezar) |
| `vote.html` | Los chicos (el QR del proyector los lleva ahí) |

- Los resultados se actualizan **cada 5 segundos** automáticamente
- El botón **↺ LIMPIAR VOTOS** (abajo izquierda, casi invisible) borra todo si necesitás empezar de nuevo
- Si querés cerrar las votaciones, simplemente sacás el QR de la pantalla

---

## Flujo del evento

1. Abrís `results.html` en el proyector → muestra el QR
2. Los chicos escanean → votan en 4 preguntas → ven el "Gracias"
3. En el proyector aparecen los resultados en vivo con el área ganadora iluminada
4. Usás el resultado para conectar con el mensaje: "Como grupo, lo que más alimentamos fue..."
