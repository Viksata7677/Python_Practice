bought_food_in_kilograms = int(input())
food_in_grams = bought_food_in_kilograms * 1000
food_consumed = 0
command = input()

while command != "Adopted":
    grams_eaten = int(command)
    food_consumed += grams_eaten
    command = input()

if food_in_grams >= food_consumed:
    print(f"Food is enough! Leftovers: {food_in_grams - food_consumed} grams." )
else:
    print(f'Food is not enough. You need {food_consumed - food_in_grams} grams more.')