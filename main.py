"""Main entry point for the Flappy Bird game."""

import pygame
import sys
from pygame.locals import *

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.sprites import Bird

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

BACKGROUND = pygame.image.load("assets/sprites/background-day.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

# Main game loop
while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(BACKGROUND, (0, 0))
    bird_group.draw(screen)
    pygame.display.update()
