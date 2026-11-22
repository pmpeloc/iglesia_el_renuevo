// Genera index.html de horizontal/ (1920×1080) y vertical/ (1080×1920) con las mismas 8 escenas.
// Uso: node build.mjs
import { writeFileSync } from 'node:fs';

const D = 10; // segundos por escena
const g = (s) => `<span class="g">${s}</span>`;
const scenes = [
  { id: 's1', img: 'p1_portada', kicker: 'Iglesia El Renuevo', title: `Casas de ${g('Oración')}`, lines: ['Todos los miércoles'], pill: '20:30 a 22:00 hs' },
  { id: 's2', img: 'p2_viuda', kicker: '¿Por qué?', title: `Jesús nos enseñó a ${g('no soltar')}`, verse: '“…orar siempre, y no desmayar”', ref: 'Lucas 18:1' },
  { id: 's3', img: 'p3_aposento', kicker: '¿Por qué?', title: `La iglesia nació ${g('orando junta')}`, verse: '“Todos éstos perseveraban unánimes en oración”', ref: 'Hechos 1:14' },
  { id: 's4', img: 'p4_asado', kicker: '¿Por qué?', title: `Empezar chico y ${g('no soltar')}`, lines: ['No hace falta orar lindo:', 'hace falta estar.'] },
  { id: 's5', img: 'p8_perico', kicker: '¿Cómo es?', title: `Cada ${g('miércoles')}`, rows: [['20:30', 'Turno abierto: llegás y orás con la guía'], ['20:50', 'Bienvenida'], ['21:00', 'Bloques de alabanza y oración'], ['21:55', 'Cierre']] },
  { id: 's6', img: 'p5_manos', kicker: 'Cada bloque', steps: [['🎶', 'Cantamos'], ['📖', 'Leemos la Palabra'], ['🙏', 'Oramos juntos']] },
  { id: 's7', img: 'p6_soga', kicker: 'Oraciones de una frase', verse: '“Señor, no queremos soltar a los que amamos.”', lines: ['Nadie está obligado a orar en voz alta.'] },
  { id: 's8', img: 'p7_ronda', kicker: 'Casas de Oración', title: `Un nombre, un miércoles y ${g('una hora')}`, pill: 'Miércoles · 20:30 hs', lines: ['¡Traé a alguien!'] },
];
const T = scenes.length * D;

function sceneHTML(s, i) {
  const parts = [];
  if (s.kicker) parts.push(`<div class="kicker">${s.kicker}</div>`);
  if (s.title) parts.push(`<div class="title">${s.title}</div>`);
  if (s.verse) parts.push(`<div class="verse">${s.verse}</div>`);
  if (s.ref) parts.push(`<div class="ref">${s.ref}</div>`);
  if (s.rows) parts.push(`<div class="rows">${s.rows.map(([h, t]) => `<div class="row"><b>${h}</b><span>${t}</span></div>`).join('')}</div>`);
  if (s.steps) parts.push(`<div class="steps">${s.steps.map(([e, t], k) => `<div class="step"><i>${e}</i><span>${t}</span></div>${k < s.steps.length - 1 ? '<div class="arrow">↓</div>' : ''}`).join('')}</div>`);
  if (s.lines) parts.push(...s.lines.map((l) => `<div class="line">${l}</div>`));
  if (s.pill) parts.push(`<div class="pill">${s.pill}</div>`);
  return `
      <div id="${s.id}" class="scene clip" data-start="${i * D}" data-duration="${D}" data-track-index="${i}" style="z-index:${i + 1}">
        <div class="wrap" id="${s.id}-wrap">
          <div class="bg"><img id="${s.id}-img" src="assets/${s.img}.png" alt="" /></div>
          <div class="veil"></div>
          <div class="txt" id="${s.id}-txt">${parts.join('\n            ')}</div>
        </div>
      </div>`;
}

const css = {
  h: `
      html, body { width: 1920px; height: 1080px; }
      .bg { position: absolute; inset: 0; }
      .bg img { width: 1920px; height: 1080px; object-fit: cover; }
      .veil { position: absolute; inset: 0; background: linear-gradient(90deg, rgba(8,20,34,.94) 0%, rgba(8,20,34,.86) 44%, rgba(8,20,34,.25) 75%, rgba(8,20,34,.1) 100%); }
      .txt { position: absolute; left: 130px; top: 0; bottom: 0; width: 1050px; display: flex; flex-direction: column; justify-content: center; gap: 34px; }
      .title { font-size: 120px; }
      .verse { font-size: 76px; }
      .line { font-size: 72px; }
      .rows .row { font-size: 58px; }
      .rows .row b { width: 190px; }
      .step { font-size: 88px; }`,
  v: `
      html, body { width: 1080px; height: 1920px; }
      .bg { position: absolute; left: 0; right: 0; top: 0; height: 860px; overflow: hidden; }
      .bg img { width: 1080px; height: 860px; object-fit: cover; }
      .veil { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,20,34,0) 0px, rgba(8,20,34,0) 600px, rgba(8,20,34,1) 860px); }
      .txt { position: absolute; left: 80px; right: 80px; top: 820px; bottom: 90px; display: flex; flex-direction: column; justify-content: center; gap: 32px; }
      .title { font-size: 104px; }
      .verse { font-size: 68px; }
      .line { font-size: 62px; }
      .rows .row { font-size: 50px; }
      .rows .row b { width: 170px; }
      .step { font-size: 80px; }`,
};

function page(kind) {
  const [W, H] = kind === 'h' ? [1920, 1080] : [1080, 1920];
  return `<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=${W}, height=${H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root { --navy: #081422; --ink: #ffffff; --orange: #FFB23E; --green: #7ED957; --cream: #F3E9DA; }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; overflow: hidden; background: var(--navy); }
      #root { width: 100%; height: 100%; position: relative; overflow: hidden; font-family: Montserrat, sans-serif; color: var(--ink); background: var(--navy); }
      .scene { position: absolute; inset: 0; }
      .wrap { position: absolute; inset: 0; background: var(--navy); }
      .bg img { display: block; }
      .kicker { font-weight: 800; font-size: 50px; letter-spacing: .14em; text-transform: uppercase; color: var(--orange); }
      .title { font-weight: 900; line-height: 1.02; letter-spacing: -.02em; }
      .g { color: var(--green); }
      .verse { font-weight: 800; line-height: 1.18; color: var(--cream); font-style: italic; }
      .ref { font-weight: 800; font-size: 58px; color: var(--orange); }
      .line { font-weight: 800; line-height: 1.2; color: var(--cream); }
      .pill { align-self: flex-start; background: #E8521A; color: #fff; font-weight: 900; font-size: 76px; padding: 18px 44px; border-radius: 26px; }
      .rows { display: flex; flex-direction: column; gap: 26px; }
      .row { display: flex; align-items: baseline; gap: 24px; font-weight: 800; line-height: 1.15; color: var(--cream); }
      .row b { flex: none; color: var(--orange); font-weight: 900; }
      .steps { display: flex; flex-direction: column; gap: 6px; }
      .step { display: flex; align-items: center; gap: 30px; font-weight: 900; }
      .step i { font-style: normal; }
      .arrow { font-size: 60px; color: var(--green); font-weight: 900; padding-left: 26px; line-height: 1; }
      ${css[kind]}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="${T}" data-width="${W}" data-height="${H}">${scenes.map(sceneHTML).join('')}
      <audio id="musica" src="assets/pad.m4a" data-start="0" data-duration="${T}" data-track-index="20" data-volume="0.6"></audio>
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
      const D = ${D};
      ${JSON.stringify(scenes.map((s) => s.id))}.forEach((id, i) => {
        const t0 = i * D;
        // fundido de entrada y salida de la escena (sobre el hijo, no el clip)
        tl.fromTo('#' + id + '-wrap', { opacity: 0 }, { opacity: 1, duration: 0.7, ease: 'power2.out' }, t0);
        tl.to('#' + id + '-wrap', { opacity: 0, duration: 0.6, ease: 'power2.in' }, t0 + D - 0.7);
        // Ken Burns lento
        tl.fromTo('#' + id + '-img', { scale: 1.02 }, { scale: 1.1, duration: D, ease: 'none' }, t0);
        // texto: cada línea entra de abajo, escalonado
        tl.fromTo('#' + id + '-txt > *', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out', stagger: 0.45 }, t0 + 0.5);
      });
      // pasos del bloque: uno tras otro, más espaciados
      tl.fromTo('#s6 .step, #s6 .arrow', { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.6, ease: 'power3.out', stagger: 0.7 }, 5 * D + 1.2);
      tl.fromTo('#s5 .row', { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.6, ease: 'power3.out', stagger: 0.6 }, 4 * D + 1.4);
      window.__timelines['main'] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
`;
}

writeFileSync(new URL('./horizontal/index.html', import.meta.url), page('h'));
writeFileSync(new URL('./vertical/index.html', import.meta.url), page('v'));
console.log('ok', T, 's');
