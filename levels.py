import pygame

class BaseLevel:
    def __init__(self, manager):
        self.manager = manager
        self.bg_color = (0, 0, 0)

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color)

class Level1(BaseLevel):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (175, 215, 70)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("level2")
            self.manager.set_level("level2")

class Level2(BaseLevel):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (70, 130, 215)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("level1")
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
        else:
            print(f"Error: Level '{level_name}' does not exist")

    def handle_event(self, event):
        if self.current_level:
            self.current_level.handle_event(event)

    def update(self):
        if self.current_level:
            self.current_level.update()

    def draw(self, surface):
        if self.current_level:
            self.current_level.draw(surface)