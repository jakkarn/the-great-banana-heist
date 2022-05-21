class Entity:
    def __init__(self, position):
        self.position = position

    def move(self, movement):
        self.position = (self.position[0] + movement[0], self.position[1] + movement[1])