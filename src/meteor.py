import random

from settings import HEIGHT, METEOR_SPEED, WIDTH
from src.game_object import GameObject


class Meteor(GameObject):

    def __init__(self, image):

        x = random.randint(0, WIDTH - image.get_width())
        y = -image.get_height()

        super().__init__(image, x, y)

        self.speed = METEOR_SPEED

    def update(self):

        self.rect.y += self.speed

        # Quando sair da tela, remove do grupo
        if self.rect.top > HEIGHT:
            self.kill()