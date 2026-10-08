import pygame
import sys

import aesthetic , grid
from fruit import FRUIT

pygame.init()

bg_screen = pygame.display.set_mode((grid.cell_number*grid.cell_size,grid.cell_number*grid.cell_size))
clock = pygame.time.Clock()

fruit_obj = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg_screen.fill(aesthetic.bg_color)
    fruit_obj.draw_fruit(bg_screen)
    pygame.display.update()
    clock.tick(60)