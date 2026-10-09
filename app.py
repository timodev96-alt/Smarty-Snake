import pygame
import sys
from pygame import Vector2 as V2

import aesthetic , grid , levels
from snake import SNAKE
from fruit import FRUIT


def main():
    pygame.init()
    bg_screen = pygame.display.set_mode((grid.cell_number*grid.cell_size,grid.cell_number*grid.cell_size))
    clock = pygame.time.Clock()

    fruit_obj = FRUIT()
    snake_obj = SNAKE()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    manager = levels.LevelManager()
    manager.set_level("level1")

    running=True
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == SCREEN_UPDATE:
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_obj.direction = V2(0,-1)
                    snake_obj.move_snake()
                if event.key == pygame.K_DOWN:
                    snake_obj.direction = V2(0, 1)
                    snake_obj.move_snake()
                if event.key == pygame.K_LEFT:
                    snake_obj.direction = V2(-1,0)
                    snake_obj.move_snake()
                if event.key == pygame.K_RIGHT:
                    snake_obj.direction = V2(1,0)
                    snake_obj.move_snake()

            manager.handle_event(event)

        manager.update()
        manager.draw(bg_screen)

        fruit_obj.draw_fruit(bg_screen)
        snake_obj.draw_snake(bg_screen)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()