total = 0

with open('numbers.txt', 'r') as numbers, open('results.txt', 'w') as result:
    for num in numbers:
        if num.strip():
            total += int(num)

    result.write(str(total))