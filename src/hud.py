import pygame

from settings import GAME_TIME
from src.game_state import GameState


class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont("Arial", 30)
        self.big_font = pygame.font.SysFont("Arial", 60)

    def draw(self, screen, state, start_time):

        if state == GameState.PLAYING:

            elapsed = (pygame.time.get_ticks() - start_time) / 1000

            remaining = max(0, GAME_TIME - int(elapsed))

            text = self.font.render(
                f"Tempo: {remaining}",
                True,
                (255, 255, 255)
            )

            screen.blit(text, (20, 20))


        elif state == GameState.GAME_OVER:

            text = self.big_font.render(

                "GAME OVER",

                True,

                (255, 50, 50)

            )

            rect = text.get_rect(center=(500, 300))

            screen.blit(text, rect)

            info = self.font.render(

                "Pressione ENTER para jogar novamente",

                True,

                (255, 255, 255)

            )

            info_rect = info.get_rect(center=(500, 360))

            screen.blit(info, info_rect)


        elif state == GameState.VICTORY:

            text = self.big_font.render(

                "VOCÊ VENCEU!",

                True,

                (50, 255, 50)

            )

            rect = text.get_rect(center=(500, 300))

            screen.blit(text, rect)

            info = self.font.render(

                "Pressione ENTER para jogar novamente",

                True,

                (255, 255, 255)

            )

            info_rect = info.get_rect(center=(500, 360))

            screen.blit(info, info_rect)