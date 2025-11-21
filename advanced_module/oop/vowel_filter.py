from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        vowels = ['a', 'e', 'i', 'o', 'u']
        return [ch for ch in function() if ch in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
