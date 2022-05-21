from game_loop import GameLoop
from player import Player

def run():
    game_loop = GameLoop()
    player = Player((5,5))

    game_loop.add_entity(player)

    while game_loop.update():
        pass

if __name__ == "__main__":
    run()