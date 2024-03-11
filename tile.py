from position import Position
from entity import Entity

class Tile:
    position: Position
    entities: list

    def __init__(self, position: Position, entities: list):
        self.position = position
        self.entities = entities
        self.tile_type = "ground"
    
    def add_entity(self, entity: Entity):
        self.entities.append(entity)
    
    def clear_entities(self):
        self.entities = []