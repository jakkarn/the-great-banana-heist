import random
from banana import Banana
from banana_peel import BananaPeel
from constants import SYMBOL_DICT, TILE_TEXTURE_MAP
from grid import Array
from guard import Guard
from player import Player
from os.path import exists

from drawable import Drawable

def load_level(number):
    path = "levels/level" + str(number)

    guard_pattern_list = []
    guard_index = 0

    if not exists(path):
        return None, None

    rows = []
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] != "G":
                rows += [line.split()]
            else:
                guard_pattern_list += [list(eval(line[1:len(line)]))]

    player = None
    entities = []
    tiles = []

    for y, row in enumerate(rows):
        for x, col in enumerate(row):

            tiles.append([(x, y), SYMBOL_DICT[col[0]]])

            for i in range(1, len(col)):
                symbol = SYMBOL_DICT[col[i]]
                if symbol == "player":
                    player = Player((x,y))
                elif symbol == "bananapeel":
                    entities += [BananaPeel((x,y))]
                elif symbol == "banana":
                    entities += [Banana((x,y))]
                elif symbol == "guard":
                    entities += [Guard((x,y), guard_pattern_list[guard_index])]
                    guard_index += 1
                elif symbol == "vines":
                    image = TILE_TEXTURE_MAP[symbol]
                    entities += [Drawable(image, (x,y), random.choice([0, 90, -90, 180]))]
                elif symbol in TILE_TEXTURE_MAP:
                    image = TILE_TEXTURE_MAP[symbol]
                    entities += [Drawable(image, (x,y))]

    # add player first in update order
    if player:
        entities = [player] + entities

    grid = Array(tiles)

    return grid, entities


#def convert_text_to_array_list(text):
#    """prepare data for array"""
#    array_list = []
#    line_list = text.split("\n")
#    y_value = 1
#    for line in line_list:
#        for x_value in range(1,len(line) + 1):
#            array_list.append([(x_value, y_value), SYMBOL_DICT[line[x_value - 1]]])
#        y_value += 1
#    return array_list
