import pygame


def draw_to_canvas(canvas, colour, size):
    """Draws a circle with specified colour and size to the canvas."""
    pygame.draw.circle(canvas, colour, pygame.mouse.get_pos(), size)
