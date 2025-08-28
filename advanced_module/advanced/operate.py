def operate(operator, *args):
    total = 0
    if operator == "+":
        for num in args:
            total += num
        return total
    elif operator == "-":
        total = args[0]
        for num in args[1:]:
            total -= num
        return total
    elif operator == '*':
        total = 1
        for num in args:
            total *= num
        return total
    elif operator == '/':
        total = args[0]
        for num in args[1:]:
            total /= num
        return total


print(operate("*", 3, 4))