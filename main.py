import pygame
import random
from player import Player
from fruit import Fruit

pygame.display.init()

END_GAME = 3
VELOCITY = 10
window_width = 500
window_height = 500
win = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("First Game")

width = height = 10

player = Player(50, 50, width, height, VELOCITY)

fruit = Fruit(width, height, window_width, window_height, VELOCITY)

run = True
while run:
    pygame.time.delay(100)

    # Check if game ended
    if player.PlayerEndedGame(END_GAME) == True:
        pygame.display.set_caption("End Game!!")
        pygame.time.delay(3000)

        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Check key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x_pos >= player.velocity:
        player.x_pos -= player.velocity
    if keys[pygame.K_RIGHT] and player.x_pos <= window_width - width - player.velocity:
        player.x_pos += player.velocity
    if keys[pygame.K_UP] and player.y_pos >= player.velocity:
        player.y_pos -= player.velocity
    if keys[pygame.K_DOWN] and player.y_pos <= window_height - height - player.velocity:
        player.y_pos += player.velocity

    # Verify if fruit was eaten
    fruit.ResetFruit(player)

    # Reset window
    win.fill((0, 0, 0))

    # Draw player
    pygame.draw.rect(win,
                     (255, 0, 0),
                     (player.x_pos,
                      player.y_pos,
                      width,
                      height))

    # Draw fruit
    pygame.draw.rect(win, (0, 255, 0), (fruit.x_pos,
                                        fruit.y_pos, width, height))

    # Update window
    pygame.display.update()

pygame.display.quit()
