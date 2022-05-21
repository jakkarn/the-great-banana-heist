import pygame
from constants import SCREEN_BACKGROUND_COLOR
from game_data import GameData
from view_port import SCREEN

class GameLoop():
    def __init__(self):
        self.running = True
        self.entities = []

    def add_entity(self, entity):

        # TODO: use grid's tiles to get all the entities instead

        self.entities += [entity]

    def update(self):
        game_data = GameData()
        game_data.events = pygame.event.get()

        for event in game_data.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        if not self.running:
            return False

        self.update_entities(game_data)
        self.draw_entities()

        return True

    def update_entities(self, game_data):
        for entity in self.entities:
            if hasattr(entity, "update"):
                entity.update(game_data)

    def draw_entities(self):

        SCREEN.fill(SCREEN_BACKGROUND_COLOR)

        for entity in self.entities:
            if hasattr(entity, "draw"):
                entity.draw()

        pygame.display.flip()