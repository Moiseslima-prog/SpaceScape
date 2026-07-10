import random

from settings import HEIGHT, WIDTH
from src.game_object import GameObject


class Meteor(GameObject):

    def __init__(self, image, speed):

        x = random.randint(0, WIDTH - image.get_width())
        y = -image.get_height()

        super().__init__(image, x, y)

        self.speed = speed

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()