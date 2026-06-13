const sharp = require(
  "C:/Users/pmpel/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp"
);

const input = process.argv[2];
const output = process.argv[3];

if (!input || !output) {
  throw new Error("Usage: node reframe-illustration.cjs <input> <output>");
}

const width = 1024;
const height = 1536;
const topSpace = 216;
const sceneHeight = height - topSpace;

const backdrop = Buffer.from(`
  <svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="${width}" height="${height}" fill="#fff4df"/>
    <path d="M0 0H205C105 66 41 143 31 260C24 349 59 423 122 480H0Z" fill="#321064"/>
    <path d="M1024 0V430C970 394 919 375 860 364C942 279 992 158 1024 0Z" fill="#ff674d"/>
    <path d="M0 305C115 281 210 291 307 335L283 454C190 419 93 411 0 430Z" fill="#2455e6"/>
  </svg>
`);

async function main() {
  const resizedScene = await sharp(input)
    .resize(width, sceneHeight, { fit: "fill" })
    .png()
    .toBuffer();

  const fadeMask = Buffer.from(`
    <svg width="${width}" height="${sceneHeight}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="white" stop-opacity="0"/>
          <stop offset="13%" stop-color="white" stop-opacity="1"/>
          <stop offset="100%" stop-color="white" stop-opacity="1"/>
        </linearGradient>
      </defs>
      <rect width="${width}" height="${sceneHeight}" fill="url(#fade)"/>
    </svg>
  `);

  const scene = await sharp(resizedScene)
    .composite([{ input: fadeMask, blend: "dest-in" }])
    .png()
    .toBuffer();

  await sharp(backdrop)
    .composite([{ input: scene, left: 0, top: topSpace }])
    .png()
    .toFile(output);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
