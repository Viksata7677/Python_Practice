file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for line in file:
    if line.strip():
        output_file.write(line)

file.close()
output_file.close()
