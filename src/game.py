import pygame

from settings import WIDTH, HEIGHT, TITLE, FPS, GAME_TIME
from src.player import Player
from src.game_state import GameState
from src.asset_manager import AssetManager
from src.meteor_manager import MeteorManager
from src.collision_manager import CollisionManager
from src.hud import HUD
from src.menu import Menu
from src.explosion import Explosion

class Game:

    def __init__(self):

        pygame.init()

        self.score = 0
        self.hud = HUD()
        self.menu = Menu()

        self.start_time = pygame.time.get_ticks()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        AssetManager.load_images()

        self.clock = pygame.time.Clock()

        self.running = True

        self.state = GameState.MENU

        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()



        self.meteor_manager = MeteorManager(
            self.all_sprites,
            self.meteors
        )

        self.player = None

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    if self.state == GameState.MENU:

                        self.reset()

                    elif self.state in (
                            GameState.GAME_OVER,
                            GameState.VICTORY
                    ):

                        self.reset()

    def update(self):

        if self.state == GameState.MENU:
            return

        if self.state == GameState.PLAYING:

            self.all_sprites.update()

            elapsed = (
                              pygame.time.get_ticks() - self.start_time
                      ) / 1000

            self.meteor_manager.update_difficulty(elapsed)

            self.meteor_manager.update()

            if CollisionManager.player_hit(
                    self.player,
                    self.meteors
            ):
                explosion = Explosion(
                    AssetManager.explosion,
                    self.player.rect.center
                )

                self.explosions.add(explosion)

                self.all_sprites.add(explosion)

                self.player.kill()

                self.player = None

                self.explosion_start = pygame.time.get_ticks()

                self.state = GameState.EXPLODING

            self.check_win()

        elif self.state == GameState.EXPLODING:

            self.explosions.update()

            if pygame.time.get_ticks() - self.explosion_start > 700:
                self.state = GameState.GAME_OVER

    def draw(self):

        self.screen.blit(
            AssetManager.background,
            (0, 0)
        )

        if self.state == GameState.MENU:

            self.menu.draw(self.screen)

        else:

            self.all_sprites.draw(self.screen)

            self.hud.draw(
                self.screen,
                self.state,
                self.start_time
            )

        pygame.display.flip()

    def check_win(self):

        if self.state != GameState.PLAYING:
            return

        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000

        if elapsed >= GAME_TIME:
            self.state = GameState.VICTORY

    def run(self):

        while self.running:
            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

        pygame.quit()

    def reset(self):

        self.all_sprites.empty()
        self.meteors.empty()

        self.player = Player(
            AssetManager.player,
            WIDTH // 2 - AssetManager.player.get_width() // 2,
            HEIGHT - AssetManager.player.get_height() - 20
        )

        self.all_sprites.add(self.player)

        self.meteor_manager = MeteorManager(
            self.all_sprites,
            self.meteors
        )

        self.start_time = pygame.time.get_ticks()
        self.score = 0
        self.state = GameState.PLAYING