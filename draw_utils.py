import pygame
from constants import TILE_SIZE, TILE_TEXTURE_MAP
from view_port import SCREEN

def to_draw_coordinates(position):
    return (position[0] * TILE_SIZE, position[1] * TILE_SIZE)

def draw_circle(color, position, radius):
    pygame.draw.circle(SCREEN, color, to_draw_coordinates(position), radius)

def draw_tile(pos, tile_type):
    image = TILE_TEXTURE_MAP[tile_type]

    draw_pos = (pos[0]-1, pos[1]-1)
    draw_pos = (draw_pos[0] * TILE_SIZE, draw_pos[1] * TILE_SIZE)

    image_rect = image.get_rect()
    #image_rect.x = pos[0] * TILE_SIZE
    #image_rect.y = pos[1] * TILE_SIZE
    image_rect.size = (TILE_SIZE, TILE_SIZE)


    SCREEN.blit(image, draw_pos)

def draw_image(image, pos):
    SCREEN.blit(image, pos[0])