

#from turtle import position


class Entity:
    def __init__(self, position):
        self.position = position
        self.is_slipping = False
        self.last_direction = (0,0)

    def update(self, game_data):

        if self.last_direction == (0,0):
            self.is_slipping = False

        if self.is_slipping:
            self.move(self.last_direction, game_data)

    def walk(self, direction, game_data):
        if self.is_slipping:
            return

        self.move(direction, game_data)

    def move(self, movement, game_data):
        grid = game_data.grid

        new_position = (self.position[0] + movement[0], self.position[1] + movement[1])

        if not grid.is_walkable(new_position):
            self.last_direction = (0,0)
            return

        self.last_direction = (new_position[0] - self.position[0], new_position[1] - self.position[1])
        self.position = new_position

        for banana_peel in game_data.get_banana_peels():
            if banana_peel.position == self.position:
                print("SLIP!")
                self.is_slipping = True
                game_data.remove_entity(banana_peel)
