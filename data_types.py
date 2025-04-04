def data_type(data_type, value):
    result = 0
    if data_type == 'int':
        result = int(value) * 2
    elif data_type == 'real':
        result = f"{float(value) * 1.5:.2f}"
    else:
        result = f"${value}$"
    return result


type_command = input()
command = input()

print(data_type(type_command, command))