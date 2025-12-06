"""Main entry point for the Flappy Bird game."""

import pygame
import sys
from pygame.locals import *

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GROUND_WIDTH
from src.sprites import Bird, Ground
from src.game import handle_events, update_ground

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

BACKGROUND = pygame.image.load("assets/sprites/background-day.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

clock = pygame.time.Clock()

# Main game loop
while True:
    clock.tick(FPS)
    handle_events(bird)

    screen.blit(BACKGROUND, (0, 0))

    update_ground(ground_group)

    bird_group.update()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)
    pygame.display.update()
