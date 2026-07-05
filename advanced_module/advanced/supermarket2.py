from collections import deque

customer_names = deque()
while True:
    command = input()
    if command == 'End':
        print(f"{len(customer_names)} people remaining.")
        break
    elif command == 'Paid':
        while len(customer_names):
            print(customer_names.popleft())
    else:
        customer_names.append(command)

