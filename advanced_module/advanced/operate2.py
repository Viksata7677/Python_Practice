def operate(operator, *args):

    if operator == "+":
        def addition():
            result = 0
            for num in args:
                result += num
            return result
        return addition()

    if operator == "-":
        def subtraction():
            result = 0
            for num in args:
                result -= num
            return result
        return subtraction()

    if operator == "*":
        def multiplication():
            result = 1
            for num in args:
                result *= num
            return result
        return multiplication()

    if operator == "/":
        def division():
            result = 1
            for num in args:
                result /= num
            return result
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
