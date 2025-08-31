file = open('numbers.txt', 'r')
result = 0

for number in file:
    result += int(number)

print(result)