import pygame

from settings import WIDTH, HEIGHT, TITLE, FPS
from src.player import Player
from src.game_state import GameState
from src.asset_manager import AssetManager

class Game:

    def __init__(self):

        pygame.init()

        AssetManager.load_images()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        # Estados do jogo
        self.state = GameState.MENU

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        # Sprite temporário da nave
        player_surface = pygame.Surface((60, 60))
        player_surface.fill((0, 120, 255))

        self.player = Player(
            player_surface,
            WIDTH // 2 - 30,
            HEIGHT - 90
        )

        self.all_sprites.add(self.player)

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):

        self.screen.fill((20, 20, 35))

        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def run(self):

        while self.running:

            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

        pygame.quit()