# Will contain a fruit class, All variants' code will be here!
import random
import pygame
from pygame.math import Vector2 as V2
import settings

class FRUIT:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.pos = V2(
            random.randint(0, settings.cell_number - 1),
            random.randint(0, settings.cell_number - 1)
        )

    def draw_fruit(self, surface):
        fruit_rect = pygame.Rect(
            int(self.pos.x * settings.cell_size),
            int(self.pos.y * settings.cell_size),
            settings.cell_size,
            settings.cell_size
        )
        pygame.draw.rect(surface, pygame.Color(126, 166, 155), fruit_rect)