"""Sprite classes for the Flappy Bird game."""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SPEED,
    GRAVITY,
    GAME_SPEED,
    GROUND_WIDTH,
    GROUND_HEIGHT,
    PIPE_WIDTH,
    PIPE_HEIGHT,
)


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load("assets/sprites/bluebird-upflap.png").convert_alpha(),
            pygame.image.load("assets/sprites/bluebird-midflap.png").convert_alpha(),
            pygame.image.load("assets/sprites/bluebird-downflap.png").convert_alpha(),
        ]

        self.speed = SPEED

        self.current_image = 0
        self.image = pygame.image.load(
            "assets/sprites/bluebird-upflap.png"
        ).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed += GRAVITY

        # UPDATE HEIGHT
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -SPEED

    def reset(self):
        """Reset bird to initial position and state."""
        self.speed = SPEED
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2


class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize, pair_id=None):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/sprites/pipe-green.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.inverted = inverted
        self.pair_id = pair_id  # Unique identifier for pipe pairs

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= GAME_SPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/base.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED
