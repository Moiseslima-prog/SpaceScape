import os
import pygame


class AssetManager:
    player = None
    meteor = None
    explosion = None
    background = None

    @classmethod
    def load_images(cls):
        base = os.path.join("assets", "images")

        cls.player = pygame.transform.scale(
            pygame.image.load(
                os.path.join(base, "player.png")
            ).convert_alpha(),
            (70, 70)
        )

        cls.meteor = pygame.transform.scale(
            pygame.image.load(
                os.path.join(base, "meteor.png")
            ).convert_alpha(),
            (60, 60)
        )

        cls.explosion = pygame.transform.scale(
            pygame.image.load(
                os.path.join(base, "explosion.png")
            ).convert_alpha(),
            (120, 120)
        )

        cls.background = pygame.transform.scale(
            pygame.image.load(
                os.path.join(base, "background.png")
            ).convert(),
            (1000, 700)
        )
