// ═══════════════════════════════════════════════════════════
//  DINÁMICA: El Menú de Mi Semana
//  Generación Selfie · Red de Jóvenes
//
//  INSTRUCCIONES:
//  1. Abrí Google Sheets → Extensiones → Apps Script
//  2. Pegá este código y hacé clic en Guardar (💾)
//  3. Clic en "Implementar" → "Nueva implementación"
//     → Tipo: Aplicación web
//     → Ejecutar como: Yo
//     → Quién tiene acceso: Cualquier persona
//  4. Copiá la URL que aparece y pegala en vote.html y results.html
// ═══════════════════════════════════════════════════════════

function doGet(e) {
  var action = (e.parameter && e.parameter.action) ? e.parameter.action : 'results';
  var result;

  if (action === 'vote')   result = recordVote(e.parameter);
  else if (action === 'reset') result = resetVotes();
  else                     result = getResults();

  return ContentService
    .createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

// ── Obtener o crear hoja ──────────────────────────────────
function getSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Votos');
  if (!sheet) {
    sheet = ss.insertSheet('Votos');
    sheet.appendRow(['Timestamp', 'Q1', 'Q2', 'Q3', 'Q4']);
    sheet.setFrozenRows(1);
    sheet.getRange(1,1,1,5).setFontWeight('bold');
  }
  return sheet;
}

// ── Registrar un voto ─────────────────────────────────────
function recordVote(params) {
  var sheet = getSheet();
  sheet.appendRow([
    new Date().toLocaleString('es-AR'),
    params.q1 || '',
    params.q2 || '',
    params.q3 || '',
    params.q4 || ''
  ]);
  return { success: true };
}

// ── Obtener resultados agregados ──────────────────────────
function getResults() {
  var sheet = getSheet();
  var tot  = { E: 0, A: 0, C: 0 }; // Q1-Q3 (¿qué alimenté?)
  var q4   = { E: 0, A: 0, C: 0 }; // Q4   (¿qué necesito nutrir?)
  var count = 0;

  if (sheet.getLastRow() > 1) {
    var data = sheet.getRange(2, 2, sheet.getLastRow() - 1, 4).getValues();
    count = data.length;
    data.forEach(function(row) {
      ['E','A','C'].forEach(function(k) {
        if (row[0] === k) tot[k]++;
        if (row[1] === k) tot[k]++;
        if (row[2] === k) tot[k]++;
        if (row[3] === k) q4[k]++;
      });
    });
  }

  var total   = tot.E + tot.A + tot.C;
  var q4total = q4.E  + q4.A  + q4.C;

  return {
    count : count,
    totals: tot,
    pct: {
      E: total > 0 ? Math.round(tot.E / total * 100) : 0,
      A: total > 0 ? Math.round(tot.A / total * 100) : 0,
      C: total > 0 ? Math.round(tot.C / total * 100) : 0
    },
    q4: q4,
    q4pct: {
      E: q4total > 0 ? Math.round(q4.E / q4total * 100) : 0,
      A: q4total > 0 ? Math.round(q4.A / q4total * 100) : 0,
      C: q4total > 0 ? Math.round(q4.C / q4total * 100) : 0
    }
  };
}

// ── Borrar todos los votos ────────────────────────────────
function resetVotes() {
  var sheet = getSheet();
  if (sheet.getLastRow() > 1) {
    sheet.deleteRows(2, sheet.getLastRow() - 1);
  }
  return { success: true, message: 'Votos eliminados' };
}
