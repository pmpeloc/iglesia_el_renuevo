// ═══════════════════════════════════════════════════════════════
//  RETO 7 DÍAS · Generación Selfie · Red de Jóvenes
//
//  CONFIGURACIÓN RÁPIDA:
//  1. Google Sheets → Extensiones → Apps Script → pegar este código
//  2. Editar las 3 constantes de abajo
//  3. Implementar → Aplicación web → Cualquier persona
//  4. Copiar la URL y pegarla en suscribir.html, reto.html y dashboard.html
//  5. En Apps Script → Activadores → Agregar los 3 triggers de email
//     (ver instrucciones al pie del archivo)
// ═══════════════════════════════════════════════════════════════

const LEADER_EMAIL   = 'pmpeloc@gmail.com';      // ← tu email
const APP_URL        = 'https://generacion-selfie.netlify.app'; // ← tu URL de Netlify
const CHALLENGE_START = '2026-06-22';             // ← fecha de inicio del reto (YYYY-MM-DD)

// ── Los 7 retos diarios ───────────────────────────────────────
const RETOS = [
  'Leé Romanos 8 de principio a fin.',
  'Antes de tocar el celular esta mañana, orá 5 minutos.',
  'Ayuná de redes sociales durante la mañana (hasta el mediodía).',
  'Escribí en un papel qué área está gobernando más en vos: ¿espíritu, alma o cuerpo?',
  'Buscá a alguien hoy y preguntale cómo está de verdad. Escuchálo sin apuro.',
  'Dedicate 15 minutos a adorar — con música, en silencio, lo que salga.',
  'Compartí con alguien lo que Dios te habló esta semana.'
];

// ── Router principal ──────────────────────────────────────────
function doGet(e) {
  var action = (e.parameter && e.parameter.action) ? e.parameter.action : '';
  var result;
  if      (action === 'suscribir')  result = suscribir(e.parameter);
  else if (action === 'completar')  result = completar(e.parameter);
  else if (action === 'dashboard')  result = getDashboard();
  else if (action === 'estado')     result = getEstado(e.parameter);
  else                              result = { error: 'Accion desconocida' };
  return ContentService
    .createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

// ── Helpers de hoja ──────────────────────────────────────────
function getSuscriptoresSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var s  = ss.getSheetByName('Suscriptores');
  if (!s) {
    s = ss.insertSheet('Suscriptores');
    s.appendRow(['Timestamp','Nombre','Email','Horario']);
    s.setFrozenRows(1);
    s.getRange(1,1,1,4).setFontWeight('bold');
  }
  return s;
}

function getLogrosSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var s  = ss.getSheetByName('Logros');
  if (!s) {
    s = ss.insertSheet('Logros');
    s.appendRow(['Timestamp','Nombre','Email','Dia','Reto']);
    s.setFrozenRows(1);
    s.getRange(1,1,1,5).setFontWeight('bold');
  }
  return s;
}

// ── Calcular día actual del reto ──────────────────────────────
function getDiaActual() {
  var start = new Date(CHALLENGE_START + 'T00:00:00');
  var hoy   = new Date();
  var diff  = Math.floor((hoy - start) / (1000*60*60*24)) + 1;
  return Math.min(Math.max(diff, 1), 7);
}

// ── Suscribir ─────────────────────────────────────────────────
function suscribir(p) {
  var nombre  = (p.nombre  || '').trim();
  var email   = (p.email   || '').trim().toLowerCase();
  var horario = (p.horario || 'manana');
  if (!nombre || !email) return { success: false, error: 'Faltan datos' };

  var sheet = getSuscriptoresSheet();

  // Verificar si ya existe
  if (sheet.getLastRow() > 1) {
    var data = sheet.getRange(2,3,sheet.getLastRow()-1,1).getValues();
    for (var i=0; i<data.length; i++) {
      if (data[i][0].toLowerCase() === email) {
        return { success: true, ya_suscripto: true };
      }
    }
  }

  sheet.appendRow([new Date().toLocaleString('es-AR'), nombre, email, horario]);

  // Email de bienvenida
  try {
    var dia1Link = APP_URL + '/reto.html?e=' + encodeURIComponent(email) + '&d=1';
    MailApp.sendEmail({
      to: email,
      subject: '🔥 ¡Estás en el Reto de 7 Días! · Generación Selfie',
      htmlBody: emailTemplate('¡Bienvenido/a, ' + nombre + '!',
        'Arrancás mañana. Cada día vas a recibir un reto por email a tu horario preferido.',
        'Reto del Día 1: ' + RETOS[0],
        dia1Link, 1)
    });
  } catch(err) { Logger.log('Error email bienvenida: ' + err); }

  return { success: true };
}

// ── Completar reto ─────────────────────────────────────────────
function completar(p) {
  var email = (p.email || '').trim().toLowerCase();
  var dia   = parseInt(p.dia) || getDiaActual();
  if (!email) return { success: false, error: 'Email requerido' };

  var sheet = getLogrosSheet();

  // Verificar si ya completó este día
  if (sheet.getLastRow() > 1) {
    var data = sheet.getRange(2,3,sheet.getLastRow()-1,2).getValues();
    for (var i=0; i<data.length; i++) {
      if (data[i][0].toLowerCase() === email && parseInt(data[i][1]) === dia) {
        return { success: true, ya_completado: true };
      }
    }
  }

  // Buscar nombre
  var nombre = email;
  var sSheet = getSuscriptoresSheet();
  if (sSheet.getLastRow() > 1) {
    var sData = sSheet.getRange(2,2,sSheet.getLastRow()-1,2).getValues();
    for (var j=0; j<sData.length; j++) {
      if (sData[j][1].toLowerCase() === email) { nombre = sData[j][0]; break; }
    }
  }

  var retoTexto = RETOS[dia-1] || '';
  sheet.appendRow([new Date().toLocaleString('es-AR'), nombre, email, dia, retoTexto]);

  // Notificar al líder
  try {
    MailApp.sendEmail({
      to: LEADER_EMAIL,
      subject: '✅ ' + nombre + ' completó el Reto Día ' + dia,
      htmlBody: '<div style="font-family:sans-serif;padding:20px">'
        + '<h2 style="color:#E8521A">✅ Reto completado</h2>'
        + '<p><strong>' + nombre + '</strong> (' + email + ') completó el Reto del Día <strong>' + dia + '</strong>.</p>'
        + '<blockquote style="border-left:4px solid #E8521A;padding-left:12px;color:#555">' + retoTexto + '</blockquote>'
        + '<p style="color:#888;font-size:13px">' + new Date().toLocaleString('es-AR') + '</p>'
        + '</div>'
    });
  } catch(err) { Logger.log('Error email lider: ' + err); }

  return { success: true, nombre: nombre, dia: dia };
}

// ── Dashboard ─────────────────────────────────────────────────
function getDashboard() {
  var sSheet = getSuscriptoresSheet();
  var lSheet = getLogrosSheet();
  var dia    = getDiaActual();

  var suscriptores = [];
  if (sSheet.getLastRow() > 1) {
    var sData = sSheet.getRange(2,1,sSheet.getLastRow()-1,4).getValues();
    sData.forEach(function(r){ suscriptores.push({nombre:r[1],email:r[2]}); });
  }

  var logros = {};
  if (lSheet.getLastRow() > 1) {
    var lData = lSheet.getRange(2,1,lSheet.getLastRow()-1,4).getValues();
    lData.forEach(function(r){
      var k = r[2].toLowerCase();
      if (!logros[k]) logros[k] = [];
      logros[k].push(parseInt(r[3]));
    });
  }

  var participantes = suscriptores.map(function(s){
    var completados = logros[s.email.toLowerCase()] || [];
    return { nombre: s.nombre, completados: completados };
  });

  return {
    dia: dia,
    reto: RETOS[dia-1] || '',
    total: suscriptores.length,
    participantes: participantes
  };
}

// ── Estado individual ─────────────────────────────────────────
function getEstado(p) {
  var email = (p.email || '').trim().toLowerCase();
  var dia   = parseInt(p.dia) || getDiaActual();
  var lSheet = getLogrosSheet();
  var completado = false;
  if (lSheet.getLastRow() > 1) {
    var data = lSheet.getRange(2,3,lSheet.getLastRow()-1,2).getValues();
    for (var i=0; i<data.length; i++) {
      if (data[i][0].toLowerCase()===email && parseInt(data[i][1])===dia) {
        completado = true; break;
      }
    }
  }
  return { dia: dia, reto: RETOS[dia-1]||'', completado: completado };
}

// ── Envío de recordatorios ─────────────────────────────────────
function enviarRecordatorios(horario) {
  var dia    = getDiaActual();
  var reto   = RETOS[dia-1] || '';
  var sheet  = getSuscriptoresSheet();
  if (sheet.getLastRow() < 2) return;

  var data = sheet.getRange(2,2,sheet.getLastRow()-1,3).getValues();
  data.forEach(function(row){
    var nombre  = row[0];
    var email   = row[1];
    var pref    = row[2];
    if (pref !== horario) return;

    var link = APP_URL + '/reto.html?e=' + encodeURIComponent(email) + '&d=' + dia;
    try {
      MailApp.sendEmail({
        to: email,
        subject: '🔥 Reto Día ' + dia + ' de 7 · Generación Selfie',
        htmlBody: emailTemplate(
          '¡Hola, ' + nombre + '! Tu reto de hoy:',
          'Día ' + dia + ' de 7 · Generación Selfie',
          reto, link, dia)
      });
    } catch(err) { Logger.log('Error email ' + email + ': ' + err); }
  });
}

function enviarManana() { enviarRecordatorios('manana'); }
function enviarTarde()  { enviarRecordatorios('tarde'); }
function enviarNoche()  { enviarRecordatorios('noche'); }

// ── Template email ─────────────────────────────────────────────
function emailTemplate(titulo, subtitulo, reto, link, dia) {
  return '<div style="background:#0a0a0a;padding:40px 0;font-family:\'Helvetica Neue\',sans-serif">'
    + '<div style="max-width:500px;margin:0 auto;background:#111;border-radius:16px;overflow:hidden">'
    + '<div style="background:#E8521A;padding:28px 32px">'
    + '<div style="font-size:12px;letter-spacing:6px;color:rgba(255,255,255,0.7);text-transform:uppercase;margin-bottom:8px">Generación Selfie</div>'
    + '<div style="font-size:28px;font-weight:900;color:#fff">' + titulo + '</div>'
    + '</div>'
    + '<div style="padding:32px">'
    + '<div style="font-size:12px;letter-spacing:4px;color:#E8521A;text-transform:uppercase;margin-bottom:16px">' + subtitulo + '</div>'
    + '<div style="font-size:20px;color:#fff;font-weight:700;line-height:1.5;margin-bottom:28px;padding:20px;background:#1a1a1a;border-radius:10px;border-left:4px solid #E8521A">'
    + reto + '</div>'
    + '<div style="text-align:center;margin-top:8px">'
    + '<a href="' + link + '" style="display:inline-block;background:#E8521A;color:#fff;font-size:18px;font-weight:700;text-decoration:none;padding:18px 40px;border-radius:50px;letter-spacing:2px">✅ COMPLETÉ MI RETO</a>'
    + '</div>'
    + '<div style="margin-top:28px;padding-top:20px;border-top:1px solid #222;font-size:13px;color:#444;text-align:center">'
    + 'Día ' + dia + ' de 7 · Espíritu, Alma y Cuerpo</div>'
    + '</div></div></div>';
}

// ═══════════════════════════════════════════════════════════════
//  CONFIGURAR TRIGGERS (hacer UNA SOLA VEZ):
//
//  En Apps Script → Activadores (ícono del reloj) → + Agregar activador
//
//  Trigger 1 — Mañana (8am):
//    Función: enviarManana | Tipo: Temporizador diario | Hora: 8am–9am
//
//  Trigger 2 — Tarde (2pm):
//    Función: enviarTarde | Tipo: Temporizador diario | Hora: 2pm–3pm
//
//  Trigger 3 — Noche (8pm):
//    Función: enviarNoche | Tipo: Temporizador diario | Hora: 8pm–9pm
// ═══════════════════════════════════════════════════════════════
