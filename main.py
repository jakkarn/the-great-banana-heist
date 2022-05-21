from game_loop import GameLoop
from grid2 import Array, convert_text_to_array_list
from player import Player

def run():

    map_design = "ddffd\nggffw\nggffw\nvv  w\nvvwww"
    tiles = convert_text_to_array_list(map_design)
    grid = Array(tiles)

    game_loop = GameLoop(grid)
    player = Player((1,1))
    game_loop.add_entity(player)

    while game_loop.update():
        pass

if __name__ == "__main__":
    run()