# Out of memory
from PIL import Image
import random

image = Image.open("winter.png")

pixels = list(image.getdata())
gray_pixels = []

for index, pixel in enumerate(pixels):
    r, g, b = pixel

    if r == g == b and 50 <= r <= 200:
        gray_pixels.append(index)

amount = int(len(gray_pixels) * 0.3)
selected_pixels = random.sample(gray_pixels, amount)

for index in selected_pixels:
    pixels[index] = (34, 139, 34)

image.putdata(pixels)
image.save("spring.png")
