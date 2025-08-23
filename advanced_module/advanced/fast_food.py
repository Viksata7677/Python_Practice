from collections import deque

quantity_of_food_for_day = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if quantity_of_food_for_day >= order:
        orders.popleft()
        quantity_of_food_for_day -= order
    else:
        print(f"Orders left: {" ".join(str(i) for i in orders)}")
        break
else:
    print('Orders complete.')
