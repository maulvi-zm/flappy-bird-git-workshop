"""Sprite classes for the Flappy Bird game."""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/sprites/bluebird-upflap.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2
