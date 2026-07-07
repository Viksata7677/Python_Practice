numbers = (float(num) for num in input().split())
counts = {}

for num in numbers:
    if num not in counts:
        counts[num] = 0
    counts[num] += 1

for num, count in counts.items():
    print(f'{num:.1f} - {count} times')

