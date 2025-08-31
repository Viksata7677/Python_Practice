with open('text.txt', 'w') as file:
    lines = [
        "-I was quick to judge him, but it wasn't his fault.\n",
        "-Is this some kind of joke?! Is it?\n",
        "-Quick, hide here. It is safer.\n"
    ]
    file.writelines(lines)

with open('text.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as output:
    for row in range(len(lines)):
        letters = 0
        marks = 0

        for symbol in lines[row]:
            if symbol.isalpha():
                letters += 1
            elif symbol in [',', '-', "'", '!', '?', '.']:
                marks += 1

        output.write(f'Line {row}: {lines[row].strip()} ({letters})({marks})\n')
