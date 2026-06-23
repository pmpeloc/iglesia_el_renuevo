from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "outputs" / "dia_padres_whatsapp"
LOGO = ROOT / "logos" / "LOGO-EL RENUEVO-R-1.png"
OUT = OUT_DIR / "dia_padres_whatsapp.png"

W, H = 1080, 1920
GREEN = (93, 190, 44)
GREEN_SOFT = (155, 225, 93)
GOLD = (233, 196, 106)
WHITE = (255, 255, 255)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)


FONT_REG = "segoeui.ttf"
FONT_SEMI = "seguisb.ttf"
FONT_BOLD = "segoeuib.ttf"
FONT_BLACK = "seguibl.ttf"


def lerp(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def add_glow(base: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int], alpha: int) -> None:
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    x, y = center
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(radius // 2))
    base.alpha_composite(glow)


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_width(draw, candidate, fnt) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw: ImageDraw.ImageDraw, xy: tuple[int, int], lines: list[str], fnt, fill, spacing: int) -> int:
    x, y = xy
    line_h = fnt.getbbox("Ag")[3] - fnt.getbbox("Ag")[1]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h + spacing
    return y


def make_background() -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    px = img.load()
    top = (20, 36, 24)
    mid = (7, 16, 11)
    bottom = (2, 4, 3)
    for y in range(H):
        t = y / (H - 1)
        if t < 0.48:
            k = t / 0.48
            col = tuple(lerp(top[i], mid[i], k) for i in range(3))
        else:
            k = (t - 0.48) / 0.52
            col = tuple(lerp(mid[i], bottom[i], k) for i in range(3))
        for x in range(W):
            px[x, y] = (*col, 255)

    add_glow(img, (170, 240), 360, GREEN, 105)
    add_glow(img, (895, 315), 320, GOLD, 44)

    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, W, 54):
        gd.line((x, 0, x, H), fill=(255, 255, 255, 15), width=1)
    for y in range(0, H, 54):
        gd.line((0, y, W, y), fill=(255, 255, 255, 13), width=1)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    for y in range(H):
        val = max(0, int(150 * (1 - y / 1040)))
        md.line((0, y, W, y), fill=val)
    img.alpha_composite(Image.composite(grid, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

    deco = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dd = ImageDraw.Draw(deco)
    for offset, alpha in [(0, 72), (86, 24), (176, 18)]:
        dd.ellipse((640 - offset, 1120 - offset, 1400 + offset, 1880 + offset), outline=(*GREEN, alpha), width=3)
    img.alpha_composite(deco)
    return img


def paste_logo_watermark(img: Image.Image) -> None:
    logo = Image.open(LOGO).convert("RGBA")
    logo = ImageOps.contain(logo, (720, 720))
    alpha = logo.getchannel("A").point(lambda p: int(p * 0.06))
    logo.putalpha(alpha)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer.alpha_composite(logo, (590, 1020))
    img.alpha_composite(layer)


def paste_footer_logo(img: Image.Image, x: int, y: int, size: int) -> None:
    logo = Image.open(LOGO).convert("RGBA")
    logo = ImageOps.fit(logo, (size, size), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((0, 0, size - 1, size - 1), fill=255)
    shadow = Image.new("RGBA", (size + 26, size + 26), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse((13, 13, size + 12, size + 12), fill=(0, 0, 0, 100))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(shadow, (x - 13, y - 13))
    img.paste(logo, (x, y), mask)


def render() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = make_background()
    paste_logo_watermark(img)
    draw = ImageDraw.Draw(img)

    regular_28 = font(FONT_REG, 28)
    semi_28 = font(FONT_SEMI, 28)
    bold_34 = font(FONT_BOLD, 34)
    black_134 = font(FONT_BLACK, 134)
    verse_font = font(FONT_BLACK, 58)
    ref_font = font(FONT_BOLD, 31)
    challenge_font = font(FONT_SEMI, 38)
    footer_font = font(FONT_BOLD, 26)

    margin = 86

    draw.text((margin, 92), "Iglesia El Renuevo", font=regular_28, fill=(255, 255, 255, 210))
    badge_text = "Día del Padre"
    badge_w = text_width(draw, badge_text, semi_28) + 50
    badge_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(badge_overlay)
    rounded_rect(
        bd,
        (W - margin - badge_w, 78, W - margin, 132),
        27,
        fill=(255, 255, 255, 13),
        outline=(255, 255, 255, 58),
        width=1,
    )
    img.alpha_composite(badge_overlay)
    draw = ImageDraw.Draw(img)
    draw.text((W - margin - badge_w + 25, 88), badge_text, font=semi_28, fill=(*GREEN_SOFT, 255))

    draw.text((margin, 314), "HONRAMOS SU FE, AMOR Y ENTREGA", font=bold_34, fill=(*GOLD, 255))
    draw.text((margin, 388), "FELIZ DÍA", font=black_134, fill=WHITE)
    draw.text((margin, 515), "DEL PADRE", font=black_134, fill=(*GREEN_SOFT, 255))

    card_x, card_y, card_w, card_h = margin, 750, W - margin * 2, 370
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((card_x + 18, card_y + 24, card_x + card_w + 18, card_y + card_h + 24), radius=10, fill=(0, 0, 0, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(24))
    img.alpha_composite(shadow)
    card_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card_overlay)
    rounded_rect(cd, (card_x, card_y, card_x + card_w, card_y + card_h), 8, fill=(255, 255, 255, 24))
    img.alpha_composite(card_overlay)
    draw = ImageDraw.Draw(img)
    draw.rectangle((card_x, card_y, card_x + 12, card_y + card_h), fill=(*GREEN, 255))

    verse = '"pero yo y mi casa serviremos a Jehová."'
    verse_lines = wrap_text(draw, verse, verse_font, card_w - 88)
    y = draw_lines(draw, (card_x + 44, card_y + 50), verse_lines, verse_font, WHITE, 12)
    draw.text((card_x + 44, y + 18), "Josué 24:15 · RVR1960", font=ref_font, fill=(*GOLD, 255))

    challenge = "El mayor legado no es solo una casa en pie, sino una familia guiada hacia Dios."
    challenge_lines = wrap_text(draw, challenge, challenge_font, int(W * 0.78))
    draw_lines(draw, (margin, 1206), challenge_lines, challenge_font, (255, 255, 255, 230), 12)

    footer_y = H - 152
    paste_footer_logo(img, margin, footer_y, 82)
    draw = ImageDraw.Draw(img)
    draw.text((margin + 102, footer_y + 10), "Movimiento Cristiano y Misionero", font=footer_font, fill=(255, 255, 255, 214))
    draw.line((margin + 478, footer_y + 42, W - margin, footer_y + 42), fill=(255, 255, 255, 58), width=1)

    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(OUT)


if __name__ == "__main__":
    render()
