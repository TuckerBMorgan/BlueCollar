from dataclasses import dataclass

@dataclass
class ControllerType:
    RANDOM = "random"
    MANUAL = "manual"
    LLM = "llm"

class Controller:
    controller_type: ControllerType
    
    def __init__(self, controller_type: ControllerType):
        self.controller_type = controller_type