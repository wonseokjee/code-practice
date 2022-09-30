from collections import deque


N = int(input())
queue = deque([int(input()) for _ in range(N)])
cnt = 0

while len(queue)>1:
    x = queue.popleft()
    y = queue.popleft()
    z = x+y
    cnt += z
    queue.append(z)

print(cnt)