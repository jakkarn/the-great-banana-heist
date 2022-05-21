import pygame
from constants import TILE_SIZE, TILE_TEXTURE_MAP
from view_port import SCREEN

def to_draw_coordinates(position):
    return (position[0] * TILE_SIZE, position[1] * TILE_SIZE)

def draw_circle(color, position, radius):
    pygame.draw.circle(SCREEN, color, to_draw_coordinates(position), radius)

def draw_tile(pos, tile_type):
    image = TILE_TEXTURE_MAP[tile_type]
    draw_pos = (pos[0], pos[1])
    draw_image(image, draw_pos)

def draw_image(image, pos):
    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    SCREEN.blit(image, (pos[0]*TILE_SIZE, pos[1]*TILE_SIZE))