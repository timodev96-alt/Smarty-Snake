# Will add the snake code here!
import pygame
from pygame.math import Vector2 as V2

import settings

class SNAKE:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [V2(5,10),V2(6,10),V2(7,10)]
        self.direction = V2(1,0)
        self.new_direction = V2(1,0)

    def change_direction(self,direction):
        if direction * -1 != self.direction:
            self.new_direction = direction

    def move_snake(self):
        self.direction = self.new_direction
        new_head = self.body[0] + self.direction
        self.body = [new_head] + self.body[:-1]

    def draw_snake(self, screen):
        for block in self.body:
            block_rect = pygame.Rect(
                int(block.x*settings.cell_size),
                int(block.y*settings.cell_size),
                settings.cell_size,
                settings.cell_size
            )
            pygame.draw.rect(screen,(183,191,232), block_rect)
            