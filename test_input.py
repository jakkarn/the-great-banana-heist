import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 360

class Player:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
  
    def draw(self, screen):
        blue = (0, 0, 255)
        pygame.draw.circle(screen, blue, (self.x_pos, self.y_pos), 20)

# Set up the drawing window
def draw(screen, player):
    white = (255, 255, 255)
    
    screen.fill(white)
    
    player.draw(screen)
    # Flip the display
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    player = Player(0.5 * SCREEN_WIDTH, 0.5 * SCREEN_HEIGHT)
    
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
                    player.x_pos -= 1
                if event.key == K_RIGHT:
                    player.x_pos += 1
                if event.key == K_UP:
                    player.y_pos -= 1
                if event.key == K_DOWN:
                    player.y_pos += 1
                        
        # Draw level
        draw(screen, player)

    # Done! Time to quit.
    pygame.quit()
    
main()