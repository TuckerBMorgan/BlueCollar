import pandas as pd
import json

input_file = "data.json"
output_file = "data.csv"

with open(input_file, 'r') as file:
    data = json.load(file)

examples = [{"example": f"{entry['input']}\n{entry['output']}"} for entry in data["data"]]

df = pd.DataFrame(examples)

df.to_csv(output_file, index=False)