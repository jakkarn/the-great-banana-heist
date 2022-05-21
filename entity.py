class Entity:
    def __init__(self, position):
        self.position = position

    def move(self, movement, game_data):
        grid = game_data.grid

        new_position = (self.position[0] + movement[0], self.position[1] + movement[1])

        if not grid.is_walkable(new_position):
            return

        self.position = new_position