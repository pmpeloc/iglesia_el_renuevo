# Reto 7 Días — Instrucciones de configuración

**Dinámica 4 · Generación Selfie · Red de Jóvenes**

---

## Archivos

| Archivo | Descripción |
|---|---|
| `Code_Reto.gs` | Google Apps Script (backend) |
| `suscribir.html` | Página de inscripción (mobile) → subir a Netlify |
| `reto.html` | Página del reto diario (mobile) → subir a Netlify |
| `dashboard.html` | Vista del líder → abrir localmente o subir a Netlify |

---

## Paso 1 — Crear la Google Sheet

1. Ir a [sheets.google.com](https://sheets.google.com) → crear hoja nueva
2. Nombrarla: **Reto 7 Días - Generación Selfie**
3. Las pestañas `Suscriptores` y `Logros` se crean automáticamente la primera vez que alguien se suscribe o completa un reto

---

## Paso 2 — Crear el Apps Script

1. En la hoja → **Extensiones → Apps Script**
2. Borrar el código vacío que aparece
3. Pegar todo el contenido de `Code_Reto.gs`
4. Editar las 3 constantes al inicio del archivo:
   ```javascript
   const LEADER_EMAIL    = 'pmpeloc@gmail.com';
   const APP_URL         = 'https://generacion-selfie.netlify.app';
   const CHALLENGE_START = '2026-06-22';  // ← fecha en que arranca el reto
   ```
5. Guardar (Ctrl+S)

---

## Paso 3 — Implementar el Apps Script

1. Click en **Implementar → Nueva implementación**
2. Tipo: **Aplicación web**
3. Configuración:
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona**
4. Click **Implementar**
5. Copiar la URL que empieza con `https://script.google.com/macros/s/...`

---

## Paso 4 — Pegar la URL en los 3 archivos HTML

Buscar `PEGAR_URL_APPS_SCRIPT_AQUI` en:
- `suscribir.html` (línea con `const SCRIPT_URL`)
- `reto.html` (línea con `const SCRIPT_URL`)
- `dashboard.html` (línea con `const SCRIPT_URL`)

Reemplazar con tu URL real. Ejemplo:
```javascript
const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycb.../exec';
```

---

## Paso 5 — Subir a Netlify

Arrastrar los 3 HTML (`suscribir.html`, `reto.html`, `dashboard.html`) al mismo sitio de Netlify donde ya están `vote.html` y `results.html`.

- URL de inscripción: `https://generacion-selfie.netlify.app/suscribir.html`
- URL del reto: `https://generacion-selfie.netlify.app/reto.html` (se usa vía email con parámetros)
- Dashboard: `https://generacion-selfie.netlify.app/dashboard.html`

---

## Paso 6 — Configurar los triggers de email (MUY IMPORTANTE)

Los emails de recordatorio se envían automáticamente. Hay que crear 3 triggers:

1. En Apps Script → click en el ícono del reloj (⏰ Activadores) en el menú lateral
2. Click en **+ Agregar activador** (abajo a la derecha)

### Trigger 1 — Mañana
- Función a ejecutar: `enviarManana`
- Tipo de evento: **Temporizador basado en tiempo**
- Tipo de tiempo: **Temporizador diario**
- Hora del día: **8:00 a 9:00**

### Trigger 2 — Tarde
- Función a ejecutar: `enviarTarde`
- Tipo de evento: Temporizador basado en tiempo
- Tipo de tiempo: Temporizador diario
- Hora del día: **14:00 a 15:00**

### Trigger 3 — Noche
- Función a ejecutar: `enviarNoche`
- Tipo de evento: Temporizador basado en tiempo
- Tipo de tiempo: Temporizador diario
- Hora del día: **20:00 a 21:00**

> Cada joven elige su horario preferido al inscribirse. Solo recibirá el email en ese turno.

---

## Paso 7 — Generar el QR para la inscripción

El QR para proyectar durante la reunión:

```
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=https://generacion-selfie.netlify.app/suscribir.html
```

Abrir esa URL en el browser y guardar la imagen. O crear un slide con el link visible.

---

## Los 7 retos

| Día | Reto |
|---|---|
| 1 | Leé Romanos 8 de principio a fin. |
| 2 | Antes de tocar el celular esta mañana, orá 5 minutos. |
| 3 | Ayuná de redes sociales durante la mañana (hasta el mediodía). |
| 4 | Escribí en un papel qué área está gobernando más en vos: ¿espíritu, alma o cuerpo? |
| 5 | Buscá a alguien hoy y preguntale cómo está de verdad. Escuchálo sin apuro. |
| 6 | Dedicate 15 minutos a adorar — con música, en silencio, lo que salga. |
| 7 | Compartí con alguien lo que Dios te habló esta semana. |

Para cambiar los retos, editar el array `RETOS` en `Code_Reto.gs` y volver a implementar.

---

## Flujo completo

```
Reunión dominical
│
├─ Proyectás el QR de suscribir.html
│  Los jóvenes se anotan con nombre + email + horario preferido
│  → Reciben email de bienvenida automáticamente
│
├─ Cada día (8am / 2pm / 8pm según preferencia):
│  → Email con el reto del día + botón "COMPLETÉ MI RETO"
│
├─ Al hacer click en el botón:
│  → Se abre reto.html con ?e=EMAIL&d=DIA
│  → Confirman y se registra el logro
│  → Vos recibís notificación en pmpeloc@gmail.com
│
└─ dashboard.html muestra en tiempo real
   quién completó cada día
```
