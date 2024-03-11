import random
from position import Position
from entity import Entity
from board import Board
from action import ActionType, Action
from controller import ControllerType, Controller 
    
class Game:
    board: Board
    entities: list
    turn_order: list
    team_names: list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White", "Brown"]
    controllers: map
    
    def __init__(self, board: Board, entities: list):
        self.board = board
        self.entities = entities
        # loop over all entities, add them to the board, and give them a random turn order
        self.turn_order = []
        for entity in self.entities:
            self.board.add_entity(entity, entity.position)
            self.turn_order.append(entity)
        # shuffle the turn order
        random.shuffle(self.turn_order)
        
        self.controllers = {}
        self.controllers[0] = Controller(ControllerType.RANDOM)
        self.controllers[1] = Controller(ControllerType.MANUAL)
        
    def preform_turn(self):
        possible_actions = self.start_turn()
        self.update(possible_actions)
        self.end_turn()            
    
    def clear_board(self):
        self.board.clear_board()
    
    def place_characters(self):
        for entity in self.entities:
            self.board.add_entity(entity, entity.position)

    def start_turn(self):
        self.clear_board()
        self.place_characters()
        
        self.llm_friendly_world_state_print()
        # get the first entity in the turn order and calculate its valid moves
        entity = self.turn_order[0]
        valid_moves = entity.calculate_valid_moves(self)
        valid_attacks = entity.calculate_valid_attacks(self)
        valid_actions = valid_moves + valid_attacks
        return valid_actions

    def update(self, possible_actions: list):
        # pick a random action
        action = random.choice(possible_actions)
        if action.action_type == ActionType.MOVE:
            self.move_entity(self.turn_order[0], action.payload)
        if action.action_type == ActionType.ATTACK:
            target_name = action.payload[1]
            # get target from name
            target = None
            for entity in self.entities:
                if entity.name == target_name:
                    target = entity
            self.preform_attack(self.turn_order[0], target)

    def preform_attack(self, entity: Entity, target: Entity):
        target.health -= entity.damage
        if target.health <= 0:
            self.remove_entity(target)
    
    def end_turn(self):
        # take the first entity in the turn order and move it to the back
        self.turn_order.append(self.turn_order.pop(0))
    
    def get_entities(self, position: Position):
        return self.board.get_entities(position)
    
    def move_entity(self, entity: Entity, position: Position):
        self.board.move_entity(entity, position)
    
    def llm_friendly_world_state_print(self):
        current_entity = self.turn_order[0]
        current_entity.llm_friendly_print()
        print("My teammates are: (team " + str(current_entity.team) + ")" )
        for entity in self.entities:
            if entity.team == current_entity.team and entity != current_entity:
                print(entity.name)
        print("")
        print("My enemies are: (team " + str(current_entity.team) + ")" )
        for entity in self.entities:
            if entity.team != current_entity.team:
                print(entity.name)
        print("")                
        action_count = 0
        print("My valid moves are: ")
        for action in current_entity.calculate_valid_moves(self):
            print(action_count, ":", action)
            action_count += 1
        print("")
        print("My valid attacks are: ")
        for action in current_entity.calculate_valid_attacks(self):
            print(action_count, ":", str(action))
            action_count += 1
        print("")
        print("The board looks like: ")
        self.board.draw_board()
        print("")
        print("The turn order is: ")
        for entity in self.turn_order:
            print(entity.name)
        print("")
    
    def remove_entity(self, entity: Entity):
        self.board.remove_entity(entity)
    
    def add_entity(self, entity: Entity, position: Position):
        self.board.add_entity(entity, position)
    
    def clear_tile(self, position: Position):
        self.board.clear_tile(position)
    
    def clear_board(self):
        self.board.clear_board()

    def is_over(self):
        # loop over all entities
        # and if an entire time has 0 or less health
        # the other team wins
        team_health = {}
        for entity in self.entities:
            if entity.team not in team_health:
                team_health[entity.team] = 0
            team_health[entity.team] += entity.health
        for team in team_health:
            if team_health[team] <= 0:
                return True
        return False
            
            

