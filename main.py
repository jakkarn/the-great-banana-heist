from game_loop import GameLoop
from grid2 import Array, convert_text_to_array_list
from player import Player

def run():

    map_design = "wwwwwwwwwwfw\nwffffffffffw\nwffffffffffw\nwffffffffffw\nwffwwwwwwwww\nwffffffffffw\nwffffffffffw\nwvvvvvwwwffw\nwvvvvvwwwffw\nwffffffffffw\nwffffffffffw\nwwwwwwwwwwww"
    tiles = convert_text_to_array_list(map_design)
    grid = Array(tiles)

    game_loop = GameLoop(grid)
    player = Player((2,2))
    game_loop.add_entity(player)

    while game_loop.update():
        pass

if __name__ == "__main__":
    run()