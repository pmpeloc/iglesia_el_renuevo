from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDF = ROOT / "raices-mockups-para-samira.pdf"
RENDER_DIR = ROOT / "_pdf-render"
CONTACT_SHEET = ROOT / "_qa-contact-sheet.png"

RENDER_DIR.mkdir(exist_ok=True)
reader = PdfReader(PDF)
if len(reader.pages) != 8:
    raise ValueError(f"Expected 8 pages, found {len(reader.pages)}")

document = pdfium.PdfDocument(PDF)
rendered = []
for index in range(len(document)):
    page = document[index]
    image = page.render(scale=0.6).to_pil().convert("RGB")
    output = RENDER_DIR / f"page-{index + 1}.png"
    image.save(output)
    rendered.append(image)

thumb_width = 234
thumb_height = 506
gap = 18
label_height = 26
sheet = Image.new("RGB", (thumb_width * 4 + gap * 5, (thumb_height + label_height) * 2 + gap * 3), "#dbe4df")
draw = ImageDraw.Draw(sheet)

for index, image in enumerate(rendered):
    image.thumbnail((thumb_width, thumb_height))
    column = index % 4
    row = index // 4
    x = gap + column * (thumb_width + gap)
    y = gap + row * (thumb_height + label_height + gap)
    sheet.paste(image, (x, y + label_height))
    draw.text((x, y + 4), f"{index + 1:02d}", fill="#173b35")

sheet.save(CONTACT_SHEET)
print(f"pages={len(reader.pages)} contact_sheet={CONTACT_SHEET}")
