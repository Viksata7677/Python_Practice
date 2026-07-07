stack = []
lines = int(input())

for i in range(lines):
    query = input()
    if '1' in query:
        _, number = query.split(' ')
        stack.append(number)
    elif query == '2':
        stack.pop()
    elif query == '3':
        print(max(stack))
    elif query == '4':
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(", ".join(reversed_stack))