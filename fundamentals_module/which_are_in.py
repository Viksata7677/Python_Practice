first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []

for i in first_sequence:
    for j in second_sequence:
        if i in j:
            substrings.append(i)
            break

print(substrings)