import sys
import pygame
from settings import level_map, SCREEN_HEIGHT, SCREEN_WIDTH
from components.level import Level

# Pygame setup
pygame.display.set_caption("First Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    level.run()
    pygame.display.update()
    clock.tick(60)
