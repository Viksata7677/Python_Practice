from collections import deque

fuel_quantity = [int(i) for i in input().split()]
additional_consumption = deque([int(i) for i in input().split()])
fuel_needed = deque([int(i) for i in input().split()])

altitudes = len(fuel_quantity)
reached_altitudes = 0

while fuel_quantity:
    fuel = fuel_quantity.pop()
    consumption = additional_consumption.popleft()
    needed = fuel_needed.popleft()

    result = fuel - consumption

    if result >= needed:
        reached_altitudes += 1
        print(f"John has reached: Altitude {reached_altitudes}")
    else:
        print(f"John did not reach: Altitude {reached_altitudes + 1}")
        break

if reached_altitudes and altitudes > reached_altitudes:
    reached = ", ".join([f'Altitude {altitude+1}' for altitude in range(reached_altitudes)])
    print(f"John failed to reach the top.\nReached altitudes: {reached}")
elif reached_altitudes < altitudes and not reached_altitudes:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
elif reached_altitudes == altitudes:
    print("John has reached all the altitudes and managed to reach the top!")
