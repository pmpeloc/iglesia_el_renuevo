const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require(
  "C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright"
);

async function render() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    headless: true,
  });
  const page = await browser.newPage({
    viewport: { width: 1280, height: 2100 },
    deviceScaleFactor: 1,
  });

  const htmlPath = path.join(__dirname, "flyer-preview.html");
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);

  await page.locator("#post").screenshot({
    path: path.join(__dirname, "cafe-emprendedor-publicacion-1080x1350.png"),
  });
  await page.locator("#story").screenshot({
    path: path.join(__dirname, "cafe-emprendedor-historia-1080x1920.png"),
  });

  await browser.close();
}

render().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
