"""Game helper functions."""

import pygame
import random
import sys
from pygame.locals import *

from src.constants import (
    SCREEN_WIDTH,
    PIPE_MIN_SIZE,
    PIPE_MAX_SIZE,
    PIPE_GAP,
    SCREEN_HEIGHT,
    GROUND_WIDTH,
    PIPE_WIDTH,
)
from src.sprites import Pipe, Ground


def is_off_screen(sprite):
    """Check if a sprite is off the left side of the screen."""
    return sprite.rect[0] < -(sprite.rect[2])


def get_random_pipes(xpos, pair_id=None):
    """Generate a pair of random pipes (top and bottom) at the given x position."""
    size = random.randint(PIPE_MIN_SIZE, PIPE_MAX_SIZE)
    pipe = Pipe(False, xpos, size, pair_id=pair_id)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP, pair_id=pair_id)
    return pipe, pipe_inverted


def handle_events(bird):
    """Handle pygame events."""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                bird.bump()


def update_ground(ground_group):
    """Update ground sprites, removing off-screen ones and adding new ones."""
    ground_sprites = ground_group.sprites()
    if ground_sprites and is_off_screen(ground_sprites[0]):
        ground_group.remove(ground_sprites[0])
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)


def update_pipes(pipe_group, passed_pipes=None):
    """Update pipe sprites, removing off-screen ones and adding new ones."""
    pipe_sprites = pipe_group.sprites()
    if len(pipe_sprites) >= 2 and is_off_screen(pipe_sprites[0]):
        # Get pair_id of pipes being removed to clean up passed_pipes
        if passed_pipes is not None:
            removed_pair_id = pipe_sprites[0].pair_id
            if removed_pair_id is not None and removed_pair_id in passed_pipes:
                passed_pipes.remove(removed_pair_id)
        
        pipe_group.remove(pipe_sprites[0])
        pipe_group.remove(pipe_sprites[1])
        
        # Generate new pair with unique ID based on x position
        new_x = SCREEN_WIDTH * 2
        new_pair_id = f"pipe_{new_x}"
        pipes = get_random_pipes(new_x, pair_id=new_pair_id)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])


def check_collisions(bird_group, ground_group, pipe_group):
    """Check for collisions between bird and ground/pipes."""
    return (
        pygame.sprite.groupcollide(
            bird_group, ground_group, False, False, pygame.sprite.collide_mask
        )
        or pygame.sprite.groupcollide(
            bird_group, pipe_group, False, False, pygame.sprite.collide_mask
        )
    )


def reset_game(bird, ground_group, pipe_group):
    """Reset game state for a new round."""
    bird.reset()

    # Reset ground
    ground_group.empty()
    for i in range(2):
        ground = Ground(GROUND_WIDTH * i)
        ground_group.add(ground)

    # Reset pipes
    pipe_group.empty()
    for i in range(2):
        xpos = SCREEN_WIDTH * i + 800
        pair_id = f"pipe_{xpos}"
        pipes = get_random_pipes(xpos, pair_id=pair_id)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    return set()  # Return passed_pipes set
