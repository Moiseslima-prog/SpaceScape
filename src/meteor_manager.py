import pygame
import random

from src.asset_manager import AssetManager
from src.meteor import Meteor
from settings import (
    INITIAL_METEOR_SPEED,
    MAX_METEOR_SPEED,
    INITIAL_SPAWN_DELAY,
    MIN_SPAWN_DELAY,
    SPEED_INCREASE,
    SPAWN_ACCELERATION
)

class MeteorManager:

    def __init__(
            self,
            all_sprites,
            meteors
    ):

        self.spawn_delay = INITIAL_SPAWN_DELAY
        self.meteor_speed = INITIAL_METEOR_SPEED
        self.all_sprites = all_sprites
        self.meteors = meteors

        self.last_spawn = pygame.time.get_ticks()

        meteor = Meteor(
            AssetManager.meteor,
            self.meteor_speed + random.uniform(-0.7, 0.7)
        )

    def update(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn >= self.spawn_delay:

            # Tamanho aleatório
            scale = random.uniform(0.7, 1.3)

            # Redimensiona a imagem
            meteor_image = pygame.transform.rotozoom(
                AssetManager.meteor,
                0,
                scale
            )

            # Velocidade baseada no tamanho
            speed = self.meteor_speed

            if scale < 0.9:
                speed *= 1.2

            elif scale > 1.15:
                speed *= 0.85

            meteor = Meteor(
                meteor_image,
                speed
            )

            self.all_sprites.add(meteor)
            self.meteors.add(meteor)

            self.last_spawn = current_time

    def update_difficulty(self, elapsed_time):
        self.meteor_speed = min(
            INITIAL_METEOR_SPEED + elapsed_time * SPEED_INCREASE,
            MAX_METEOR_SPEED
        )

        self.spawn_delay = max(
            INITIAL_SPAWN_DELAY - elapsed_time * SPAWN_ACCELERATION,
            MIN_SPAWN_DELAY
        )