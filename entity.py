class Entity:
    def __init__(self, position):
        self.position = position
        self.is_slipping = False
        self.last_direction = (0,0)
        self.alive = True

    def update(self, game_data):

        if not self.alive:
            return

        if self.last_direction == (0,0):
            self.is_slipping = False

        if self.is_slipping:
            self.move(self.last_direction, game_data)

        grid = game_data.grid
        if grid.is_deadly(self.position):
            self.alive = False

    def walk(self, direction, game_data):
        if self.is_slipping:
            return False

        return self.move(direction, game_data)

    def move(self, movement, game_data):
        grid = game_data.grid

        new_position = (self.position[0] + movement[0], self.position[1] + movement[1])

        if not grid.is_walkable(new_position, self.position):
            self.last_direction = (0,0)
            return False

        self.last_direction = (new_position[0] - self.position[0], new_position[1] - self.position[1])
        self.position = new_position

        banana_peels_to_remove = []
        for banana_peel in game_data.get_banana_peels():
            if banana_peel.position == self.position:
                self.is_slipping = True
                banana_peels_to_remove += [banana_peel]

        for banana_peel in banana_peels_to_remove:
            game_data.remove_entity(banana_peel)

        return True
