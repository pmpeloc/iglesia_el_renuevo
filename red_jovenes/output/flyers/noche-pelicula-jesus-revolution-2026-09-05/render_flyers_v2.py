from pathlib import Path
from random import Random
from shutil import copy2

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps


ROOT = Path(r"C:\Users\pmpel\projects\iglesia_el_renuevo")
OUT = ROOT / "red_jovenes" / "output" / "flyers" / "noche-pelicula-jesus-revolution-2026-09-05"
ART = Path(r"C:\Users\pmpel\.codex\generated_images\01a06c56-96eb-7112-8af0-616d06004ca5\exec-12d41837-b691-4af3-ac23-c6b77a90e011.png")
LETTERING = Path(r"C:\Users\pmpel\.codex\generated_images\01a06c56-96eb-7112-8af0-616d06004ca5\exec-a8f15eab-e6f2-41aa-8075-e3709c490482.png")

COOPER = r"C:\Windows\Fonts\COOPBL.TTF"
BAUHAUS = r"C:\Windows\Fonts\BAUHS93.TTF"
ROCKWELL = r"C:\Windows\Fonts\ROCKB.TTF"

CREAM = (255, 239, 204, 255)
ORANGE = (224, 70, 10, 255)
MARIGOLD = (247, 171, 4, 255)
AUBERGINE = (50, 12, 58, 255)
GREEN = (104, 208, 35, 255)


def font(path, size):
    return ImageFont.truetype(path, max(10, round(size)))


def fit_font(draw, text, path, max_size, max_width, stroke=0):
    size = round(max_size)
    while size > 10:
        fnt = font(path, size)
        box = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
        if box[2] - box[0] <= max_width:
            return fnt
        size -= 2
    return font(path, 10)


def centered_text(draw, text, center, fnt, fill, stroke=0, stroke_fill=AUBERGINE):
    box = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    x = center[0] - (box[2] - box[0]) / 2 - box[0]
    y = center[1] - (box[3] - box[1]) / 2 - box[1]
    draw.text((x, y), text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def cover(source, size, focus_y):
    image = ImageOps.fit(source, size, method=Image.Resampling.LANCZOS, centering=(0.5, focus_y))
    return ImageEnhance.Color(image).enhance(1.05).convert("RGBA")


def remove_checkerboard(image):
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, _ = pixels[x, y]
            chroma = max(r, g, b) - min(r, g, b)
            score = max((chroma - 4) * 9, (220 - min(r, g, b)) * 5)
            alpha = max(0, min(255, score))
            pixels[x, y] = (r, g, b, alpha)
    return image.crop(image.getchannel("A").getbbox())


def logo(path, max_width, max_height, recolor_black=False):
    image = Image.open(path).convert("RGBA")
    if recolor_black:
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = pixels[x, y]
                if a and max(r, g, b) < 105:
                    pixels[x, y] = (*CREAM[:3], a)
    image = image.crop(image.getchannel("A").getbbox())
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    return image


def paste_centered(base, asset, center_x, center_y):
    base.alpha_composite(asset, (round(center_x - asset.width / 2), round(center_y - asset.height / 2)))


def irregular_polygon(width, height, inset, jitter, seed):
    rng = Random(seed)
    points = []
    steps = 12
    for i in range(steps + 1):
        points.append((inset + (width - 2 * inset) * i / steps, inset + rng.randint(-jitter, jitter)))
    for i in range(1, steps + 1):
        points.append((width - inset + rng.randint(-jitter, jitter), inset + (height - 2 * inset) * i / steps))
    for i in range(1, steps + 1):
        points.append((width - inset - (width - 2 * inset) * i / steps, height - inset + rng.randint(-jitter, jitter)))
    for i in range(1, steps):
        points.append((inset + rng.randint(-jitter, jitter), height - inset - (height - 2 * inset) * i / steps))
    return points


def ticket(text, width, height, fill, text_fill, font_path, font_size, angle, seed, outline=AUBERGINE):
    scale = width / 900
    margin = round(60 * scale)
    inset = round(22 * scale)
    layer = Image.new("RGBA", (width + margin, height + margin))
    d = ImageDraw.Draw(layer)
    shape = irregular_polygon(layer.width, layer.height, inset, max(2, round(5 * scale)), seed)
    shadow = [(x + 7 * scale, y + 10 * scale) for x, y in shape]
    d.polygon(shadow, fill=ORANGE)
    d.polygon(shape, fill=fill, outline=outline, width=max(3, round(5 * scale)))
    rng = Random(seed + 10)
    for _ in range(150):
        x, y = rng.randrange(35, layer.width - 35), rng.randrange(35, layer.height - 35)
        d.ellipse((x, y, x + rng.choice((1, 2, 3)), y + rng.choice((1, 2))), fill=(*AUBERGINE[:3], rng.randrange(15, 45)))
    fnt = fit_font(d, text, font_path, font_size, width - 100, stroke=1)
    centered_text(d, text, (layer.width / 2, layer.height / 2), fnt, text_fill, stroke=1, stroke_fill=outline)
    return layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)


def filmstrip_footer(image, y, height, scale):
    w = image.width
    layer = Image.new("RGBA", image.size)
    d = ImageDraw.Draw(layer)
    rng = Random(29)
    top = [(0, y + rng.randint(-6, 6))]
    for x in range(0, w + 1, max(30, round(70 * scale))):
        top.append((x, y + rng.randint(-6, 6)))
    bottom_y = y + height
    bottom = [(x, bottom_y + rng.randint(-5, 5)) for x in range(w, -1, -max(30, round(70 * scale)))]
    d.polygon(top + bottom, fill=(35, 8, 48, 244), outline=CREAM)
    hole_w, hole_h = round(30 * scale), round(13 * scale)
    gap = round(70 * scale)
    for x in range(round(24 * scale), w - hole_w, gap):
        d.rounded_rectangle((x, y + 13 * scale, x + hole_w, y + 13 * scale + hole_h), radius=3 * scale, fill=MARIGOLD)
        d.rounded_rectangle((x, bottom_y - 25 * scale, x + hole_w, bottom_y - 25 * scale + hole_h), radius=3 * scale, fill=MARIGOLD)
    image.alpha_composite(layer)

    church = logo(ROOT / "logos" / "LOGO-EL RENUEVO-R-1.png", round(110 * scale), round(110 * scale))
    roots = logo(ROOT / "red_jovenes" / "logos" / "Logotipo.png", round(255 * scale), round(98 * scale), recolor_black=True)
    teens = logo(ROOT / "red_adolescentes" / "logos" / "BLANCO Y NEGRO" / "BLANCOVASTAGOS.png", round(260 * scale), round(92 * scale))
    cy = y + height * 0.53
    for asset, cx in ((church, w * 0.18), (roots, w * 0.50), (teens, w * 0.82)):
        paste_centered(image, asset, cx, cy)
    d = ImageDraw.Draw(image)
    label = font(ROCKWELL, 15 * scale)
    centered_text(d, "IGLESIA EL RENUEVO", (w * 0.18, y + height - 39 * scale), label, CREAM)


def banner(image, text, center_y, scale):
    d = ImageDraw.Draw(image)
    fnt = font(COOPER, 31 * scale)
    box = d.textbbox((0, 0), text, font=fnt)
    width = box[2] - box[0] + 80 * scale
    height = 65 * scale
    points = [
        (image.width / 2 - width / 2, center_y),
        (image.width / 2 - width / 2 + 22 * scale, center_y - height / 2),
        (image.width / 2 + width / 2 - 22 * scale, center_y - height / 2),
        (image.width / 2 + width / 2, center_y),
        (image.width / 2 + width / 2 - 22 * scale, center_y + height / 2),
        (image.width / 2 - width / 2 + 22 * scale, center_y + height / 2),
    ]
    d.polygon([(x + 5 * scale, y + 7 * scale) for x, y in points], fill=AUBERGINE)
    d.polygon(points, fill=ORANGE, outline=CREAM)
    centered_text(d, text, (image.width / 2, center_y), fnt, CREAM)


def event_stack(image, scale, y0, compact=False):
    w = image.width
    widths = (round(w * 0.82), round(w * 0.76), round(w * 0.66))
    heights = (round(72 * scale), round(90 * scale), round(65 * scale))
    gap = round(7 * scale)
    date = ticket("SÁBADO 5 DE SEPTIEMBRE", widths[0], heights[0], AUBERGINE, CREAM, COOPER, 43 * scale, -1.4, 5, outline=MARIGOLD)
    time = ticket("20:30 HS / ¡PUNTUALES!", widths[1], heights[1], CREAM, AUBERGINE, BAUHAUS, 53 * scale, 1.1, 12)
    place = ticket("REPÚBLICA DE SIRIA 255", widths[2], heights[2], ORANGE, CREAM, ROCKWELL, 34 * scale, -0.7, 19)
    cursor = y0
    for asset in (date, time, place):
        paste_centered(image, asset, w / 2, cursor + asset.height / 2)
        cursor += asset.height - round(38 * scale) + gap
    d = ImageDraw.Draw(image)
    tagline_y = cursor + (12 if compact else 20) * scale
    tagline = "POCHOCLOS • PELÍCULA • ALGO PARA COMPARTIR"
    tagline_font = fit_font(d, tagline, COOPER, 24 * scale, w - 110 * scale)
    centered_text(d, tagline, (w / 2, tagline_y), tagline_font, MARIGOLD, stroke=2, stroke_fill=AUBERGINE)
    slogan_y = tagline_y + 48 * scale
    slogan_font = fit_font(d, "¡HAY UN LUGAR PARA VOS!", BAUHAUS, 39 * scale, w - 100 * scale)
    centered_text(d, "¡HAY UN LUGAR PARA VOS!", (w / 2, slogan_y), slogan_font, CREAM, stroke=2, stroke_fill=AUBERGINE)


def render_story(art, lettering):
    w, h = 1080, 1920
    image = cover(art, (w, h), 0.48)
    title = lettering.copy()
    title.thumbnail((930, 900), Image.Resampling.LANCZOS)
    paste_centered(image, title, w / 2, 530)
    banner(image, "NOCHE DE PELÍCULA", 92, 1)
    d = ImageDraw.Draw(image)
    centered_text(d, "JÓVENES  +  ADOLESCENTES", (w / 2, 945), font(BAUHAUS, 34), AUBERGINE, stroke=2, stroke_fill=CREAM)
    event_stack(image, 1, 995)
    filmstrip_footer(image, 1630, 220, 1)
    return image.convert("RGB")


def render_feed(art, lettering, size):
    w, h = size
    scale = w / 1080
    image = cover(art, size, 0.37)
    title = lettering.copy()
    title.thumbnail((880 * scale, 640 * scale), Image.Resampling.LANCZOS)
    paste_centered(image, title, w / 2, 360 * scale)
    banner(image, "NOCHE DE PELÍCULA", 61 * scale, scale)
    d = ImageDraw.Draw(image)
    centered_text(d, "JÓVENES  +  ADOLESCENTES", (w / 2, 665 * scale), font(BAUHAUS, 29 * scale), AUBERGINE, stroke=2, stroke_fill=CREAM)
    event_stack(image, scale, 690 * scale, compact=True)
    filmstrip_footer(image, round(1150 * scale), round(175 * scale), scale)
    return image.convert("RGB")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    art = Image.open(ART).convert("RGB")
    lettering = remove_checkerboard(Image.open(LETTERING))
    copy2(ART, OUT / "base-ilustrada-v2.png")
    lettering.save(OUT / "lettering-dibujado-v2.png")
    render_story(art, lettering).save(OUT / "whatsapp-status-1080x1920-v2.jpg", quality=95, optimize=True, subsampling=0)
    render_feed(art, lettering, (1080, 1350)).save(OUT / "instagram-1080x1350-v2.jpg", quality=95, optimize=True, subsampling=0)
    render_feed(art, lettering, (1200, 1500)).save(OUT / "facebook-1200x1500-v2.jpg", quality=95, optimize=True, subsampling=0)


if __name__ == "__main__":
    main()
