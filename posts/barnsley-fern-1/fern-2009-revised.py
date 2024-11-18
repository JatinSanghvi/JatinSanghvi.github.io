"""Draws the Barnsley fern - Year 2009 Version (Revised)."""

import random

from PIL import Image, ImageDraw

SCALE = 4
FINAL_DIM = 512
IMAGE_DIM = FINAL_DIM * SCALE

image = Image.new(mode="RGB", size=(IMAGE_DIM, IMAGE_DIM), color="LightYellow")
draw = ImageDraw.Draw(image)

x, y = 0.0, 0.0
stem_i = 0
hue = 0

for i in range(5000000):
    r = random.random()
    if i - stem_i >= 30 or r < 0.01:
        x, y = 0, 0.16 * y
        stem_i = i
        hue = 0
    elif r < 0.86:
        x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        if hue == 0:
            hue = min((i - stem_i) * 18, 359)

    draw.point((int((x + 5) / 10 * IMAGE_DIM), int(y / 10 * IMAGE_DIM)), f"hsl({hue}, 100%, 40%)")

image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image = image.resize((FINAL_DIM, FINAL_DIM), Image.Resampling.LANCZOS)
image.save("fern-2009-revised.png")
