from collections import deque

queue = deque()
water_quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

command = input()
while command != 'End':
    if command.startswith('refill'):
        _, liters = command.split()
        water_quantity += int(liters)
    else:
        liters = int(command)
        person = queue.popleft()

        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    command = input()

print(f"{water_quantity} liters left")
