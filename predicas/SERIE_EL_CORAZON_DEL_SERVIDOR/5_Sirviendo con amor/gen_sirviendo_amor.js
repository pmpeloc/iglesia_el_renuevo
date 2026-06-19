const fs = require("node:fs/promises");
const path = require("node:path");
const os = require("node:os");
const { pathToFileURL } = require("node:url");
const Module = require("node:module");

const runtimeNodeModules = path.join(
  os.homedir(),
  ".cache",
  "codex-runtimes",
  "codex-primary-runtime",
  "dependencies",
  "node",
  "node_modules",
);

process.env.NODE_PATH = [runtimeNodeModules, process.env.NODE_PATH]
  .filter(Boolean)
  .join(path.delimiter);
Module._initPaths();

const HERE = __dirname;
const ROOT = path.resolve(HERE, "..", "..", "..");
const DESIGN_DIR = path.join(ROOT, "predicas", "Predica General");
const ASSET_DIR = path.join(DESIGN_DIR, "assets");
const OUT_PPTX = path.join(HERE, "sirviendo_con_amor.pptx");
const PREVIEW_DIR =
  process.env.PREVIEW_DIR || path.join(HERE, "_preview_sirviendo_con_amor");

const W = 1920;
const H = 1080;
const CREAM = "#F7F1E8";
const CREAM_70 = "#CFC7BA";
const INK = "#1A1A1A";
const INK_SOFT = "#2A2A2A";
const GREEN = "#5DBE2C";
const GREEN_DEEP = "#4A9E22";
const WHITE = "#FFFFFF";

const FONT_DISPLAY = "Anton";
const FONT_BODY = "Montserrat";
const FONT_QUOTE = "Playfair Display";

const content = [
  {
    type: "portada",
    titleTop: "SIRVIENDO",
    titleHighlight: "CON AMOR",
    verse:
      "Teniendo así un gran afecto por vosotros, nos hemos complacido en impartiros no solo el evangelio de Dios, sino también nuestras propias vidas.",
    ref: "1 TESALONICENSES 2:8",
  },
  {
    type: "punto",
    number: "01",
    label: "PRIMER PUNTO",
    title: "UN AMOR QUE SE DA, NO QUE SE PRESTA",
  },
  {
    type: "subpoint",
    label: "PUNTO 01 · A",
    title: "Darse a sí mismo, no solo el tiempo",
    body:
      "Pablo no ofreció un servicio: ofreció su vida. La palabra griega PSYCHAS (almas) indica el ser completo, no el tiempo sobrante.",
    verse: "1 Tesalonicenses 2:8",
  },
  {
    type: "subpoint",
    label: "PUNTO 01 · B",
    title: "Un afecto que nace del corazón, no del deber",
    body:
      "HOMEIROMAI — hapax del NT. El anhelo entrañable de unos padres por su hijo. No obligación: amor que duele cuando está lejos.",
    verse: "1 Tesalonicenses 2:8",
  },
  {
    type: "subpoint",
    label: "PUNTO 01 · C",
    title: "Un amor probado bajo fuego, no decorativo",
    body:
      "Llegaron a Tesalónica después de ser azotados y encarcelados en Filipos. No suavizaron el mensaje. El amor real no desaparece cuando servir cuesta algo.",
    verse: "1 Tesalonicenses 2:1-2",
  },
  {
    type: "aplicacion",
    label: "APLICACIÓN",
    main:
      "¿Debemos preguntarnos si lo que ofrecemos en el servicio es nuestra vida o solo lo que nos sobra?",
    secondary:
      "Necesitamos examinar si nuestro afecto por la iglesia es genuino o protocolar.",
  },
  {
    type: "punto",
    number: "02",
    label: "SEGUNDO PUNTO",
    title: "UN AMOR QUE CUIDA CON TERNURA",
  },
  {
    type: "subpoint",
    label: "PUNTO 02 · A",
    title: "La imagen de la nodriza-madre",
    body:
      'TROPHOS — nodriza que es a la vez madre. Pablo, ex-fariseo con autoridad apostólica, elige la imagen más tierna posible. John Stott: "Es algo muy hermoso que un hombre tan masculino como Pablo se haya servido de esta metáfora femenina."',
    verse: "1 Tesalonicenses 2:7",
  },
  {
    type: "subpoint",
    label: "PUNTO 02 · B",
    title: "Ternura que ajusta su vida al otro",
    body:
      "Una madre no sirve a conveniencia: adapta todo su ritmo al del bebé. Pablo ajustó su ministerio a los tesalonicenses, no al revés.",
    verse: "1 Tesalonicenses 2:7-8",
  },
  {
    type: "subpoint",
    label: "PUNTO 02 · C",
    title: "Cuando servimos así, imitamos a Dios",
    body:
      'Dios mismo usa esta imagen en Isaías 49:15 — "¿Puede una mujer olvidarse de lo que dio a luz?" La ternura en el servicio no es debilidad: es imitar el carácter de Dios.',
    verse: "Isaías 49:15",
  },
  {
    type: "aplicacion",
    label: "APLICACIÓN",
    main: "¿Tenemos ternura real en el servicio o solo eficiencia?",
    secondary:
      "Necesitamos reconocer que la dureza en el servicio no es virtud — es falta de amor.",
  },
  {
    type: "punto",
    number: "03",
    label: "TERCER PUNTO",
    title: "UN AMOR QUE TRABAJA SIN COBRAR",
  },
  {
    type: "subpoint",
    label: "PUNTO 03 · A",
    title: "Trabaja sin buscar ser carga",
    body:
      "Pablo trabajó de noche y de día para no pesar sobre la iglesia recién plantada. El amor no calcula lo que le deben.",
    verse: "1 Tesalonicenses 2:9",
  },
  {
    type: "subpoint",
    label: "PUNTO 03 · B",
    title: "Renuncia a sus derechos por el bien del otro",
    body:
      "Tenían derecho reconocido a ser sostenidos (1 Corintios 9). Lo conocían. Decidieron no ejercerlo. El amor elige el sacrificio cuando hay una razón mayor.",
    verse: "1 Corintios 9",
  },
  {
    type: "subpoint",
    label: "PUNTO 03 · C",
    title: "Predica el mensaje y da el ejemplo",
    body:
      "No solo anunciaron el evangelio: dejaron un modelo de trabajo digno. El amor que sirve también forma carácter en los que observan.",
    verse: "1 Tesalonicenses 2:9",
  },
  {
    type: "aplicacion",
    label: "APLICACIÓN",
    main:
      "¿Debemos preguntarnos si usamos el servicio para recibir reconocimiento, o para genuinamente no ser carga?",
    secondary: "Necesitamos evaluar qué esperamos cuando servimos.",
  },
  {
    type: "cierre",
    quote:
      "El amor de Cristo es el combustible que mueve la maquinaria de nuestros afectos.",
    attribution: "Sugel Michelén",
    secondary: "IGLESIA EL RENUEVO · MCYM · REUNIÓN GENERAL",
  },
];

function textBox(slide, name, text, position, style = {}) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    name,
    position,
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = text;
  shape.text.style = {
    typeface: FONT_BODY,
    fontSize: 36,
    color: INK,
    verticalAlignment: "middle",
    wrap: "square",
    autoFit: "shrinkText",
    ...style,
  };
  return shape;
}

function rect(slide, name, position, fill, line = "none", borderRadius = 0) {
  return slide.shapes.add({
    geometry: borderRadius ? "roundRect" : "rect",
    name,
    position,
    fill,
    line:
      line === "none"
        ? { style: "solid", fill: "none", width: 0 }
        : line,
    ...(borderRadius ? { borderRadius } : {}),
  });
}

function rule(slide, name, left, top, width, fill = INK) {
  return rect(slide, name, { left, top, width, height: 4 }, fill);
}

async function readImage(name) {
  const bytes = await fs.readFile(path.join(ASSET_DIR, name));
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

function addImage(slide, blob, name, position, alt, fit = "contain") {
  return slide.images.add({
    blob,
    contentType: "image/png",
    alt,
    fit,
    position,
    name,
  });
}

function addCornerMark(slide, assets, onInk = false) {
  addImage(
    slide,
    assets.markGreen,
    "corner-mark",
    { left: W - 64 - 88, top: 56, width: 88, height: 88 },
    "Iglesia El Renuevo",
    "contain",
  );
  if (onInk) return;
}

function addKicker(slide, text, left, top, width, color = GREEN_DEEP, size = 34) {
  return textBox(slide, "kicker", text.toUpperCase(), { left, top, width, height: 56 }, {
    typeface: FONT_BODY,
    fontSize: size,
    bold: true,
    color,
  });
}

function portadaSlide(presentation, assets, data) {
  const slide = presentation.slides.add();
  slide.background.fill = INK;
  addCornerMark(slide, assets, true);

  addKicker(slide, "SERIE · EL CORAZÓN DEL SERVIDOR", 120, 250, 1160, GREEN, 38);

  textBox(slide, "title-top", data.titleTop, { left: 120, top: 325, width: 1280, height: 175 }, {
    typeface: FONT_DISPLAY,
    fontSize: 170,
    color: CREAM,
  });

  rect(slide, "title-highlight-bg", { left: 120, top: 505, width: 680, height: 172 }, GREEN, "none", 3);
  textBox(slide, "title-highlight", data.titleHighlight, { left: 145, top: 510, width: 640, height: 160 }, {
    typeface: FONT_DISPLAY,
    fontSize: 158,
    color: INK,
  });

  textBox(slide, "cover-verse", `“${data.verse}”`, { left: 120, top: 725, width: 1260, height: 170 }, {
    typeface: FONT_QUOTE,
    fontSize: 48,
    italic: true,
    color: CREAM_70,
  });

  rect(slide, "reference-pill", { left: 120, top: 928, width: 590, height: 68 }, GREEN, "none", 34);
  textBox(slide, "reference", data.ref, { left: 150, top: 934, width: 530, height: 56 }, {
    typeface: FONT_BODY,
    fontSize: 32,
    bold: true,
    color: INK,
    alignment: "center",
  });
}

function puntoSlide(presentation, assets, data) {
  const slide = presentation.slides.add();
  slide.background.fill = CREAM;
  addCornerMark(slide, assets);

  textBox(slide, `point-${data.number}`, data.number, { left: 120, top: 180, width: 700, height: 300 }, {
    typeface: FONT_DISPLAY,
    fontSize: 320,
    color: GREEN,
  });
  addKicker(slide, data.label, 130, 500, 760, GREEN_DEEP, 46);
  textBox(slide, "point-title", data.title, { left: 120, top: 575, width: 1440, height: 250 }, {
    typeface: FONT_DISPLAY,
    fontSize: data.title.length > 34 ? 116 : 132,
    color: INK,
  });
  rule(slide, "point-rule", 120, 865, 150, INK);
}

function bodyFontSize(text) {
  if (text.length > 260) return 30;
  if (text.length > 210) return 32;
  if (text.length > 165) return 35;
  return 38;
}

function subpointSlide(presentation, assets, data) {
  const slide = presentation.slides.add();
  slide.background.fill = CREAM;

  rect(slide, "image-column", { left: 1160, top: 0, width: 760, height: 1080 }, INK);
  addImage(
    slide,
    assets.markGreenCircle,
    "image-watermark",
    { left: 1422, top: 390, width: 236, height: 236 },
    "Marca El Renuevo",
    "contain",
  );
  rect(slide, "watermark-dim", { left: 1160, top: 0, width: 760, height: 1080 }, `${INK}/84`);
  textBox(slide, "image-label", "IMAGEN", { left: 1250, top: 505, width: 580, height: 58 }, {
    typeface: FONT_BODY,
    fontSize: 28,
    bold: true,
    color: "#F7F1E8/42",
    alignment: "center",
  });

  addCornerMark(slide, assets);
  addKicker(slide, data.label, 120, 166, 820, GREEN_DEEP, 34);

  textBox(slide, "subpoint-title", data.title, { left: 120, top: 235, width: 900, height: 230 }, {
    typeface: FONT_BODY,
    fontSize: data.title.length > 42 ? 56 : 64,
    bold: true,
    color: INK,
  });

  rule(slide, "subpoint-rule", 120, 486, 120, GREEN);

  textBox(slide, "subpoint-body", data.body, { left: 120, top: 530, width: 850, height: 330 }, {
    typeface: FONT_BODY,
    fontSize: bodyFontSize(data.body),
    bold: true,
    color: INK,
  });

  rect(slide, "verse-pill", { left: 120, top: 910, width: 520, height: 64 }, GREEN, "none", 32);
  textBox(slide, "verse-reference", data.verse.toUpperCase(), { left: 150, top: 916, width: 460, height: 52 }, {
    typeface: FONT_BODY,
    fontSize: 28,
    bold: true,
    color: INK,
    alignment: "center",
  });
}

function aplicacionSlide(presentation, assets, data) {
  const slide = presentation.slides.add();
  slide.background.fill = CREAM;
  addCornerMark(slide, assets);

  rect(
    slide,
    "application-box",
    { left: 235, top: 230, width: 1450, height: 620 },
    INK,
    "none",
    14,
  ).shadow = "0 24px 60px #1A1A1A/22";

  addKicker(slide, data.label, 310, 302, 720, GREEN, 48);

  textBox(slide, "application-main", data.main, { left: 310, top: 385, width: 1300, height: 250 }, {
    typeface: FONT_BODY,
    fontSize: data.main.length > 108 ? 52 : 60,
    bold: true,
    color: CREAM,
  });

  rect(slide, "application-accent", { left: 310, top: 658, width: 190, height: 14 }, GREEN);

  textBox(slide, "application-secondary", data.secondary, { left: 310, top: 700, width: 1170, height: 95 }, {
    typeface: FONT_BODY,
    fontSize: data.secondary.length > 78 ? 38 : 42,
    bold: true,
    color: WHITE,
  });
}

function cierreSlide(presentation, assets, data) {
  const slide = presentation.slides.add();
  slide.background.fill = INK;

  addImage(
    slide,
    assets.markGreen,
    "center-mark",
    { left: 890, top: 150, width: 140, height: 140 },
    "Iglesia El Renuevo",
    "contain",
  );

  textBox(slide, "closing-quote", `“${data.quote}”`, { left: 180, top: 355, width: 1560, height: 270 }, {
    typeface: FONT_QUOTE,
    fontSize: 78,
    italic: true,
    color: CREAM,
    alignment: "center",
  });

  textBox(slide, "closing-attribution", data.attribution.toUpperCase(), { left: 520, top: 640, width: 880, height: 58 }, {
    typeface: FONT_BODY,
    fontSize: 34,
    bold: true,
    color: GREEN,
    alignment: "center",
  });

  textBox(slide, "meeting-signature", data.secondary, { left: 360, top: 785, width: 1200, height: 60 }, {
    typeface: FONT_BODY,
    fontSize: 30,
    bold: true,
    color: GREEN,
    alignment: "center",
  });
}

async function writeBlob(filePath, blob) {
  await fs.writeFile(filePath, new Uint8Array(await blob.arrayBuffer()));
}

async function writeTraceFiles() {
  await fs.mkdir(PREVIEW_DIR, { recursive: true });
  await fs.writeFile(
    path.join(PREVIEW_DIR, "source-notes.txt"),
    [
      "Sirviendo con amor - source notes",
      "",
      "Content source: user-provided sermon slide prompt for Mensaje 5, Serie El corazón del servidor.",
      "Design source: predicas/Predica General design system exported from Claude Design.",
      "Assets: predicas/Predica General/assets/mark-green.png and mark-green-circle.png.",
      "No external images or unsupported biblical quotations were added.",
      "",
    ].join("\n"),
    "utf8",
  );
  await fs.writeFile(
    path.join(PREVIEW_DIR, "slide-plan.txt"),
    [
      "Sirviendo con amor - slide plan",
      "",
      "Deck size: 1920x1080.",
      "Palette: cream #F7F1E8, ink #1A1A1A, green #5DBE2C.",
      "Fonts: Anton for display, Montserrat for body/kickers, Playfair Display for scripture/quotes.",
      "Archetypes: portada, punto, subpoint, aplicacion, cierre.",
      "Slide count: 17.",
      "",
    ].join("\n"),
    "utf8",
  );
}

async function renderPreviews(presentation) {
  await fs.mkdir(PREVIEW_DIR, { recursive: true });
  for (const [index, slide] of presentation.slides.items.entries()) {
    const stem = `slide-${String(index + 1).padStart(2, "0")}`;
    await writeBlob(
      path.join(PREVIEW_DIR, `${stem}.png`),
      await presentation.export({ slide, format: "png", scale: 1 }),
    );
    await fs.writeFile(
      path.join(PREVIEW_DIR, `${stem}.layout.json`),
      await (await slide.export({ format: "layout" })).text(),
      "utf8",
    );
  }
}

async function main() {
  const { Presentation, PresentationFile } = await import(
    pathToFileURL(require.resolve("@oai/artifact-tool")).href
  );

  const assets = {
    markGreen: await readImage("mark-green.png"),
    markGreenCircle: await readImage("mark-green-circle.png"),
  };

  const presentation = Presentation.create({
    slideSize: { width: W, height: H },
  });

  presentation.theme.colorScheme = {
    name: "El Renuevo Predica General",
    themeColors: {
      accent1: GREEN,
      accent2: GREEN_DEEP,
      accent3: CREAM,
      accent4: INK,
      accent5: INK_SOFT,
      accent6: WHITE,
      bg1: CREAM,
      bg2: INK,
      tx1: INK,
      tx2: CREAM,
      dk1: "#000000",
      dk2: INK,
      lt1: WHITE,
      lt2: CREAM,
      hlink: GREEN,
      folHlink: GREEN_DEEP,
    },
  };

  for (const slideData of content) {
    if (slideData.type === "portada") portadaSlide(presentation, assets, slideData);
    if (slideData.type === "punto") puntoSlide(presentation, assets, slideData);
    if (slideData.type === "subpoint") subpointSlide(presentation, assets, slideData);
    if (slideData.type === "aplicacion") aplicacionSlide(presentation, assets, slideData);
    if (slideData.type === "cierre") cierreSlide(presentation, assets, slideData);
  }

  if (presentation.slides.items.length !== 17) {
    throw new Error(`Expected 17 slides, got ${presentation.slides.items.length}`);
  }

  await writeTraceFiles();
  if (process.env.WITH_PREVIEW === "1") await renderPreviews(presentation);

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(OUT_PPTX);
  await fs.rm(`${OUT_PPTX}.inspect.ndjson`, { force: true });

  console.log(`Generated ${presentation.slides.items.length} slides`);
  console.log(OUT_PPTX);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
