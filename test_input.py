import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 360

def to_draw_coordinates(game_coordinates):
    TILE_SIZE = (32, 32)
    return (game_coordinates[0] * TILE_SIZE[0], game_coordinates[1] * TILE_SIZE[1])

class Entity:
    def __init__(self, position):
        self.position = position
  
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, to_draw_coordinates(self.position), 20)
    
    def move(self, movement):
        self.position = (self.position[0] + movement[0], self.position[1] + movement[1])

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)
  
    def draw(self, screen):
        blue = (0, 0, 255)
        super().draw(screen, blue)

class Banana_Peel(Entity):
    def __init__(self, position):
        super().__init__(position)
  
    def draw(self, screen):
        banana_color = (255, 255, 0)
        super().draw(screen, banana_color)

# Set up the drawing window
def draw(screen, player, banana_peels):
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    
    player.draw(screen)
    
    for peel in banana_peels:
        peel.draw(screen)
    
    # Flip the display
    pygame.display.flip()

def main():
    # Initialize game
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player((0, 0))
    banana_peels = []
    
    running = True
    while running:
        # Get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    player.move((-1, 0))
                if event.key == K_RIGHT:
                    player.move((1, 0))
                if event.key == K_UP:
                    player.move((0, -1))
                if event.key == K_DOWN:
                    player.move((0, 1))
                if event.key == K_SPACE:
                    banana_peels += [Banana_Peel(player.position)]
                        
        # Draw level
        draw(screen, player, banana_peels)

    # Done! Time to quit.
    pygame.quit()
    
main()