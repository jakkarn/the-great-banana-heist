import pygame
from constants import PLAYER_BLUE, TILE_SIZE
from draw_utils import draw_circle
from entity import Entity

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)

    def update(self, game_data):
        self.update_movement(game_data.events)

    def draw(self):
        draw_circle(PLAYER_BLUE, self.position, TILE_SIZE/2)

    def update_movement(self, events):

        # TODO: cooldown

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move((-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.move((1, 0))
                if event.key == pygame.K_UP:
                    self.move((0, -1))
                if event.key == pygame.K_DOWN:
                    self.move((0, 1))

    #def banana_action_pressed():
    #    for event in pygame.event.get():
    #        if event.key == K_SPACE:
    #            banana_peels += [Banana_Peel(self.position)]
