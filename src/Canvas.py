import pygame


class Canvas:
    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("First Game")
        self.width = width
        self.height = height

    def RedrawCanvas(self):
        self.window.fill((0, 0, 0))
