from functools import wraps


def make_bold(function):
    @wraps(function)
    def wrapper(*args):
        res = function(*args)
        return f"<b>{res}</b>"

    return wrapper


def make_italic(function):
    @wraps(function)
    def wrapper(*args):
        res = function(*args)
        return f"<i>{res}</i>"

    return wrapper


def make_underline(function):
    @wraps(function)
    def wrapper(*args):
        res = function(*args)
        return f"<u>{res}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))