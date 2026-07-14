symbols_to_replace = ['-', ',', '.', '!', '?', '.']

with open('text.txt', 'r') as text, open('output.txt', 'w') as output:
    for line_number, line in enumerate(text, start=0):
        if line_number % 2 != 0:
            continue

        for symbol in symbols_to_replace:
            line = line.replace(symbol, '@')

        words = line.split()
        reversed_words = words[::-1]
        final_line = " ".join(reversed_words)

        output.write(final_line + '\n')