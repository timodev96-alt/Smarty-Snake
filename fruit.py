# Will contain a fruit class, All variants' code will be here!
import pygame
from pygame.math import Vector2 as V2
import grid

class FRUIT:
    def __init__(self):
        self.x = 0
        self.y = 10
        self.pos = V2(self.x,self.y)

    def draw_fruit(self, surface):
        fruit_rect = pygame.Rect(
            int(int(self.pos.x * grid.cell_size)),
            int(int(self.pos.y * grid.cell_size)),
            grid.cell_size,
            grid.cell_size
        )
        pygame.draw.rect(surface,pygame.Color(126,166,155), fruit_rect)