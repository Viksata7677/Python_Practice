with open('text.txt', 'w') as text_file:
    lines = ["-I was quick to judge him, but it wasn't his fault.\n",
             "-Is this some kind of joke?! Is it?\n",
             "-Quick, hide here. It is safer."]
    text_file.writelines(lines)

with open('text.txt', 'r') as text_file:
    for index, line in enumerate(text_file):
        if index % 2 == 0:
            for ch in "-", ",", ".", "!", "?":
                line = line.replace(ch, '@')
            print(" ".join(reversed(line.split())))
