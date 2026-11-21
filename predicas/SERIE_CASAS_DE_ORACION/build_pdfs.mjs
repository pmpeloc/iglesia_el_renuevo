// Genera apunte y guía en A4 y Liquid Mode (105×190 mm) e imprime los PDF con Chrome headless.
// Uso: node build_pdfs.mjs <carpeta-del-taller> <slug> "<título>" <n-taller> <slug-guia> "<título guía>"
import { readFileSync, writeFileSync, copyFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const [dir, slug, title, n, gslug, gtitle] = process.argv.slice(2);
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const site = resolve('sitio', `t${n}`);

const base = (size, m, body, sub, lh, bar, verse, label) => `
@page { size:${size}; margin:${m};
  @top-left { content:"%TITLE%"; font:8pt Arial,sans-serif; color:#777; }
  @bottom-right { content:counter(page); font:9pt Arial,sans-serif; color:#555; } }
*{box-sizing:border-box} body{margin:0;color:#111;font:${body}pt/${lh} Arial,sans-serif}
.logos{text-align:right;margin:-2pt 0 4pt}.logos img{height:${size==='A4'?26:20}pt;margin-left:6pt}
.bar{padding:9pt 12pt;background:#000;color:#fff;font:600 ${bar}pt/1.15 Montserrat,sans-serif;text-transform:uppercase}
.bar small{display:block;font:400 ${Math.round(bar*0.55)}pt Montserrat,sans-serif;text-transform:none;color:#ddd;margin-top:3pt}
.base{margin:8pt 0;font-size:${sub}pt}
.verse{margin:8pt 0 12pt;padding:10pt 12pt;border:1.5pt solid #000;text-align:center;font:400 ${verse}pt/1.3 Montserrat,sans-serif;break-inside:avoid}
.verse .ref{display:block;margin-top:6pt;font:600 13pt Montserrat,sans-serif}
.label{background:#000;color:#fff;padding:1pt 5pt;font:600 ${label}pt Montserrat,sans-serif;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.block{margin:12pt 0 0}.block>p{margin:5pt 0}
ol.subs{margin:5pt 0 0;padding-left:18pt;list-style:lower-alpha;font-size:${sub}pt}ol.subs li{margin:5pt 0}
.term{font-weight:bold;text-decoration:underline}.num{font-weight:bold;margin-right:3pt}
.app{margin:7pt 0 0;padding:6pt 9pt;border-left:3pt solid #5DBE2C;background:#f1f8ec;font-size:${sub}pt;break-inside:avoid}
.app b{display:block;font:600 9.5pt Montserrat,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.keep{break-inside:avoid}
.bloque{margin:12pt 0 0}.bloque h2{margin:0 0 3pt;font:600 ${label}pt Montserrat,sans-serif;text-transform:uppercase;color:#1a5fb4;break-after:avoid}
.proclama{margin:0 0 4pt;color:#1a5fb4}
.bloque li{break-inside:auto}.vv{display:block;break-inside:avoid}.bloque q{display:block;margin:3pt 0 0;font-style:italic}.bloque q:before{content:"“"}.bloque q:after{content:"”"}
.bloque cite{display:block;font:600 ${sub-1}pt Montserrat,sans-serif;font-style:normal;text-align:right}
.nombres{margin-top:16pt;font-weight:bold;break-inside:avoid}
`;

const variants = {
  a4: base('A4', '16mm 15mm 14mm', 14, 14, 1.15, 18, 22, 14),
  mobile: base('105mm 190mm', '8mm', 14, 13, 1.4, 20, 18, 14),
};

function build(content, name, t) {
  const body = readFileSync(join(dir, content), 'utf8').replaceAll('../sitio/img/', '../sitio/img/');
  for (const [v, css] of Object.entries(variants)) {
    const html = `<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>${t}</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<style>${css.replace('%TITLE%', t)}</style></head><body>${body}</body></html>`;
    const file = resolve(dir, `${name}_${v}.html`);
    writeFileSync(file, html);
    const pdf = resolve(dir, `${name}_${v === 'a4' ? 'apunte' : 'mobile'}.pdf`);
    execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
      `--print-to-pdf=${pdf}`, 'file:///' + file.replaceAll('\\', '/')], { stdio: 'ignore' });
    copyFileSync(pdf, join(site, `${name}_${v === 'a4' ? 'A4' : 'celular'}.pdf`));
    console.log('ok', pdf);
  }
}

build('apunte_contenido.html', slug, title);
build('guia_contenido.html', gslug, gtitle);
