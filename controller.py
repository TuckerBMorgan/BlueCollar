from dataclasses import dataclass
import random

@dataclass
class ControllerType:
    RANDOM = "random"
    MANUAL = "manual"
    LLM = "llm"

class Controller:
    controller_type: ControllerType

    def __init__(self, controller_type: ControllerType):
        self.controller_type = controller_type

    def choose_actions(self, game, actions) -> int:
        if self.controller_type == ControllerType.RANDOM:
            return self.random_action(actions)
        if self.controller_type == ControllerType.MANUAL:
            return self.manual_action(actions)
        if self.controller_type == ControllerType.LLM:
            return self.llm_action(game, actions)

    def random_action(self, actions) -> int:
        number_of_choices = len(actions)
        return random.randint(0, number_of_choices - 1)

    def manual_action(self, actions) -> int:
        print("Choose an action:")
        for i in range(len(actions)):
            print(i, ":", actions[i])
        choice = int(input())
        return choice

    def llm_action(self, game, actions) -> int:
        # this is where the LLM will make a decision
        # for now, just choose the first action
        return 0
