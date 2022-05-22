from banana import Banana
from banana_peel import BananaPeel
from constants import SYMBOL_DICT
from grid import Array
from guard import Guard
from player import Player


def load_level(number):
    path = "levels/level" + str(number)

    guard_pattern_list = []
    guard_index = 0

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

            if len(col) == 2:
                if SYMBOL_DICT[col[1]] == "player":
                    player = Player((x,y))
                if SYMBOL_DICT[col[1]] == "bananapeel":
                    entities += [BananaPeel((x,y))]
                if SYMBOL_DICT[col[1]] == "banana":
                    entities += [Banana((x,y))]
                if SYMBOL_DICT[col[1]] == "guard":
                    entities += [Guard((x,y), guard_pattern_list[guard_index])]
                    guard_index += 1

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
