from constants import IMAGE_BANANA
from draw_utils import draw_image
from entity import Entity

class Banana(Entity):

    def __init__(self, position):
        super().__init__(position)

    def draw(self):
        draw_image(IMAGE_BANANA, self.position)