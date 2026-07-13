words_file = open('words.txt', 'r')
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

words = words_file.read().lower().split()

text = input_file.read().lower()

counts = {}

for word in words:
    counts[word] = text.count(word)

sorted_counts = sorted(counts.items(), key=lambda x: -x[1])

for word, count in sorted_counts:
    output_file.write(f"{word} - {count}\n")

words_file.close()
input_file.close()
output_file.close()