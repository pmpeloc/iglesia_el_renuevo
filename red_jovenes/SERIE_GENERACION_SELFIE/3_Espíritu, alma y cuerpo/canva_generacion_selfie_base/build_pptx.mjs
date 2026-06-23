import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  Presentation,
  PresentationFile,
} from "file:///C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, "..", "..", "..");
const seriesDir = path.resolve(__dirname, "..");
const finalPptx = path.join(seriesDir, "generacion_selfie_presentacion_base_texto_grande_v2.pptx");
const logoPath = path.join(root, "logos", "Identificador.png");
const workspace = path.join(os.tmpdir(), "codex-presentations", "manual-generacion-selfie-base-texto-grande-v2");
const tmpDir = path.join(workspace, "tmp");
const previewDir = path.join(tmpDir, "preview");
const layoutDir = path.join(tmpDir, "layout");
const qaDir = path.join(tmpDir, "qa");

for (const dir of [workspace, tmpDir, previewDir, layoutDir, qaDir]) {
  await fs.mkdir(dir, { recursive: true });
}

await fs.writeFile(
  path.join(tmpDir, "source-notes.txt"),
  [
    "Source ledger",
    "",
    "- Brief: canva_presentacion_base_brief.md, user-provided local brief for the Generación Selfie reusable Canva presentation base.",
    "- Logo: logos/Identificador.png, user-provided Red de Jóvenes / Raíces identifier, used discreetly on footer and closing slides.",
    "- No external claims, statistics, or third-party images used. Visual language is built from editable PowerPoint shapes and text placeholders.",
    "",
  ].join("\n"),
  "utf8",
);

await fs.writeFile(
  path.join(tmpDir, "slide-plan.txt"),
  [
    "Create-mode plan",
    "",
    "Deck: Generación Selfie - Presentación base.",
    "Audience: jóvenes y adolescentes de iglesia. Tone: pastoral, directo, desafiante, actual.",
    "Slide count: 12.",
    "Palette: #111111 and #1E1E1E dominant dark backgrounds; #FFFFFF high-contrast text; #E84A2A main accent; #B73222 secondary red; #D9D9D9 secondary text.",
    "Fonts: Arial bold for headings and Arial for body; Office-safe and editable.",
    "Scale: cover 76-100px, section titles 58-78px, body/subtitles 32-44px, repeated labels 22px, footer 20px.",
    "Objects: editable text boxes, rectangles, rounded rectangles, lines, ovals, a discreet PNG logo, and phone/camera/viewfinder placeholders made from shapes.",
    "Slides: 1 series cover, 2 message cover, 3 question, 4 scripture, 5 central idea, 6 three-point map, 7 point template, 8 multimedia frame, 9 contrast columns, 10 application, 11 response, 12 close.",
    "",
  ].join("\n"),
  "utf8",
);

const W = 1280;
const H = 720;
const C = {
  black: "#111111",
  dark: "#1E1E1E",
  white: "#FFFFFF",
  muted: "#D9D9D9",
  orange: "#E84A2A",
  red: "#B73222",
};

const presentation = Presentation.create({ slideSize: { width: W, height: H } });
const logoBytes = await fs.readFile(logoPath);
const logoBlob = logoBytes.buffer.slice(
  logoBytes.byteOffset,
  logoBytes.byteOffset + logoBytes.byteLength,
);

function rect(slide, name, position, fill, lineFill = "none", width = 0, geometry = "rect") {
  return slide.shapes.add({
    geometry,
    name,
    position,
    fill,
    line: { style: "solid", fill: lineFill, width },
  });
}

function text(slide, name, value, position, style = {}) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    name,
    position,
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = value;
  shape.text.style = {
    typeface: "Arial",
    fontSize: 32,
    color: C.white,
    ...style,
  };
  return shape;
}

function bg(slide, variant = "grid") {
  slide.background.fill = C.black;
  rect(slide, "bg-dark", { left: 0, top: 0, width: W, height: H }, C.black);
  rect(slide, "bg-side-depth", { left: 820, top: 0, width: 460, height: H }, "#181818");
  rect(slide, "accent-glow", { left: 840, top: -145, width: 360, height: 360 }, "#3A1710", "none", 0, "ellipse");
  if (variant === "grid") {
    for (let x = 0; x < W; x += 64) {
      rect(slide, "grid-v", { left: x, top: 0, width: 1, height: H }, "#202020");
    }
    for (let y = 0; y < H; y += 64) {
      rect(slide, "grid-h", { left: 0, top: y, width: W, height: 1 }, "#202020");
    }
  }
}

function footer(slide, value = "Red de Jóvenes - Raíces") {
  slide.images.add({
    blob: logoBlob,
    contentType: "image/png",
    alt: "Identificador Raíces",
    fit: "contain",
    position: { left: 912, top: 632, width: 54, height: 54 },
  });
  text(slide, "footer-text", value, { left: 980, top: 646, width: 286, height: 38 }, {
    fontSize: 20,
    bold: true,
    color: "#BFBFBF",
  });
}

function label(slide, value, x = 72, y = 62, w = 220) {
  rect(slide, "label-outline", { left: x, top: y, width: w, height: 56 }, "none", C.orange, 1.5);
  rect(slide, "label-dot", { left: x + 18, top: y + 20, width: 16, height: 16 }, C.orange, "none", 0, "ellipse");
  text(slide, "label-text", value.toUpperCase(), { left: x + 50, top: y + 14, width: w - 62, height: 30 }, {
    fontSize: 22,
    bold: true,
    color: C.muted,
  });
}

function redBar(slide, x, y, w = 360, h = 24) {
  rect(slide, "red-impact-bar", { left: x, top: y, width: w, height: h }, C.red);
  rect(slide, "orange-impact-bar", { left: x + w * 0.55, top: y, width: w * 0.45, height: h }, C.orange);
}

function phone(slide, x, y, w, h, name = "phone") {
  rect(slide, `${name}-outer`, { left: x, top: y, width: w, height: h }, "#050505", C.white, 6, "roundRect");
  rect(slide, `${name}-screen`, { left: x + 22, top: y + 54, width: w - 44, height: h - 128 }, "#171717", "#6A6A6A", 1.2);
  rect(slide, `${name}-speaker`, { left: x + w / 2 - 28, top: y + 22, width: 56, height: 7 }, C.white, "none", 0, "roundRect");
  rect(slide, `${name}-button`, { left: x + w / 2 - 22, top: y + h - 52, width: 44, height: 44 }, "none", "#BBBBBB", 2, "ellipse");
  rect(slide, `${name}-corner-tl-h`, { left: x + 46, top: y + 84, width: 56, height: 6 }, C.orange);
  rect(slide, `${name}-corner-tl-v`, { left: x + 46, top: y + 84, width: 6, height: 56 }, C.orange);
  rect(slide, `${name}-corner-br-h`, { left: x + w - 102, top: y + h - 150, width: 56, height: 6 }, C.orange);
  rect(slide, `${name}-corner-br-v`, { left: x + w - 52, top: y + h - 200, width: 6, height: 56 }, C.orange);
  text(slide, `${name}-ui-left`, "FLASH", { left: x + 34, top: y + h - 96, width: 72, height: 20 }, {
    fontSize: 11,
    bold: true,
    color: "#AFAFAF",
  });
  text(slide, `${name}-ui-right`, "SELFIE", { left: x + w - 98, top: y + h - 96, width: 72, height: 20 }, {
    fontSize: 11,
    bold: true,
    color: "#AFAFAF",
    alignment: "right",
  });
}

{
  const slide = presentation.slides.add();
  bg(slide);
  redBar(slide, 72, 438, 520, 34);
  label(slide, "Serie base", 72, 64, 265);
  text(slide, "script-generacion", "Generación", { left: 74, top: 148, width: 650, height: 86 }, {
    fontSize: 72,
    bold: true,
    italic: true,
  });
  text(slide, "title-selfie", "SELFIE", { left: 72, top: 230, width: 710, height: 124 }, {
    fontSize: 100,
    bold: true,
    color: C.orange,
  });
  text(slide, "subtitle", "¿Qué ves cuando te ves?", { left: 76, top: 370, width: 650, height: 58 }, {
    fontSize: 42,
    color: C.muted,
  });
  phone(slide, 846, 92, 278, 515, "cover-phone");
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Mensaje", 72, 64, 225);
  text(slide, "message-title", "Espíritu,\nalma y cuerpo", { left: 72, top: 135, width: 760, height: 205 }, {
    fontSize: 74,
    bold: true,
  });
  rect(slide, "title-accent", { left: 70, top: 338, width: 250, height: 12 }, C.orange);
  [
    ["Texto base", "1 Tesalonicenses 5:23"],
    ["Fecha", "Reunión / fecha"],
    ["Serie", "Generación Selfie"],
  ].forEach(([a, b], i) => {
    const y = 410 + i * 68;
    text(slide, `field-label-${i}`, a.toUpperCase(), { left: 72, top: y, width: 150, height: 28 }, {
      fontSize: 18,
      bold: true,
      color: C.orange,
    });
    text(slide, `field-value-${i}`, b, { left: 238, top: y - 10, width: 510, height: 46 }, {
      fontSize: 32,
      color: C.muted,
    });
    rect(slide, `field-line-${i}`, { left: 238, top: y + 38, width: 500, height: 2 }, "#626262");
  });
  phone(slide, 890, 110, 215, 402, "message-phone");
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Pregunta disparadora", 72, 64, 450);
  text(slide, "question", "¿Qué parte de nosotros está tomando\nel control?", { left: 96, top: 208, width: 1088, height: 198 }, {
    fontSize: 78,
    bold: true,
    alignment: "center",
  });
  rect(slide, "question-line", { left: 210, top: 492, width: 860, height: 2 }, "#595959");
  rect(slide, "question-lens", { left: 590, top: 462, width: 100, height: 100 }, "none", C.orange, 4, "ellipse");
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Texto bíblico", 72, 64, 305);
  rect(slide, "scripture-box", { left: 104, top: 164, width: 940, height: 360 }, "#202020", "#343434", 1);
  rect(slide, "scripture-accent", { left: 104, top: 164, width: 12, height: 360 }, C.orange);
  text(slide, "scripture-main", "Texto del pasaje bíblico principal.\nEste espacio está preparado para una cita larga sin perder claridad al proyectar.", { left: 152, top: 205, width: 830, height: 240 }, {
    fontSize: 44,
  });
  text(slide, "scripture-ref", "REFERENCIA DESTACADA", { left: 152, top: 462, width: 650, height: 46 }, {
    fontSize: 34,
    bold: true,
    color: C.orange,
  });
  rect(slide, "scripture-frame-ghost", { left: 980, top: 470, width: 185, height: 185 }, "none", "#333333", 2);
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  rect(slide, "corner-top-h", { left: 135, top: 150, width: 170, height: 10 }, C.orange);
  rect(slide, "corner-top-v", { left: 135, top: 150, width: 10, height: 170 }, C.orange);
  rect(slide, "corner-bottom-h", { left: 980, top: 560, width: 170, height: 10 }, C.orange);
  rect(slide, "corner-bottom-v", { left: 1140, top: 400, width: 10, height: 170 }, C.orange);
  text(slide, "central-idea", "Lo que", { left: 95, top: 258, width: 380, height: 90 }, {
    fontSize: 84,
    bold: true,
    alignment: "right",
  });
  text(slide, "central-highlight", "alimentamos", { left: 500, top: 258, width: 620, height: 90 }, {
    fontSize: 84,
    bold: true,
    color: C.orange,
  });
  text(slide, "central-close", "se fortalece.", { left: 220, top: 365, width: 840, height: 92 }, {
    fontSize: 84,
    bold: true,
    alignment: "center",
  });
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Mapa del mensaje", 72, 64, 375);
  text(slide, "map-title", "Tres lentes para mirar\nlo que somos", { left: 72, top: 124, width: 780, height: 136 }, {
    fontSize: 58,
    bold: true,
  });
  [
    ["01", "Espíritu", "Lo que Dios despierta y guía en nosotros."],
    ["02", "Alma", "Pensamientos, emociones, deseos y decisiones."],
    ["03", "Cuerpo", "Lo visible, los hábitos y nuestras acciones."],
  ].forEach(([num, heading, body], i) => {
    const x = 72 + i * 390;
    rect(slide, `map-card-${i}`, { left: x, top: 300, width: 340, height: 300 }, "#222222", "#3B3B3B", 1);
    text(slide, `map-num-${i}`, num, { left: x + 28, top: 322, width: 90, height: 48 }, {
      fontSize: 42,
      bold: true,
      color: C.orange,
    });
    text(slide, `map-heading-${i}`, heading, { left: x + 28, top: 400, width: 285, height: 58 }, {
      fontSize: 46,
      bold: true,
    });
    text(slide, `map-body-${i}`, body, { left: x + 28, top: 480, width: 285, height: 92 }, {
      fontSize: 28,
      color: C.muted,
    });
  });
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Punto principal", 72, 64, 345);
  text(slide, "point-kicker", "PUNTO 1", { left: 72, top: 160, width: 220, height: 46 }, {
    fontSize: 36,
    bold: true,
    color: C.orange,
  });
  text(slide, "point-title", "Título corto editable", { left: 72, top: 220, width: 760, height: 102 }, {
    fontSize: 68,
    bold: true,
  });
  text(slide, "point-body", "Una frase de desarrollo para explicar la idea sin llenar demasiado la pantalla.", { left: 76, top: 360, width: 690, height: 136 }, {
    fontSize: 38,
    color: C.muted,
  });
  rect(slide, "visual-frame", { left: 860, top: 145, width: 270, height: 410 }, "none", "#5A5A5A", 2);
  rect(slide, "visual-circle", { left: 915, top: 225, width: 160, height: 160 }, C.orange, "none", 0, "ellipse");
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Ilustración visual", 72, 64, 380);
  text(slide, "media-title", "Espacio para imagen,\nvideo o captura", { left: 72, top: 148, width: 600, height: 140 }, {
    fontSize: 58,
    bold: true,
  });
  text(slide, "media-body", "Usá este layout para ejemplos visuales, publicaciones, capturas o recursos multimedia.", { left: 76, top: 322, width: 560, height: 122 }, {
    fontSize: 34,
    color: C.muted,
  });
  rect(slide, "media-frame", { left: 720, top: 100, width: 420, height: 500 }, "#191919", C.white, 5);
  rect(slide, "media-corner-t-h", { left: 720, top: 100, width: 86, height: 10 }, C.orange);
  rect(slide, "media-corner-t-v", { left: 720, top: 100, width: 10, height: 86 }, C.orange);
  rect(slide, "media-corner-b-h", { left: 1054, top: 590, width: 86, height: 10 }, C.orange);
  rect(slide, "media-corner-b-v", { left: 1130, top: 514, width: 10, height: 86 }, C.orange);
  text(slide, "media-placeholder", "INSERTAR\nIMAGEN / VIDEO", { left: 760, top: 300, width: 340, height: 120 }, {
    fontSize: 44,
    bold: true,
    color: "#9D9D9D",
    alignment: "center",
  });
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Contraste espiritual", 72, 64, 430);
  text(slide, "contrast-title", "Lo que mostramos y\nlo que Dios ve", { left: 72, top: 120, width: 820, height: 138 }, {
    fontSize: 58,
    bold: true,
  });
  [
    ["Selfie", ["Apariencia", "Carne", "Lo que muestro", "Control propio"], C.orange],
    ["Verdad", ["Interior", "Espíritu", "Lo que Dios ve", "Guía de Dios"], C.white],
  ].forEach(([heading, items, color], i) => {
    const x = 96 + i * 550;
    rect(slide, `contrast-card-${i}`, { left: x, top: 292, width: 500, height: 340 }, "#222222", "#3B3B3B", 1);
    text(slide, `contrast-heading-${i}`, heading, { left: x + 32, top: 320, width: 330, height: 54 }, {
      fontSize: 44,
      bold: true,
      color,
    });
    items.forEach((item, j) => {
      text(slide, `contrast-item-${i}-${j}`, item, { left: x + 36, top: 392 + j * 54, width: 420, height: 40 }, {
        fontSize: 34,
        color: C.muted,
      });
      rect(slide, `contrast-line-${i}-${j}`, { left: x + 32, top: 434 + j * 54, width: 420, height: 1 }, "#474747");
    });
  });
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Aplicación práctica", 72, 64, 405);
  text(slide, "application-main", "Necesitamos\npreguntarnos\nqué estamos", { left: 72, top: 165, width: 760, height: 250 }, {
    fontSize: 68,
    bold: true,
  });
  text(slide, "application-highlight", "alimentando.", { left: 72, top: 420, width: 700, height: 80 }, {
    fontSize: 74,
    bold: true,
    color: C.orange,
  });
  text(slide, "application-note", "Un desafío en primera persona plural para responder juntos, con claridad y cuidado pastoral.", { left: 76, top: 535, width: 760, height: 90 }, {
    fontSize: 30,
    color: C.muted,
  });
  rect(slide, "application-placeholder", { left: 910, top: 130, width: 240, height: 440 }, "none", "#626262", 2);
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  rect(slide, "response-vignette", { left: 0, top: 0, width: W, height: H }, "#0B0B0B");
  label(slide, "Momento de respuesta", 410, 124, 460);
  text(slide, "response-title", "Dios no mira solo la imagen.\nMira el corazón.", { left: 180, top: 238, width: 920, height: 150 }, {
    fontSize: 66,
    bold: true,
    alignment: "center",
  });
  text(slide, "response-subtitle", "Espacio para oración, reflexión o llamado final.", { left: 240, top: 424, width: 800, height: 58 }, {
    fontSize: 38,
    color: C.muted,
    alignment: "center",
  });
  rect(slide, "response-line", { left: 430, top: 520, width: 420, height: 5 }, C.orange);
  footer(slide);
}

{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  slide.images.add({
    blob: logoBlob,
    contentType: "image/png",
    alt: "Identificador Raíces",
    fit: "contain",
    position: { left: 572, top: 118, width: 136, height: 136 },
  });
  text(slide, "close-title", "Red de Jóvenes - Raíces", { left: 180, top: 292, width: 920, height: 90 }, {
    fontSize: 66,
    bold: true,
    alignment: "center",
  });
  rect(slide, "close-bar", { left: 388, top: 404, width: 504, height: 22 }, C.orange);
  text(slide, "close-next", "Próxima reunión / fecha", { left: 260, top: 482, width: 760, height: 58 }, {
    fontSize: 40,
    bold: true,
    color: C.muted,
    alignment: "center",
  });
}

for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  const png = await presentation.export({ slide, format: "png", scale: 1 });
  await fs.writeFile(path.join(previewDir, `${stem}.png`), new Uint8Array(await png.arrayBuffer()));
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(path.join(layoutDir, `${stem}.layout.json`), await layout.text(), "utf8");
}

const montage = await presentation.export({ format: "webp", montage: true, scale: 1 });
await fs.writeFile(path.join(previewDir, "deck-montage.webp"), new Uint8Array(await montage.arrayBuffer()));
const snapshot = await presentation.inspect({ kind: "slide,textbox,shape,image,layout", maxChars: 12000 });
await fs.writeFile(path.join(tmpDir, "inspect.ndjson"), snapshot.ndjson, "utf8");

const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(finalPptx);

await fs.writeFile(
  path.join(qaDir, "visual-qa.txt"),
  [
    "Visual QA",
    "",
    "- Rendered all 12 slides to PNG and a montage.",
    "- Deck uses editable text boxes and shapes plus the user-provided Raíces identifier PNG.",
    "- Checked intended structure: series cover, message cover, question, scripture, central idea, map, point template, media placeholder, contrast, application, response, close.",
    "- Remaining caveat: Canva may reinterpret PowerPoint fonts/shape styling during import, so the Canva result should be spot-checked after upload.",
    "",
  ].join("\n"),
  "utf8",
);

console.log(
  JSON.stringify(
    {
      finalPptx,
      workspace,
      preview: path.join(previewDir, "deck-montage.webp"),
      slides: presentation.slides.items.length,
    },
    null,
    2,
  ),
);
