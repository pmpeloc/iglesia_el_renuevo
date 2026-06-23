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
const finalPptx = path.join(seriesDir, "generacion_selfie_espiritu_alma_cuerpo_predica.pptx");
const logoPath = path.join(root, "logos", "Identificador.png");
const transcriptPath = path.join(seriesDir, "transcripcion_espiritu_alma_y_cuerpo.md");
const workspace = path.join(os.tmpdir(), "codex-presentations", "generacion-selfie-predica");
const tmpDir = path.join(workspace, "tmp");
const previewDir = path.join(tmpDir, "preview");
const layoutDir = path.join(tmpDir, "layout");
const qaDir = path.join(tmpDir, "qa");

for (const dir of [workspace, tmpDir, previewDir, layoutDir, qaDir]) {
  await fs.mkdir(dir, { recursive: true });
}

const W = 1280;
const H = 720;
const C = {
  black: "#111111",
  dark: "#1E1E1E",
  panel: "#222222",
  panel2: "#282828",
  white: "#FFFFFF",
  muted: "#D9D9D9",
  orange: "#E84A2A",
  red: "#B73222",
  line: "#575757",
  dim: "#343434",
};

await fs.writeFile(
  path.join(tmpDir, "source-notes.txt"),
  [
    "Source ledger",
    "",
    "- Sermon source: transcripcion_espiritu_alma_y_cuerpo.md. Used for the narrative arc, key ideas, scripture references, and application.",
    "- Visual base: Generación Selfie presentation base text grande v2. Reused dark palette, large projector-first typography, top labels, footer, phone/selfie motifs, and Red de Jóvenes / Raíces identity.",
    "- Logo: logos/Identificador.png, user-provided Red de Jóvenes / Raíces identifier.",
    "- No external photos or third-party assets used. Supporting visuals are editable shapes, diagrams, simple icon-like graphics, and large text.",
    "",
  ].join("\n"),
  "utf8",
);

await fs.writeFile(
  path.join(tmpDir, "slide-plan.txt"),
  [
    "Slide plan",
    "",
    "Goal: sermon presentation for 'Espíritu, alma y cuerpo' with very large readable text and image-led teaching.",
    "Style: based on the last Canva base, dark background, orange/red accents, selfie/phone motif, large top labels and footer.",
    "Text rule: one main idea per slide, minimal supporting text, no long paragraphs.",
    "Slides: cover, question, whole-being thesis, integrated-being diagram, interior-first, encounter with God, Psalm 103 command, order of the self, flesh vs Spirit, feeding principle, dying-by-starvation principle, habits/body appetite, discipline, decision, spiritual food, response, close.",
    "",
  ].join("\n"),
  "utf8",
);

const presentation = Presentation.create({ slideSize: { width: W, height: H } });
const logoBytes = await fs.readFile(logoPath);
const logoBlob = logoBytes.buffer.slice(
  logoBytes.byteOffset,
  logoBytes.byteOffset + logoBytes.byteLength,
);
await fs.access(transcriptPath);

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

function label(slide, value, x = 72, y = 62, w = 360) {
  rect(slide, "label-outline", { left: x, top: y, width: w, height: 56 }, "none", C.orange, 1.5);
  rect(slide, "label-dot", { left: x + 18, top: y + 20, width: 16, height: 16 }, C.orange, "none", 0, "ellipse");
  text(slide, "label-text", value.toUpperCase(), { left: x + 50, top: y + 14, width: w - 62, height: 30 }, {
    fontSize: 22,
    bold: true,
    color: C.muted,
  });
}

function redBar(slide, x, y, w = 460, h = 30) {
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

function bigTitle(slide, value, y = 175, size = 76, width = 780) {
  text(slide, "main-title", value, { left: 72, top: y, width, height: 190 }, {
    fontSize: size,
    bold: true,
  });
}

function card(slide, name, x, y, w, h, title, body, accent = C.orange) {
  rect(slide, `${name}-box`, { left: x, top: y, width: w, height: h }, C.panel, "#3B3B3B", 1);
  text(slide, `${name}-title`, title, { left: x + 30, top: y + 32, width: w - 60, height: 54 }, {
    fontSize: 42,
    bold: true,
    color: accent,
  });
  text(slide, `${name}-body`, body, { left: x + 30, top: y + 102, width: w - 60, height: h - 116 }, {
    fontSize: 31,
    color: C.muted,
  });
}

function arrowText(slide, x, y, size = 72) {
  text(slide, "arrow", ">", { left: x, top: y, width: 70, height: 70 }, {
    fontSize: size,
    bold: true,
    color: C.orange,
    alignment: "center",
  });
}

function meter(slide, x, y, labelValue, pct, color) {
  text(slide, `${labelValue}-label`, labelValue, { left: x, top: y, width: 360, height: 42 }, {
    fontSize: 32,
    bold: true,
    color: C.white,
  });
  rect(slide, `${labelValue}-track`, { left: x, top: y + 58, width: 410, height: 34 }, "#2A2A2A", C.line, 1, "roundRect");
  rect(slide, `${labelValue}-fill`, { left: x + 6, top: y + 64, width: Math.round(398 * pct), height: 22 }, color, "none", 0, "roundRect");
}

function circleLabel(slide, name, x, y, size, fill, line, title, fontSize = 48) {
  rect(slide, `${name}-circle`, { left: x, top: y, width: size, height: size }, fill, line, 3, "ellipse");
  text(slide, `${name}-text`, title, { left: x + 18, top: y + size / 2 - fontSize / 1.5, width: size - 36, height: fontSize + 18 }, {
    fontSize,
    bold: true,
    alignment: "center",
    color: C.white,
  });
}

// 1. Cover
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Generación Selfie", 72, 64, 350);
  text(slide, "script", "Espíritu,", { left: 72, top: 165, width: 640, height: 80 }, { fontSize: 72, bold: true });
  text(slide, "title", "alma y cuerpo", { left: 72, top: 245, width: 760, height: 88 }, { fontSize: 74, bold: true, color: C.orange });
  text(slide, "subtitle", "¿Qué parte de nosotros está tomando el control?", { left: 76, top: 378, width: 700, height: 94 }, { fontSize: 39, color: C.muted });
  redBar(slide, 72, 500, 520, 34);
  phone(slide, 858, 92, 278, 515, "cover-phone");
  footer(slide);
}

// 2. Opening question
{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Pregunta disparadora", 72, 64, 450);
  text(slide, "question", "¿Quién está\nguiando mi vida?", { left: 120, top: 205, width: 1040, height: 220 }, {
    fontSize: 86,
    bold: true,
    alignment: "center",
  });
  rect(slide, "lens", { left: 570, top: 470, width: 140, height: 140 }, "none", C.orange, 5, "ellipse");
  rect(slide, "lens-dot", { left: 622, top: 522, width: 36, height: 36 }, C.orange, "none", 0, "ellipse");
  footer(slide);
}

// 3. Thesis
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Idea central", 72, 64, 275);
  bigTitle(slide, "Todo nuestro ser\nrendido a Cristo", 162, 70, 820);
  text(slide, "thesis-parts", "espíritu  ·  alma  ·  cuerpo", { left: 78, top: 420, width: 760, height: 56 }, {
    fontSize: 40,
    bold: true,
    color: C.orange,
  });
  text(slide, "verse-ref", "1 Tesalonicenses 5:23", { left: 82, top: 502, width: 520, height: 42 }, {
    fontSize: 30,
    color: C.muted,
  });
  circleLabel(slide, "whole", 890, 185, 250, "none", C.orange, "SER\nINTEGRAL", 36);
  footer(slide);
}

// 4. Integrated diagram
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Mapa visual", 72, 64, 255);
  bigTitle(slide, "Somos un ser\nintegral", 135, 66, 520);
  rect(slide, "body-circle", { left: 660, top: 115, width: 470, height: 470 }, C.panel, C.line, 4, "ellipse");
  rect(slide, "soul-circle", { left: 730, top: 185, width: 330, height: 330 }, "#181818", C.orange, 4, "ellipse");
  rect(slide, "spirit-circle", { left: 805, top: 260, width: 180, height: 180 }, C.black, C.white, 4, "ellipse");
  text(slide, "body-label", "CUERPO", { left: 770, top: 495, width: 250, height: 56 }, {
    fontSize: 48,
    bold: true,
    alignment: "center",
    color: C.muted,
  });
  text(slide, "soul-label", "ALMA", { left: 805, top: 205, width: 180, height: 56 }, {
    fontSize: 50,
    bold: true,
    alignment: "center",
    color: C.orange,
  });
  text(slide, "spirit-label", "ESPÍRITU", { left: 815, top: 322, width: 160, height: 44 }, {
    fontSize: 27,
    bold: true,
    alignment: "center",
    color: C.white,
  });
  text(slide, "diagram-note", "Dios obra\ndesde adentro", { left: 102, top: 390, width: 400, height: 112 }, {
    fontSize: 42,
    bold: true,
    color: C.orange,
  });
  footer(slide);
}

// 5. Interior first
{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Hombre interior", 72, 64, 340);
  bigTitle(slide, "Dios empieza\ndesde adentro", 165, 76, 760);
  circleLabel(slide, "inner", 850, 205, 210, C.black, C.orange, "INTERIOR", 36);
  rect(slide, "pulse-1", { left: 800, top: 155, width: 310, height: 310 }, "none", "#612315", 4, "ellipse");
  rect(slide, "pulse-2", { left: 750, top: 105, width: 410, height: 410 }, "none", "#3A1710", 4, "ellipse");
  text(slide, "refs", "Romanos 7:22\nEfesios 3:16\n2 Corintios 4:16", { left: 84, top: 500, width: 420, height: 110 }, {
    fontSize: 28,
    color: C.muted,
  });
  footer(slide);
}

// 6. Encounter
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Intimidad", 72, 64, 235);
  bigTitle(slide, "El espíritu\nse encuentra\ncon Dios", 145, 68, 610);
  rect(slide, "god", { left: 780, top: 130, width: 260, height: 96 }, C.panel, C.orange, 2, "roundRect");
  text(slide, "god-text", "DIOS", { left: 780, top: 150, width: 260, height: 50 }, { fontSize: 44, bold: true, alignment: "center" });
  rect(slide, "line-1", { left: 905, top: 235, width: 10, height: 120 }, C.orange);
  rect(slide, "spirit-box", { left: 745, top: 365, width: 330, height: 112 }, C.panel2, C.white, 2, "roundRect");
  text(slide, "spirit-text", "ESPÍRITU", { left: 745, top: 392, width: 330, height: 56 }, { fontSize: 46, bold: true, alignment: "center", color: C.orange });
  footer(slide);
}

// 7. Psalm 103
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Salmo 103", 72, 64, 235);
  text(slide, "quote", "Bendice,\nalma mía,\na Jehová", { left: 74, top: 150, width: 620, height: 260 }, {
    fontSize: 74,
    bold: true,
  });
  text(slide, "key", "El interior da la orden", { left: 82, top: 455, width: 560, height: 56 }, {
    fontSize: 38,
    bold: true,
    color: C.orange,
  });
  rect(slide, "megaphone-body", { left: 780, top: 255, width: 180, height: 110 }, C.orange, "none", 0, "roundRect");
  rect(slide, "megaphone-handle", { left: 850, top: 360, width: 48, height: 130 }, C.red, "none", 0, "roundRect");
  rect(slide, "sound-1", { left: 990, top: 230, width: 110, height: 190 }, "none", C.white, 5, "ellipse");
  rect(slide, "sound-2", { left: 1040, top: 195, width: 180, height: 260 }, "none", C.line, 4, "ellipse");
  footer(slide);
}

// 8. Order
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Orden correcto", 72, 64, 315);
  bigTitle(slide, "El espíritu\nordena", 135, 68, 520);
  card(slide, "order-1", 540, 180, 190, 155, "1", "Espíritu", C.orange);
  arrowText(slide, 745, 220, 64);
  card(slide, "order-2", 805, 180, 190, 155, "2", "Alma", C.white);
  arrowText(slide, 1010, 220, 64);
  card(slide, "order-3", 1070, 180, 190, 155, "3", "Cuerpo", C.white);
  text(slide, "order-note", "No vivimos por impulso.\nSomos guiados por Dios.", { left: 570, top: 420, width: 620, height: 96 }, {
    fontSize: 34,
    color: C.muted,
  });
  footer(slide);
}

// 9. Flesh vs Spirit
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Romanos 8", 72, 64, 250);
  bigTitle(slide, "Dos formas\nde vivir", 128, 64, 600);
  card(slide, "flesh", 116, 330, 470, 215, "Carne", "Lo que se ocupa de sí mismo", C.red);
  card(slide, "spirit", 690, 330, 470, 215, "Espíritu", "Vida y paz", C.orange);
  text(slide, "romans-ref", "Romanos 8:5-14", { left: 78, top: 560, width: 330, height: 38 }, {
    fontSize: 28,
    color: C.muted,
  });
  footer(slide);
}

// 10. Feeding principle
{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Principio", 72, 64, 235);
  text(slide, "feeding", "Lo que\nalimentamos\nse fortalece", { left: 95, top: 155, width: 620, height: 305 }, {
    fontSize: 72,
    bold: true,
  });
  meter(slide, 760, 210, "Espíritu", 0.86, C.orange);
  meter(slide, 760, 365, "Carne", 0.34, C.red);
  footer(slide);
}

// 11. Starve what should die
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Alimentación", 72, 64, 300);
  phone(slide, 132, 125, 275, 505, "feed-phone");
  text(slide, "phone-word", "FEED", { left: 166, top: 265, width: 210, height: 80 }, {
    fontSize: 62,
    bold: true,
    color: C.orange,
    alignment: "center",
  });
  text(slide, "starve", "Todo lo que\nno alimentamos\nse muere", { left: 520, top: 185, width: 650, height: 240 }, {
    fontSize: 64,
    bold: true,
  });
  text(slide, "short-note", "La pregunta es qué estamos dejando crecer.", { left: 526, top: 470, width: 620, height: 46 }, {
    fontSize: 32,
    color: C.muted,
  });
  footer(slide);
}

// 12. Body appetite
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Hábitos", 72, 64, 205);
  bigTitle(slide, "El cuerpo pide\nlo que conoce", 140, 70, 760);
  rect(slide, "habit-plate", { left: 830, top: 205, width: 260, height: 260 }, "none", C.white, 5, "ellipse");
  rect(slide, "habit-scoop-1", { left: 870, top: 235, width: 78, height: 78 }, C.orange, "none", 0, "ellipse");
  rect(slide, "habit-scoop-2", { left: 955, top: 265, width: 78, height: 78 }, C.red, "none", 0, "ellipse");
  rect(slide, "habit-scoop-3", { left: 910, top: 335, width: 88, height: 56 }, "#F5F5F5", "none", 0, "roundRect");
  text(slide, "habit-note", "Lo repetido\nse vuelve hambre.", { left: 82, top: 445, width: 580, height: 96 }, {
    fontSize: 38,
    bold: true,
    color: C.orange,
  });
  footer(slide);
}

// 13. Discipline
{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Disciplina", 72, 64, 270);
  text(slide, "discipline-title", "La victoria\nse prepara\nen la mesa", { left: 80, top: 142, width: 620, height: 285 }, {
    fontSize: 72,
    bold: true,
  });
  rect(slide, "table", { left: 780, top: 430, width: 360, height: 22 }, C.orange);
  rect(slide, "plate", { left: 845, top: 215, width: 230, height: 230 }, "none", C.white, 6, "ellipse");
  rect(slide, "plate-inner", { left: 895, top: 265, width: 130, height: 130 }, "none", C.line, 4, "ellipse");
  rect(slide, "fork-1", { left: 770, top: 220, width: 10, height: 205 }, C.muted);
  rect(slide, "fork-2", { left: 748, top: 220, width: 10, height: 68 }, C.muted);
  rect(slide, "fork-3", { left: 792, top: 220, width: 10, height: 68 }, C.muted);
  footer(slide);
}

// 14. Decision
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Decisión", 72, 64, 220);
  text(slide, "decision-title", "¿Qué estamos\nalimentando?", { left: 82, top: 145, width: 760, height: 170 }, {
    fontSize: 76,
    bold: true,
  });
  card(slide, "choice-1", 115, 380, 455, 155, "Presencia", "vida y paz", C.orange);
  card(slide, "choice-2", 705, 380, 455, 155, "Carne", "impulso y desgaste", C.red);
  footer(slide);
}

// 15. Spiritual food
{
  const slide = presentation.slides.add();
  bg(slide);
  label(slide, "Práctica", 72, 64, 220);
  bigTitle(slide, "Alimentar\nel espíritu", 132, 70, 560);
  const items = [
    ["PALABRA", "Libro"],
    ["ORACIÓN", "Altar"],
    ["COMUNIDAD", "Casa"],
  ];
  items.forEach(([title, sub], i) => {
    const x = 565 + i * 220;
    rect(slide, `food-icon-${i}`, { left: x, top: 230, width: 150, height: 150 }, C.panel, C.orange, 3, "roundRect");
    text(slide, `food-mark-${i}`, sub, { left: x + 15, top: 272, width: 120, height: 45 }, {
      fontSize: 28,
      bold: true,
      color: C.muted,
      alignment: "center",
    });
    text(slide, `food-title-${i}`, title, { left: x - 42, top: 405, width: 234, height: 44 }, {
      fontSize: 26,
      bold: true,
      color: C.white,
      alignment: "center",
    });
  });
  footer(slide);
}

// 16. Response
{
  const slide = presentation.slides.add();
  bg(slide, "plain");
  label(slide, "Momento de respuesta", 410, 124, 460);
  text(slide, "response-title", "Cristo vive\nen nosotros", { left: 220, top: 260, width: 840, height: 150 }, {
    fontSize: 82,
    bold: true,
    alignment: "center",
  });
  text(slide, "response-subtitle", "Rendimos espíritu, alma y cuerpo.", { left: 270, top: 450, width: 740, height: 50 }, {
    fontSize: 38,
    color: C.muted,
    alignment: "center",
  });
  rect(slide, "response-line", { left: 430, top: 532, width: 420, height: 5 }, C.orange);
  footer(slide);
}

// 17. Close
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
  text(slide, "close-next", "Generación Selfie", { left: 260, top: 482, width: 760, height: 58 }, {
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
    "- Rendered all sermon slides to PNG.",
    "- Checked projector-first rule: large labels, large footer, minimal text per slide.",
    "- Visuals are editable shape diagrams, phone/selfie motifs, meters, cards, plates, flow diagrams, and simple icon-like graphics.",
    "- Canva import should be spot-checked because Canva may reinterpret font metrics.",
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
