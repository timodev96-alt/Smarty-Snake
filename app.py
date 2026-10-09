import pygame
import sys

import aesthetic , grid , levels
from fruit import FRUIT


def main():
    pygame.init()
    bg_screen = pygame.display.set_mode((grid.cell_number*grid.cell_size,grid.cell_number*grid.cell_size))
    clock = pygame.time.Clock()

    fruit_obj = FRUIT()
    manager = levels.LevelManager()
    manager.set_level("level1")

    running=True
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)

        manager.update()
        manager.draw(bg_screen)

        fruit_obj.draw_fruit(bg_screen)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()