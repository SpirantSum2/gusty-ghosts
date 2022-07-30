import pygame

from . import consts
from .painter import display_brush, display_colour_selection, draw_to_canvas

WIDTH, HEIGHT = (740, 580)
CANV_WIDTH, CANV_HEIGHT = (640, 480)

if __name__ == "__main__":
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    CANVAS = pygame.Surface((CANV_WIDTH, CANV_HEIGHT))

    # Set the title of the window
    pygame.display.set_caption("Picphone")

    CANVAS.fill(consts.WHITE)
    WINDOW.fill(consts.GREY)
    current_colour = consts.BLACK
    current_size = 10

    colour_selection = display_colour_selection(WINDOW, consts.COLOURS)

    while True:
        for event in pygame.event.get():
            # quitting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # change size with scroll
            elif event.type == pygame.MOUSEBUTTONDOWN:
                display_brush(WINDOW, consts.GREY, 30)
                if event.button == 4:
                    current_size += 1
                elif event.button == 5:
                    current_size -= 1
                if current_size < 1:
                    current_size = 1
                elif current_size > 30:
                    current_size = 30

        # left mouse button
        if pygame.mouse.get_pressed()[0]:
            draw_to_canvas(CANVAS, current_colour, current_size)  # draw to canvas
            display_brush(WINDOW, consts.GREY, 30)

            for i, rect in enumerate(colour_selection):
                if rect.collidepoint(pygame.mouse.get_pos()):
                    current_colour = consts.COLOURS[i]
                    display_brush(WINDOW, current_colour, current_size)

        # right click
        elif pygame.mouse.get_pressed()[2]:
            draw_to_canvas(CANVAS, consts.WHITE, current_size)  # white (eraser)

        # middle click
        elif pygame.mouse.get_pressed()[1]:
            CANVAS.fill(consts.WHITE)  # clear canvas

        WINDOW.blit(CANVAS, (0, 0))
        display_brush(WINDOW, current_colour, current_size)
        display_colour_selection(WINDOW, consts.COLOURS)

        pygame.display.update()
