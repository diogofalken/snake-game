import pygame


class Snake:
    def __init__(self, color, _x_pos, _y_pos, velocity):
        self.color = color
        self.x_pos = _x_pos
        self.y_pos = _y_pos
        self.velocity = velocity

    def move(self, window):
        # Check if "X" quit button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # Check key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x_pos >= self.velocity:
            self.x_pos -= self.velocity
        if keys[pygame.K_RIGHT] and self.x_pos <= window.width - 20 - self.velocity:
            self.x_pos += self.velocity
        if keys[pygame.K_UP] and self.y_pos >= self.velocity:
            self.y_pos -= self.velocity
        if keys[pygame.K_DOWN] and self.y_pos <= window.height - 20 - self.velocity:
            self.y_pos += self.velocity

        # Then it is all good
        return True

    def reset(self, pos):
        pass

    def draw(self, window):
        pygame.draw.rect(window,
                         self.color,
                         (self.x_pos,
                          self.y_pos,
                             20,
                             20))
