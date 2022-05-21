
class GameData():
    def __init__(self):
        self.events = []
        self.grid = None
        self.entities = []

    def add_entity(self, entity):
        self.entities += [entity]