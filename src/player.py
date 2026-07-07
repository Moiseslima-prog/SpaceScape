import pygame

from settings import PLAYER_SPEED, WIDTH
from src.game_object import GameObject


class Player(GameObject):

    def __init__(self, image, x, y):

        super().__init__(image, x, y)

        self.speed = PLAYER_SPEED

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH