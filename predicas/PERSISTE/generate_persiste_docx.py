import os
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    borders = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
    for b_name, b_val in borders.items():
        if b_val:
            elem = parse_xml(f'<w:{b_name} {nsdecls("w")} w:val="{b_val.get("val","single")}" w:sz="{b_val.get("sz","4")}" w:space="0" w:color="{b_val.get("color","auto")}"/>')
            tcBorders.append(elem)
        else:
            elem = parse_xml(f'<w:{b_name} {nsdecls("w")} w:val="none"/>')
            tcBorders.append(elem)
    tcPr.append(tcBorders)

def build_persiste_doc(output_path):
    doc = Document()
    
    # Page setup - A4
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(6)

    # 1. Header Bar / Top Banner
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.47)
    cell = table.rows[0].cells[0]
    set_cell_background(cell, "1A1A1A")
    set_cell_margins(cell, top=180, bottom=180, left=240, right=240)
    
    p_inst = cell.paragraphs[0]
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("IGLESIA EL RENUEVO · MOVIMIENTO CRISTIANO Y MISIONERO")
    r_inst.font.name = 'Arial'
    r_inst.font.size = Pt(9.5)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0x5D, 0xBE, 0x2C) # Brand green

    p_title = cell.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("PERSISTE")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    p_sub = cell.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(0)
    r_sub = p_sub.add_run("La fidelidad inquebrantable en medio de los procesos de Dios")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)

    # Spacing
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(4)

    # 2. Metadata Card
    meta_table = doc.add_table(rows=1, cols=1)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.columns[0].width = Inches(6.47)
    meta_cell = meta_table.rows[0].cells[0]
    set_cell_background(meta_cell, "F4F6F4")
    set_cell_borders(meta_cell, left={'val': 'single', 'sz': '24', 'color': '5DBE2C'})
    set_cell_margins(meta_cell, top=140, bottom=140, left=200, right=180)

    p_meta = meta_cell.paragraphs[0]
    p_meta.paragraph_format.space_after = Pt(2)
    
    r = p_meta.add_run("Predicador: ")
    r.bold = True
    p_meta.add_run("Pastor Misael Peloc   |   ")
    r = p_meta.add_run("Reunión: ")
    r.bold = True
    p_meta.add_run("General de Jueves\n")
    r = p_meta.add_run("Duración estimada: ")
    r.bold = True
    p_meta.add_run("40 minutos   |   ")
    r = p_meta.add_run("Tono: ")
    r.bold = True
    p_meta.add_run("Reflexivo y Pastoral\n")
    r = p_meta.add_run("Pasajes clave: ")
    r.bold = True
    p_meta.add_run("2 Reyes 13:18-19  ·  Génesis 26:15-22  ·  Gálatas 6:9  ·  Salmo 23:5")

    # 3. Idea Central Callout
    p_space2 = doc.add_paragraph()
    p_space2.paragraph_format.space_after = Pt(4)

    idea_table = doc.add_table(rows=1, cols=1)
    idea_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    idea_table.columns[0].width = Inches(6.47)
    idea_cell = idea_table.rows[0].cells[0]
    set_cell_background(idea_cell, "FFFFFF")
    set_cell_borders(idea_cell, 
                     top={'val': 'single', 'sz': '6', 'color': 'CCCCCC'},
                     bottom={'val': 'single', 'sz': '6', 'color': 'CCCCCC'},
                     left={'val': 'single', 'sz': '24', 'color': '1A1A1A'},
                     right={'val': 'single', 'sz': '6', 'color': 'CCCCCC'})
    set_cell_margins(idea_cell, top=140, bottom=140, left=200, right=180)

    p_idea_lbl = idea_cell.paragraphs[0]
    p_idea_lbl.paragraph_format.space_after = Pt(2)
    r_idea_lbl = p_idea_lbl.add_run("IDEA CENTRAL DEL MENSAJE")
    r_idea_lbl.font.name = 'Arial'
    r_idea_lbl.font.size = Pt(9)
    r_idea_lbl.font.bold = True
    r_idea_lbl.font.color.rgb = RGBColor(0x77, 0x77, 0x77)

    p_idea = idea_cell.add_paragraph()
    p_idea.paragraph_format.space_after = Pt(0)
    r_idea = p_idea.add_run("«La constancia espiritual no consiste en la ausencia de cansancio, sino en negarnos a abandonar el propósito de Dios frente al conformismo, la oposición o la falta de resultados inmediatos. Para Dios, el éxito y la bendición no significan ausencia de problemas, sino persistencia y fruto en medio de ellos».")
    r_idea.font.size = Pt(11.5)
    r_idea.font.bold = True
    r_idea.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    doc.add_paragraph()

    # SECTION: INTRODUCCIÓN
    h_intro = doc.add_paragraph()
    h_intro.paragraph_format.space_before = Pt(8)
    h_intro.paragraph_format.space_after = Pt(4)
    r_h_intro = h_intro.add_run("INTRODUCCIÓN: La tentación de aflojar a mitad de camino")
    r_h_intro.font.name = 'Arial'
    r_h_intro.font.size = Pt(14)
    r_h_intro.font.bold = True
    r_h_intro.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p = doc.add_paragraph()
    p.add_run("Vivimos en una cultura moldeada por la inmediatez. Hoy todo lo medimos por la rapidez con la que obtenemos una respuesta: la velocidad de la conexión a internet, la entrega instantánea de una compra o la solución mágica para un problema complejo. Inconscientemente, muchas veces trasladamos esa misma expectativa a nuestra relación con Dios y a nuestro caminar en la vida cotidiana.")

    p = doc.add_paragraph()
    p.add_run("Sin embargo, en el Reino de Dios las cosas no funcionan por atajos ni por microondas espirituales. Dios trabaja mediante procesos formativos de largo aliento. Si miramos con sinceridad nuestra congregación, nuestras familias e incluso nuestro propio corazón, descubriremos que la gran mayoría de las veces no fracasamos por falta de entusiasmo inicial. Empezamos proyectos con gran energía, iniciamos años con metas claras de oración y lectura bíblica, y emprendemos cambios en nuestro hogar con profunda convicción.")

    p = doc.add_paragraph()
    p.add_run("El verdadero conflicto surge cuando pasan las semanas y los meses, y la emoción del primer día se apaga. Aparece la rutina, surgen roces inesperados o los resultados tardan más de lo planeado. Es allí donde se libra la verdadera batalla: ¿somos personas que perseveran o personas que abandonan cuando el camino se pone empinado?")

    p = doc.add_paragraph()
    p.add_run("Esta noche la Palabra nos invita a reflexionar en tres dimensiones fundamentales de la constancia a través de historias bíblicas profundas, para que podamos examinarnos y recibir de Dios la gracia de permanecer.")

    doc.add_paragraph()

    # PUNTO 1
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(4)
    r_h1 = h1.add_run("1. EL PELIGRO DE ABANDONAR ANTES DE TIEMPO")
    r_h1.font.name = 'Arial'
    r_h1.font.size = Pt(13.5)
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p_ref1 = doc.add_paragraph()
    p_ref1.paragraph_format.space_after = Pt(4)
    r_ref1 = p_ref1.add_run("Texto bíblico: 2 Reyes 13:14-19 — El rey Joás de Israel y el profeta Eliseo")
    r_ref1.font.bold = True
    r_ref1.font.color.rgb = RGBColor(0x5D, 0xBE, 0x2C)

    p = doc.add_paragraph()
    p.add_run("Eliseo estaba en su lecho de muerte enfermo de la enfermedad de la cual moriría. El rey Joás desciende a visitarlo llorando sobre su rostro. En ese momento culminante, Eliseo le da una orden profética: le hace abrir la ventana hacia el oriente y tirar una flecha. Eliseo declara: ")
    r_v = p.add_run("«Saeta de salvación de Jehová, y saeta de salvación contra Siria; porque herirás a los sirios en Afec hasta consumirlos»")
    r_v.italic = True
    p.add_run(" (v. 17).")

    p = doc.add_paragraph()
    p.add_run("La promesa de Dios estaba dada. El decreto divino de victoria era total. Pero inmediatamente Eliseo le dice: ")
    r_v2 = p.add_run("«Toma las saetas... Golpea la tierra»")
    r_v2.italic = True
    p.add_run(". Y el relato registra una de las escenas más aleccionadoras de toda la Escritura: ")
    r_v3 = p.add_run("«Y él la golpeó tres veces, y se detuvo. Entonces el varón de Dios, enojado contra él, dijo: De haber dado cinco o seis golpes, habrías derrotado a Siria hasta no quedar ninguno; pero ahora sólo tres veces derrotarás a Siria»")
    r_v3.italic = True
    p.add_run(" (vv. 18-19).")

    p = doc.add_paragraph()
    p.add_run("¿Por qué se indignó el profeta? Joás no falló por mala puntería ni por falta de flechas. Falló por ")
    r_b = p.add_run("conformismo y falta de intensidad interior")
    r_b.bold = True
    p.add_run(". Golpeó por cumplir con el trámite, dio tres golpes superficiales y se detuvo antes de tiempo. Con su actitud displicente, Joás achicó la victoria que Dios ya había puesto en sus manos. Se conformó con un alivio temporario cuando Dios quería darle una liberación definitiva.")

    # Ilustracion 1 Box
    i1_table = doc.add_table(rows=1, cols=1)
    i1_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    i1_table.columns[0].width = Inches(6.47)
    i1_cell = i1_table.rows[0].cells[0]
    set_cell_background(i1_cell, "F9F9F9")
    set_cell_borders(i1_cell, left={'val': 'single', 'sz': '18', 'color': '5DBE2C'})
    set_cell_margins(i1_cell, top=120, bottom=120, left=180, right=160)

    p_i1 = i1_cell.paragraphs[0]
    p_i1.paragraph_format.space_after = Pt(2)
    r_i1_t = p_i1.add_run("ILUSTRACIÓN: El martillo del picapedrero (Jacob Riis)\n")
    r_i1_t.font.bold = True
    r_i1_t.font.size = Pt(10)
    r_i1_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    r_i1_b = p_i1.add_run("El célebre periodista social Jacob Riis compartía una reflexión que se convirtió en una de las mayores metáforas de la perseverancia: «Cuando siento que nada me ayuda, voy a mirar al picapedrero martillando su roca. Quizás le da cien golpes seguidos con fuerza y la piedra no muestra ni una sola grieta visible en la superficie. Pero al golpe número ciento uno, la roca se parte en dos. Y sé perfectamente que no fue ese último golpe el que la quebró, sino los cien golpes anteriores que nadie celebró».")
    r_i1_b.font.italic = True
    r_i1_b.font.size = Pt(10)

    # Aplicacion 1
    p_app1 = doc.add_paragraph()
    p_app1.paragraph_format.space_before = Pt(6)
    r_app1_tag = p_app1.add_run("→ Aplicación pastoral: ")
    r_app1_tag.bold = True
    r_app1_tag.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    p_app1.add_run("¿Cuántas veces nos hemos detenido en el golpe número tres? En nuestra intercesión por la conversión de un familiar, en el esfuerzo por reconstruir la intimidad matrimonial o en un emprendimiento honesto, a menudo aflojamos justo cuando estábamos a pocos golpes de quebrar la dureza de la situación. Debemos renunciar al conformismo de orar a medias o servir a medias. Necesitamos pedirle al Espíritu Santo que renueve nuestras fuerzas para seguir golpeando la tierra con fe e insistencia hasta ver la victoria completa de Dios.")

    doc.add_paragraph()

    # PUNTO 2
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(12)
    h2.paragraph_format.space_after = Pt(4)
    r_h2 = h2.add_run("2. SEGUIR CAVANDO SIN AMARGARNOS ANTE LA OPOSICIÓN")
    r_h2.font.name = 'Arial'
    r_h2.font.size = Pt(13.5)
    r_h2.font.bold = True
    r_h2.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p_ref2 = doc.add_paragraph()
    p_ref2.paragraph_format.space_after = Pt(4)
    r_ref2 = p_ref2.add_run("Texto bíblico: Génesis 26:15-22 — Isaac en el valle de Gerar")
    r_ref2.font.bold = True
    r_ref2.font.color.rgb = RGBColor(0x5D, 0xBE, 0x2C)

    p = doc.add_paragraph()
    p.add_run("Isaac se encontraba viviendo en territorio extranjero en medio de un contexto complejo. Los filisteos, consumidos por la envidia al ver cómo Dios prosperaba a Isaac (Génesis 26:14), cegaron y llenaron de tierra todos los pozos de agua que su padre Abraham había abierto. En aquella geografía desértica, tapar un pozo de agua no era una broma pesada; era un atentado directo contra la subsistencia de sus rebaños y familias.")

    p = doc.add_paragraph()
    p.add_run("La reacción natural de cualquiera de nosotros habría sido la confrontación violenta, el litigio interminable o la amargura. Pero el texto bíblico nos enseña la maravillosa madurez de un hombre perseverante:")

    p = doc.add_paragraph()
    r = p.add_run("• Primer pozo — ")
    r.bold = True
    r_name = p.add_run("Esek (עֵשֶׂק): ")
    r_name.bold = True
    p.add_run("Significa ")
    p.add_run("«contienda, disputa o litigio»").italic = True
    p.add_run(". Los siervos de Isaac cavaron y hallaron un manantial de aguas vivas, pero los pastores de Gerar riñeron diciendo: «El agua es nuestra». Isaac no se desgastó en una guerra judicial estéril; dejó el pozo y siguió su marcha.")

    p = doc.add_paragraph()
    r = p.add_run("• Segundo pozo — ")
    r.bold = True
    r_name = p.add_run("Sitna (שִׂטְנָה): ")
    r_name.bold = True
    p.add_run("Significa ")
    p.add_run("«enemistad, hostilidad u oposición»").italic = True
    p.add_run(" (proviene de la misma raíz de Satán, el adversario acusador). Volvieron a cavar con gran esfuerzo y la oposición volvió a manifestarse con ferocidad. Cualquier otro habría dicho: «Esto no es para mí, renuncio a todo». Isaac decidió no envenenar su corazón.")

    p = doc.add_paragraph()
    r = p.add_run("• Tercer pozo — ")
    r.bold = True
    r_name = p.add_run("Rehobot (רְחֹבוֹת): ")
    r_name.bold = True
    p.add_run("Significa ")
    p.add_run("«espacio amplio, ensanche y fructificación»").italic = True
    p.add_run(". Isaac se apartó de allí, cavó otro pozo y ya no pelearon sobre él. Y proclamó con gratitud: ")
    r_v = p.add_run("«Porque ahora Jehová nos ha hecho prosperar, y fructificaremos en la tierra»")
    r_v.italic = True
    p.add_run(" (v. 22).")

    # Ilustracion 2 Box
    i2_table = doc.add_table(rows=1, cols=1)
    i2_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    i2_table.columns[0].width = Inches(6.47)
    i2_cell = i2_table.rows[0].cells[0]
    set_cell_background(i2_cell, "F9F9F9")
    set_cell_borders(i2_cell, left={'val': 'single', 'sz': '18', 'color': '5DBE2C'})
    set_cell_margins(i2_cell, top=120, bottom=120, left=180, right=160)

    p_i2 = i2_cell.paragraphs[0]
    p_i2.paragraph_format.space_after = Pt(2)
    r_i2_t = p_i2.add_run("ILUSTRACIÓN: El vuelo del águila y el cuervo\n")
    r_i2_t.font.bold = True
    r_i2_t.font.size = Pt(10)
    r_i2_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    r_i2_b = p_i2.add_run("En el reino animal, el único pájaro que se atreve a hostigar y picotear el lomo de un águila en pleno vuelo es el cuervo. Sin embargo, el águila no pierde su tiempo ni gasta sus preciosas energías peleando o respondiendo a sus ataques. Simplemente abre sus alas y comienza a elevarse a mayor altitud. A medida que el águila sube, el aire se vuelve más enrarecido y el oxígeno disminuye drásticamente, hasta que el cuervo no puede respirar y termina cayendo por su propio peso.")
    r_i2_b.font.italic = True
    r_i2_b.font.size = Pt(10)

    # Aplicacion 2
    p_app2 = doc.add_paragraph()
    p_app2.paragraph_format.space_before = Pt(6)
    r_app2_tag = p_app2.add_run("→ Aplicación pastoral: ")
    r_app2_tag.bold = True
    r_app2_tag.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    p_app2.add_run("¿Cuánta de nuestra energía espiritual y emocional se nos va discutiendo en nuestros propios Esek y Sitna? A veces en el ambiente laboral alguien nos «tapa el pozo» desvalorizando nuestro trabajo; en la familia surgen roces que buscan robarnos la paz; y en el servicio aparecen incomprensiones. Si nos quedamos atascados peleando con quien nos tapa el pozo, nos quedaremos sin agua y llenos de rencor. Debemos aprender a sacudirnos la ofensa, cuidar el corazón de la amargura y seguir cavando en la dirección de Dios. Nos toca elevarnos en madurez hasta que Dios mismo ensanche nuestro camino y nos lleve a nuestro Rehobot.")

    doc.add_paragraph()

    # PUNTO 3
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after = Pt(4)
    r_h3 = h3.add_run("3. LA CONSTANCIA SILENCIOSA QUE ECHA RAÍCES PROFUNDAS")
    r_h3.font.name = 'Arial'
    r_h3.font.size = Pt(13.5)
    r_h3.font.bold = True
    r_h3.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p_ref3 = doc.add_paragraph()
    p_ref3.paragraph_format.space_after = Pt(4)
    r_ref3 = p_ref3.add_run("Texto bíblico: Gálatas 6:9 y Hebreos 10:35-36")
    r_ref3.font.bold = True
    r_ref3.font.color.rgb = RGBColor(0x5D, 0xBE, 0x2C)

    p = doc.add_paragraph()
    p.add_run("El apóstol Pablo nos deja una exhortación pastoral que toca el nervio vivo de toda experiencia cristiana: ")
    r_v = p.add_run("«No nos cansemos, pues, de hacer bien; porque a su tiempo segaremos, si no desmayamos»")
    r_v.italic = True
    p.add_run(" (Gálatas 6:9).")

    p = doc.add_paragraph()
    p.add_run("En el griego original, la riqueza de los términos utilizados nos abre una ventana de gran profundidad:")

    p = doc.add_paragraph()
    r = p.add_run("• Desmayar — ")
    r.bold = True
    r_grk1 = p.add_run("Ekkakeō (ἐκκακέω): ")
    r_grk1.bold = True
    p.add_run("Literalmente significa «perder el valor interno», desfallecer en secreto o rendirse en el corazón antes de que se note externamente. Es el desgaste sutil que nos hace pensar: «¿Para qué sigo orando si nada cambia? ¿Para qué sigo siendo honesto si a los demás les va mejor?»")

    p = doc.add_paragraph()
    r = p.add_run("• Paciencia / Perseverancia — ")
    r.bold = True
    r_grk2 = p.add_run("Hypomonē (ὑπομονή): ")
    r_grk2.bold = True
    p.add_run("En Hebreos 10:36 («porque os es necesaria la paciencia...»), el término está compuesto por ")
    p.add_run("hypo (debajo)").italic = True
    p.add_run(" y ")
    p.add_run("menō (permanecer firme)").italic = True
    p.add_run(". No describe una resignación pasiva o quejosa, sino la capacidad activa de mantenerse en pie bajo un peso enorme sin quebrarse ni retroceder.")

    p = doc.add_paragraph()
    p.add_run("La promesa de Dios tiene un momento exacto garantizado: ")
    r_b = p.add_run("«a su tiempo»")
    r_b.bold = True
    p.add_run(". Es el tiempo de Dios (kairós), no el de nuestro reloj biológico o nuestra ansiedad. Entre la siembra fiel y la cosecha abundante, siempre media una temporada silenciosa donde la semilla está trabajando bajo tierra.")

    # Ilustracion 3 Box
    i3_table = doc.add_table(rows=1, cols=1)
    i3_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    i3_table.columns[0].width = Inches(6.47)
    i3_cell = i3_table.rows[0].cells[0]
    set_cell_background(i3_cell, "F9F9F9")
    set_cell_borders(i3_cell, left={'val': 'single', 'sz': '18', 'color': '5DBE2C'})
    set_cell_margins(i3_cell, top=120, bottom=120, left=180, right=160)

    p_i3 = i3_cell.paragraphs[0]
    p_i3.paragraph_format.space_after = Pt(2)
    r_i3_t = p_i3.add_run("ILUSTRACIÓN: La parábola natural del bambú japonés\n")
    r_i3_t.font.bold = True
    r_i3_t.font.size = Pt(10)
    r_i3_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    r_i3_b = p_i3.add_run("Cuando un agricultor siembra la semilla del bambú japonés, debe regarla y cuidarla con paciencia durante siete años continuos sin ver brotar absolutamente nada en la superficie. Para quien no comprende el proceso natural, parecería que la tierra es infértil y el esfuerzo diario ha sido un fracaso. Sin embargo, al séptimo año, en un lapso de apenas seis semanas, el bambú crece más de 30 metros de altura. ¿Creció en seis semanas o en siete años? Indudablemente creció en siete años: durante todo ese tiempo silencioso estuvo tejiendo un complejo sistema de raíces subterráneas, sin las cuales la altura futura colapsaría ante la primera ráfaga de viento.")
    r_i3_b.font.italic = True
    r_i3_b.font.size = Pt(10)

    # Aplicacion 3
    p_app3 = doc.add_paragraph()
    p_app3.paragraph_format.space_before = Pt(6)
    r_app3_tag = p_app3.add_run("→ Aplicación pastoral: ")
    r_app3_tag.bold = True
    r_app3_tag.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)
    p_app3.add_run("¿En qué área de nuestra vida sentimos hoy que nuestro esfuerzo parece estéril? Muchas veces nos desanimamos en la crianza de nuestros hijos, en la constancia de congregarnos o en la disciplina del trabajo bien hecho porque no vemos frutos instantáneos. Necesitamos recordar que cuando Dios parece guardar silencio afuera, está consolidando raíces adentro. Debemos perseverar en el bien sabiendo que ninguna oración, ninguna lágrima y ninguna siembra en el Señor quedan jamás en el olvido.")

    doc.add_paragraph()

    # CONCLUSIÓN Y CLÍMAX
    h_concl = doc.add_paragraph()
    h_concl.paragraph_format.space_before = Pt(14)
    h_concl.paragraph_format.space_after = Pt(4)
    r_h_concl = h_concl.add_run("CONCLUSIÓN: Fructificar en medio de nuestras angustias")
    r_h_concl.font.name = 'Arial'
    r_h_concl.font.size = Pt(14)
    r_h_concl.font.bold = True
    r_h_concl.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p = doc.add_paragraph()
    p.add_run("Al contemplar el cuadro completo de la Escritura, encontramos un hilo conductor que transforma radicalmente nuestra concepción de la vida cristiana:")

    # Highlight box for the central climax
    climax_table = doc.add_table(rows=1, cols=1)
    climax_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    climax_table.columns[0].width = Inches(6.47)
    climax_cell = climax_table.rows[0].cells[0]
    set_cell_background(climax_cell, "1A1A1A")
    set_cell_margins(climax_cell, top=140, bottom=140, left=200, right=180)

    p_c = climax_cell.paragraphs[0]
    p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c.paragraph_format.space_after = Pt(0)
    r_c = p_c.add_run("«PARA DIOS, EL ÉXITO Y LA BENDICIÓN NO SIGNIFICAN AUSENCIA DE PROBLEMAS, SINO PERSISTENCIA Y FRUTO EN MEDIO DE ELLOS».")
    r_c.font.name = 'Arial'
    r_c.font.size = Pt(12)
    r_c.font.bold = True
    r_c.font.color.rgb = RGBColor(0x5D, 0xBE, 0x2C)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.add_run("Muchas veces caemos en la trampa espiritual de postergar nuestra consagración diciendo: «Cuando se resuelvan todos mis problemas familiares, cuando mejore la economía o cuando nadie me critique en el trabajo, entonces sí voy a servir a Dios con alegría». Si esperamos la ausencia total de dificultades, jamás seremos personas constantes.")

    p = doc.add_paragraph()
    p.add_run("Observemos la sabiduría del testimonio bíblico:")
    p = doc.add_paragraph()
    p.add_run("1. ")
    p.add_run("Isaac").bold = True
    p.add_run(" no necesitó que los filisteos se convirtieran para hallar agua; perseveró cavando hasta que brotó Rehobot en la misma tierra de su peregrinación (Génesis 26:22).")
    p = doc.add_paragraph()
    p.add_run("2. ")
    p.add_run("José").bold = True
    p.add_run(" le puso por nombre a su segundo hijo Efraín, proclamando con lágrimas de gratitud: ")
    p.add_run("«Dios me hizo fructificar en la tierra de mi aflicción»").italic = True
    p.add_run(" (Génesis 41:52). Dios no lo sacó de Egipto para bendecirlo; lo hizo dar fruto en la tierra misma de sus mayores dolores.")
    p = doc.add_paragraph()
    p.add_run("3. ")
    p.add_run("David").bold = True
    p.add_run(" canta en el Salmo 23:5 con total elocuencia: ")
    p.add_run("«Aderezas mesa delante de mí en presencia de mis angustiadores»").italic = True
    p.add_run(". Dios no tuvo que exterminar a los adversarios para servir el banquete; preparó la mesa en su misma presencia. Y en el Salmo 4:1 añade: ")
    p.add_run("«Cuando estaba en angustia, tú me hiciste ensanchar»").italic = True
    p.add_run(".")

    doc.add_paragraph()

    # LLAMADO FINAL
    h_call = doc.add_paragraph()
    h_call.paragraph_format.space_before = Pt(8)
    h_call.paragraph_format.space_after = Pt(4)
    r_h_call = h_call.add_run("LLAMADO FINAL Y MINISTRACIÓN COMUNITARIA")
    r_h_call.font.name = 'Arial'
    r_h_call.font.size = Pt(13)
    r_h_call.font.bold = True
    r_h_call.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32)

    p_call = doc.add_paragraph()
    p_call.add_run("Hoy el Señor nos confronta con amor y nos llama a ponernos de pie:")
    p = doc.add_paragraph()
    p.add_run("• ")
    p.add_run("No soltemos las saetas: ").bold = True
    p.add_run("Si nos detuvimos al tercer golpe en nuestra búsqueda espiritual o en nuestras responsabilidades diarias, volvamos a tomar las flechas de la fe.")
    p = doc.add_paragraph()
    p.add_run("• ")
    p.add_run("Dejemos atrás Esek y Sitna: ").bold = True
    p.add_run("Renunciemos al desgaste de la queja y el resentimiento; perdonemos, soltemos la contienda y sigamos cavando hacia nuestro Rehobot.")
    p = doc.add_paragraph()
    p.add_run("• ")
    p.add_run("Sigamos regando con fidelidad: ").bold = True
    p.add_run("Aunque hoy parezca que nada se mueve en la superficie, confiemos en que a su tiempo segaremos si no desmayamos.")

    p_final = doc.add_paragraph()
    p_final.paragraph_format.space_before = Pt(6)
    r_final = p_final.add_run("Oración comunitaria: «Padre, te pedimos perdón por las veces en que nos hemos rendido antes de tiempo, por los momentos en que el cansancio o la oposición apagaron nuestra perseverancia. Fortalécenos con tu Espíritu Santo. Enséñanos a no buscar una vida sin dificultades, sino a experimentar tu poder y dar fruto abundante aun en medio de nuestras mayores tensiones. En el nombre precioso de Jesús, amén».")
    r_final.italic = True
    r_final.bold = True
    r_final.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Save
    doc.save(output_path)
    print(f"Document saved to: {output_path}")

if __name__ == '__main__':
    local_path = r"C:\Users\pmpel\projects\iglesia_el_renuevo\predicas\PERSISTE\PERSISTE.docx"
    gdrive_path = r"G:\Mi unidad\Predicas\PERSISTE.docx"
    
    build_persiste_doc(local_path)
    
    try:
        shutil.copy2(local_path, gdrive_path)
        print(f"Document successfully copied to Google Drive: {gdrive_path}")
    except Exception as e:
        print(f"Error copying to Google Drive: {e}")
