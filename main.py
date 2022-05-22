from game_loop import GameLoop
from level_loader import load_level

def run():

    #map_design = "wwwwwwwwwwfw\nwffffffffffw\nwffffffffffw\nwffffffffffw\nwffwwwwwwwww\nwffffffffffw\nwffffffffffw\nwvvvvvwwwffw\nwvvvvvwwwffw\nwffffffffffw\nwffffffffffw\nwwwwwwwwwwww"
    grid, entities = load_level("level1")
    game_loop = GameLoop(grid)

    for entity in entities:
        game_loop.add_entity(entity)

    while game_loop.update():
        pass

if __name__ == "__main__":
    run()