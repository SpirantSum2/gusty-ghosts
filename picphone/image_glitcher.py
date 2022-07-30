import random

from pygame import PixelArray


def get_image(canvas):
    """Gets the image in the required format from the canvas"""
    pix = PixelArray(canvas)  # must be .close()ed after use

    image = []
    for x in range(640):
        column = []
        for y in range(480):
            val = pix[x, y]  # returns a 24-bit int so i have to do this stupid conversion
            r = (val & 255 << 16) >> 16
            g = (val & 255 << 8) >> 8
            b = val & 255
            column.append((r, g, b))
        image.append(column)

    pix.close()  # surface gets frozen otherwise

    return image


def set_image(image, canvas):
    """Sets the image in the canvas"""
    pix = PixelArray(canvas)

    for x in range(640):
        for y in range(480):
            pix[x, y] = image[x][y]

    pix.close()


def noisy_image(image, pixels, colours, swaps):
    """Adds random colours to random pixels in the image."""
    for _ in range(swaps):  # so you can set "glitchyness"
        x = random.randint(0, 639)
        y = random.randint(0, 479)
        image[x][y] = random.choice(colours)

    return image


def swap_colours(image, swaps, colours):
    """Swaps 2 random chosen colours in the image."""
    for _ in range(swaps):
        col1 = random.choice(colours)
        col2 = random.choice(colours)

        for column in image:
            for i, pixel in enumerate(column):
                if pixel == col1:
                    column[i] = col2
                elif pixel == col2:
                    column[i] = col1

    return image


def censor_image(image):
    """Selects 1/16 of the image and replaces it with black."""
    x = random.randint(0, 479)
    y = random.randint(0, 359)

    for i in range(160):
        for j in range(120):
            image[x+i][y+j] = (0, 0, 0)

    return image
