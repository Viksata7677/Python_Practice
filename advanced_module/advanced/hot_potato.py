from collections import deque

queue = deque()
names = input().split()
for name in names:
    queue.append(name)
toss = int(input())

while len(queue) > 1:
    for i in range(toss - 1):
        queue.append(queue.popleft())
    removed = queue.popleft()
    print(f'Removed {removed}')

print(f'Last is {queue[0]}')