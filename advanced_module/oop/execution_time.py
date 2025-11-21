import time
from functools import wraps


def exec_time(function):
    @wraps(function)
    def wrapper(start, end):
        start_time = time.time()
        res = function(start, end)
        end_time = time.time()
        return f"Execution time {end_time - start_time}"

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))