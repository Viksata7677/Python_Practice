def print_triangle(size):
    for i in range(1, size + 1):
        for num in range(1, i + 1):
            print(num, end=" ")
        print()

    for i in range(size - 1, 0, -1):
        for num in range(1, i + 1):
            print(num, end=" ")
        print()