import pygame
import sys

import aesthetic

pygame.init()

bg_screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()

bg_screen.fill(aesthetic.bg_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)