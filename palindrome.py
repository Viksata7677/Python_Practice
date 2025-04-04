def is_palindrome(num):
    return str(num) == str(num)[::-1]


def check_palindromes(numbers):
    numbers_list = numbers.split(", ")

    for num in numbers_list:
        print(is_palindrome(num))


numbers = input()

check_palindromes(numbers)