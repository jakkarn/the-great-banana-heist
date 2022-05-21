import pygame
from constants import TILE_SIZE
from view_port import SCREEN

def to_draw_coordinates(position):
    return (position[0] * TILE_SIZE, position[1] * TILE_SIZE)

def draw_circle(color, position, radius):
    pygame.draw.circle(SCREEN, color, to_draw_coordinates(position), radius)