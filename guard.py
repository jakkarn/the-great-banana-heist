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
            self.index_in_move_pattern = index
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

    def find_movement(self):
        new_pos = self.find_next_poition()
        x_vec = new_pos[0] - self.position[0]
        y_vec = new_pos[1] - self.position[1]

