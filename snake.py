# Will add the snake code here!
import pygame
from pygame.math import Vector2 as V2

import grid

class SNAKE:
    def __init__(self):
        self.body = [V2(5,10),V2(6,10),V2(7,10)]

        self.direction = V2(1,0)

    def draw_snake(self, screen):
        for block in self.body:
            block_rect = pygame.Rect(
                int(block.x*grid.cell_size),
                int(block.y*grid.cell_size),
                grid.cell_size,
                grid.cell_size)
            pygame.draw.rect(screen,(183,191,232), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy