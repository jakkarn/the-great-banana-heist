
from banana_peel import BananaPeel


class GameData():
    def __init__(self):
        self.events = []
        self.grid = None
        self.entities = []

    def add_entity(self, entity):
        self.entities += [entity]

    def get_banana_peels(self):
        return [banana_peel for banana_peel in self.entities if isinstance(banana_peel, BananaPeel)]

    def remove_entity(self, entity):
        self.entities.remove(entity)
        self.entities = [e for e in self.entities if e is entity]