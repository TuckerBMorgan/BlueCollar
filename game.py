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
            self.board.set_entity(entity, entity.position)
            self.turn_order.append(entity)
        # shuffle the turn order
        random.shuffle(self.turn_order)
        
        self.controllers = {}
        self.controllers[0] = Controller(ControllerType.RANDOM)
        self.controllers[1] = Controller(ControllerType.MANUAL)
        
    def preform_turn(self):
        possible_actions = self.start_turn()
        
        # use the controller associated with the team to pick the action
        controller = self.controllers[self.turn_order[0].team]
        action_index = controller.choose_actions(self, possible_actions)
        chosen_action = possible_actions[action_index]
        self.update(chosen_action)
        self.end_turn()            
    
    def clear_board(self):
        self.board.clear_board()
    
    def place_characters(self):
        for entity in self.entities:
            self.board.add_entity(entity, entity.position)

    def start_turn(self):
        self.clear_board()
        self.place_characters()
        
        print(self.llm_friendly_world_state_string())
        # get the first entity in the turn order and calculate its valid moves
        entity = self.turn_order[0]
        valid_moves = entity.calculate_valid_moves(self)
        valid_attacks = entity.calculate_valid_attacks(self)
        valid_actions = valid_moves + valid_attacks
        return valid_actions

    
    def update(self, chosen_action):
        # pick a random action
        if chosen_action.action_type == ActionType.MOVE:
            self.move_entity(self.turn_order[0], chosen_action.payload)
        if chosen_action.action_type == ActionType.ATTACK:
            target_name = chosen_action.payload[1]
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
    
    def llm_friendly_world_state_string(self):
        output = ""
        current_entity = self.turn_order[0]
        output += current_entity.llm_friendly_string() + "\n"
        output += "My teammates are: (team " + str(current_entity.team) + ")\n"
        for entity in self.entities:
            if entity.team == current_entity.team and entity != current_entity:
                output += entity.name + "\n"
        output += "\nMy enemies are: (team " + str((current_entity.team + 1) % 2) + ")\n"
        for entity in self.entities:
            if entity.team != current_entity.team:
                output += entity.name + "\n"
        output += "\nMy valid moves are:\n"
        action_count = 0
        for action in current_entity.calculate_valid_moves(self):
            output += str(action_count) + ": " + str(action) + "\n"
            action_count += 1
        output += "\nMy valid attacks are:\n"
        for action in current_entity.calculate_valid_attacks(self):
            output += str(action_count) + ": " + str(action) + "\n"
            action_count += 1
        output += "\nThe board looks like:\n"
        output += self.board.draw_board_string() + "\n"
        output += "The turn order is:\n"
        for entity in self.turn_order:
            output += entity.name + "\n"
        return output
    
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
            
            

