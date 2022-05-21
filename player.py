import pygame
from constants import IMAGE_MONKEY, PLAYER_BLUE, TILE_SIZE
from draw_utils import draw_circle
from entity import Entity
from view_port import SCREEN

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)

    def update(self, game_data):
        self.update_movement(game_data)

    def draw(self):
        SCREEN.blit(IMAGE_MONKEY, self.position * TILE_SIZE)

    def update_movement(self, game_data):

        # TODO: cooldown

        for event in game_data.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move((-1, 0), game_data)
                if event.key == pygame.K_RIGHT:
                    self.move((1, 0), game_data)
                if event.key == pygame.K_UP:
                    self.move((0, -1), game_data)
                if event.key == pygame.K_DOWN:
                    self.move((0, 1), game_data)

    #def banana_action_pressed():
    #    for event in pygame.event.get():
    #        if event.key == K_SPACE:
    #            banana_peels += [Banana_Peel(self.position)]
