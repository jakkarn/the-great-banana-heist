import pygame
from banana_peel import BananaPeel
from constants import IMAGE_BANANA, IMAGE_MONKEY, PLAYER_BLUE, TILE_SIZE, PLAYER_MAX_ENERGY, PLAYER_START_BANANA_COUNT
from draw_utils import draw_circle, draw_font, draw_image
from entity import Entity
from view_port import SCREEN

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.energy = PLAYER_MAX_ENERGY
        self.banana_count = PLAYER_START_BANANA_COUNT

    def update(self, game_data):
        self.check_if_winning(game_data)
        self.eat_banana_action(game_data)
        self.update_movement(game_data)
        self.pick_up_banana(game_data)

        if self.energy <= 0:
            self.eat_banana(game_data)

    def draw(self):
        draw_image(IMAGE_MONKEY, self.position)
        draw_image(IMAGE_BANANA, (13,1))
        draw_font(f"x {self.banana_count}", (14,1))

    def update_movement(self, game_data):
        walked = False
        super().update(game_data)
        for event in game_data.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    walked = self.walk((-1, 0), game_data)
                if event.key == pygame.K_RIGHT:
                    walked = self.walk((1, 0), game_data)
                if event.key == pygame.K_UP:
                    walked = self.walk((0, -1), game_data)
                if event.key == pygame.K_DOWN:
                    walked = self.walk((0, 1), game_data)
        if walked == True:
            self.energy -= 1

    def pick_up_banana(self, game_data):
        bananas = game_data.get_bananas()
        bananas_to_pickup = [banana for banana in bananas if banana.position == self.position]

        for banana in bananas_to_pickup:
            self.banana_count += 1
            game_data.remove_entity(banana)

    def eat_banana_action(self, game_data):
        for event in game_data.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.eat_banana(game_data)

    def check_if_winning(self, game_data):
        if game_data.grid.is_winningtile(self.position):
            print("you win!")

    def eat_banana(self, game_data):
        self.banana_count -= 1
        self.energy = PLAYER_MAX_ENERGY

        bananas = game_data.get_banana_peels()
        for banana_peel in bananas:
            if banana_peel.position == self.position:
                return # TODO: put SUPER BANANA INSTEAD

        game_data.entities += [BananaPeel(self.position)]
    #def banana_action_pressed():
    #    for event in pygame.event.get():
    #        if event.key == K_SPACE:
    #            banana_peels += [Banana_Peel(self.position)]
