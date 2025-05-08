def decode_message(message, commands):
    for command in commands:
        instructions = command.split('|')
        instruction = instructions[0]

        if instruction == 'Move':
            num_letters = int(instructions[1])
            message = message[num_letters:] + message[:num_letters]

        elif instruction == 'Insert':
            index = int(instructions[1])
            value = instructions[2]
            message = message[:index] + value + message[index:]

        elif instruction == 'ChangeAll':
            substring = instructions[1]
            replacement = instructions[2]
            message = message.replace(substring, replacement)

        elif instruction == 'Decode':
            print(f'The decrypted message is: {message}')


message = input()
command_list = []

while True:
    command = input()
    command_list.append(command)
    if command == 'Decode':
        break


decode_message(message, command_list)