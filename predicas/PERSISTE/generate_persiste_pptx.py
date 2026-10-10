import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# 16:9 Dimensions
SW = Inches(13.333)
SH = Inches(7.5)

# Brand Colors
CREAM = RGBColor(0xF7, 0xF1, 0xE8)
INK = RGBColor(0x1A, 0x1A, 0x1A)
GREEN = RGBColor(0x5D, 0xBE, 0x2C)
GREEN_DEEP = RGBColor(0x4A, 0x9E, 0x22)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY_CARD = RGBColor(0xEA, 0xE4, 0xDA)
GRAY_TEXT = RGBColor(0x77, 0x77, 0x77)
GRAY_LIGHT = RGBColor(0xF0, 0xEA, 0xDF)

# Fonts
FONT_TITLE = "Anton"
FONT_BODY = "Montserrat"
FONT_QUOTE = "Playfair Display"

LOGO_PATH = r"C:\Users\pmpel\projects\iglesia_el_renuevo\predicas\Predica General\assets\mark-green.png"
if not os.path.exists(LOGO_PATH):
    LOGO_PATH = r"C:\Users\pmpel\projects\iglesia_el_renuevo\logos\LOGO-EL RENUEVO-R-4.png"

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    blank_layout = prs.slide_layouts[6]

    def add_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_corner_logo(slide):
        if os.path.exists(LOGO_PATH):
            logo_w = Inches(0.7)
            logo_h = Inches(0.7)
            slide.shapes.add_picture(LOGO_PATH, SW - logo_w - Inches(0.6), Inches(0.5), width=logo_w, height=logo_h)

    def add_kicker(slide, text, top=Inches(0.6), left=Inches(0.8), color=GREEN_DEEP):
        tx_box = slide.shapes.add_textbox(left, top, Inches(10), Inches(0.5))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text.upper()
        p.font.name = FONT_BODY
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color
        return tx_box

    # =========================================================================
    # SLIDE 1: PORTADA (INK BG)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, INK)
    add_corner_logo(s1)

    # Eyebrow / Kicker
    add_kicker(s1, "IGLESIA EL RENUEVO · MCYM · REUNIÓN GENERAL", top=Inches(1.2), left=Inches(1.0), color=GREEN)

    # Hero Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "PERSISTE"
    p.font.name = FONT_TITLE
    p.font.size = Pt(100)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Subtitle with green highlight pill
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.2), Inches(7.5), Inches(0.65))
    pill.fill.solid()
    pill.fill.fore_color.rgb = GREEN
    pill.line.fill.background()
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.alignment = PP_ALIGN.CENTER
    p_pill.text = "LA FIDELIDAD EN LOS PROCESOS DE DIOS"
    p_pill.font.name = FONT_BODY
    p_pill.font.size = Pt(15)
    p_pill.font.bold = True
    p_pill.font.color.rgb = INK

    # Base Scripture quote
    v_box = s1.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.4))
    v_tf = v_box.text_frame
    v_tf.word_wrap = True
    p = v_tf.paragraphs[0]
    p.text = "«No nos cansemos, pues, de hacer bien; porque a su tiempo segaremos, si no desmayamos»."
    p.font.name = FONT_QUOTE
    p.font.size = Pt(22)
    p.font.italic = True
    p.font.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)

    p2 = v_tf.add_paragraph()
    p2.text = "GÁLATAS 6:9"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 2: INTRODUCCIÓN (CREAM BG)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2, CREAM)
    add_corner_logo(s2)
    add_kicker(s2, "INTRODUCCIÓN")

    t_box = s2.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.7), Inches(1.8))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "LA TENTACIÓN DE AFLOJAR A MITAD DE CAMINO"
    p.font.name = FONT_TITLE
    p.font.size = Pt(54)
    p.font.color.rgb = INK

    # Two columns / comparison cards
    card1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.2), Inches(5.6), Inches(3.4))
    card1.fill.solid()
    card1.fill.fore_color.rgb = WHITE
    card1.line.color.rgb = GRAY_CARD
    card1.line.width = Pt(1.5)
    tf1 = card1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "LA CULTURA DE LA INMEDIATEZ"
    p.font.name = FONT_BODY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
    p = tf1.add_paragraph()
    p.text = "\n• Queremos respuestas instantáneas y atajos rápidos.\n• Empezamos con gran entusiasmo pero sin raíz.\n• Ante la rutina o la demora, abandonamos."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    card2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.2), Inches(5.6), Inches(3.4))
    card2.fill.solid()
    card2.fill.fore_color.rgb = INK
    card2.line.fill.background()
    tf2 = card2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "LA PEDAGOGÍA DE DIOS"
    p.font.name = FONT_BODY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = tf2.add_paragraph()
    p.text = "\n• Dios no forma el carácter en un microondas espiritual.\n• El Reino trabaja a través de procesos profundos.\n• La victoria pertenece a quienes perseveran."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 3: IDEA CENTRAL (CREAM BG + BLACK CARD)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3, CREAM)
    add_corner_logo(s3)
    add_kicker(s3, "IDEA CENTRAL DEL MENSAJE")

    bcard = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.0))
    bcard.fill.solid()
    bcard.fill.fore_color.rgb = INK
    bcard.line.color.rgb = GREEN
    bcard.line.width = Pt(2)
    b_tf = bcard.text_frame
    b_tf.word_wrap = True

    p = b_tf.paragraphs[0]
    p.text = "LA VERDAD CLAVE DE ESTA NOCHE"
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = GREEN

    p = b_tf.add_paragraph()
    p.text = "\n«La constancia espiritual no consiste en la ausencia de cansancio, sino en negarnos a abandonar el propósito de Dios frente al conformismo, la oposición o la falta de resultados inmediatos.»"
    p.font.name = FONT_QUOTE
    p.font.size = Pt(26)
    p.font.italic = True
    p.font.color.rgb = WHITE

    p = b_tf.add_paragraph()
    p.text = "\nPara Dios, el éxito y la bendición no significan ausencia de problemas, sino persistencia y fruto en medio de ellos."
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 4: PUNTO 1 (CREAM BG)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4, CREAM)
    add_corner_logo(s4)
    add_kicker(s4, "PRIMER PUNTO")

    # Big green number
    num_box = s4.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(2.5), Inches(2.2))
    num_tf = num_box.text_frame
    p = num_tf.paragraphs[0]
    p.text = "01"
    p.font.name = FONT_TITLE
    p.font.size = Pt(110)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # Title in Anton
    t_box = s4.shapes.add_textbox(Inches(3.2), Inches(1.2), Inches(9.3), Inches(2.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EL PELIGRO DE ABANDONAR ANTES DE TIEMPO"
    p.font.name = FONT_TITLE
    p.font.size = Pt(54)
    p.font.color.rgb = INK

    # Content box
    box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.5), Inches(11.7), Inches(3.2))
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = GRAY_CARD
    box.line.width = Pt(1.5)
    b_tf = box.text_frame
    b_tf.word_wrap = True
    p = b_tf.paragraphs[0]
    p.text = "2 REYES 13:18-19 · EL REY JOÁS Y EL PROFETA ELISEO"
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = GREEN_DEEP

    p = b_tf.add_paragraph()
    p.text = "«Y él la golpeó tres veces, y se detuvo. Entonces el varón de Dios, enojado contra él, dijo: De haber dado cinco o seis golpes, habrías derrotado a Siria hasta consumirla...»"
    p.font.name = FONT_QUOTE
    p.font.size = Pt(20)
    p.font.italic = True
    p.font.color.rgb = INK

    p = b_tf.add_paragraph()
    p.text = "\n• Joás no falló por mala puntería ni falta de armas; falló por conformismo interior.\n• Dio tres golpes superficiales por cumplir el trámite y se detuvo antes de tiempo.\n• La falta de persistencia achicó la dimensión de la victoria que Dios quería otorgarle."
    p.font.name = FONT_BODY
    p.font.size = Pt(17)
    p.font.color.rgb = INK

    # =========================================================================
    # SLIDE 5: ILUSTRACIÓN 1 (CREAM BG)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5, CREAM)
    add_corner_logo(s5)
    add_kicker(s5, "ILUSTRACIÓN · PUNTO 01")

    t_box = s5.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.7), Inches(1.2))
    tf = t_box.text_frame
    p = tf.paragraphs[0]
    p.text = "EL MARTILLO DEL PICAPEDRERO"
    p.font.name = FONT_TITLE
    p.font.size = Pt(50)
    p.font.color.rgb = INK

    card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.5), Inches(11.7), Inches(4.3))
    card.fill.solid()
    card.fill.fore_color.rgb = INK
    card.line.fill.background()
    c_tf = card.text_frame
    c_tf.word_wrap = True

    p = c_tf.paragraphs[0]
    p.text = "«Cuando siento que nada me ayuda, voy a mirar al picapedrero martillando su roca. Quizás le da cien golpes seguidos y la piedra no muestra ni una sola grieta visible. Pero al golpe ciento uno, la roca se parte en dos.\n\nY sé perfectamente que no fue ese último golpe el que la quebró, sino los cien golpes anteriores que nadie celebró»."
    p.font.name = FONT_QUOTE
    p.font.size = Pt(22)
    p.font.italic = True
    p.font.color.rgb = WHITE

    p = c_tf.add_paragraph()
    p.text = "\n— Jacob Riis (Periodista social)"
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.color.rgb = GREEN

    p = c_tf.add_paragraph()
    p.text = "EL RIESGO ESPIRITUAL: Muchas veces nos detenemos en el golpe número 3, justo a pocos pasos de quebrar la dureza de una situación."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 6: APLICACIÓN 1 (BLACKCARD)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6, CREAM)
    add_corner_logo(s6)
    add_kicker(s6, "APLICACIÓN")

    bcard = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.0))
    bcard.fill.solid()
    bcard.fill.fore_color.rgb = INK
    bcard.line.color.rgb = GREEN
    bcard.line.width = Pt(2)
    b_tf = bcard.text_frame
    b_tf.word_wrap = True

    p = b_tf.paragraphs[0]
    p.text = "¿EN QUÉ ÁREAS HEMOS SOLTADO LAS FLECHAS?"
    p.font.name = FONT_TITLE
    p.font.size = Pt(36)
    p.font.color.rgb = GREEN

    p = b_tf.add_paragraph()
    p.text = "\n• ¿En la oración por un hijo o familiar que aún no conoce al Señor?\n• ¿En el esfuerzo silencioso por reconstruir nuestro matrimonio?\n• ¿En un proyecto de trabajo o servicio que se tornó monótono?"
    p.font.name = FONT_BODY
    p.font.size = Pt(21)
    p.font.color.rgb = WHITE

    p = b_tf.add_paragraph()
    p.text = "\nDESAFÍO PASTORAL: Necesitamos pedirle a Dios la determinación de no conformarnos con victorias a medias. Debemos volver a tomar las saetas de la fe y seguir golpeando hasta ver su obra completa."
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 7: PUNTO 2 (CREAM BG)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7, CREAM)
    add_corner_logo(s7)
    add_kicker(s7, "SEGUNDO PUNTO")

    num_box = s7.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(2.5), Inches(2.2))
    num_tf = num_box.text_frame
    p = num_tf.paragraphs[0]
    p.text = "02"
    p.font.name = FONT_TITLE
    p.font.size = Pt(110)
    p.font.bold = True
    p.font.color.rgb = GREEN

    t_box = s7.shapes.add_textbox(Inches(3.2), Inches(1.2), Inches(9.3), Inches(2.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SEGUIR CAVANDO SIN AMARGARNOS ANTE LA OPOSICIÓN"
    p.font.name = FONT_TITLE
    p.font.size = Pt(48)
    p.font.color.rgb = INK

    box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.5), Inches(11.7), Inches(3.2))
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = GRAY_CARD
    box.line.width = Pt(1.5)
    b_tf = box.text_frame
    b_tf.word_wrap = True
    p = b_tf.paragraphs[0]
    p.text = "GÉNESIS 26:15-22 · ISAAC EN EL VALLE DE GERAR"
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = GREEN_DEEP

    p = b_tf.add_paragraph()
    p.text = "«Y todos los pozos que habían abierto los criados de Abraham su padre... los filisteos los habían cegado y llenado de tierra.»"
    p.font.name = FONT_QUOTE
    p.font.size = Pt(20)
    p.font.italic = True
    p.font.color.rgb = INK

    p = b_tf.add_paragraph()
    p.text = "\n• En el desierto, tapar un pozo era un ataque a la subsistencia familiar.\n• Isaac enfrentó envidia, hostilidad y bloqueo sistemático.\n• Su respuesta no fue la violencia ni la queja: no se amargó y siguió cavando."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    # =========================================================================
    # SLIDE 8: LOS 3 POZOS (CREAM BG + 3 CARDS)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8, CREAM)
    add_corner_logo(s8)
    add_kicker(s8, "GÉNESIS 26:19-22 · LA PROGRESIÓN DE ISAAC")

    # 3 Columns
    col_w = Inches(3.64)
    gap = Inches(0.4)
    left_base = Inches(0.8)

    # Card 1: ESEK
    c1 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base, Inches(1.8), col_w, Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = GRAY_CARD
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "1. ESEK (עֵשֶׂק)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.color.rgb = INK
    p = tf1.add_paragraph()
    p.text = "«CONTIENDA O LITIGIO»\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
    p = tf1.add_paragraph()
    p.text = "Los pastores riñeron diciendo: «El agua es nuestra».\n\nIsaac no se estancó en una guerra judicial estéril. Soltó el pozo y avanzó."
    p.font.name = FONT_BODY
    p.font.size = Pt(17)
    p.font.color.rgb = INK

    # Card 2: SITNA
    c2 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base + col_w + gap, Inches(1.8), col_w, Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = WHITE
    c2.line.color.rgb = GRAY_CARD
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "2. SITNA (שִׂטְנָה)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.color.rgb = INK
    p = tf2.add_paragraph()
    p.text = "«ENEMISTAD U OPOSICIÓN»\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xD3, 0x54, 0x00)
    p = tf2.add_paragraph()
    p.text = "Hostilidad directa (raíz de acusador/adversario).\n\nCualquiera hubiera renunciado. Isaac cuidó su corazón del veneno del rencor y volvió a cavar."
    p.font.name = FONT_BODY
    p.font.size = Pt(17)
    p.font.color.rgb = INK

    # Card 3: REHOBOT (INK)
    c3 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base + (col_w + gap)*2, Inches(1.8), col_w, Inches(5.0))
    c3.fill.solid()
    c3.fill.fore_color.rgb = INK
    c3.line.color.rgb = GREEN
    c3.line.width = Pt(2)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "3. REHOBOT (רְחֹבוֹת)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.color.rgb = GREEN
    p = tf3.add_paragraph()
    p.text = "«ESPACIO AMPLIO Y FRUTO»\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p = tf3.add_paragraph()
    p.text = "«Porque ahora Jehová nos ha hecho prosperar, y fructificaremos en la tierra» (v. 22).\n\nYa no pelearon sobre él. La constancia abrió paso a la bendición."
    p.font.name = FONT_BODY
    p.font.size = Pt(17)
    p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 9: ILUSTRACIÓN 2 (CREAM BG)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9, CREAM)
    add_corner_logo(s9)
    add_kicker(s9, "ILUSTRACIÓN · PUNTO 02")

    t_box = s9.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.7), Inches(1.2))
    tf = t_box.text_frame
    p = tf.paragraphs[0]
    p.text = "EL VUELO DEL ÁGUILA Y EL CUERVO"
    p.font.name = FONT_TITLE
    p.font.size = Pt(50)
    p.font.color.rgb = INK

    card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.5), Inches(11.7), Inches(4.3))
    card.fill.solid()
    card.fill.fore_color.rgb = INK
    card.line.fill.background()
    c_tf = card.text_frame
    c_tf.word_wrap = True

    p = c_tf.paragraphs[0]
    p.text = "En el reino de las aves, el único pájaro que se atreve a atacar y picotear el lomo de un águila en pleno vuelo es el cuervo.\n\nSin embargo, el águila no pierde su tiempo ni gasta energías peleando con él. Simplemente abre sus grandes alas y comienza a elevarse a mayor altitud.\n\nA medida que el águila sube, el aire se enrarece y el oxígeno disminuye drásticamente, hasta que el cuervo no puede respirar y cae por su propio peso."
    p.font.name = FONT_BODY
    p.font.size = Pt(21)
    p.font.color.rgb = WHITE

    p = c_tf.add_paragraph()
    p.text = "\nPRINCIPIO: Isaac no gastó sus años peleando en Esek o Sitna; se elevó en madurez espiritual, siguió cavando y Dios lo llevó a Rehobot."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 10: APLICACIÓN 2 (BLACKCARD)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10, CREAM)
    add_corner_logo(s10)
    add_kicker(s10, "APLICACIÓN")

    bcard = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.0))
    bcard.fill.solid()
    bcard.fill.fore_color.rgb = INK
    bcard.line.color.rgb = GREEN
    bcard.line.width = Pt(2)
    b_tf = bcard.text_frame
    b_tf.word_wrap = True

    p = b_tf.paragraphs[0]
    p.text = "¿CUÁNTA ENERGÍA PERDEMOS EN ESEK Y SITNA?"
    p.font.name = FONT_TITLE
    p.font.size = Pt(36)
    p.font.color.rgb = GREEN

    p = b_tf.add_paragraph()
    p.text = "\n• En el trabajo cuando nos «tapan el pozo» o nos quitan el crédito.\n• En la familia cuando surgen roces que quieren robarnos la paz.\n• En el ministerio ante incomprensiones o palabras hirientes."
    p.font.name = FONT_BODY
    p.font.size = Pt(21)
    p.font.color.rgb = WHITE

    p = b_tf.add_paragraph()
    p.text = "\nDESAFÍO PASTORAL: Debemos negarnos a gastar la vida en pleitos estériles. Nos toca sacudirnos la ofensa, proteger nuestro corazón de la amargura y seguir cavando con fidelidad hasta que Dios nos abra paso a nuestro Rehobot."
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 11: PUNTO 3 (CREAM BG)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11, CREAM)
    add_corner_logo(s11)
    add_kicker(s11, "TERCER PUNTO")

    num_box = s11.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(2.5), Inches(2.2))
    num_tf = num_box.text_frame
    p = num_tf.paragraphs[0]
    p.text = "03"
    p.font.name = FONT_TITLE
    p.font.size = Pt(110)
    p.font.bold = True
    p.font.color.rgb = GREEN

    t_box = s11.shapes.add_textbox(Inches(3.2), Inches(1.2), Inches(9.3), Inches(2.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "LA CONSTANCIA SILENCIOSA QUE ECHA RAÍCES PROFUNDAS"
    p.font.name = FONT_TITLE
    p.font.size = Pt(46)
    p.font.color.rgb = INK

    box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.5), Inches(11.7), Inches(3.2))
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = GRAY_CARD
    box.line.width = Pt(1.5)
    b_tf = box.text_frame
    b_tf.word_wrap = True
    p = b_tf.paragraphs[0]
    p.text = "GÁLATAS 6:9 · LA PROMESA DE LA COSECHA A SU TIEMPO"
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = GREEN_DEEP

    p = b_tf.add_paragraph()
    p.text = "«No nos cansemos, pues, de hacer bien; porque a su tiempo segaremos, si no desmayamos.»"
    p.font.name = FONT_QUOTE
    p.font.size = Pt(22)
    p.font.italic = True
    p.font.color.rgb = INK

    p = b_tf.add_paragraph()
    p.text = "\n• Entre la siembra fiel y la cosecha visible, media un tiempo donde parece que nada pasa.\n• La promesa no dice «si no nos cansamos», sino «si no desmayamos».\n• El cansancio físico es natural; desmayar es rendir el corazón."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    # =========================================================================
    # SLIDE 12: EXÉGESIS BÍBLICA (CREAM BG + 2 CARDS)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12, CREAM)
    add_corner_logo(s12)
    add_kicker(s12, "PROFUNDIDAD BÍBLICA · DOS TÉRMINOS GRIEGOS CLAVE")

    c1 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = GRAY_CARD
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "EKKAKEŌ (ἐκκακέω)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(30)
    p.font.color.rgb = INK
    p = tf1.add_paragraph()
    p.text = "«DESMAYAR O PERDER EL VALOR»\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
    p = tf1.add_paragraph()
    p.text = "• Desfallecer en el interior antes de que se note afuera.\n• El desgaste sutil que murmura: «¿Para qué sigo orando si nada cambia?»\n• Es aflojar la guardia de la fe en el corazón."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    c2 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = INK
    c2.line.color.rgb = GREEN
    c2.line.width = Pt(2)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "HYPOMONĒ (ὑπομονή)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(30)
    p.font.color.rgb = GREEN
    p = tf2.add_paragraph()
    p.text = "«PERMANECER FIRME BAJO EL PESO»\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p = tf2.add_paragraph()
    p.text = "• Hypo (debajo) + Menō (permanecer).\n• Hebreos 10:36: «Os es necesaria la paciencia...»\n• No es resignación quejosa, sino la capacidad activa de sostenerse sin doblarse."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 13: ILUSTRACIÓN 3 (CREAM BG)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13, CREAM)
    add_corner_logo(s13)
    add_kicker(s13, "ILUSTRACIÓN · PUNTO 03")

    t_box = s13.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.7), Inches(1.2))
    tf = t_box.text_frame
    p = tf.paragraphs[0]
    p.text = "LA PARÁBOLA DEL BAMBÚ JAPONÉS"
    p.font.name = FONT_TITLE
    p.font.size = Pt(50)
    p.font.color.rgb = INK

    card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.5), Inches(11.7), Inches(4.3))
    card.fill.solid()
    card.fill.fore_color.rgb = INK
    card.line.fill.background()
    c_tf = card.text_frame
    c_tf.word_wrap = True

    p = c_tf.paragraphs[0]
    p.text = "Cuando se siembra la semilla del bambú japonés, se riega y fertiliza durante SIETE AÑOS SEGUIDOS sin que se vea un solo brote en la superficie.\n\nPara quien no conoce la especie, pensaría que la tierra es estéril. Pero al séptimo año, en solo seis semanas, el bambú crece más de 30 metros de altura.\n\n¿Creció en seis semanas o en siete años? Indudablemente en siete años: todo ese tiempo estuvo echando raíces subterráneas masivas para sostener la estructura futura."
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.color.rgb = WHITE

    p = c_tf.add_paragraph()
    p.text = "\nPRINCIPIO: Cuando parece que nada se mueve afuera, Dios está forjando raíces profundas adentro."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 14: APLICACIÓN 3 (BLACKCARD)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14, CREAM)
    add_corner_logo(s14)
    add_kicker(s14, "APLICACIÓN")

    bcard = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.0))
    bcard.fill.solid()
    bcard.fill.fore_color.rgb = INK
    bcard.line.color.rgb = GREEN
    bcard.line.width = Pt(2)
    b_tf = bcard.text_frame
    b_tf.word_wrap = True

    p = b_tf.paragraphs[0]
    p.text = "¿DÓNDE SENTIMOS QUE EL ESFUERZO NO DA FRUTO?"
    p.font.name = FONT_TITLE
    p.font.size = Pt(36)
    p.font.color.rgb = GREEN

    p = b_tf.add_paragraph()
    p.text = "\n• En la crianza diaria de nuestros hijos.\n• En la disciplina de la oración cuando el cielo parece en silencio.\n• En la fidelidad de servir y trabajar con excelencia día a día."
    p.font.name = FONT_BODY
    p.font.size = Pt(21)
    p.font.color.rgb = WHITE

    p = b_tf.add_paragraph()
    p.text = "\nDESAFÍO PASTORAL: Debemos recordar que ninguna oración, ninguna lágrima y ninguna siembra en Dios queda en el olvido. Necesitamos perseverar sabiendo que a su tiempo segaremos si no desmayamos."
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 15: CLÍMAX TEOLÓGICO (INK BG)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_bg(s15, INK)
    add_corner_logo(s15)
    add_kicker(s15, "LA GRAN VERDAD DE CIERRE", color=GREEN)

    t_box = s15.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(4.2))
    tf = t_box.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "«PARA DIOS, EL ÉXITO Y LA BENDICIÓN NO SIGNIFICAN AUSENCIA DE PROBLEMAS,"
    p.font.name = FONT_TITLE
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = WHITE

    p2 = tf.add_paragraph()
    p2.text = "SINO PERSISTENCIA Y FRUTO EN MEDIO DE ELLOS»."
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(46)
    p2.font.bold = True
    p2.font.color.rgb = GREEN

    p3 = tf.add_paragraph()
    p3.text = "\nNo esperemos que todo esté calmo para buscar a Dios con constancia. La madurez cristiana consiste en dar fruto aun en medio de la tensión."
    p3.font.name = FONT_BODY
    p3.font.size = Pt(22)
    p3.font.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)

    # =========================================================================
    # SLIDE 16: TESTIMONIOS BÍBLICOS (CREAM BG + 3 CARDS)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16, CREAM)
    add_corner_logo(s16)
    add_kicker(s16, "FRUCTIFICAR EN MEDIO DE LA DIFICULTAD")

    # 3 Cards
    # Card 1: ISAAC
    c1 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base, Inches(1.8), col_w, Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = GRAY_CARD
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "ISAAC"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.color.rgb = INK
    p = tf1.add_paragraph()
    p.text = "GÉNESIS 26:22\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GREEN_DEEP
    p = tf1.add_paragraph()
    p.text = "Dios no eliminó a los filisteos para darle agua.\n\nIsaac siguió cavando hasta que brotó Rehobot en la misma tierra de la hambruna."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    # Card 2: JOSÉ
    c2 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base + col_w + gap, Inches(1.8), col_w, Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = WHITE
    c2.line.color.rgb = GRAY_CARD
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "JOSÉ (EFRAÍN)"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.color.rgb = INK
    p = tf2.add_paragraph()
    p.text = "GÉNESIS 41:52\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GREEN_DEEP
    p = tf2.add_paragraph()
    p.text = "«Dios me hizo fructificar en la tierra de mi aflicción».\n\nNo necesitó salir de Egipto para experimentar la bendición de Dios."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = INK

    # Card 3: DAVID
    c3 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_base + (col_w + gap)*2, Inches(1.8), col_w, Inches(5.0))
    c3.fill.solid()
    c3.fill.fore_color.rgb = INK
    c3.line.color.rgb = GREEN
    c3.line.width = Pt(2)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "DAVID"
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.color.rgb = GREEN
    p = tf3.add_paragraph()
    p.text = "SALMO 23:5 · SALMO 4:1\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p = tf3.add_paragraph()
    p.text = "«Aderezas mesa delante de mí en presencia de mis angustiadores».\n\n«En la angustia me hiciste ensanchar». Dios sirve la mesa en medio de la prueba."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 17: LLAMADO FINAL (INK BG)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_bg(s17, INK)
    add_corner_logo(s17)
    add_kicker(s17, "LLAMADO FINAL", color=GREEN)

    t_box = s17.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.3), Inches(1.2))
    tf = t_box.text_frame
    p = tf.paragraphs[0]
    p.text = "PERSISTE: LA HORA DE AVANZAR"
    p.font.name = FONT_TITLE
    p.font.size = Pt(56)
    p.font.color.rgb = WHITE

    # 3 Bullet Points Callout Box
    call_box = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.7), Inches(11.3), Inches(3.6))
    call_box.fill.solid()
    call_box.fill.fore_color.rgb = RGBColor(0x26, 0x26, 0x26)
    call_box.line.color.rgb = GREEN
    call_box.line.width = Pt(1.5)
    c_tf = call_box.text_frame
    c_tf.word_wrap = True

    p = c_tf.paragraphs[0]
    p.text = "1. VOLVAMOS A TOMAR LAS SAETAS"
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = c_tf.add_paragraph()
    p.text = "   No nos conformemos con tres golpes; vayamos por la victoria completa de Dios.\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    p = c_tf.add_paragraph()
    p.text = "2. DEJEMOS ATRÁS ESEK Y SITNA"
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = c_tf.add_paragraph()
    p.text = "   Soltemos las peleas estériles y el resentimiento; sigamos cavando hacia Rehobot.\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    p = c_tf.add_paragraph()
    p.text = "3. SIGAMOS REGANDO CON FIDELIDAD"
    p.font.name = FONT_BODY
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p = c_tf.add_paragraph()
    p.text = "   No desmayemos en el silencio; a su tiempo segaremos con fruto abundante."
    p.font.name = FONT_BODY
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE

    # Footer
    f_box = s17.shapes.add_textbox(Inches(1.0), Inches(6.5), Inches(11.3), Inches(0.5))
    f_tf = f_box.text_frame
    p = f_tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "IGLESIA EL RENUEVO · MCYM · SAN SALVADOR DE JUJUY"
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    out_file = r"C:\Users\pmpel\projects\iglesia_el_renuevo\predicas\PERSISTE\PERSISTE_presentacion.pptx"
    create_deck(out_file)
