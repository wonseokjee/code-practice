from collections import deque
n = int(input())
visited = [[i] for i in range(1000001)]

def bfs():
    queue = deque([n])
    while(queue):
        k = queue.popleft()
        if k ==1:
            break
        for i in (k/2,k/3,k-1):
            if i == int(i) and i>=1:
                l = int(i)
                # print(l, visited[l])
                if len(visited[l]) == 1:
                    for m in visited[k]:
                        visited[l].append(m)
                        # print(m)
                    queue.append(l)
bfs()
ans = list(reversed(visited[1]))
print(len(ans)-1)
print(*ans)
