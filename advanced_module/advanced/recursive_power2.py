def recursive_power(num, pow):
    if pow == 1 :
        return num

    result = num * recursive_power(num, pow - 1)
    return result

print(recursive_power(2, 3))