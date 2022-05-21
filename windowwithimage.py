import sys, pygame
pygame.init()

size = width, height = 800, 600
monkey = pygame.image.load("monkeysprite.png")
black = 0, 0, 0
monkeysize = monkey.get_rect()

screen = pygame.display.set_mode(size)
speed = [0, 0]

from pygame.locals import *

while 1:
    screen.fill(black)
    screen.blit(monkey, monkeysize)
    pygame.display.flip()
