from functools import wraps


def tags(tag):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            res = function(*args)
            start_tag = f'<{tag}>'
            end_tag = f"</{tag}>"
            return f"{start_tag}{res}{end_tag}"

        return wrapper
    return decorator


@tags('h1')
def to_upper(text):

    return text.upper()


print(to_upper('hello'))
