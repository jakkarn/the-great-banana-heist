from game_loop import GameLoop

def run():
    game_loop = GameLoop()

    while game_loop.update():
        pass

if __name__ == "__main__":
    run()