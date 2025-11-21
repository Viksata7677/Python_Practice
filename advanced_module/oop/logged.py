from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        args_list = ", ".join([repr(a) for a in args])
        return f'you called {function.__name__}({args_list})\nit returned {result}'

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))