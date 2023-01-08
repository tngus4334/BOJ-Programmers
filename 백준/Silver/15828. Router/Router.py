from collections import deque
n = int(input())
queue = deque()
while True:
    x = int(input())
    if x == -1:
        break
    if x == 0 and len(queue) != 0:
        queue.popleft()

    elif x != 0 and len(queue) != n:
        queue.append(x)

if len(queue) == 0:
    print("empty")
else:
    print(*queue)