import pygame


class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Arial", 64, bold=True)
        self.text_font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 22)

    def draw(self, screen):

        width = screen.get_width()

        # Título
        title = self.title_font.render(
            "SPACE ESCAPE",
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            title.get_rect(center=(width // 2, 100))
        )

        # Objetivo
        objective = self.text_font.render(
            "Sobreviva por 30 segundos",
            True,
            (255, 255, 255)
        )

        screen.blit(
            objective,
            objective.get_rect(center=(width // 2, 200))
        )

        # Controles
        controls = self.text_font.render(
            "Controles:",
            True,
            (255, 255, 255)
        )

        screen.blit(
            controls,
            controls.get_rect(center=(width // 2, 280))
        )

        arrows = self.small_font.render(
            "<-  ->   ou   A / D  para mover",
            True,
            (220, 220, 220)
        )

        screen.blit(
            arrows,
            arrows.get_rect(center=(width // 2, 320))
        )

        start = self.text_font.render(
            "Pressione ENTER para iniciar",
            True,
            (255, 255, 0)
        )

        screen.blit(
            start,
            start.get_rect(center=(width // 2, 450))
        )