import pygame

TILE_SIZE = 32

BANANA_YELLOW = (255, 255, 0)
PLAYER_BLUE = (0, 0, 255)
MIDNIGHT_BLACK = (0, 0, 4)


SCREEN_BACKGROUND_COLOR = MIDNIGHT_BLACK

SYMBOL_DICT = {"w":"wall", "g":"grass", "d":"dirt", "v":"water", "f":"floor", " ":"space"}
NON_WALKABLE = ["wall"]

IMAGE_MONKEY = pygame.image.load("textures/monkeysprite.png")
IMAGE_WALL = pygame.image.load("textures/redbrickwall.png")
IMAGE_FLOOR = pygame.image.load("textures/stone.png")
IMAGE_BANANAPEEL = pygame.image.load("textures/peel.png")
IMAGE_BANANA = pygame.image.load("textures/banana.png")

TILE_TEXTURE_MAP = {
    "wall":IMAGE_WALL,
    "floor":IMAGE_FLOOR,
    "grass":IMAGE_FLOOR,
    "water":IMAGE_FLOOR,
    "space":IMAGE_FLOOR,
    "dirt":IMAGE_FLOOR,
}