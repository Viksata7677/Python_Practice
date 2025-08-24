nums_of_commands = int(input())
parking_lot = set()

for i in range(nums_of_commands):
    record = input()
    direction, car_number = record.split(", ")

    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)

if parking_lot:
    for number in parking_lot:
        print(number)
else:
    print("Parking Lot is Empty")