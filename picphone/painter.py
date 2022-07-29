import pygame


def draw_to_canvas(canvas, colour, size):
    """Draws a circle with specified colour and size to the canvas."""
    pygame.draw.circle(canvas, colour, pygame.mouse.get_pos(), size)


def display_brush(canvas, colour, size):
    """Displays the current brush colour and size."""
    pygame.draw.circle(canvas, colour, (50, 530), size)


def display_colour_selection(canvas, colours):
    """Displays the colour selection."""
    rects = []

    for i, colour in enumerate(colours):
        pos = pygame.Rect(85+50*i, 515, 30, 30)
        rects.append(pos)
        pygame.draw.rect(canvas, colour, pos)

    return rects
