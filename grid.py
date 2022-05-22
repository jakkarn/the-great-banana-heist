
import sys

class Array(object):
    """Array is the map"""

    def __init__(self, tile_list:list):
        # tile_list == [[coordinate, static_object, variable_object] ... ]
        self.tile_inst_dict = {}
        for tile in tile_list:
            if len(tile) == 3:
                self.tile_inst_dict[tile[0]] = Tile(tile[1], tile[2])
            else:
                self.tile_inst_dict[tile[0]] = Tile(tile[1])

class Tile(object):
    """Tile is a tile on the map"""

    def __init__(self, static_obj, variable_obj = None) -> None:
        self.static_obj = static_obj
        #self.variable_obj = variable_obj

    def change_variable_obj(self, new_variable_obj):
        self.variable_obj = new_variable_obj

    def remove_variable_obj(self):
        self.variable_obj = None

def convert_file_to_array_list(file, symbol_dict):
    """prepare data for array"""
    opened_file = file.open()
    line_list = opened_file.readlines()
    array_list = []
    y_value = 1
    for line in line_list:
        for x_value in range(len(line) - 1):
            array_list.append([(x_value,y_value), symbol_dict[line[x_value - 1]]])
    return array_list

def convert_text_to_array_list(text, symbol_dict):
    """prepare data for array"""
    array_list = []
    line_list = text.split("\n")
    y_value = 1
    for line in line_list:
        for x_value in range(1,len(line) + 1):
            array_list.append([(x_value, y_value), symbol_dict[line[x_value - 1]]])
        y_value += 1
    return array_list

def print_array(array_inst:Array, x_range:int, y_range:int):
    """print all static object of an array"""
    for y_value in range(1,y_range + 1):
        row = ""
        for x_value in range(1,x_range + 1):
            row += array_inst.tile_inst_dict[(x_value, y_value)].static_obj + " "
        print(row)

def create_map_interactive():
    """allows user to write a map_string in the terminal"""
    map_str = ""
    inp = input("Str>>")
    while inp != "q":
        map_str += inp + "\n"
        inp = input("Str>>")
    map_str = map_str[0: len(map_str) - 1]
    print(map_str)


if __name__ == "__main__":
    """some test-functions"""
    array_list = [[(1,1), "wall"], [(2,1), "wall"], [(3,1), "wall"], [(4,1), "wall"], [(1,2), "dirt"], [(2,2), "grass"]\
        , [(3,2), "grass"], [(4,2), "wall"], [(1,3), "dirt"], [(2,3), "grass"], [(3,3), "water"], [(4,3), "wall"]\
            , [(1,4), "dirt"], [(2,4), "grass"], [(3,4), "grass"], [(4,4), "wall"]]
    text = "wwww\ndggw\ndgvw\ndggw"
    symbol_dict = {"w":"wall", "g":"grass", "d":"dirt", "v":"water", "f":"floor", " ":"space"}
    text2 = "ddffd\nggffw\nggffw\nvv  w\nvvwww" 

    test_text1 = "wwwwwwfwww\nwffffffffw\nwfwwfffvfw\nwffffwwffw\nwffwfwfffw\nwffwfwfvfw\nwfvffffffw\nwfvfwwwffw\nwffffffffw\nwwwwwwwwww"
    lvl1 = "wwwwwwwwwwfw\nwffffffffffw\nwffffffffffw\nwffffffffffw\nwffwwwwwwwww\nwffffffffffw\nwffffffffffw\nwvvvvvwwwffw\nwvvvvvwwwffw\nwffffffffffw\nwffffffffffw\nwwwwwwwwwwww"


    array_info = convert_text_to_array_list(text, symbol_dict)
    array = Array(array_info)
    array_info2 = convert_text_to_array_list(text2, symbol_dict)
    array2 = Array(array_info2)
    array_info3 = convert_text_to_array_list(test_text1, symbol_dict)
    array3 = Array(array_info3)
    #print(array_info3)
    #print_array(array3, 10, 10)
    array_info4 = convert_text_to_array_list(lvl1, symbol_dict)
    array4 = Array(array_info4)
    print_array(array4, 12, 12)
    #create_map_interactive()

