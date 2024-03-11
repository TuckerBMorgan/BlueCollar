from position import Position
from entity import Entity


class Board:
    tiles: list
    x_size: int
    y_size: int
    
    def __init__(self, tiles: list, x_size: int = 5, y_size: int = 5):
        self.tiles = tiles
        self.x_size = x_size
        self.y_size = y_size
    
    def get_tile(self, position: Position):
        for tile in self.tiles:
            if tile.position.x == position.x and tile.position.y == position.y:
                return tile
        print(f"Tile not found at position {position}")
        return None

    def get_entities(self, position: Position):
        tile = self.get_tile(position)
        return tile.entities
    
    def move_entity(self, entity: Entity, position: Position):
        tile = self.get_tile(entity.position)
        tile.entities.remove(entity)
        tile = self.get_tile(position)
        tile.add_entity(entity)
        entity.position = position
    
    def remove_entity(self, entity: Entity):
        tile = self.get_tile(entity.position)
        tile.entities.remove(entity)
    
    def add_entity(self, entity: Entity, position: Position):
        tile = self.get_tile(position)
        tile.add_entity(entity)
        entity.position = position
    
    def clear_tile(self, position: Position):
        tile = self.get_tile(position)
        tile.clear_entities()
    
    def clear_board(self):
        for tile in self.tiles:
            tile.clear_entities()
    
    def draw_board(self):
        for x in range(self.x_size):
            for y in range(self.y_size):
                tile = self.get_tile(Position(x, y))
                if tile.entities == []:
                    print(f"-", end=" ")
                else:
                    print(f"{tile.entities[0].display_character}" , end=" ")
            print()
                
