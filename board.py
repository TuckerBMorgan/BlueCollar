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

    def get_entity(self, position: Position):
        tile = self.get_tile(position)
        return tile.get_entity()
    
    def move_entity(self, entity: Entity, position: Position):
        tile = self.get_tile(entity.position)
        tile.remove_entity()
        tile = self.get_tile(position)
        tile.set_entity(entity)
        entity.position = position
    
    def remove_entity(self, entity: Entity):
        tile = self.get_tile(entity.position)
        tile.remove_entity()
    
    def set_entity(self, entity: Entity, position: Position):
        tile = self.get_tile(position)
        tile.set_entity(entity)
        entity.position = position
    
    def clear_tile(self, position: Position):
        tile = self.get_tile(position)
        tile.remove_entity()
    
    def clear_board(self):
        for tile in self.tiles:
            tile.remove_entity()
    
    def draw_board_string(self):
        board_string = ""
        for x in range(self.x_size):
            for y in range(self.y_size):
                tile = self.get_tile(Position(x, y))
                if not tile.entity:
                    board_string += "- "
                else:
                    board_string += f"{tile.entity.display_character} "
            board_string += "\n"  # Move to the next line after each row is processed
        return board_string
                
