class Player:
    def __init__(self, _x_pos, _y_pos, _width, _height, _velocity):
        self.x_pos = _x_pos
        self.y_pos = _y_pos
        self.width = _width
        self.height = _height
        self.points = 0
        self.velocity = _velocity

    def PlayerEndedGame(self, maxPoints):
        if self.points == maxPoints:
            return True
        return False
