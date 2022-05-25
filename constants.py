import pygame

TILE_SIZE = 64

BANANA_YELLOW = (255, 255, 0)
PLAYER_BLUE = (0, 0, 255)
MIDNIGHT_BLACK = (0, 0, 4)

SCREEN_BACKGROUND_COLOR = MIDNIGHT_BLACK

SYMBOL_DICT = {
    "?":"void",
    "#":"wall",
    "|":"wall-decal",
    "-":"wall-decal-2",
    "g":"grass",
    "d":"dirt",
    "~":"water",
    ".":"floor",
    " ":"space",
    "=":"trottoar",
    "y":"bananapeel",
    "E":"exit",
    "$":"banana",
    "@":"player",
    "p":"powerline_on",
    "u":"powerline_off",
    "G":"guard",
    "X":"lockedexit",
    "B":"blender",
    "z":"vines",
}
NON_WALKABLE = ["wall", "lockedexit", "blender", "trottoar", "void"]
DEADLY = ["water"]
WINNABLE = ["exit", "unlockedexit"]

IMAGE_MONKEY = pygame.image.load("textures/monkeysprite.png")
IMAGE_WALL = pygame.image.load("textures/redbrickwall.png")
IMAGE_WALL_DECAL = pygame.image.load("textures/red-dark-blendx-brickwall.png")
IMAGE_WALL_DECAL_2 = pygame.image.load("textures/red-dark-blendy-brickwall.png")
IMAGE_GRASS = pygame.image.load("textures/vines-brickwalldarker.png")
IMAGE_WATER = pygame.image.load("textures/water.gif")
IMAGE_FLOOR = pygame.image.load("textures/stone.png")
IMAGE_BANANAPEEL = pygame.image.load("textures/peel.png")
IMAGE_BANANA = pygame.image.load("textures/banana.png")
IMAGE_EXIT = pygame.image.load("textures/red-brick-exit.png")
IMAGE_LOCKEDEXIT = pygame.image.load("textures/red-brick-locked.png")
IMAGE_UNLOCKEDEXIT = pygame.image.load("textures/red-brick-unlocked.png")
IMAGE_BLENDER = pygame.image.load("textures/blender_inactive.png")
IMAGE_BLENDER_ACTIVE = pygame.image.load("textures/blender_active.png")
IMAGE_GUARD = pygame.image.load("textures/guardsprite.png")
IMAGE_POWERLINEOFF = pygame.image.load("textures/powerline_off.png")
IMAGE_POWELINEON = pygame.image.load("textures/powerline_on.png")
IMAGE_BANANAPEEL_RED = pygame.image.load("textures/red_peel.png")
IMAGE_TROTTOAR = pygame.image.load("textures/dark-blendy-brickwall.png")
IMAGE_VINES = pygame.image.load("textures/vines.png")

TILE_TEXTURE_MAP = {
    "wall":IMAGE_WALL,
    "wall-decal":IMAGE_WALL_DECAL,
    "wall-decal-2":IMAGE_WALL_DECAL_2,
    "floor":IMAGE_FLOOR,
    "grass":IMAGE_GRASS,
    "water":IMAGE_WATER,
    "space":IMAGE_FLOOR,
    "dirt":IMAGE_FLOOR,
    "exit":IMAGE_EXIT,
    "banana":IMAGE_BANANA,
    "lockedexit":IMAGE_LOCKEDEXIT,
    "unlockedexit":IMAGE_UNLOCKEDEXIT,
    "powerline_on":IMAGE_POWELINEON,
    "powerline_off":IMAGE_POWELINEON,
    "blender":IMAGE_BLENDER,
    "trottoar":IMAGE_TROTTOAR,
    "vines":IMAGE_VINES,
}

PLAYER_MAX_ENERGY = 5
PLAYER_START_BANANA_COUNT = 30
START_LEVEL = 9
