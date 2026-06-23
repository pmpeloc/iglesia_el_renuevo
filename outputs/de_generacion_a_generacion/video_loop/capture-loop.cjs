const fs = require("node:fs");
const path = require("node:path");

const { chromium } = require("C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/playwright@1.60.0/node_modules/playwright");

const folder = __dirname;
const htmlPath = path.join(folder, "de_generacion_a_generacion_loop.html");
const previewPath = path.join(folder, "de_generacion_a_generacion_preview.png");
const finalVideoPath = path.join(folder, "de_generacion_a_generacion_loop.webm");

const WIDTH = 1920;
const HEIGHT = 1080;
const DURATION_MS = 30000;

function toFileUrl(filePath) {
  return `file:///${filePath.replace(/\\/g, "/")}`;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: WIDTH, height: HEIGHT },
    deviceScaleFactor: 1,
    recordVideo: {
      dir: folder,
      size: { width: WIDTH, height: HEIGHT }
    }
  });

  const page = await context.newPage();
  await page.goto(toFileUrl(htmlPath), { waitUntil: "load" });
  await page.waitForFunction(() => window.__loopReady === true, null, { timeout: 10000 });
  await page.waitForTimeout(800);
  await page.screenshot({ path: previewPath, fullPage: false });
  await page.waitForTimeout(DURATION_MS);

  const recordedVideo = page.video();
  const rawVideoPath = await recordedVideo.path();
  await context.close();
  await browser.close();

  fs.copyFileSync(rawVideoPath, finalVideoPath);
  console.log(`Preview: ${previewPath}`);
  console.log(`Video: ${finalVideoPath}`);
})();
