from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
CURRENT_DIR = Path(__file__).resolve().parent
LOGO = ROOT / "logos" / "Identificador.png"

OUT_A4 = CURRENT_DIR / "espiritu_alma_y_cuerpo_apunte.pdf"
OUT_MOBILE = CURRENT_DIR / "espiritu_alma_y_cuerpo_mobile.pdf"

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(FONT_DIR / "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", str(FONT_DIR / "ariali.ttf")))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", str(FONT_DIR / "arialbi.ttf")))


TITLE = "ESPÍRITU, ALMA Y CUERPO"
RUNNING = "Espíritu, alma y cuerpo - Generación Selfie"
SERIES = "Generación Selfie - Mensaje 3"
BASE_TEXT = "1 Tesalonicenses 5:23"
VERSE = (
    "Y el mismo Dios de paz os santifique por completo; y todo vuestro ser, "
    "espíritu, alma y cuerpo, sea guardado irreprensible para la venida de "
    "nuestro Señor Jesucristo."
)
VERSE_REF = "1 Tesalonicenses 5:23 RVR1960"


CONTENT = [
    {
        "kind": "intro",
        "label": "Introducción",
        "text": (
            "Somos un ser integral: espíritu, alma y cuerpo. Dios no quiere tratar "
            "solo lo visible; Él quiere ordenar todo nuestro ser desde adentro."
        ),
    },
    {
        "kind": "point",
        "number": "1.",
        "title": "Dios obra adentro",
        "text": (
            "La transformación comienza en el hombre interior. Antes de cambiar lo "
            "que se ve, Dios quiere fortalecer lo que no siempre se ve."
        ),
        "subs": [
            (
                "a.",
                "El hombre interior",
                "Romanos 7:22, Efesios 3:16 y 2 Corintios 4:16 muestran que Dios trabaja en lo profundo: deleite, fortaleza y renovación interior.",
            ),
            (
                "b.",
                "El encuentro con Dios",
                "Nuestro espíritu se encuentra con el Espíritu de Dios. De allí nace la intimidad, la dirección y una vida que no depende solo de emociones.",
            ),
            (
                "c.",
                "Todo el ser responde",
                "En el Salmo 103, David le habla a su alma y a todo su ser. El interior da una orden: bendecir a Dios.",
            ),
        ],
        "app": "¿Estamos dejando que Dios nos ordene desde adentro, o vivimos reaccionando desde lo externo?",
    },
    {
        "kind": "point",
        "number": "2.",
        "title": "El orden correcto",
        "text": (
            "No vivimos por impulso. Somos guiados por Dios. El espíritu debe ser "
            "guiado por Dios, el alma debe alinearse y el cuerpo debe obedecer."
        ),
        "subs": [
            (
                "a.",
                "Espíritu guiado por Dios",
                "El espíritu no se alimenta de apariencia ni de aprobación, sino de la presencia de Dios.",
            ),
            (
                "b.",
                "Alma alineada",
                "Pensamientos, emociones, memoria, razón y voluntad necesitan rendirse a Dios para no gobernar sin dirección espiritual.",
            ),
            (
                "c.",
                "Cuerpo rendido",
                "Nuestros sentidos y hábitos responden a lo que repetimos. El cuerpo termina pidiendo aquello que aprendió a recibir.",
            ),
        ],
        "app": "Necesitamos reconocer quién está al mando: espíritu, alma o cuerpo.",
    },
    {
        "kind": "point",
        "number": "3.",
        "title": "Alimentar lo eterno",
        "text": (
            "Romanos 8 muestra dos maneras de vivir: según la carne o según el "
            "Espíritu. Aquello que alimentamos se fortalece."
        ),
        "subs": [
            (
                "a.",
                "La carne pide más",
                "Cuando alimentamos deseos, impulsos y hábitos sin Dios, eso gana fuerza y termina ocupando el centro.",
            ),
            (
                "b.",
                "El Espíritu da vida y paz",
                "Cuando alimentamos el espíritu con oración, Palabra, adoración y obediencia, crece el deseo por la presencia de Dios.",
            ),
            (
                "c.",
                "La disciplina prepara la victoria",
                "La victoria no empieza en el momento de la prueba; se prepara en lo que decidimos alimentar cada día.",
            ),
        ],
        "app": "Esta semana necesitamos decidir qué vamos a alimentar y qué vamos a dejar de alimentar.",
    },
    {
        "kind": "conclusion",
        "label": "Conclusión",
        "text": (
            "Lo que alimentamos se fortalece. Si no alimentamos la carne, se irá "
            "debilitando; si alimentamos el espíritu, todo nuestro ser buscará más "
            "de Dios."
        ),
    },
    {
        "kind": "challenge",
        "label": "Reto 7 días",
        "text": (
            "Durante esta semana elegimos una acción concreta para alimentar el "
            "espíritu: oración diaria, lectura de Romanos 8, ayuno de una app/red "
            "social o una obediencia específica."
        ),
    },
    {
        "kind": "response",
        "label": "Para responder",
        "items": [
            "Esta semana necesito dejar de alimentar:",
            "Esta semana voy a alimentar mi espíritu con:",
            "Mi horario para el reto de 7 días será:",
        ],
    },
]


def p(text: str) -> str:
    return escape(text).replace("\n", "<br/>")


def label_html(text: str, font_size: int) -> str:
    return (
        f'<font name="Arial-Bold" size="{font_size}" color="white" '
        f'backColor="black">{p(text)}</font>'
    )


def header_footer(canvas, doc):
    width, height = doc.pagesize
    canvas.saveState()
    if LOGO.exists():
        canvas.drawImage(str(LOGO), doc.leftMargin, height - 15 * mm, width=8 * mm, height=8 * mm, mask="auto")
    canvas.setFont("Arial-Italic", 8.5 if width < 400 else 9.5)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(doc.leftMargin + 10 * mm, height - 11.5 * mm, RUNNING)
    canvas.setFont("Arial-BoldItalic", 13 if width < 400 else 11)
    canvas.setFillColor(colors.black)
    canvas.drawRightString(width - doc.rightMargin, 7 * mm, str(doc.page))
    canvas.restoreState()


def make_styles(scale: str):
    if scale == "mobile":
        return {
            "body": ParagraphStyle(
                "body",
                fontName="Arial",
                fontSize=13.2,
                leading=18.4,
                alignment=TA_LEFT,
                spaceAfter=5,
            ),
            "body_just": ParagraphStyle(
                "body_just",
                fontName="Arial",
                fontSize=13.2,
                leading=18.4,
                alignment=TA_LEFT,
                spaceAfter=5,
            ),
            "sub": ParagraphStyle(
                "sub",
                fontName="Arial",
                fontSize=12.6,
                leading=17.5,
                leftIndent=17,
                firstLineIndent=-17,
                spaceAfter=4,
            ),
            "verse": ParagraphStyle(
                "verse",
                fontName="Arial",
                fontSize=17.4,
                leading=25,
                alignment=TA_CENTER,
            ),
            "verse_ref": ParagraphStyle(
                "verse_ref",
                fontName="Arial-Bold",
                fontSize=12.8,
                leading=16,
                alignment=TA_CENTER,
            ),
            "meta": ParagraphStyle(
                "meta",
                fontName="Arial-Italic",
                fontSize=13.2,
                leading=17,
                textColor=colors.HexColor("#666666"),
                spaceAfter=9,
            ),
            "base": ParagraphStyle(
                "base",
                fontName="Arial",
                fontSize=14.2,
                leading=18,
                spaceAfter=15,
            ),
            "title": 20,
            "label": 13,
        }
    return {
        "body": ParagraphStyle("body", fontName="Arial", fontSize=11.6, leading=14.6, alignment=TA_JUSTIFY, spaceAfter=4),
        "body_just": ParagraphStyle("body_just", fontName="Arial", fontSize=11.6, leading=14.6, alignment=TA_JUSTIFY, spaceAfter=4),
        "sub": ParagraphStyle("sub", fontName="Arial", fontSize=10.9, leading=13.7, leftIndent=17, firstLineIndent=-17, spaceAfter=3.2),
        "verse": ParagraphStyle("verse", fontName="Arial", fontSize=18.2, leading=24, alignment=TA_CENTER),
        "verse_ref": ParagraphStyle("verse_ref", fontName="Arial-Bold", fontSize=11.8, leading=14, alignment=TA_CENTER),
        "meta": ParagraphStyle("meta", fontName="Arial-Italic", fontSize=12.2, leading=15, textColor=colors.HexColor("#666666"), spaceAfter=8),
        "base": ParagraphStyle("base", fontName="Arial", fontSize=12.4, leading=15, spaceAfter=10),
        "title": 18,
        "label": 11.4,
    }


def title_bar(styles, width):
    t = Table(
        [[Paragraph(f'<font name="Arial-Bold" color="white" size="{styles["title"]}">{p(TITLE)}</font>', ParagraphStyle("tb", alignment=TA_CENTER, leading=styles["title"] + 5))]],
        colWidths=[width],
    )
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.black),
                ("BOX", (0, 0), (-1, -1), 0, colors.black),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return t


def verse_box(styles, width):
    inner = [
        Paragraph(f'"{p(VERSE)}"', styles["verse"]),
        Spacer(1, 5),
        Paragraph(p(VERSE_REF), styles["verse_ref"]),
    ]
    t = Table([[inner]], colWidths=[width])
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1.1, colors.black),
                ("LEFTPADDING", (0, 0), (-1, -1), 11),
                ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                ("TOPPADDING", (0, 0), (-1, -1), 13),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
            ]
        )
    )
    return t


def point_flow(item, styles):
    title = label_html(item["title"], styles["label"])
    flow = [
        Paragraph(f'<font name="Arial" size="{styles["label"] + 1}">{item["number"]}</font> {title} {p(item["text"])}', styles["body"]),
    ]
    for letter, sub_title, text in item["subs"]:
        flow.append(
            Paragraph(
                f"{letter} <b>{p(sub_title)}:</b> {p(text)}",
                styles["sub"],
            )
        )
    flow.append(Paragraph(f'<b>Aplicación:</b> {p(item["app"])}', styles["sub"]))
    return flow


def build_story(styles, width, mode):
    story = []
    story.append(title_bar(styles, width))
    story.append(Spacer(1, 12 if mode == "mobile" else 8))
    story.append(Paragraph(p(SERIES), styles["meta"]))
    story.append(Paragraph(f"<b>Texto base:</b> {p(BASE_TEXT)}", styles["base"]))
    story.append(verse_box(styles, width))
    story.append(Spacer(1, 14 if mode == "mobile" else 8))

    for item in CONTENT:
        if item["kind"] == "intro":
            story.append(Paragraph(f"{label_html(item['label'], styles['label'])} {p(item['text'])}", styles["body"]))
        elif item["kind"] == "point":
            if mode == "a4" and item["number"] == "3.":
                story.append(PageBreak())
            # Keep title + first subpoint together, but allow long point to flow naturally.
            flows = point_flow(item, styles)
            story.append(KeepTogether(flows[:2]))
            story.extend(flows[2:])
        elif item["kind"] in {"conclusion", "challenge"}:
            story.append(Paragraph(f"{label_html(item['label'], styles['label'])} {p(item['text'])}", styles["body"]))
        elif item["kind"] == "response":
            story.append(Paragraph(f"{label_html(item['label'], styles['label'])}", styles["body"]))
            for item_text in item["items"]:
                line = "_" * (18 if mode == "mobile" else 38)
                story.append(Paragraph(f"□ {p(item_text)}<br/>{line}", styles["sub"]))
        story.append(Spacer(1, 5 if mode == "mobile" else 3))
    return story


def build_pdf(path: Path, pagesize, mode: str, exactly_two=False):
    styles = make_styles(mode)
    if mode == "mobile":
        left = right = 8 * mm
        top = 25 * mm
        bottom = 13 * mm
    else:
        left = right = 15 * mm
        top = 20 * mm
        bottom = 13 * mm
    width, height = pagesize
    frame = Frame(left, bottom, width - left - right, height - top - bottom, id="normal")
    doc = BaseDocTemplate(
        str(path),
        pagesize=pagesize,
        leftMargin=left,
        rightMargin=right,
        topMargin=top,
        bottomMargin=bottom,
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=header_footer)])
    story = build_story(styles, width - left - right, mode)

    doc.build(story)


if __name__ == "__main__":
    build_pdf(OUT_MOBILE, (105 * mm, 190 * mm), "mobile")
    build_pdf(OUT_A4, A4, "a4", exactly_two=True)
    print(OUT_MOBILE)
    print(OUT_A4)
