# Copyright (c) 2024 Jatin Sanghvi
# All rights reserved.

"""Draws the Barnsley fern - Year 2009 Version."""

import random

from PIL import Image, ImageDraw

IMAGE_DIM = 512

image = Image.new("RGB", (IMAGE_DIM, IMAGE_DIM), "LightYellow")
draw = ImageDraw.Draw(image)

for i in range(1000000):
    x, y, hue = 0.0, 0.0, 0
    for j in range(20):
        r = random.random()
        if r < 0.85:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.92:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        elif r < 0.99:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
            if hue == 0:
                hue = j * 18
        else:
            x, y = 0, 0.16 * y

    draw.point((int((x + 5) / 10 * IMAGE_DIM), int(y / 10 * IMAGE_DIM)), f"hsl({hue}, 100%, 40%)")

image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).save("fern-2009.png")
