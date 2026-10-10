import { chromium } from 'file:///C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import { mkdir } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const htmlPath = path.join(here, 'raices-mockups.html');
const pngDir = path.join(here, 'png');
await mkdir(pngDir, { recursive: true });

const browser = await chromium.launch({
  headless: true,
  executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
});
const page = await browser.newPage({ viewport: { width: 1600, height: 1100 }, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);

const screens = page.locator('.screen');
for (let index = 0; index < await screens.count(); index += 1) {
  const screen = screens.nth(index);
  const name = await screen.getAttribute('data-name');
  await screen.screenshot({ path: path.join(pngDir, `${name}.png`) });
}

await browser.close();
