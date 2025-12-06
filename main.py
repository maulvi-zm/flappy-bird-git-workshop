"""Main entry point for the Flappy Bird game."""

import pygame
import sys
from pygame.locals import *

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GROUND_WIDTH
from src.sprites import Bird, Ground
from src.game import (
    handle_events,
    update_ground,
    update_pipes,
    check_collisions,
    get_random_pipes,
    reset_game,
)

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

pipe_group = pygame.sprite.Group()
for i in range(2):
    xpos = SCREEN_WIDTH * i + 800
    pair_id = f"pipe_{xpos}"
    pipes = get_random_pipes(xpos, pair_id=pair_id)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()

# Main game loop - restarts after each loss
# BUG: score is initialized outside the loop, so it doesn't reset on restart
score = 0
passed_pipes = set()

while True:
    clock.tick(FPS)
    handle_events(bird)

    screen.blit(BACKGROUND, (0, 0))

    update_ground(ground_group)
    update_pipes(pipe_group, passed_pipes)

    bird_group.update()
    ground_group.update()
    pipe_group.update()

    bird_group.draw(screen)
    pipe_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()

    if check_collisions(bird_group, ground_group, pipe_group):
        pygame.time.wait(1000)
        reset_game(bird, ground_group, pipe_group)
        # BUG: score and passed_pipes are not reset here
        # They should be reset to 0 and set() respectively
