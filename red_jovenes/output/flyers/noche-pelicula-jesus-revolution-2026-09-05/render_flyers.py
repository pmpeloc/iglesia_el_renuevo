from pathlib import Path
from shutil import copy2

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


ROOT = Path(r"C:\Users\pmpel\projects\iglesia_el_renuevo")
OUT = ROOT / "red_jovenes" / "output" / "flyers" / "noche-pelicula-jesus-revolution-2026-09-05"
SOURCE = Path(r"C:\Users\pmpel\.codex\generated_images\01a06c56-96eb-7112-8af0-616d06004ca5\exec-45920b58-28d5-4167-a6df-73cf57609fad.png")

FONT_HEAD = r"C:\Windows\Fonts\impact.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\arial.ttf"

CREAM = "#FFF1D5"
ORANGE = "#FF5A1F"
GOLD = "#FFC45B"
INDIGO = "#211440"
VIOLET = "#39206C"


def font(path, size):
    return ImageFont.truetype(path, max(10, round(size)))


def fit_font(draw, text, path, max_size, max_width, stroke=0):
    size = round(max_size)
    while size > 10:
        candidate = font(path, size)
        box = draw.textbbox((0, 0), text, font=candidate, stroke_width=stroke)
        if box[2] - box[0] <= max_width:
            return candidate
        size -= 2
    return font(path, 10)


def centered(draw, text, y, fnt, fill, stroke=0, stroke_fill=INDIGO):
    box = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    x = (draw.im.size[0] - (box[2] - box[0])) / 2 - box[0]
    draw.text((x + 3, y + 5), text, font=fnt, fill=(8, 4, 23, 150), stroke_width=stroke)
    draw.text((x, y), text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def cover(source, size, focus_y):
    image = ImageOps.fit(source, size, method=Image.Resampling.LANCZOS, centering=(0.5, focus_y))
    return ImageEnhance.Contrast(image).enhance(1.05).convert("RGBA")


def overlays(image, bottom_start):
    w, h = image.size
    shade = Image.new("RGBA", image.size)
    pixels = shade.load()
    for y in range(h):
        top = max(0, 72 - int(y / h * 170))
        bottom = max(0, int((y / h - bottom_start) / (1 - bottom_start) * 225)) if y / h > bottom_start else 0
        alpha = min(230, max(top, bottom))
        for x in range(w):
            pixels[x, y] = (22, 10, 54, alpha)
    image.alpha_composite(shade)


def logo(path, max_width, max_height, recolor_black=False):
    image = Image.open(path).convert("RGBA")
    if recolor_black:
        px = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = px[x, y]
                if a and max(r, g, b) < 105:
                    px[x, y] = (255, 241, 213, a)
    box = image.getchannel("A").getbbox()
    image = image.crop(box)
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    return image


def paste_centered(base, asset, center_x, center_y):
    base.alpha_composite(asset, (round(center_x - asset.width / 2), round(center_y - asset.height / 2)))


def draw_logo_bar(image, y, height, scale):
    w = image.width
    layer = Image.new("RGBA", image.size)
    d = ImageDraw.Draw(layer)
    pad = round(38 * scale)
    d.rounded_rectangle((pad, y, w - pad, y + height), radius=round(24 * scale), fill=(18, 10, 45, 218), outline=(255, 241, 213, 95), width=max(1, round(2 * scale)))
    image.alpha_composite(layer)

    church = logo(ROOT / "logos" / "LOGO-EL RENUEVO-R-1.png", round(118 * scale), round(118 * scale))
    roots = logo(ROOT / "red_jovenes" / "logos" / "Logotipo.png", round(260 * scale), round(104 * scale), recolor_black=True)
    teens = logo(ROOT / "red_adolescentes" / "logos" / "BLANCO Y NEGRO" / "BLANCOVASTAGOS.png", round(270 * scale), round(100 * scale))

    centers = (w * 0.19, w * 0.50, w * 0.81)
    cy = y + height * 0.45
    paste_centered(image, church, centers[0], cy - 5 * scale)
    paste_centered(image, roots, centers[1], cy)
    paste_centered(image, teens, centers[2], cy)

    d = ImageDraw.Draw(image)
    label = font(FONT_BOLD, 19 * scale)
    text = "IGLESIA EL RENUEVO"
    box = d.textbbox((0, 0), text, font=label)
    d.text((centers[0] - (box[2] - box[0]) / 2, y + height - 38 * scale), text, font=label, fill=CREAM)


def render_story(source):
    w, h = 1080, 1920
    s = w / 1080
    image = cover(source, (w, h), 0.5)
    overlays(image, 0.52)
    d = ImageDraw.Draw(image)

    tag = font(FONT_BOLD, 39 * s)
    tag_box = d.textbbox((0, 0), "NOCHE DE PELÍCULA", font=tag)
    tw = tag_box[2] - tag_box[0]
    d.rounded_rectangle(((w - tw) / 2 - 32, 120, (w + tw) / 2 + 32, 184), radius=30, fill=ORANGE)
    centered(d, "NOCHE DE PELÍCULA", 128, tag, CREAM)

    title1 = fit_font(d, "LA REVOLUCIÓN", FONT_HEAD, 132, w - 112, stroke=4)
    title2 = fit_font(d, "DE JESÚS", FONT_HEAD, 175, w - 112, stroke=5)
    centered(d, "LA REVOLUCIÓN", 222, title1, CREAM, stroke=4, stroke_fill=INDIGO)
    centered(d, "DE JESÚS", 345, title2, GOLD, stroke=5, stroke_fill=INDIGO)
    centered(d, "JÓVENES + ADOLESCENTES", 535, font(FONT_BOLD, 38), INDIGO, stroke=2, stroke_fill=CREAM)

    centered(d, "SÁBADO 5 DE SEPTIEMBRE", 1060, font(FONT_HEAD, 63), CREAM, stroke=2, stroke_fill=INDIGO)
    d.rounded_rectangle((100, 1160, w - 100, 1268), radius=28, fill=CREAM, outline=ORANGE, width=5)
    centered(d, "20:30 HS · ¡PUNTUALES!", 1176, font(FONT_HEAD, 67), INDIGO)
    centered(d, "REPÚBLICA DE SIRIA 255", 1303, font(FONT_BOLD, 43), CREAM, stroke=2, stroke_fill=INDIGO)
    centered(d, "POCHOCLOS Y UNA HISTORIA", 1384, font(FONT_BOLD, 33), GOLD)
    centered(d, "PARA COMPARTIR", 1427, font(FONT_BOLD, 33), GOLD)
    centered(d, "¡HAY UN LUGAR PARA VOS!", 1490, font(FONT_HEAD, 47), CREAM)

    draw_logo_bar(image, 1602, 214, 1)
    return image.convert("RGB")


def render_feed(source, size):
    w, h = size
    s = w / 1080
    image = cover(source, size, 0.36)
    overlays(image, 0.48)
    d = ImageDraw.Draw(image)

    tag = font(FONT_BOLD, 30 * s)
    tag_box = d.textbbox((0, 0), "NOCHE DE PELÍCULA", font=tag)
    tw = tag_box[2] - tag_box[0]
    d.rounded_rectangle(((w - tw) / 2 - 26 * s, 55 * s, (w + tw) / 2 + 26 * s, 108 * s), radius=24 * s, fill=ORANGE)
    centered(d, "NOCHE DE PELÍCULA", 62 * s, tag, CREAM)

    title1 = fit_font(d, "LA REVOLUCIÓN", FONT_HEAD, 116 * s, w - 100 * s, stroke=4)
    title2 = fit_font(d, "DE JESÚS", FONT_HEAD, 155 * s, w - 100 * s, stroke=5)
    centered(d, "LA REVOLUCIÓN", 130 * s, title1, CREAM, stroke=4, stroke_fill=INDIGO)
    centered(d, "DE JESÚS", 238 * s, title2, GOLD, stroke=5, stroke_fill=INDIGO)
    centered(d, "JÓVENES + ADOLESCENTES", 400 * s, font(FONT_BOLD, 31 * s), INDIGO, stroke=2, stroke_fill=CREAM)

    centered(d, "SÁBADO 5 DE SEPTIEMBRE", 710 * s, font(FONT_HEAD, 54 * s), CREAM, stroke=2, stroke_fill=INDIGO)
    d.rounded_rectangle((90 * s, 792 * s, w - 90 * s, 884 * s), radius=25 * s, fill=CREAM, outline=ORANGE, width=max(3, round(5 * s)))
    centered(d, "20:30 HS · ¡PUNTUALES!", 805 * s, font(FONT_HEAD, 58 * s), INDIGO)
    centered(d, "REPÚBLICA DE SIRIA 255", 910 * s, font(FONT_BOLD, 36 * s), CREAM, stroke=2, stroke_fill=INDIGO)
    centered(d, "POCHOCLOS Y UNA HISTORIA PARA COMPARTIR", 970 * s, fit_font(d, "POCHOCLOS Y UNA HISTORIA PARA COMPARTIR", FONT_BOLD, 28 * s, w - 100 * s), GOLD)
    centered(d, "¡HAY UN LUGAR PARA VOS!", 1022 * s, font(FONT_HEAD, 41 * s), CREAM)

    draw_logo_bar(image, round(1100 * s), round(190 * s), s)
    return image.convert("RGB")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    copy2(SOURCE, OUT / "base-cinematografica.png")
    render_story(source).save(OUT / "whatsapp-status-1080x1920.jpg", quality=94, optimize=True, subsampling=0)
    render_feed(source, (1080, 1350)).save(OUT / "instagram-1080x1350.jpg", quality=94, optimize=True, subsampling=0)
    render_feed(source, (1200, 1500)).save(OUT / "facebook-1200x1500.jpg", quality=94, optimize=True, subsampling=0)


if __name__ == "__main__":
    main()
