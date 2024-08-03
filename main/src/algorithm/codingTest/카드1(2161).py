from collections import deque
N = int(input())
queue = deque([])
for i in range(1,N+1):
    queue.append(i)
while(queue):
    x = queue.popleft()
    if len(queue)>0:
        y = queue.popleft()
        queue.append(y)
    print(x, end=' ')