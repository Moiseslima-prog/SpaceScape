import pygame

from settings import METEOR_SPAWN_TIME
from src.asset_manager import AssetManager
from src.meteor import Meteor


class MeteorManager:

    def __init__(
            self,
            all_sprites,
            meteors
    ):

        self.all_sprites = all_sprites
        self.meteors = meteors

        self.last_spawn = pygame.time.get_ticks()

    def update(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn >= METEOR_SPAWN_TIME:

            meteor = Meteor(AssetManager.meteor)

            self.all_sprites.add(meteor)
            self.meteors.add(meteor)

            self.last_spawn = current_time

