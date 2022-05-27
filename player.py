import pygame
from banana_peel import BananaPeel
from constants import IMAGE_BANANA, IMAGE_MONKEY, PLAYER_BLUE, SOUND_PLAYER_DEATH, SOUND_PLAYER_EAT, SOUND_PLAYER_SLIP, TILE_SIZE, PLAYER_MAX_ENERGY, PLAYER_START_BANANA_COUNT
from draw_utils import draw_circle, draw_death, draw_font, draw_image
from entity import Entity
from guard import Guard
from view_port import SCREEN
from timer import Timer

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.energy = PLAYER_MAX_ENERGY
        self.banana_count = PLAYER_START_BANANA_COUNT
        self.death_timer = Timer(0)
        self.death_started = False
        self.is_playing_slip_sound = False

    def update(self, game_data):
        if not self.alive:
            self.death(game_data)
            return
        
        if self.is_slipping:
            self.play_slip_sound()
            self.is_playing_slip_sound = True
        else:
            self.is_playing_slip_sound = False

        self.check_if_winning(game_data)
        self.check_if_guard(game_data)
        self.eat_banana_action(game_data)
        self.update_movement(game_data)
        self.pick_up_banana(game_data)

        if self.energy <= 0:
            self.eat_banana(game_data)

    def draw(self):
        draw_font(f"x {self.banana_count}", (14,1))
        draw_image(IMAGE_BANANA, (13,0.75))
        draw_font(f"energy: {self.energy}", (13,3))
        draw_font(f"eat: <space>", (13,5))
        draw_font(f"move: arrow keys", (13,6))

        if not self.alive:
            draw_death(self.position)
            return

        draw_image(IMAGE_MONKEY, self.position)

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
        if walked and self.energy > 0:
            self.energy -= 1
        elif walked:
            self.alive = False

    def death(self, game_data):
        if not self.death_started:
            self.death_started = True
            self.death_timer = Timer(2)
            pygame.mixer.Sound.play(SOUND_PLAYER_DEATH)
            return

        if self.death_timer:
            return

        game_data.remove_entity(self)

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
            game_data.has_won = True

    def check_if_guard(self, game_data):
        for entity in game_data.entities:
            if entity.position == self.position and isinstance(entity, Guard):
                self.alive = False

    def eat_banana(self, game_data):

        if self.banana_count <= 0:
            return

        self.banana_count -= 1
        self.energy = PLAYER_MAX_ENERGY
        pygame.mixer.Sound.play(SOUND_PLAYER_EAT)

        bananas = game_data.get_banana_peels()
        for banana_peel in bananas:
            if banana_peel.position == self.position:
                return # TODO: put SUPER BANANA INSTEAD

        game_data.entities += [BananaPeel(self.position)]
    
    def play_slip_sound(self):

        if self.is_playing_slip_sound:
            return
        else:
            pygame.mixer.Sound.play(SOUND_PLAYER_SLIP)