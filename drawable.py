from constants import IMAGE_VINES
from draw_utils import draw_image


class Drawable():
    def __init__(self, image, pos, angle=0):
        self.position = pos
        self.image = image
        self.angle = angle
    
    def draw(self):
        draw_image(self.image, self.position, self.angle)