from entity import Entity
from constants import IMAGE_GUARD
from draw_utils import draw_image
from timer import Timer

class Guard(Entity):
    """Guard is an Entity representing a guard"""
    def __init__(self, position, move_pattern:list):
        super().__init__(position)
        self.is_slipping = False
        self.last_direction = (0,0)
        self.move_pattern = move_pattern
        self.index_in_move_pattern = 0
        self.move_timer = Timer(0)

    def find_next_poition(self):
        """calculate the guards next pos based on its move_pattern, index and pos"""
        next_position = self.position
        if self.position == self.move_pattern[self.index_in_move_pattern]:
            index = (self.index_in_move_pattern + 1)%len(self.move_pattern)
            next_position = self.move_pattern[index]
            self.index_in_move_pattern = index
        else:
            vector_to_old_pos = (self.move_pattern[self.index_in_move_pattern][0] - self.position[0]\
                , self.move_pattern[self.index_in_move_pattern][1] - self.position[1])
            if vector_to_old_pos[0] > 0:
                next_position = (self.position[0] + 1, self.position[1])
            elif vector_to_old_pos[0] < 0:
                next_position = (self.position[0] - 1, self.position[1])
            elif vector_to_old_pos[1] > 0:
                next_position = (self.position[0], self.position[1] + 1)
            elif vector_to_old_pos[1] < 0:
                next_position = (self.position[0], self.position[1] - 1)
            else:
                print(f"Error in Guard.find_next_pos(): pos == {vector_to_old_pos}")
        return next_position

    def find_movement(self):
        """calculate the guards movement"""
        new_pos = self.find_next_poition()
        x_vec = new_pos[0] - self.position[0]
        y_vec = new_pos[1] - self.position[1]
        print((x_vec, y_vec))
        return (x_vec, y_vec)

    def draw(self):
        """draw the guard"""
        draw_image(IMAGE_GUARD, self.position)

    def update(self, game_data):
        super().update(game_data)

        walked = False

        if not self.move_timer:
            walked = self.walk(self.find_movement(),game_data)
        #self.walk(self.find_movement(),game_data)

        if walked:
            self.move_timer = 0.5