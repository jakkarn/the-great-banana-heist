import pygame
from banana_peel import BananaPeel
from constants import IMAGE_MONKEY, PLAYER_BLUE, TILE_SIZE
from draw_utils import draw_circle, draw_image
from entity import Entity
from view_port import SCREEN

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)

    def update(self, game_data):
        self.eat_banana(game_data)
        self.update_movement(game_data)

    def draw(self):
        draw_image(IMAGE_MONKEY, self.position)

    def update_movement(self, game_data):

        super().update(game_data)
        for event in game_data.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.walk((-1, 0), game_data)
                if event.key == pygame.K_RIGHT:
                    self.walk((1, 0), game_data)
                if event.key == pygame.K_UP:
                    self.walk((0, -1), game_data)
                if event.key == pygame.K_DOWN:
                    self.walk((0, 1), game_data)

    def eat_banana(self, game_data):
        for event in game_data.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                # TODO: not duplicate banana peels

                game_data.entities += [BananaPeel(self.position)]


    #def banana_action_pressed():
    #    for event in pygame.event.get():
    #        if event.key == K_SPACE:
    #            banana_peels += [Banana_Peel(self.position)]
