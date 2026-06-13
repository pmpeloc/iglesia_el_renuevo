const fs = require("fs");
const path = require("path");
const sharp = require(
  "C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp"
);

const input = process.argv[2];
const outputDir = process.argv[3];

if (!input || !outputDir) {
  throw new Error("Usage: node split-transparent-logo.cjs <input> <output-dir>");
}

async function main() {
  fs.mkdirSync(outputDir, { recursive: true });

  const { data, info } = await sharp(input)
    .ensureAlpha()
    .raw()
    .toBuffer({ resolveWithObject: true });

  const { width, height, channels } = info;
  const labels = new Int32Array(width * height);
  const queue = new Int32Array(width * height);
  const components = [];
  let label = 0;

  for (let start = 0; start < labels.length; start += 1) {
    if (labels[start] !== 0 || data[start * channels + 3] < 8) continue;

    label += 1;
    let head = 0;
    let tail = 0;
    let count = 0;
    let minX = width;
    let minY = height;
    let maxX = 0;
    let maxY = 0;

    labels[start] = label;
    queue[tail++] = start;

    while (head < tail) {
      const index = queue[head++];
      const x = index % width;
      const y = Math.floor(index / width);

      count += 1;
      minX = Math.min(minX, x);
      minY = Math.min(minY, y);
      maxX = Math.max(maxX, x);
      maxY = Math.max(maxY, y);

      if (x > 0) visit(index - 1);
      if (x + 1 < width) visit(index + 1);
      if (y > 0) visit(index - width);
      if (y + 1 < height) visit(index + width);
    }

    components.push({ label, count, minX, minY, maxX, maxY });

    function visit(next) {
      if (labels[next] !== 0 || data[next * channels + 3] < 8) return;
      labels[next] = label;
      queue[tail++] = next;
    }
  }

  const selected = components
    .filter((component) => component.count > 1000)
    .sort((a, b) => b.count - a.count)
    .slice(0, 2);

  const names = ["cafe-emprendedor-logo.png", "cafe-emprendedor-icono.png"];

  for (let i = 0; i < selected.length; i += 1) {
    const component = selected[i];
    const padding = 10;
    const left = Math.max(0, component.minX - padding);
    const top = Math.max(0, component.minY - padding);
    const right = Math.min(width - 1, component.maxX + padding);
    const bottom = Math.min(height - 1, component.maxY + padding);
    const outWidth = right - left + 1;
    const outHeight = bottom - top + 1;
    const output = Buffer.alloc(outWidth * outHeight * 4);

    for (let y = top; y <= bottom; y += 1) {
      for (let x = left; x <= right; x += 1) {
        const sourceIndex = y * width + x;
        if (labels[sourceIndex] !== component.label) continue;

        const sourceOffset = sourceIndex * channels;
        const targetOffset = ((y - top) * outWidth + (x - left)) * 4;
        output[targetOffset] = data[sourceOffset];
        output[targetOffset + 1] = data[sourceOffset + 1];
        output[targetOffset + 2] = data[sourceOffset + 2];
        output[targetOffset + 3] = data[sourceOffset + 3];
      }
    }

    await sharp(output, {
      raw: { width: outWidth, height: outHeight, channels: 4 },
    })
      .png()
      .toFile(path.join(outputDir, names[i]));
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
