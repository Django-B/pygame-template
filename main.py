import pygame 
import random


WIDTH = 500
HEIGHT = 500
FPS = 30

# colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create window
pygame.init()
# game.mixer.init() # on sounds
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# game cycle
running = True
while running:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # update
    screen.fill(BLACK)
    # visualization
    pygame.display.flip()

pygame.quit()
