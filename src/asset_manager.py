import os
import pygame


class AssetManager:
    """
    Responsável por carregar e armazenar todos os assets do jogo.
    """

    player = None
    meteor = None
    background = None
    explosion = None

    @classmethod
    def load_images(cls):

        base_path = os.path.join("assets", "images")

        cls.player = pygame.image.load(
            os.path.join(base_path, "player.png")
        ).convert_alpha()

        cls.meteor = pygame.image.load(
            os.path.join(base_path, "meteor.png")
        ).convert_alpha()

        cls.background = pygame.image.load(
            os.path.join(base_path, "background.png")
        ).convert()

        cls.explosion = pygame.image.load(
            os.path.join(base_path, "explosion.png")
        ).convert_alpha()