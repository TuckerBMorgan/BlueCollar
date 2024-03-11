
# I want to have something like an enum for the action type
# This is the action.py file
from dataclasses import dataclass

@dataclass
class ActionType:
    MOVE = "move"
    ATTACK = "attack"
    DEFEND = "defend"
    WAIT = "wait"

class Action:
    action_type: ActionType
    payload: any
    
    def __init__(self, action_type: ActionType, payload: any):
        self.action_type = action_type
        self.payload = payload

    def __str__(self) -> str:
        if self.action_type == ActionType.MOVE:
            return "I can move to " + str(self.payload)
        elif self.action_type == ActionType.ATTACK:
            total_str = "I can Attack "
            total_str += str(self.payload[1])
            total_str += " at " + str(self.payload[0])
            return total_str

