eggs_size = input()
eggs_color = input()
partidi_number = int(input())
egg_price = 0

if eggs_size == 'Large':
    if eggs_color == 'Red':
        egg_price = 16
    elif eggs_color == 'Green':
        egg_price = 12
    elif eggs_color == 'Yellow':
        egg_price = 9
elif eggs_size == 'Medium':
    if eggs_color == 'Red':
        egg_price = 13
    elif eggs_color == 'Green':
        egg_price = 9
    elif eggs_color == 'Yellow':
        egg_price = 7
elif eggs_size == 'Small':
    if eggs_color == 'Red':
        egg_price = 9
    elif eggs_color == 'Green':
        egg_price = 8
    elif eggs_color == 'Yellow':
        egg_price = 5

total_egg_price = egg_price * partidi_number
total_price_after_tax = total_egg_price * 0.65

print(f'{total_price_after_tax:.2f} leva.')