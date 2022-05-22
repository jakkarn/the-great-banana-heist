import pygame
from constants import SCREEN_BACKGROUND_COLOR
from game_data import GameData
from level_loader import load_level
from player import Player
from view_port import SCREEN

class GameLoop():
    def __init__(self):
        self.running = True
        self.current_level = 1
        self.reload_level()
        pygame.font.init() # you have to call this at the start

    def add_entity(self, entity):
        self.entities += [entity]

    def update(self):

        if self.no_player():
            self.reload_level()

        game_data = GameData()
        game_data.events = pygame.event.get()
        game_data.grid = self.grid
        game_data.entities = self.entities

        for event in game_data.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        if not self.running:
            return False

        self.update_entities(game_data)
        self.grid.update(game_data)
        self.draw_entities(game_data)

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

    def no_player(self):
        for entity in self.entities:
            if isinstance(entity, Player):
                return False

        return True

    def reload_level(self):
        self.grid, self.entities = load_level(self.current_level)

    def load_next_level(self):
        self.current_level += 1
        self.grid, self.entities = load_level(self.current_level)