from unsloth import FastLanguageModel

max_seq_length = 2048
dtype = None
load_in_4bit = True

prompt_template = """### Input:
{}

### Response:
{}"""

test_input = """I am Charlie represented by the letter C
I have 8 health
I can do 2 damage per turn
I can move 1 tile per turn
My attack range is 1 tile
I am at position (3, 3)

My teammates are:
Charlie (health: 3, damage: 3)
Eve (health: 4, damage: 1)
Grace (health: 1, damage: 2)
Heidi (health: 6, damage: 3)

My enemies are:
Alice (health: 3, damage: 3)
Bob (health: 5, damage: 3)
David (health: 1, damage: 1)
Frank (health: 5, damage: 1)
Ivan (health: 7, damage: 1)

My valid moves are:
0 : I can move to (2, 2)
1 : I can move to (2, 3)
2 : I can move to (2, 4)
3 : I can move to (3, 2)
4 : I can move to (3, 3)
5 : I can move to (4, 2)
6 : I can move to (4, 3)

My valid attacks are:
7 : I can attack David at (4, 4)

The board looks like:
----I-
-F----
H----A
B--C--
-E-GD-
------

The turn order is:
Charlie
Ivan
Eve
Grace
Bob
Frank
Heidi
David
Alice

Choose an action:
0 : I can move to (2, 2)
1 : I can move to (2, 3)
2 : I can move to (2, 4)
3 : I can move to (3, 2)
4 : I can move to (3, 3)
5 : I can move to (4, 2)
6 : I can move to (4, 3)
7 : I can attack David at (4, 4)"""

# unsloth/mistral-7b-bnb-4bit
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "williamsl/DungeonsAndDragonsGPT",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
FastLanguageModel.for_inference(model)

inputs = tokenizer(
[
    prompt_template.format(
        test_input,
        ""
    )
], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 1024, use_cache = True)
tokenizer.batch_decode(outputs)