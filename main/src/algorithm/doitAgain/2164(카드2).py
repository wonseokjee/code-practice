from collections import deque
n = int(input())
queue = deque(i for i in range(1,n+1))
# print(queue)
while(len(queue) > 1):
    queue.popleft()
    x = queue.popleft()
    queue.append(x)
print(queue[0])