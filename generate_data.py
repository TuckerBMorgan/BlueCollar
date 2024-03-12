import random

character_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Laura", "Mallory", "Nancy", "Oscar", "Peggy", "Quentin", "Romeo", "Sybil", "Trent", "Ursula", "Victor", "Walter", "Xander", "Yvonne", "Zelda"]

for i in range(1):
    num_characters = random.randint(2, 10)
    teams = None
    while True:
        teams = [random.randint(0, 1) for j in range(num_characters)]
        has_0 = False
        has_1 = False
        for j in range(num_characters):
            if teams[j] == 0:
                has_0 = True
            elif teams[j] == 1:
                has_1 = True
        if has_0 and has_1:
            break
    my_index = random.randint(0, num_characters - 1)
    board_size = random.randint(4, 8)

    board = [[None for k in range(board_size)] for j in range(board_size)]
    positions = []
    for j in range(num_characters):
        unoccupied_position = None
        while True:
            unoccupied_position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
            if board[unoccupied_position[0]][unoccupied_position[1]] == None:
                break
        board[unoccupied_position[0]][unoccupied_position[1]] = j
        positions.append(unoccupied_position)

    teammates = "".join([f"{character_names[j]}\n" if teams[j] == teams[my_index] else "" for j in range(num_characters)])
    enemies = "".join([f"{character_names[j]}\n" if teams[j] != teams[my_index] else "" for j in range(num_characters)])

    actions = []
    for j in range(positions[my_index][0] - 1, positions[my_index][0] + 2):
        if j < 0 or j >= board_size:
            continue
        for k in range(positions[my_index][1] - 1, positions[my_index][1] + 2):
            if k < 0 or k >= board_size:
                continue
            if board[j][k] == None:
                actions.append(("M", (j, k)))
            else:
                actions.append(("A", (j, k)))

    moves = "".join([f"{j} : I can move to {actions[j][1]}\n" if actions[j][0] == "M" else "" for j in range(len(actions))])
    attacks = "".join([f"{j} : I can attack {character_names[board[actions[j][1][0]][actions[j][1][1]]]} at {actions[j][1]}\n" if actions[j][0] == "A" else "" for j in range(len(actions))])

    print(f"num_characters {num_characters}")
    print(f"teams {teams}")
    print(f"my_index {my_index}")
    print(f"board_size {board_size}")
    print(f"positions {positions}")
    print()

    data = f"""I am {character_names[my_index]} I am represented by {character_names[my_index][0]}
I am on team {teams[my_index]}
I have {random.randint(1, 10)} health
I can do 1 damage
I can move 1 tiles
My attack range is 1 tiles
I am at position {positions[my_index]}

My teammates are: (team {teams[my_index]})
{teammates}
My enemies are: (team {0 if teams[my_index] == 1 else 1})
{enemies}
My valid moves are:
{moves}
My valid attacks are:
{attacks}
The board looks like:
A - - - -
- B - - -
- - C - D
- - - - -
- - - - E

The turn order is:
Charlie
Alice
Eve
Bob
David

Choose an action:
0 : I can move to (1, 1)
1 : I can move to (1, 2)
2 : I can move to (1, 3)
3 : I can move to (2, 1)
4 : I can move to (2, 3)
5 : I can move to (3, 1)
6 : I can move to (3, 2)
7 : I can move to (3, 3)
8 : I can Attack Bob at (1, 1)"""
    print(data)