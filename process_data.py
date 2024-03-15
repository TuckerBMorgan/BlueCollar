import json
from sklearn.model_selection import train_test_split

input_file = "data.json"
train_output_file = "train.json"
test_output_file = "test.json"

with open(input_file, 'r') as file:
    data = json.load(file)

intstructions_string = f"""You are a player in a simplified game of Dungeons and Dragons (D&D).
It is your turn to act. You can choose to move to one of the valid move positions, or execute one of the valid attacks.
All characters can move 1 tile per turn, and have an attack range of 1 tile.
The top left of the board has coordinates (0, 0).

First, provide thoughtful reflection on the best strategy to win the game from this point. Then, provide your decision using the index of the action.

Here is an example of the expected output format.
Reasoning: I will prioritize attacking enemies with lower health to take them out quickly and reduce the overall damage I and my teammates receive. Therefore, attacking Eve at (2, 3) is a good decision.
Action: 4

Now make your decision based on the following state of the game."""
examples = [f"<s> [INST]\n{intstructions_string}\n\n{key}\n[/INST]\n\n{value} </s>" for entry in data["data"] for key, value in entry.items()]

train_examples, test_examples = train_test_split(examples, test_size=0.1, random_state=42)

with open(train_output_file, 'w') as train_file:
    for example in train_examples:
        train_file.write(json.dumps({"example": example}) + '\n')
with open(test_output_file, 'w') as test_file:
    for example in test_examples:
        test_file.write(json.dumps({"example": example}) + '\n')