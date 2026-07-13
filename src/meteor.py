import random

from settings import HEIGHT, WIDTH
from src.game_object import GameObject


class Meteor(GameObject):

    def __init__(self, image, speed):

        x = random.randint(0, WIDTH - image.get_width())
        y = -image.get_height()

        super().__init__(image, x, y)

        self.speed = speed

        # Evita contabilizar o mesmo meteoro mais de uma vez
        self.counted = False

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            return True

        return False