import pygame

TILE_SIZE = 64

BANANA_YELLOW = (255, 255, 0)
PLAYER_BLUE = (0, 0, 255)
MIDNIGHT_BLACK = (0, 0, 4)

SCREEN_BACKGROUND_COLOR = MIDNIGHT_BLACK

SYMBOL_DICT = {
    "#":"wall",
    "g":"grass",
    "d":"dirt",
    "~":"water",
    ".":"floor",
    " ":"space",
    "y":"bananapeel",
    "E":"exit",
    "$":"banana",
    "@":"player",
    "p":"powered",
    "u":"unpowered",
    "X":"lockedexit"
}
NON_WALKABLE = ["wall"]
WINNABLE = ["exit"]

IMAGE_MONKEY = pygame.image.load("textures/monkeysprite.png")
IMAGE_WALL = pygame.image.load("textures/redbrickwall.png")
IMAGE_GRASS = pygame.image.load("textures/vines-brickwalldarker.png")
IMAGE_WATER = pygame.image.load("textures/water.gif")
IMAGE_FLOOR = pygame.image.load("textures/stone.png")
IMAGE_BANANAPEEL = pygame.image.load("textures/peel.png")
IMAGE_BANANA = pygame.image.load("textures/banana.png")
IMAGE_EXIT = pygame.image.load("textures/red-brick-exit.png")
IMAGE_LOCKEDEXIT = pygame.image.load("textures/red-brick-locked.png")
IMAGE_UNLOCKEDEXIT = pygame.image.load("textures/red-brick-unlocked.png")

TILE_TEXTURE_MAP = {
    "wall":IMAGE_WALL,
    "floor":IMAGE_FLOOR,
    "grass":IMAGE_GRASS,
    "water":IMAGE_WATER,
    "space":IMAGE_FLOOR,
    "dirt":IMAGE_FLOOR,
    "exit":IMAGE_EXIT,
    "lockedexit":IMAGE_LOCKEDEXIT,
    "unlockedexit":IMAGE_UNLOCKEDEXIT,
}

PLAYER_MAX_ENERGY = 5
