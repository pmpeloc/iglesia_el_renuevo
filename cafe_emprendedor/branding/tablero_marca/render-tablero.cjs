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
    viewport: { width: 1600, height: 2400 },
    deviceScaleFactor: 1,
  });

  const htmlPath = path.join(__dirname, "tablero-marca.html");
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);

  await page.locator("#brand-board").screenshot({
    path: path.join(__dirname, "tablero-marca-cafe-emprendedor.png"),
  });

  await page.pdf({
    path: path.join(__dirname, "tablero-marca-cafe-emprendedor.pdf"),
    width: "1600px",
    height: "2400px",
    printBackground: true,
    pageRanges: "1",
  });

  await browser.close();
}

render().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
