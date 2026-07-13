import os
import pygame


class AssetManager:

    # Imagens
    player = None
    meteor = None
    explosion = None
    background = None

    # Sons
    explosion_sound = None

    menu_music = None
    gameplay_music = None
    game_over_music = None
    victory_music = None

    @classmethod
    def load_assets(cls):

        image_path = os.path.join("assets", "images")
        sound_path = os.path.join("assets", "sounds")

        # ---------- IMAGENS ----------

        cls.player = pygame.transform.scale(
            pygame.image.load(
                os.path.join(image_path, "player.png")
            ).convert_alpha(),
            (70, 70)
        )

        cls.meteor = pygame.transform.scale(
            pygame.image.load(
                os.path.join(image_path, "meteor.png")
            ).convert_alpha(),
            (60, 60)
        )

        cls.explosion = pygame.transform.scale(
            pygame.image.load(
                os.path.join(image_path, "explosion.png")
            ).convert_alpha(),
            (120, 120)
        )

        cls.background = pygame.transform.scale(
            pygame.image.load(
                os.path.join(image_path, "background.png")
            ).convert(),
            (1000, 700)
        )

        # ---------- EFEITO ----------

        cls.explosion_sound = pygame.mixer.Sound(
            os.path.join(sound_path, "explosion.wav")
        )

        cls.explosion_sound.set_volume(0.3)

        # ---------- MÚSICAS ----------

        cls.menu_music = os.path.join(
            sound_path,
            "menu.mp3"
        )

        cls.gameplay_music = os.path.join(
            sound_path,
            "game_play.mp3"
        )

        cls.game_over_music = os.path.join(
            sound_path,
            "game_over.mp3"
        )

        cls.victory_music = os.path.join(
            sound_path,
            "victory.mp3"
        )