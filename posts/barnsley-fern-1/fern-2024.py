"""Draws the Barnsley fern using deterministic algorithm."""

from PIL import Image, ImageDraw

SCALE = 4
FINAL_DIM = 512
IMAGE_DIM = FINAL_DIM * SCALE

image = Image.new(mode="RGB", size=(IMAGE_DIM, IMAGE_DIM), color="LightYellow")
draw = ImageDraw.Draw(image)


def draw_fern(polygon, size, i, hue):
    """Recursively draws Barnsley fern."""
    if size > 1 / (IMAGE_DIM * IMAGE_DIM):  # Determines pixel density and computation time.
        xy = [(int((x + 5) / 10 * IMAGE_DIM), int(y / 10 * IMAGE_DIM)) for x, y in polygon]
        draw.polygon(xy=xy, fill=f"hsl({hue}, 100%, 40%)", outline=None)

        # New sizes were found by calculating determinants of transformation matrices.
        draw_fern([(0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6) for x, y in polygon], size * 0.7241, i + 1, hue)
        draw_fern([(0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6) for x, y in polygon], size * 0.1038, i + 1, hue)
        draw_fern([(-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44) for x, y in polygon], size * 0.1088, i + 1, hue if hue else min(i * 18, 360))


draw_fern([(-0.02, 0), (0.02, 0), (0.017, 1.6), (-0.02, 1.6)], 1, 0, 0)

image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image = image.resize((FINAL_DIM, FINAL_DIM), Image.Resampling.LANCZOS)
image.save("fern-2024.png")
