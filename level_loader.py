from banana import Banana
from banana_peel import BananaPeel
from constants import SYMBOL_DICT
from grid2 import Array
from player import Player


def load_level(filename):
    path = "levels/" + filename

    rows = []
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            rows += [line.split()]

    player = None
    entities = []
    tiles = []

    #   . .g
    for y, row in enumerate(rows):
        for x, col in enumerate(row):

            tiles.append([(x, y), SYMBOL_DICT[col[0]]])

            if len(col) == 2:
                if SYMBOL_DICT[col[1]] == "player":
                    player = Player((x,y))
                if SYMBOL_DICT[col[1]] == "bananapeel":
                    entities += [BananaPeel((x,y))]
                if SYMBOL_DICT[col[1]] == "banana":
                    entities += [Banana((x,y))]

    # add player first in update order
    if player:
        entities = [player] + entities

    print(entities)

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