import os

command = input()

while command != 'End':
    command = command.split('-')
    action = command[0]
    file_name = command[1]
    if action == 'Create':
        with open(file_name, 'w') as file:
            pass
    elif action == 'Add':
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif action == 'Replace':
        old_string = command[2]
        new_string = command[3]
        if not os.path.exists(file_name):
            print('An error occurred')
            continue

        with open(file_name, 'r') as file:
            text = file.read()

        text = text.replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write(text)
    elif action == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
    command = input()
