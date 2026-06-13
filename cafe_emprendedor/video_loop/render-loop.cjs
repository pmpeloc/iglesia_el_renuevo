const fs = require("node:fs");
const path = require("node:path");
const { spawn } = require("node:child_process");
const sharp = require("sharp");

const ROOT = path.resolve(__dirname, "..", "..");
const OUTPUT_DIR = path.join(ROOT, "cafe_emprendedor", "video_loop");
const PREVIEW_DIR = path.join(ROOT, "outputs", "cafe-emprendedor-video-preview");
const VIDEO_PATH = path.join(OUTPUT_DIR, "cafe-emprendedor-loop-1920x1080.mp4");

const WIDTH = 1920;
const HEIGHT = 1080;
const FPS = 25;
const DURATION = 24;
const TOTAL_FRAMES = FPS * DURATION;

const ASSETS = {
  background: path.join(ROOT, "cafe_emprendedor", "branding", "ilustracion-campana-01.png"),
  cafe: path.join(ROOT, "cafe_emprendedor", "branding", "cafe-emprendedor-logo.png"),
  raices: path.join(ROOT, "red_jovenes", "logos", "Horizontal.png"),
  jesus: path.join(ROOT, "cafe_emprendedor", "branding", "aliados", "jesus-vive-lockup.png"),
  renuevo: path.join(ROOT, "logos", "LOGO-EL RENUEVO-PORTADA-2.png"),
};

const LOGOS = [
  {
    id: "cafe",
    start: 0.3,
    end: 5.8,
    maxWidth: 600,
    maxHeight: 660,
    panelFill: "#fff4df",
    accent: "#ff674d",
    transition: "pop",
  },
  {
    id: "raices",
    start: 5.9,
    end: 11.4,
    maxWidth: 1080,
    maxHeight: 480,
    panelFill: "#fff4df",
    accent: "#f15a24",
    transition: "slide",
  },
  {
    id: "jesus",
    start: 11.5,
    end: 17,
    maxWidth: 800,
    maxHeight: 590,
    panelFill: "#abcff1",
    accent: "#ffffff",
    transition: "wipe",
  },
  {
    id: "renuevo",
    start: 17.1,
    end: 22.6,
    maxWidth: 1050,
    maxHeight: 500,
    panelFill: "#ffffff",
    accent: "#79d11f",
    transition: "rise",
  },
];

function clamp(value, min = 0, max = 1) {
  return Math.min(max, Math.max(min, value));
}

function easeInOut(value) {
  const t = clamp(value);
  return t * t * (3 - 2 * t);
}

function easeInCubic(value) {
  const t = clamp(value);
  return t * t * t;
}

function easeOutCubic(value) {
  const t = clamp(value);
  return 1 - Math.pow(1 - t, 3);
}

function easeOutBack(value) {
  const t = clamp(value);
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
}

function logoState(item, time) {
  if (time < item.start || time >= item.end) return null;

  const local = time - item.start;
  const total = item.end - item.start;
  const entryDuration = 1.05;
  const exitDuration = 1.15;
  const entry = clamp(local / entryDuration);
  const exit = clamp((local - (total - exitDuration)) / exitDuration);
  const entryEase = easeOutCubic(entry);
  const exitEase = easeInCubic(exit);

  const state = {
    opacity: clamp(entryEase * (1 - exitEase)),
    scale: 1,
    rotation: 0,
    x: 0,
    y: 0,
    wipe: 1,
    panelScale: 0.96 + 0.04 * entryEase - 0.03 * exitEase,
  };

  if (item.transition === "pop") {
    state.scale = 0.22 + 0.78 * easeOutBack(entry);
    state.scale *= 1 - 0.12 * exitEase;
    state.rotation = -8 * (1 - entryEase) + 6 * exitEase;
    state.y = 80 * (1 - entryEase);
    state.x = 220 * exitEase;
  } else if (item.transition === "slide") {
    state.scale = 0.9 + 0.1 * entryEase;
    state.x = -170 * (1 - entryEase);
    state.y = 150 * (1 - entryEase) - 130 * exitEase;
  } else if (item.transition === "wipe") {
    state.scale = 0.96 + 0.04 * entryEase;
    state.x = 45 * (1 - entryEase) + 90 * exitEase;
    state.wipe = exit > 0 ? 1 - easeInOut(exit) : easeInOut(entry);
    state.opacity = clamp((0.25 + 0.75 * entryEase) * (1 - exitEase));
  } else if (item.transition === "rise") {
    state.scale = 0.68 + 0.32 * easeOutBack(entry);
    state.scale *= 1 + 0.08 * exitEase;
    state.y = 150 * (1 - entryEase) - 80 * exitEase;
  }

  return state;
}

function screenOverlaySvg() {
  return Buffer.from(`
    <svg width="${WIDTH}" height="${HEIGHT}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="shade" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#210949" stop-opacity=".42"/>
          <stop offset=".5" stop-color="#321064" stop-opacity=".23"/>
          <stop offset="1" stop-color="#210949" stop-opacity=".46"/>
        </linearGradient>
        <radialGradient id="light" cx=".5" cy=".5" r=".62">
          <stop offset="0" stop-color="#fff4df" stop-opacity=".13"/>
          <stop offset=".72" stop-color="#fff4df" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="1920" height="1080" fill="url(#shade)"/>
      <rect width="1920" height="1080" fill="url(#light)"/>
    </svg>
  `);
}

function panelSvg(item, state) {
  const panelWidth = 1230 * state.panelScale;
  const panelHeight = 700 * state.panelScale;
  const x = (WIDTH - panelWidth) / 2 + state.x * 0.12;
  const y = (HEIGHT - panelHeight) / 2 + state.y * 0.1;
  const opacity = Math.min(0.96, state.opacity * 0.96);
  const shadowOpacity = state.opacity * 0.34;

  return Buffer.from(`
    <svg width="${WIDTH}" height="${HEIGHT}" xmlns="http://www.w3.org/2000/svg">
      <rect x="${x + 24}" y="${y + 28}" width="${panelWidth}" height="${panelHeight}"
            rx="78" fill="#210949" opacity="${shadowOpacity}"/>
      <rect x="${x}" y="${y}" width="${panelWidth}" height="${panelHeight}"
            rx="78" fill="${item.panelFill}" opacity="${opacity}"
            stroke="#321064" stroke-width="10"/>
      <path d="M ${x + 84} ${y + panelHeight - 92}
               C ${x + 230} ${y + panelHeight - 28},
                 ${x + 350} ${y + panelHeight - 142},
                 ${x + 500} ${y + panelHeight - 72}"
            fill="none" stroke="${item.accent}" stroke-width="16"
            stroke-linecap="round" opacity="${state.opacity * 0.8}"/>
      <circle cx="${x + panelWidth - 104}" cy="${y + 96}" r="20"
              fill="${item.accent}" opacity="${state.opacity * 0.92}"/>
      <circle cx="${x + panelWidth - 158}" cy="${y + 96}" r="11"
              fill="#ffd41f" opacity="${state.opacity * 0.86}"/>
    </svg>
  `);
}

async function opacityBuffer(input, opacity) {
  return sharp(input)
    .ensureAlpha()
    .linear([1, 1, 1, opacity], [0, 0, 0, 0])
    .png()
    .toBuffer();
}

async function prepareLogo(source, maxWidth, maxHeight) {
  return sharp(source)
    .trim({ background: { r: 255, g: 255, b: 255, alpha: 0 } })
    .resize({
      width: maxWidth,
      height: maxHeight,
      fit: "inside",
      withoutEnlargement: false,
      kernel: sharp.kernel.lanczos3,
    })
    .png()
    .toBuffer({ resolveWithObject: true });
}

async function transformLogo(prepared, item, state) {
  const width = Math.max(2, Math.round(prepared.info.width * state.scale));
  const height = Math.max(2, Math.round(prepared.info.height * state.scale));
  let image = sharp(prepared.data)
    .resize(width, height, { fit: "fill", kernel: sharp.kernel.lanczos3 });

  if (item.transition === "wipe") {
    const visibleWidth = Math.max(2, Math.round(width * clamp(state.wipe, 0.002, 1)));
    image = image.extract({ left: 0, top: 0, width: visibleWidth, height });
  }

  if (Math.abs(state.rotation) > 0.05) {
    image = image.rotate(state.rotation, {
      background: { r: 0, g: 0, b: 0, alpha: 0 },
    });
  }

  const rendered = await image.png().toBuffer({ resolveWithObject: true });
  return {
    data: await opacityBuffer(rendered.data, state.opacity),
    width: rendered.info.width,
    height: rendered.info.height,
  };
}

async function buildContext() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  fs.mkdirSync(PREVIEW_DIR, { recursive: true });

  const backgroundWidth = 2080;
  const backgroundHeight = 1170;
  const background = await sharp(ASSETS.background)
    .resize(backgroundWidth, backgroundHeight, {
      fit: "cover",
      position: "centre",
      kernel: sharp.kernel.lanczos3,
    })
    .blur(2.2)
    .modulate({ brightness: 0.96, saturation: 1.08 })
    .png()
    .toBuffer();

  const prepared = {};
  for (const item of LOGOS) {
    prepared[item.id] = await prepareLogo(
      ASSETS[item.id],
      item.maxWidth,
      item.maxHeight,
    );
  }

  return {
    background,
    backgroundWidth,
    backgroundHeight,
    overlay: screenOverlaySvg(),
    prepared,
  };
}

async function renderFrame(context, time, raw = true) {
  const progress = clamp(time / (DURATION - 1 / FPS));
  const maxX = context.backgroundWidth - WIDTH;
  const maxY = context.backgroundHeight - HEIGHT;
  const left = Math.round(
    maxX / 2 + (maxX / 2 - 8) * Math.sin(Math.PI * 2 * progress),
  );
  const top = Math.round(
    maxY / 2 + (maxY / 2 - 8) * Math.sin(Math.PI * 4 * progress),
  );

  const composites = [
    { input: context.overlay, left: 0, top: 0 },
  ];

  const active = LOGOS.find((item) => time >= item.start && time < item.end);
  if (active) {
    const state = logoState(active, time);
    composites.push({ input: panelSvg(active, state), left: 0, top: 0 });

    const logo = await transformLogo(context.prepared[active.id], active, state);
    const logoLeft = Math.round((WIDTH - logo.width) / 2 + state.x);
    const logoTop = Math.round((HEIGHT - logo.height) / 2 + state.y);
    composites.push({
      input: logo.data,
      left: logoLeft,
      top: logoTop,
    });
  }

  const image = sharp(context.background)
    .extract({ left, top, width: WIDTH, height: HEIGHT })
    .composite(composites);

  return raw
    ? image.ensureAlpha().raw().toBuffer()
    : image.png().toBuffer();
}

function findFfmpeg() {
  const runtime = path.join(ROOT, "outputs", "cafe-emprendedor-video-runtime", "ffmpeg");
  const stack = [runtime];
  while (stack.length) {
    const current = stack.pop();
    if (!fs.existsSync(current)) continue;
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const fullPath = path.join(current, entry.name);
      if (entry.isDirectory()) stack.push(fullPath);
      if (entry.isFile() && entry.name.toLowerCase() === "ffmpeg.exe") return fullPath;
    }
  }
  throw new Error("No se encontró ffmpeg.exe en el runtime descargado.");
}

async function writeToStream(stream, buffer) {
  if (stream.write(buffer)) return;
  await new Promise((resolve) => stream.once("drain", resolve));
}

async function renderVideo(context) {
  const ffmpeg = findFfmpeg();
  const args = [
    "-y",
    "-hide_banner",
    "-loglevel", "warning",
    "-stats",
    "-f", "rawvideo",
    "-pixel_format", "rgba",
    "-video_size", `${WIDTH}x${HEIGHT}`,
    "-framerate", String(FPS),
    "-i", "pipe:0",
    "-an",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    "-r", String(FPS),
    VIDEO_PATH,
  ];

  const process = spawn(ffmpeg, args, {
    stdio: ["pipe", "inherit", "inherit"],
  });

  const closed = new Promise((resolve, reject) => {
    process.on("error", reject);
    process.on("close", (code) => {
      if (code === 0) resolve();
      else reject(new Error(`FFmpeg terminó con código ${code}.`));
    });
  });

  for (let frame = 0; frame < TOTAL_FRAMES; frame += 1) {
    const time = frame / FPS;
    const buffer = await renderFrame(context, time, true);
    await writeToStream(process.stdin, buffer);
    if (frame % FPS === 0) {
      console.log(`Render: ${Math.round(time)}s / ${DURATION}s`);
    }
  }
  process.stdin.end();
  await closed;
}

async function renderPreviews(context) {
  const times = [0, 1.4, 7.2, 12.9, 18.5, 23.96];
  for (const time of times) {
    const output = path.join(PREVIEW_DIR, `frame-${String(time).replace(".", "_")}s.png`);
    fs.writeFileSync(output, await renderFrame(context, time, false));
  }
  console.log(PREVIEW_DIR);
}

async function main() {
  const context = await buildContext();
  if (process.argv.includes("--preview")) {
    await renderPreviews(context);
    return;
  }
  await renderVideo(context);
  console.log(VIDEO_PATH);
}

main().catch((error) => {
  console.error(error.stack || error.message || String(error));
  process.exit(1);
});
