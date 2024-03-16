import json

input_file = "raw_data.json"
output_file = "data.json"

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

examples = [{"instruction": intstructions_string, "input": key, "output": value} for entry in data["data"] for key, value in entry.items()]

with open(output_file, 'w') as train_file:
    for example in examples:
        train_file.write(json.dumps(example) + '\n')