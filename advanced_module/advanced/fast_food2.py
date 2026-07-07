from collections import deque

quantity_of_food = int(input())
quantity_of_food_each_order = deque(int(i) for i in input().split(' '))

print(max(quantity_of_food_each_order))
completed = True

while quantity_of_food_each_order:
    order = quantity_of_food_each_order[0]
    if quantity_of_food >= order:
        quantity_of_food -= order
        quantity_of_food_each_order.popleft()
    else:
        print(f'Orders left: {" ".join(str(order) for order in quantity_of_food_each_order)}')
        completed = False
        break

if completed:
    print('Orders complete')


