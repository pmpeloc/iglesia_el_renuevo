from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from render_flyers_v2 import (
    AUBERGINE,
    BAUHAUS,
    COOPER,
    CREAM,
    MARIGOLD,
    ORANGE,
    OUT,
    ROCKWELL,
    ROOT,
    centered_text,
    fit_font,
    font,
    logo,
    paste_centered,
)


LETTERING = OUT / "lettering-dibujado-v2.png"
PAPER = (248, 229, 190, 255)
SOFT_ORANGE = (232, 100, 30, 255)


def minimal_background(size):
    w, h = size
    image = Image.new("RGBA", size, PAPER)
    d = ImageDraw.Draw(image)

    # One focal sun; all other space stays intentionally quiet.
    radius = round(w * 0.39)
    cx, cy = w // 2, round(h * 0.27)
    d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=SOFT_ORANGE)
    d.arc((cx - radius - 28, cy - radius - 28, cx + radius + 28, cy + radius + 28), 195, 345, fill=MARIGOLD, width=max(4, round(w / 180)))

    # Five reduced silhouettes: community without becoming another background pattern.
    base_y = round(h * 0.63)
    for index, x in enumerate((0.07, 0.16, 0.84, 0.93)):
        head = round(w * (0.032 if index % 2 else 0.038))
        px = round(w * x)
        py = base_y + (index % 2) * round(h * 0.018)
        d.ellipse((px - head, py - head * 2, px + head, py), fill=AUBERGINE)
        d.ellipse((px - head * 2, py - head // 2, px + head * 2, py + head * 3), fill=AUBERGINE)

    # A single film line along the edge, away from all information.
    line_y = round(h * 0.88)
    d.line((0, line_y, w, line_y - round(h * 0.025)), fill=ORANGE, width=max(5, round(w / 130)))
    for x in range(round(w * 0.03), w, round(w * 0.09)):
        d.rounded_rectangle((x, line_y - 7, x + round(w * 0.035), line_y + 7), radius=4, fill=AUBERGINE)
    return image


def title_block(image, center_y, max_width, max_height, scale):
    title = Image.open(LETTERING).convert("RGBA")
    title.thumbnail((round(max_width), round(max_height)), Image.Resampling.LANCZOS)
    paste_centered(image, title, image.width / 2, center_y)
    d = ImageDraw.Draw(image)
    centered_text(d, "NOCHE DE PELÍCULA", (image.width / 2, 52 * scale), font(COOPER, 29 * scale), AUBERGINE)
    d.line((image.width * 0.33, 78 * scale, image.width * 0.67, 78 * scale), fill=ORANGE, width=max(3, round(4 * scale)))


def info_panel(image, box, scale):
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(image)
    shadow = round(10 * scale)
    d.rounded_rectangle((x0 + shadow, y0 + shadow, x1 + shadow, y1 + shadow), radius=round(26 * scale), fill=ORANGE)
    d.rounded_rectangle(box, radius=round(26 * scale), fill=AUBERGINE)
    d.rectangle((x0, y0 + round(22 * scale), x0 + round(10 * scale), y1 - round(22 * scale)), fill=MARIGOLD)

    center_x = (x0 + x1) / 2
    centered_text(d, "SÁBADO 5 DE SEPTIEMBRE", (center_x, y0 + 64 * scale), fit_font(d, "SÁBADO 5 DE SEPTIEMBRE", COOPER, 41 * scale, x1 - x0 - 80 * scale), CREAM)
    centered_text(d, "20:30 HS", (center_x, y0 + 150 * scale), font(BAUHAUS, 76 * scale), MARIGOLD)

    badge_w, badge_h = 300 * scale, 52 * scale
    bx0, by0 = center_x - badge_w / 2, y0 + 196 * scale
    d.rounded_rectangle((bx0, by0, bx0 + badge_w, by0 + badge_h), radius=badge_h / 2, fill=ORANGE)
    centered_text(d, "¡PUNTUALES!", (center_x, by0 + badge_h / 2), font(COOPER, 27 * scale), CREAM)

    centered_text(d, "REPÚBLICA DE SIRIA 255", (center_x, y0 + 280 * scale), fit_font(d, "REPÚBLICA DE SIRIA 255", ROCKWELL, 34 * scale, x1 - x0 - 80 * scale), CREAM)
    d.line((x0 + 65 * scale, y0 + 315 * scale, x1 - 65 * scale, y0 + 315 * scale), fill=(255, 239, 204, 90), width=max(1, round(2 * scale)))
    centered_text(d, "POCHOCLOS + PELÍCULA + ALGO PARA COMPARTIR", (center_x, y0 + 345 * scale), fit_font(d, "POCHOCLOS + PELÍCULA + ALGO PARA COMPARTIR", ROCKWELL, 23 * scale, x1 - x0 - 70 * scale), CREAM)
    centered_text(d, "¡HAY UN LUGAR PARA VOS!", (center_x, y0 + 390 * scale), fit_font(d, "¡HAY UN LUGAR PARA VOS!", BAUHAUS, 32 * scale, x1 - x0 - 70 * scale), MARIGOLD)


def logo_footer(image, y, height, scale):
    w = image.width
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((34 * scale, y, w - 34 * scale, y + height), radius=round(20 * scale), fill=(255, 245, 222, 245), outline=AUBERGINE, width=max(2, round(3 * scale)))
    d.line((w * 0.34, y + 30 * scale, w * 0.34, y + height - 30 * scale), fill=(50, 12, 58, 75), width=max(1, round(2 * scale)))
    d.line((w * 0.67, y + 30 * scale, w * 0.67, y + height - 30 * scale), fill=(50, 12, 58, 75), width=max(1, round(2 * scale)))

    church = logo(ROOT / "logos" / "LOGO-EL RENUEVO-R-1.png", round(95 * scale), round(95 * scale))
    roots = logo(ROOT / "red_jovenes" / "logos" / "Logotipo.png", round(245 * scale), round(95 * scale))
    teens = logo(ROOT / "red_adolescentes" / "logos" / "PRINCIPAL" / "LOGOTIPOVASTAGOS.png", round(245 * scale), round(88 * scale))
    cy = y + height * 0.46
    for asset, cx in ((church, w * 0.18), (roots, w * 0.505), (teens, w * 0.835)):
        paste_centered(image, asset, cx, cy)
    centered_text(d, "IGLESIA EL RENUEVO", (w * 0.18, y + height - 24 * scale), font(ROCKWELL, 14 * scale), AUBERGINE)


def render_story():
    w, h = 1080, 1920
    image = minimal_background((w, h))
    title_block(image, 480, 850, 790, 1)
    info_panel(image, (90, 920, 990, 1340), 1)
    logo_footer(image, 1475, 220, 1)
    return image.convert("RGB")


def render_feed(size):
    w, h = size
    scale = w / 1080
    image = minimal_background(size)
    title_block(image, 330 * scale, 780 * scale, 570 * scale, scale)
    info_panel(image, (85 * scale, 615 * scale, w - 85 * scale, 1030 * scale), scale)
    logo_footer(image, 1100 * scale, 185 * scale, scale)
    return image.convert("RGB")


def main():
    render_story().save(OUT / "whatsapp-status-1080x1920-v3.jpg", quality=95, optimize=True, subsampling=0)
    render_feed((1080, 1350)).save(OUT / "instagram-1080x1350-v3.jpg", quality=95, optimize=True, subsampling=0)
    render_feed((1200, 1500)).save(OUT / "facebook-1200x1500-v3.jpg", quality=95, optimize=True, subsampling=0)


if __name__ == "__main__":
    main()
