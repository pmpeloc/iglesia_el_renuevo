from pathlib import Path

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from PIL import Image

ROOT = Path(__file__).resolve().parent
PNG_DIR = ROOT / "png"
OUTPUT = ROOT / "raices-mockups-para-samira.pdf"

images = sorted(PNG_DIR.glob("*.png"))
if not images:
    raise SystemExit("No mockup PNGs found")

first = Image.open(images[0])
page_size = (first.width, first.height)
canvas = Canvas(str(OUTPUT), pagesize=page_size)

for image_path in images:
    with Image.open(image_path) as image:
        if image.size != page_size:
            raise ValueError(f"Unexpected image size: {image_path.name} {image.size}")
    canvas.drawImage(ImageReader(str(image_path)), 0, 0, page_size[0], page_size[1])
    canvas.showPage()

canvas.save()
print(OUTPUT)
