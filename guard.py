from entity import Entity

class Guard(Entity):
    def __init__(self, position, move_pattern:list):
        super().__init__(position)
        self.is_slipping = False
        self.last_direction = (0,0)
        self.move_pattern = move_pattern
        self.index_in_move_pattern = 0

    def find_next_poition(self):
        if self.position == self.move_pattern[self.index_in_move_pattern]:
            index = (self.index_in_move_pattern + 1)%len(self.move_pattern)
            next_position = self.move_pattern[index]
        else:
            vector_to_old_pos = (self.move_pattern[self.index_in_move_pattern][0] - self.position[0]\
                , self.move_pattern[self.index_in_move_pattern][1] - self.position[1])
            if vector_to_old_pos[0] > 0:
                next_position = (self.position[0] + 1, self.position[1])
            elif vector_to_old_pos < 0:
                next_position = (self.position[0] - 1, self.position[1])
            elif vector_to_old_pos[1] > 0:
                next_position = (self.position[0], self.position[1] + 1)
            elif vector_to_old_pos[1] > 0:
                next_position = (self.position[0], self.position[1] - 1)
            else:
                print("Error in Guard.find_next_pos()")
        return next_position

    def move(self, game_data):
        grid = game_data.grid

        new_position = self.find_next_pos()

        self.last_direction = (new_position[0] - self.position[0], new_position[1] - self.position[1])
        self.position = new_position

        for banana_peel in game_data.get_banana_peels():
            if banana_peel.position == self.position:
                print("SLIP!")
                self.is_slipping = True
                game_data.remove_entity(banana_peel)
