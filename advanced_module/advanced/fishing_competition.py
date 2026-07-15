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

while command != 'collect the nets':
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)



    command = input()