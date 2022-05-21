from constants import IMAGE_BANANAPEEL
from draw_utils import draw_image
from entity import Entity

class BananaPeel(Entity):
    def __init__(self, position):
        super().__init__(position)

    def draw(self):
        image = IMAGE_BANANAPEEL
        draw_image(image, self.position)