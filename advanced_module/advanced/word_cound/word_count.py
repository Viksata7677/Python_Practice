words_file = open('words.txt', 'w')
words_file.write('quick is fault')

input_file = open('input.txt', 'w')
input_lines = ["-I was quick to judge him, but it wasn't his fault.\n",
               "-Is this some kind of joke?! Is it?\n",
               "-Quick, hide here...It is safer."]
input_file.writelines(input_lines)

with open('words.txt', 'r') as words_file:
    words = words_file.read().split()

with open('input.txt', 'r') as input_file:
    text = input_file.read().lower()

occurrences = {}

for word in words:
    count = text.count(word)
    occurrences[word] = count

sorted_occurrences = sorted(occurrences.items(), key=lambda x: -x[1])

with open('output.txt', 'w') as f:
    for word, count in sorted_occurrences:
        line = f"{word} - {count}\n"
        f.write(line)
        print(line)
