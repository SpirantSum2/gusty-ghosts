import random


def get_image(canvas):
    """Gets the image in the required format from the canvas"""
    ...


def noisy_image(image, pixels, colours, swaps):
    """Adds random colours to random pixels in the image."""
    for _ in range(swaps):
        x = random.randint(0, 639)
        y = random.randint(0, 479)
        image[y][x] = random.choice(colours)

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
            image[y+i][x+j] = (0, 0, 0)
