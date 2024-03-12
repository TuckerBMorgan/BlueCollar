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
    
    def draw_board_string(self):
        board_string = ""
        for x in range(self.x_size):
            for y in range(self.y_size):
                tile = self.get_tile(Position(x, y))
                if not tile.entities:
                    board_string += "- "
                else:
                    board_string += f"{tile.entities[0].display_character} "
            board_string += "\n"  # Move to the next line after each row is processed
        return board_string
                
