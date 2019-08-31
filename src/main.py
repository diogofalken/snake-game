from Snake import Snake
from Canvas import Canvas
from Fruit import Fruit
import pygame
import random
#from player import Player

pygame.display.init()

END_GAME = 3
VELOCITY = 10

# Create canvas
win = Canvas(500, 500)

width = height = 20

#player = Player(50, 50, width, height, VELOCITY)

snake = Snake((255, 0, 0), 20, 20, VELOCITY)

fruit = Fruit((0, 255, 0), VELOCITY, height, win)

clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(100)
    clock.tick(10)

    # Check if game ended
    # if player.PlayerEndedGame(END_GAME) == True:
    #   pygame.display.set_caption("End Game!!")
    #   pygame.time.delay(3000)
    #  run = False

    # Check snake movement or if the 'X' quit button was pressed
    run = snake.move(win)

    # Verify if fruit was eaten
    fruit.CheckFruitState(snake)

    # Reset window
    win.RedrawCanvas()

    snake.draw(win.window)

    # Draw fruit
    fruit.Draw()

    # Update window
    pygame.display.update()

pygame.display.quit()
