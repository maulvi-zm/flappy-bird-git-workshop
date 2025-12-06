"""Game helper functions."""

import pygame
import sys
from pygame.locals import *

from src.constants import GROUND_WIDTH
from src.sprites import Ground


def handle_events(bird):
    """Handle pygame events."""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                bird.bump()


def is_off_screen(sprite):
    """Check if a sprite is off the left side of the screen."""
    return sprite.rect[0] < -(sprite.rect[2])


def update_ground(ground_group):
    """Update ground sprites, removing off-screen ones and adding new ones."""
    ground_sprites = ground_group.sprites()
    if ground_sprites and is_off_screen(ground_sprites[0]):
        ground_group.remove(ground_sprites[0])
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)
