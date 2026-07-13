class NotIntegerError(Exception):
    pass


try:
    number = int(input())
    print(number * number)
except ValueError:
    raise NotIntegerError("Input must me an integer")
