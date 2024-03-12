from position import Position
from entity import Entity

class Tile:
    position: Position
    entity: Entity

    def __init__(self, position: Position):
        self.position = position
        self.entity = None
        self.tile_type = "ground"
    
    def set_entity(self, entity: Entity):
        self.entity = entity
    
    def remove_entity(self):
        self.entity = None
    
    def get_entity(self):
        return self.entity