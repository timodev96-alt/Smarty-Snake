import pygame
import sys

import levels
import settings

def main():
    pygame.init()
    bg_screen = pygame.display.set_mode((settings.screen_size, settings.screen_size))
    clock = pygame.time.Clock()

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

        pygame.display.update()
        clock.tick(settings.FPS)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()