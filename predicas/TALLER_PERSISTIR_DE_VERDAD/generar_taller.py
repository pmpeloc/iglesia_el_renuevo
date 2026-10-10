"""Genera hoja de actividades (DOCX), guía del líder (DOCX) y presentación (PPTX)
del taller "Persistir de verdad". Textos bíblicos: RVR1960."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "..", "..", "logos", "LOGO-EL RENUEVO-R-4.png")
TITULO = "PERSISTIR DE VERDAD"
FONT = "Arial"  # ponytail: Montserrat no está instalada en esta PC ni se sabe en la del proyector

# (pregunta, [opciones], índice correcto, (vers. A, vers. B), vers. correcto)
RONDAS = [
    {
        "titulo": "Cuando el escombro es mucho",
        "ref": "Nehemías 4 y 6",
        "versiculos": [
            ("4:3", "Y estaba junto a él Tobías amonita, el cual dijo: Lo que ellos edifican del muro de piedra, si subiere una zorra lo derribará."),
            ("4:6", "Edificamos, pues, el muro, y toda la muralla fue terminada hasta la mitad de su altura, porque el pueblo tuvo ánimo para trabajar."),
            ("4:9", "Entonces oramos a nuestro Dios, y por causa de ellos pusimos guarda contra ellos de día y de noche."),
            ("4:10", "Y dijo Judá: Las fuerzas de los acarreadores se han debilitado, y el escombro es mucho, y no podemos edificar el muro."),
            ("6:15", "Fue terminado, pues, el muro, el veinticinco del mes de Elul, en cincuenta y dos días."),
            ("6:16", "Y cuando lo oyeron todos nuestros enemigos, temieron todas las naciones que estaban alrededor de nosotros, y se sintieron humillados, y conocieron que por nuestro Dios había sido hecha esta obra."),
        ],
        "preguntas": [
            ("¿Qué amenazaba frenar la obra desde adentro del propio pueblo?",
             ["La burla de Tobías", "El cansancio de los que cargaban", "La conspiración para atacarlos"], 1,
             ("4:3", "4:10"), "4:10"),
            ("¿Cómo respondieron ante la amenaza de ataque?",
             ["Dejaron de trabajar hasta que pasara el peligro", "Solo oraron y esperaron que Dios los defendiera",
              "Oraron y además pusieron guardia día y noche"], 2,
             ("4:6", "4:9"), "4:9"),
            ("¿Qué reconocieron los enemigos cuando terminó el muro?",
             ["Que la obra había sido hecha por Dios", "Que Nehemías era un gran líder",
              "Que los judíos eran más fuertes de lo que creían"], 0,
             ("6:15", "6:16"), "6:16"),
        ],
        "conversen": "¿Cuál es el «escombro» que hoy nos hace decir «no podemos»?",
    },
    {
        "titulo": "Cuando la respuesta tarda",
        "ref": "Lucas 18",
        "versiculos": [
            ("18:1", "También les refirió Jesús una parábola sobre la necesidad de orar siempre, y no desmayar,"),
            ("18:3", "Había también en aquella ciudad una viuda, la cual venía a él, diciendo: Hazme justicia de mi adversario."),
            ("18:4", "Y él no quiso por algún tiempo; pero después de esto dijo dentro de sí: Aunque ni temo a Dios, ni tengo respeto a hombre,"),
            ("18:5", "sin embargo, porque esta viuda me es molesta, le haré justicia, no sea que viniendo de continuo, me agote la paciencia."),
            ("18:6", "Y dijo el Señor: Oíd lo que dijo el juez injusto."),
            ("18:7", "¿Y acaso Dios no hará justicia a sus escogidos, que claman a él día y noche? ¿Se tardará en responderles?"),
        ],
        "preguntas": [
            ("¿Para qué contó Jesús esta parábola?",
             ["Para enseñar cómo deben ser los jueces justos",
              "Para mostrar que Dios responde solo si insistimos lo suficiente",
              "Para enseñar a orar siempre y no desmayar"], 2,
             ("18:1", "18:6"), "18:1"),
            ("¿Qué obstáculo enfrentaba la viuda?",
             ["El juez no quiso atenderla por algún tiempo", "No tenía dinero para pagarle al juez",
              "Su adversario la amenazaba para que no fuera"], 0,
             ("18:3", "18:4"), "18:4"),
            ("¿En qué se parece Dios a este juez?",
             ["En que también tarda, para que aprendamos a insistir",
              "En nada: Jesús los contrasta; Dios sí hará justicia a los suyos",
              "En que responde para que dejemos de insistir"], 1,
             ("18:5", "18:7"), "18:7"),
        ],
        "conversen": "¿Qué oración dejamos de hacer porque «no pasaba nada»?",
    },
    {
        "titulo": "Cuando no se ve nada",
        "ref": "1 Reyes 18",
        "versiculos": [
            ("18:1", "Pasados muchos días, vino palabra de Jehová a Elías en el tercer año, diciendo: Ve, muéstrate a Acab, y yo haré llover sobre la faz de la tierra."),
            ("18:41", "Entonces Elías dijo a Acab: Sube, come y bebe; porque una lluvia grande se oye."),
            ("18:42", "Acab subió a comer y a beber. Y Elías subió a la cumbre del Carmelo, y postrándose en tierra, puso su rostro entre las rodillas."),
            ("18:43", "Y dijo a su criado: Sube ahora, y mira hacia el mar. Y él subió, y miró, y dijo: No hay nada. Y él le volvió a decir: Vuelve siete veces."),
            ("18:44", "A la séptima vez dijo: Yo veo una pequeña nube como la palma de la mano de un hombre, que sube del mar. Y él dijo: Ve, y di a Acab: Unce tu carro y desciende, para que la lluvia no te ataje."),
            ("18:45", "Y aconteció, estando en esto, que los cielos se oscurecieron con nubes y viento, y hubo una gran lluvia."),
        ],
        "preguntas": [
            ("¿Por qué Elías estaba seguro de que iba a llover?",
             ["Porque escuchaba el ruido de la lluvia", "Porque Dios ya lo había prometido",
              "Porque había visto nubes desde el monte"], 1,
             ("18:1", "18:41"), "18:1"),
            ("¿Qué hizo Elías cuando el criado le dijo «no hay nada»?",
             ["Le pidió a Dios otra señal", "Bajó del monte a esperar",
              "Lo mandó a mirar otra vez, hasta siete veces"], 2,
             ("18:42", "18:43"), "18:43"),
            ("¿Cómo fue la primera señal de la respuesta?",
             ["Una nube pequeña como la palma de una mano", "Un cielo oscuro y un viento fuerte",
              "Una gran lluvia de golpe"], 0,
             ("18:44", "18:45"), "18:44"),
        ],
        "conversen": "¿Cuál es la «nube pequeña» que Dios ya nos mostró y no estamos valorando?",
    },
]
AREAS = ["Oración por alguien", "Familia", "Servicio", "Trabajo o estudio", "Salud", "Otra: ____________"]
FRASE_FINAL = "Para Dios, el éxito no es ausencia de problemas, sino persistencia y fruto en medio de ellos."
LETRAS = "abc"
BASE = 15  # tamaño de letra de la hoja (mínimo 14)


# ---------------------------------------------------------------- DOCX helpers
def shade(paragraph, hex_fill):
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    pPr.append(shd)


def para(doc, text="", size=BASE, bold=False, color=None, before=0, after=2, indent=0, align=None, keep=True):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = 1.0
    pf.left_indent = Cm(indent)
    pf.keep_with_next = keep
    if align is not None:
        p.alignment = align
    if text:
        r = p.add_run(text)
        r.font.size, r.font.bold = Pt(size), bold
        if color:
            r.font.color.rgb = color
    return p


def run(p, text, size=BASE, bold=False, color=None):
    r = p.add_run(text)
    r.font.size, r.font.bold = Pt(size), bold
    if color:
        r.font.color.rgb = color
    return r


def barra(doc, text, size=18, before=6):
    p = para(doc, before=before, after=4)
    shade(p, "000000")
    run(p, " " + text, size=size, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
    return p


def nuevo_doc(margen=1.3):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    st.font.size = Pt(BASE)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin = sec.bottom_margin = Cm(margen)
    sec.left_margin = sec.right_margin = Cm(margen + 0.2)
    sec.header_distance = Cm(0.6)
    hp = sec.header.paragraphs[0]
    hp.paragraph_format.space_after = Pt(0)
    r = hp.add_run("Persistir de verdad · Taller en equipo")
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    if os.path.exists(LOGO):
        r = hp.add_run("\t\t")
        hp.add_run().add_picture(LOGO, height=Cm(0.8))
    return doc


# ------------------------------------------------------------ hoja de actividades
def hoja():
    doc = nuevo_doc()
    barra(doc, TITULO + " · TALLER EN EQUIPO", size=18, before=0)
    p = para(doc, after=4, keep=False)
    run(p, "Cómo trabajar: ", bold=True)
    run(p, "lean los versículos en la pantalla, marquen UNA respuesta, elijan qué versículo "
           "la indica y explíquenle a su compañero por qué.")
    for i, rd in enumerate(RONDAS, 1):
        barra(doc, f"RONDA {i} · {rd['titulo'].upper()}")
        for n, (preg, ops, _ok, (va, vb), _vok) in enumerate(rd["preguntas"], 1):
            p = para(doc, before=5, after=1)
            run(p, f"{n}. {preg}", bold=True)
            for k, op in enumerate(ops):
                para(doc, f"☐  {LETRAS[k]}) {op}", indent=0.6, after=0)
            p = para(doc, before=2, after=0, indent=0.6, keep=False)
            run(p, "Versículo:  ", bold=True)
            run(p, f"☐ {va}    ☐ {vb}     ")
            run(p, "¿Por qué? ", bold=True)
            run(p, "_" * 22)
        p = para(doc, before=5, after=2, keep=False)
        run(p, "Conversen: ", bold=True)
        run(p, rd["conversen"])
    barra(doc, "MI ÁREA PARA PERSISTIR")
    para(doc, "Marquemos un área y oremos uno por el otro:", after=2)
    para(doc, "     ".join("☐ " + a for a in AREAS[:3]), after=1)
    para(doc, "     ".join("☐ " + a for a in AREAS[3:]), after=0)
    out = os.path.join(HERE, "persistir_de_verdad_hoja.docx")
    doc.save(out)
    return out


# ------------------------------------------------------------------ guía líder
def guia():
    doc = nuevo_doc(margen=1.5)
    barra(doc, TITULO + " · GUÍA DEL LÍDER", before=0)
    para(doc, "0–3 apertura · 3–11 ronda 1 · 11–19 ronda 2 · 19–27 ronda 3 · "
              "27–35 puesta en común · 35–40 conclusión y oración", size=12, after=4, keep=False)
    for i, rd in enumerate(RONDAS, 1):
        barra(doc, f"RONDA {i} · {rd['titulo'].upper()}", size=14, before=4)
        for n, (preg, ops, ok, _v, vok) in enumerate(rd["preguntas"], 1):
            p = para(doc, after=1, keep=False)
            run(p, f"{n}. {preg}  ", size=12, bold=True)
            run(p, f"→ {LETRAS[ok]}) {ops[ok]} · v. {vok}", size=12)
    barra(doc, "PUESTA EN COMÚN (27–35)", size=14, before=4)
    para(doc, "Por pregunta: una pareja dice la respuesta y otra explica por qué eligió ese versículo. "
              "Al final: «¿Qué tienen en común Nehemías, la viuda y Elías?»", size=12, keep=False)
    barra(doc, "CONCLUSIÓN (35–40)", size=14, before=4)
    for t in [
        "Nehemías: los obstáculos vinieron en capas (burla, amenaza, cansancio). Oraron y trabajaron a la vez; muro terminado en 52 días (6:15).",
        "La viuda: Dios NO es como el juez; Jesús argumenta por contraste (v. 7). «Desmayar» (v. 1) es ekkakéō, la misma palabra de Gálatas 6:9 que vimos en «Persiste».",
        "Elías: tenía la promesa (18:1) y aun así oró y mandó a mirar siete veces. Lo opuesto a Joás, que se detuvo al tercer golpe. Santiago 5:17-18: era un hombre como nosotros.",
        "Patrón: los tres tenían un obstáculo real, siguieron sin ver el final, y Dios respondió.",
        "Cierre: cada uno marca «Mi área para persistir» y oran en parejas.",
        "Frase final: «" + FRASE_FINAL + "»",
    ]:
        para(doc, "• " + t, size=12, after=2, keep=False)
    out = os.path.join(HERE, "persistir_de_verdad_guia_lider.docx")
    doc.save(out)
    return out


# ------------------------------------------------------------------------ PPTX
INK, WHITE, GREEN = PRGB(0x1A, 0x1A, 0x1A), PRGB(0xFF, 0xFF, 0xFF), PRGB(0x5D, 0xBE, 0x2C)
GRAY = PRGB(0xBB, 0xBB, 0xBB)
SW, SH = Inches(13.333), Inches(7.5)


def pptx():
    prs = Presentation()
    prs.slide_width, prs.slide_height = SW, SH

    def slide():
        s = prs.slides.add_slide(prs.slide_layouts[6])
        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
        bg.fill.solid()
        bg.fill.fore_color.rgb = INK
        bg.line.fill.background()
        if os.path.exists(LOGO):
            s.shapes.add_picture(LOGO, SW - Inches(1.0), Inches(0.25), height=Inches(0.6))
        return s

    def text(s, x, y, w, h, lines, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
        """lines: [(texto, tamaño, bold, color)] o párrafos con runs: [[(t,sz,b,c),...]]"""
        tf = s.shapes.add_textbox(x, y, w, h).text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        for i, ln in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            p.space_after = PPt(6)
            for t, sz, b, c in (ln if isinstance(ln, list) else [ln]):
                r = p.add_run()
                r.text = t
                r.font.name, r.font.size, r.font.bold, r.font.color.rgb = FONT, PPt(sz), b, c
        return tf

    def centrado(lines):
        s = slide()
        text(s, Inches(0.8), Inches(0.5), Inches(11.7), Inches(6.2), lines, MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)
        return s

    centrado([("TALLER EN EQUIPO", 24, True, GREEN), (TITULO, 80, True, WHITE),
              ("Iglesia El Renuevo · Reunión General", 24, False, GRAY)])

    s = slide()
    text(s, Inches(0.8), Inches(0.5), Inches(11.7), Inches(1), [("¿CÓMO TRABAJAMOS?", 40, True, GREEN)])
    text(s, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.4), [
        ("1. Formamos parejas con la persona de al lado.", 34, False, WHITE),
        ("2. Leemos los versículos en la pantalla.", 34, False, WHITE),
        ("3. Marcamos UNA respuesta en la hoja.", 34, False, WHITE),
        ("4. Elegimos qué versículo la indica.", 34, False, WHITE),
        ("5. Le explicamos al compañero POR QUÉ.", 34, False, WHITE),
        ("3 rondas · 8 minutos cada una", 30, True, GREEN),
    ])

    for i, rd in enumerate(RONDAS, 1):
        centrado([(f"RONDA {i}", 36, True, GREEN), (rd["titulo"].upper(), 66, True, WHITE),
                  (rd["ref"], 36, False, GRAY)])
        s = slide()
        text(s, Inches(0.5), Inches(0.25), Inches(12.3), Inches(0.7),
             [[(f"RONDA {i} · ", 26, True, GREEN), (rd["titulo"].upper(), 26, True, WHITE),
               (f"   {rd['ref']} (RVR1960)", 22, False, GRAY)]])
        vs = rd["versiculos"]
        for col in range(2):
            text(s, Inches(0.5 + col * 6.25), Inches(1.1), Inches(6.0), Inches(6.1),
                 [[(f"{ref}  ", 24, True, GREEN), (t, 24, False, WHITE)] for ref, t in vs[col * 3:col * 3 + 3]])

    centrado([("PUESTA EN COMÚN", 66, True, WHITE)])
    for i, rd in enumerate(RONDAS, 1):
        s = slide()
        text(s, Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.9),
             [[(f"RONDA {i} · ", 36, True, GREEN), (rd["titulo"].upper(), 36, True, WHITE)]])
        lines = []
        for n, (preg, ops, ok, _v, vok) in enumerate(rd["preguntas"], 1):
            lines.append((f"{n}. {preg}", 26, True, WHITE))
            lines.append([(f"     {LETRAS[ok]}) {ops[ok]}", 26, False, GREEN), (f"  ·  v. {vok}", 26, True, GREEN)])
        text(s, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5), lines)
    centrado([("¿Qué tienen en común", 54, True, WHITE), ("Nehemías, la viuda y Elías?", 54, True, GREEN)])
    centrado([("«" + FRASE_FINAL + "»", 46, True, WHITE)])
    centrado([("MI ÁREA PARA PERSISTIR", 54, True, GREEN),
              ("Marquemos un área en la hoja", 36, False, WHITE),
              ("y oremos uno por el otro", 36, False, WHITE)])

    out = os.path.join(HERE, "persistir_de_verdad_presentacion.pptx")
    prs.save(out)
    return out


if __name__ == "__main__":
    for r in RONDAS:  # check: la respuesta correcta siempre es uno de los dos versículos ofrecidos
        for preg, ops, ok, par, vok in r["preguntas"]:
            assert vok in par and 0 <= ok < len(ops), preg
            assert vok in [v for v, _ in r["versiculos"]], vok
    print(hoja(), guia(), pptx(), sep="\n")
