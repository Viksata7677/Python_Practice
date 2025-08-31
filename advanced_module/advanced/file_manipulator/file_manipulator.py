import os

command = input().split('-')
while command[0] != 'End':
    file_name = command[1]
    if command[0] == 'Create':
        with open(file_name, 'w'):
            pass
    elif command[0] == 'Add':
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')
    elif command[0] == 'Replace':
        old_string = command[2]
        new_string = command[3]
        try:
            with open(file_name, 'r+') as file:
                lines = file.read()
                lines = lines.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(lines)
        except FileNotFoundError:
            print('An error occurred')
    elif command[0] == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input().split('-')
