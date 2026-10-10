from pathlib import Path

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "raices-wireflow.png"
OUTPUT = ROOT / "raices-wireflow.pdf"

with Image.open(SOURCE) as image:
    width, height = image.size

canvas = Canvas(str(OUTPUT), pagesize=(width, height))
canvas.drawImage(ImageReader(str(SOURCE)), 0, 0, width, height)
canvas.showPage()
canvas.save()
print(OUTPUT)
