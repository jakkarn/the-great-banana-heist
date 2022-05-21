
import sys

class Array(object):

    def __init__(self, tile_list:list):
        # tile_list == [coordinate, static_object, variable_object]
        self.tile_inst_dict = {}
        for tile in tile_list:
            if len(tile) == 3:
                self.tile_inst_dict[tile[0]] = Tile(tile[1], tile[2])
            else:
                self.tile_inst_dict[tile[0]] = Tile(tile[1])

class Tile(object):

    def __init__(self, static_obj, variable_obj = None) -> None:
        self.static_obj = static_obj
        self.variable_obj = variable_obj

    def change_variable_obj(self, new_variable_obj):
        self.variable_obj = new_variable_obj

    def remove_variable_obj(self):
        self.variable_obj = None


array_list = [["1,1", "wall"], ["2,1", "wall"], ["3,1", "wall"], ["4,1", "wall"], ["1,2", "dirt"], ["2,2", "grass"]\
    , ["3,2", "grass"], ["4,2", "wall"], ["1,3", "dirt"], ["2,3", "grass"], ["3,3", "water"], ["4,3", "wall"]\
        , ["1,4", "dirt"], ["2,4", "grass"], ["3,4", "grass"], ["4,4", "wall"]]

#array = Array(array_list)
#print(array.tile_inst_dict["2,4"].static_obj)
#print(array.tile_inst_dict)

symbol_dict = {"w":"wall", "g":"grass", "d":"dirt", "v":"water"}

def convert_file_to_array_list(file, symbol_dict):
    opened_file = file.open()
    line_list = opened_file.readlines()
    array_list = []
    y_value = 1
    for line in line_list:
        for x_value in range(len(line) - 1):
            array_list.append([f"{str(x_value)},{str(y_value)}", symbol_dict[line[x_value - 1]]])
    return array_list

def convert_text_to_array_list(text, symbol_dict):
    array_list = []
    y_value = 1
    for line in line_list:
        for x_value in range(len(line) - 1):
            array_list.append([f"{str(x_value)},{str(y_value)}", symbol_dict[line[x_value - 1]]])
    return array_list


print(convert_file_to_array_list(sys.argv[1], symbol_dict))