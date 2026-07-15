def get_next_position(position, direction_mapper, direction, matrix):
    current_row, current_col = position
    row, col = direction_mapper[direction]
    desired_row = current_row + row
    desired_col = current_col + col

    if 0 <= desired_row < len(matrix) and 0 <= desired_col < len(matrix):
        return desired_row, desired_col

    if desired_row < 0:
        desired_row = len(matrix) - 1
    elif desired_row >= len(matrix):
        desired_row = 0

    if desired_col < 0:
        desired_col = len(matrix) - 1
    elif desired_col >= len(matrix):
        desired_col = 0

    return desired_row, desired_col


n = int(input())

direction_mapper = {
    "up": (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

matrix = []
position = None

for row_index in range(n):
    data = list(input())

    if 'S' in data:
        current_col = data.index('S')
        position = [row_index, current_col]
    matrix.append(data)

command = input()
collected_fish = 0

while command != 'collect the nets':
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = 'S'
    matrix[current_row_index][current_col_index] = '-'
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinated of the ship: {position}")
        exit()

    command = input()

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!\n"
          f"You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons")

for row in matrix:
    print(f"{''.join(row)}")