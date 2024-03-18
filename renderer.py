import pygame

scale_factor = 4.0
tile_size = 16
total = tile_size * scale_factor

def load_tile_images():
    # Placeholder function to load images.
    # Return a dictionary mapping tile types to Pygame images.
    # Example: {"grass": pygame.image.load("grass_tile.png"), "water": pygame.image.load("water_tile.png")}
    tiles = {}
    tiles["ground"] = pygame.image.load("./assets/tile_0049.png")
    tiles["Alice"] = pygame.image.load("./assets/tile_0084.png")
    
    tiles["Bob"] = pygame.image.load("./assets/tile_0086.png")
    
    tiles["Charlie"] = pygame.image.load("./assets/tile_0086.png")
    
    tiles["David"] = pygame.image.load("./assets/tile_0087.png")
    
    tiles["Eve"] = pygame.image.load("./assets/tile_0088.png")
    return tiles

# Global dictionary of tile images
TILE_IMAGES = load_tile_images()

def render_tile(screen, tile):
    """
    Render a single tile on the screen based on its type and position.
    
    :param screen: Pygame screen to render the tile on.
    :param tile: Tile object with 'position' and 'tile_type' attributes.
    """

    tile_image = TILE_IMAGES.get(tile.tile_type)
    if tile_image:
        position = ( tile.position.x * total, tile.position.y * total)
        screen.blit(pygame.transform.scale(tile_image, (total, total)), position)

def render_tiles(screen, game_state):
    """
    Loop over the 'tiles' field of the game state and render each tile.
    
    :param screen: Pygame screen to render the tiles on.
    :param game_state: The game state object or dictionary with a 'tiles' field.
    """
    for tile in game_state.tiles:
        render_tile(screen, tile)

def render_entities(screen, game_state):
    """
    Loop over the 'entities' field of the game state and render each entity.
    
    :param screen: Pygame screen to render the entities on.
    :param game_state: The game state object or dictionary with an 'entities' field.
    """
    for entity in game_state.entities:
        if entity.name in TILE_IMAGES:
            entity_image = TILE_IMAGES[entity.name]
            position = (entity.position.x * total, entity.position.y * total)
            screen.blit(pygame.transform.scale(entity_image, (total * 0.75, total * 0.75)), position)


def render(game_state, screen):
    screen.fill((0, 0, 0))  # Fill the screen with black (or any background)
    render_tiles(screen, game_state.board)  # Render the tiles
    render_entities(screen, game_state)  # Render the entities
    pygame.display.flip()
