def even_odd(*args):
    even = []
    odd = []
    command = args[-1]

    if command == 'even':
        for num in args[:-1]:
            if num % 2 == 0:
                even.append(num)
        return even
    elif command == 'odd':
        for num in args[:-1]:
            if num % 2 != 0:
                odd.append(num)
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, "even"))