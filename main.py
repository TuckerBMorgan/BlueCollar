import random
import pygame
from position import Position
from entity import Entity, EntityRecipe
from board import Board
from tile import Tile
from game import Game
from renderer import render

# Path: main.py

twnenty_entity_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Laura", "Mallory", "Nancy", "Oscar", "Peggy", "Quentin", "Romeo", "Sybil", "Trent", "Ursula", "Victor", "Walter", "Xander", "Yvonne", "Zelda"]

entities = []
for i in range(5):
    entity_recipe = EntityRecipe.default()
    entity_recipe.position = Position(i, i)
    entity_recipe.name = twnenty_entity_names[i]
    if i % 2 == 0:
        entity_recipe.team = 1
        
        entities.append(Entity(entity_recipe))
    else:    
        entities.append(Entity(entity_recipe))
    
tiles = []
for i in range(5):
    for j in range(5):
        tiles.append(Tile(Position(i, j)))
board = Board(tiles)
game = Game(board, entities)
print(game.llm_friendly_world_state_string())

pygame.init()
screen = pygame.display.set_mode((800, 600))

while game.is_over() == False:
    game.preform_turn()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    render(game, screen)
    pygame.time.wait(16)

while game.is_over() == False:
    game.preform_turn()


