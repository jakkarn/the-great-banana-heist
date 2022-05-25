import pygame
from constants import IMAGE_BANANA, SCREEN_BACKGROUND_COLOR, START_LEVEL
from draw_utils import draw_font, draw_image
from game_data import GameData
from level_loader import load_level
from player import Player
from view_port import SCREEN

class GameLoop():
    def __init__(self):
        self.running = True
        self.current_level = START_LEVEL
        self.has_won = False
        self.win_screen = False
        pygame.font.init() # you have to call this at the start
        self.reload_level()

    def add_entity(self, entity):
        self.entities += [entity]

    def update(self):

        if self.no_player():
            self.reload_level()

        if self.has_won:
            self.load_next_level()

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        if not self.running:
            return False

        if self.win_screen:
            self.draw_win_screen()
            return True

        game_data = GameData()
        game_data.events = events
        game_data.grid = self.grid
        game_data.entities = self.entities

        self.update_entities(game_data)
        self.grid.update(game_data)
        self.draw_entities(game_data)

        self.has_won = game_data.has_won

        return True

    def update_entities(self, game_data):
        for entity in self.entities:
            if hasattr(entity, "update"):
                entity.update(game_data)

    def draw_entities(self, game_data):

        SCREEN.fill(SCREEN_BACKGROUND_COLOR)

        game_data.grid.draw()

        for entity in self.entities:
            if hasattr(entity, "draw"):
                entity.draw()

        pygame.display.flip()

    def draw_win_screen(self):

        SCREEN.fill(SCREEN_BACKGROUND_COLOR)
        draw_font("No more levels T.T", (3,2))
        draw_font("YOU WIN", (3.5,4))
        draw_image(IMAGE_BANANA, (2.25, 3.75))
        draw_image(IMAGE_BANANA, (6, 3.75))
        draw_font("Why not add more levels in levels directory?", (1,6))
        pygame.display.flip()

    def no_player(self):
        if not self.entities:
            return True

        for entity in self.entities:
            if isinstance(entity, Player):
                return False

        return True

    def reload_level(self):
        if self.win_screen:
            return

        self.grid, self.entities = load_level(self.current_level)

        if self.grid == None:
            self.win_screen = True

    def load_next_level(self):
        if self.win_screen:
            return

        self.current_level += 1
        self.grid, self.entities = load_level(self.current_level)

        if self.grid == None:
            self.win_screen = True