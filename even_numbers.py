def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

numbers = list(map(int, input().split()))

print(filter_even_numbers(numbers))
