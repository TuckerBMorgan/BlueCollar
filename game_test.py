# Simple pygame program


# Import and initialize the pygame library

import pygame




def load_tile_images():
    # Placeholder function to load images.
    # Return a dictionary mapping tile types to Pygame images.
    # Example: {"grass": pygame.image.load("grass_tile.png"), "water": pygame.image.load("water_tile.png")}
    tiles = {}
    tiles["ground"] = pygame.image.load("./assets/tile_0049.png")
    return tiles

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])


# Run until the user asks to quit

running = True

TILE_IMAGES = load_tile_images()
while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((255, 255, 255))

    tile_image = TILE_IMAGES.get("ground")
    if tile_image:
        # Draw a solid blue circle in the center
        screen.blit(tile_image, (0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()