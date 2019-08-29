import random


class Fruit:
    def __init__(self, _width, _height, w_width, w_height, _velocity):
        self.width = _width
        self.height = _height
        self.w_width = w_width
        self.w_height = w_height
        self.velocity = _velocity
        self.x_pos = self.RandomXPos()
        self.y_pos = self.RandomYPos()

    def RandomXPos(self):
        return random.randrange(0, self.w_width, self.velocity)

    def RandomYPos(self):
        return random.randrange(0, self.w_height, self.velocity)

    def ResetFruit(self, player):
        if(player.x_pos == self.x_pos and player.y_pos == self.y_pos):
            self.x_pos = self.RandomXPos()
            self.y_pos = self.RandomYPos()
            player.points += 1
