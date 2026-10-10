from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(r"C:\Users\pmpel\projects\iglesia_el_renuevo")
OUT = ROOT / "red_jovenes" / "output" / "flyers" / "noche-pelicula-jesus-revolution-2026-09-05"
BASE = OUT / "prueba-montaje-grupo-4x5.png"
RENUEVO = ROOT / "logos" / "LOGO-EL RENUEVO-R-1.png"
RAICES = ROOT / "red_jovenes" / "logos" / "Horizontal.png"
VASTAGOS = ROOT / "red_adolescentes" / "logos" / "PARA FONDO BLANCO" / "SECUNDARIO_1VASTAGOS.png"

ROCKWELL = r"C:\Windows\Fonts\ROCKB.TTF"
COOPER = r"C:\Windows\Fonts\COOPBL.TTF"
DARK = (43, 34, 27, 255)
ORANGE = (239, 111, 5, 255)
PAPER = (247, 226, 182, 255)


def font(path, size):
    return ImageFont.truetype(path, round(size))


def centered(draw, text, x, y, face, fill):
    box = draw.textbbox((0, 0), text, font=face)
    draw.text((x - (box[2] - box[0]) / 2 - box[0], y - (box[3] - box[1]) / 2 - box[1]), text, font=face, fill=fill)


def trim(asset):
    asset = Image.open(asset).convert("RGBA")
    box = asset.getchannel("A").getbbox()
    return asset.crop(box) if box else asset


def contain(asset, max_width, max_height, monochrome=False):
    asset = trim(asset)
    if monochrome:
        alpha = asset.getchannel("A")
        asset = ImageOps.grayscale(asset).convert("RGBA")
        asset.putalpha(alpha)
    asset.thumbnail((round(max_width), round(max_height)), Image.Resampling.LANCZOS)
    return asset


def paste_center(base, asset, center_x, center_y):
    base.alpha_composite(asset, (round(center_x - asset.width / 2), round(center_y - asset.height / 2)))


def paper_background(base, size):
    width, height = size
    patch = base.crop((0, 690, base.width, 950)).resize((width, round(260 * width / base.width)), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, PAPER)
    y = 0
    flip = False
    while y < height:
        tile = ImageOps.flip(patch) if flip else patch
        canvas.alpha_composite(tile, (0, y))
        y += tile.height
        flip = not flip
    return canvas


def feathered_piece(base, crop_box, target_width):
    piece = base.crop(crop_box).convert("RGBA")
    height = round(piece.height * target_width / piece.width)
    piece = piece.resize((round(target_width), height), Image.Resampling.LANCZOS)
    mask = Image.new("L", piece.size, 0)
    inset = max(8, round(piece.width * 0.018))
    ImageDraw.Draw(mask).rectangle((inset, inset, piece.width - inset, piece.height - inset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(inset))
    piece.putalpha(ImageChops.multiply(piece.getchannel("A"), mask))
    return piece


def add_footer(image, y, height, scale):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, y, image.width, image.height), fill=(249, 232, 195, 248))
    draw.line((0, y, image.width, y), fill=ORANGE, width=max(3, round(4 * scale)))

    raices = contain(RAICES, 350 * scale, 100 * scale, monochrome=True)
    vastagos = contain(VASTAGOS, 420 * scale, 92 * scale, monochrome=True)
    center_y = y + height * 0.52
    paste_center(image, raices, image.width * 0.30, center_y)
    paste_center(image, vastagos, image.width * 0.72, center_y)


def add_copy(image, scale, y1, y2, y3, badge_top, address_y):
    draw = ImageDraw.Draw(image)
    cx = image.width / 2
    centered(draw, "Te invitamos este Sábado 5", cx, y1, font(ROCKWELL, 34 * scale), DARK)
    centered(draw, "a la Noche de Película", cx, y2, font(ROCKWELL, 34 * scale), DARK)
    centered(draw, "Comenzamos puntuales a las 20:30", cx, y3, font(ROCKWELL, 30 * scale), DARK)

    badge_w, badge_h = 470 * scale, 58 * scale
    left = cx - badge_w / 2
    draw.rounded_rectangle((left, badge_top, left + badge_w, badge_top + badge_h), radius=badge_h / 2, fill=ORANGE)
    centered(draw, "¡TRAE A UNA AMIG@!", cx, badge_top + badge_h / 2, font(COOPER, 29 * scale), (255, 248, 229, 255))
    centered(draw, "REPÚBLICA DE SIRIA 255", cx, address_y, font(ROCKWELL, 22 * scale), DARK)


def render_feed(size):
    width, height = size
    scale = width / 1080
    base = Image.open(BASE).convert("RGBA")
    image = paper_background(base, size)

    title = feathered_piece(base, (20, 82, 982, 680), 900 * scale)
    paste_center(image, title, width / 2, 330 * scale)
    paste_center(image, contain(RENUEVO, 72 * scale, 72 * scale, monochrome=True), width / 2, 43 * scale)

    add_copy(image, scale, 624 * scale, 670 * scale, 723 * scale, 753 * scale, 835 * scale)

    group = feathered_piece(base, (0, 955, base.width, 1495), 980 * scale)
    paste_center(image, group, width / 2, 1102 * scale)
    add_footer(image, 1240 * scale, 110 * scale, scale)
    return image.convert("RGB")


def render_story():
    width, height = 1080, 1920
    base = Image.open(BASE).convert("RGBA")
    image = paper_background(base, (width, height))

    title = feathered_piece(base, (20, 82, 982, 680), 980)
    paste_center(image, title, width / 2, 410)
    paste_center(image, contain(RENUEVO, 92, 92, monochrome=True), width / 2, 60)

    add_copy(image, 1, 754, 810, 874, 910, 1000)

    group = feathered_piece(base, (0, 955, base.width, 1495), 1060)
    paste_center(image, group, width / 2, 1340)
    add_footer(image, 1700, 190, 1)
    return image.convert("RGB")


def render_clean(size):
    base = Image.open(BASE).convert("RGBA")
    image = paper_background(base, size)
    fitted = ImageOps.contain(base, size, Image.Resampling.LANCZOS)
    pad_x = (size[0] - fitted.width) // 2
    pad_y = (size[1] - fitted.height) // 2
    mask = Image.new("L", fitted.size, 255)
    draw = ImageDraw.Draw(mask)
    if pad_x:
        fade = min(42, fitted.width // 12)
        for x in range(fade):
            alpha = round(255 * x / fade)
            draw.line((x, 0, x, fitted.height), fill=alpha)
            draw.line((fitted.width - 1 - x, 0, fitted.width - 1 - x, fitted.height), fill=alpha)
    if pad_y:
        fade = min(64, fitted.height // 12)
        for y in range(fade):
            alpha = round(255 * y / fade)
            draw.line((0, y, fitted.width, y), fill=alpha)
            draw.line((0, fitted.height - 1 - y, fitted.width, fitted.height - 1 - y), fill=alpha)
    fitted.putalpha(mask)
    paste_center(image, fitted, size[0] / 2, size[1] / 2)
    return image.convert("RGB")


def main():
    render_story().save(OUT / "whatsapp-status-1080x1920-v4.jpg", quality=95, optimize=True, subsampling=0)
    render_feed((1080, 1350)).save(OUT / "instagram-1080x1350-v4.jpg", quality=95, optimize=True, subsampling=0)
    render_feed((1200, 1500)).save(OUT / "facebook-1200x1500-v4.jpg", quality=95, optimize=True, subsampling=0)
    render_clean((1080, 1920)).save(OUT / "whatsapp-status-sin-texto-1080x1920.jpg", quality=95, optimize=True, subsampling=0)
    render_clean((1080, 1350)).save(OUT / "instagram-sin-texto-1080x1350.jpg", quality=95, optimize=True, subsampling=0)
    render_clean((1200, 1500)).save(OUT / "facebook-sin-texto-1200x1500.jpg", quality=95, optimize=True, subsampling=0)


if __name__ == "__main__":
    main()
