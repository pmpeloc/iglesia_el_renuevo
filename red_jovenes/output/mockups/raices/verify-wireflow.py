from pathlib import Path

import pypdfium2 as pdfium
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDF = ROOT / "raices-wireflow.pdf"
OUTPUT = ROOT / "_qa-wireflow-pdf.png"

reader = PdfReader(PDF)
if len(reader.pages) != 1:
    raise ValueError(f"Expected 1 page, found {len(reader.pages)}")

document = pdfium.PdfDocument(PDF)
page = document[0]
image = page.render(scale=0.55).to_pil().convert("RGB")
image.save(OUTPUT)
print(f"pages=1 render={OUTPUT}")
