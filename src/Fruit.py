import random
import pygame


class Fruit:
    def __init__(self, color, velocity, size, window):
        self.velocity = velocity
        self.size = size
        self.color = color
        self.window = window
        self.x_pos = self.RandomXPos()
        self.y_pos = self.RandomYPos()

        # Draw fruit
        self.Draw()

    def CheckFruitState(self, snake):
        if(snake.x_pos == self.x_pos and snake.y_pos == self.y_pos):
            self.x_pos = self.RandomXPos()
            self.y_pos = self.RandomYPos()

    def Draw(self):
        pygame.draw.rect(self.window.window, self.color,
                         (self.x_pos, self.y_pos, self.size, self.size))

    def RandomXPos(self):
        return random.randrange(0, self.window.width, self.velocity)

    def RandomYPos(self):
        return random.randrange(0, self.window.height, self.velocity)
