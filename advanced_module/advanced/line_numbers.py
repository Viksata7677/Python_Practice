with open('text.txt', 'r') as text, open('output.txt', 'w') as output:
    punctuation_marks = [',', '-', "'", '.', '!', '?']

    for line_number, line in enumerate(text, start=1):
        line = line.strip()
        punctuation_total = 0
        letters_total = 0
        for symbol in line:
            if symbol in punctuation_marks:
                punctuation_total += 1
            elif symbol.isalpha():
                letters_total += 1

        output.write(f"Line {line_number}: {line} {letters_total} {punctuation_total}\n")
