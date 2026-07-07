numbers = input().split()
list_nums = []

for i in numbers:
    list_nums.append(int(i))

stack = []

while list_nums:
    stack.append(str(list_nums.pop()))

print(" ".join(stack))
