# Will contain a fruit class, All variants' code will be here!
import pygame
from pygame.math import Vector2 as V2
import settings

class FRUIT:
    def __init__(self):
        self.pos = V2(0,0)

    def draw_fruit(self, surface):
        fruit_rect = pygame.Rect(
            int(int(self.pos.x * settings.cell_size)),
            int(int(self.pos.y * settings.cell_size)),
            settings.cell_size,
            settings.cell_size
        )
        pygame.draw.rect(surface,pygame.Color(126,166,155), fruit_rect)