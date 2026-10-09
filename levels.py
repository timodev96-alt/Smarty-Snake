import pygame
from pygame.math import Vector2 as V2
import settings
from snake import SNAKE
from fruit import FRUIT

class BaseLevel:
    def __init__(self, manager):
        self.manager = manager
        self.bg_color = (0, 0, 0)

        self.snake = SNAKE()
        self.fruit = FRUIT()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.change_direction(V2(0,-1))
                self.snake.move_snake()
            elif event.key == pygame.K_DOWN:
                self.snake.change_direction(V2(0,1))
                self.snake.move_snake()
            elif event.key == pygame.K_LEFT:
                self.snake.change_direction(V2(-1,0))
                self.snake.move_snake()
            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction(V2(1,0))
                self.snake.move_snake()

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color)
        self.fruit.draw_fruit(surface)
        self.snake.draw_snake(surface)

class Level1(BaseLevel):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = pygame.Color(175,215,70)

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Level 2")
            self.manager.set_level("level2")

class Level2(BaseLevel):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = pygame.Color('blue')

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Level 1")
            self.manager.set_level("level1")

class LevelManager:
    def __init__(self):
        self.level_classes = {
            "level1": Level1,
            "level2": Level2,
        }
        self.current_level = None

    def set_level(self, level_name):
        if level_name in self.level_classes:
            self.current_level = self.level_classes[level_name](self)

    def handle_event(self, event):
        if self.current_level:
            self.current_level.handle_event(event)

    def update(self):
        if self.current_level:
            self.current_level.update()

    def draw(self, surface):
        if self.current_level:
            self.current_level.draw(surface)