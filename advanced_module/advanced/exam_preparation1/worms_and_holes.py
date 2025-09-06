from collections import deque

worms = [int(i) for i in input().split()]
holes = deque([int(i) for i in input().split()])

matches = 0
total_worms = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm <= 0:
        continue

    if worm == hole:
        matches += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == total_worms:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {", ".join([str(worm) for worm in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {[hole for hole in holes]}")