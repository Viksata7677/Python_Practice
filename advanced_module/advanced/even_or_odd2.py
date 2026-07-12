def even_odd(*args):
    even_nums = []
    odd_nums = []
    command = args[-1]

    if command == 'even':
        for num in args[:-1]:
            if num % 2 == 0:
                even_nums.append(num)
        return even_nums

    elif command == 'odd':
        for num in args[:-1]:
            if num % 2 != 0:
                odd_nums.append(num)
        return odd_nums

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))