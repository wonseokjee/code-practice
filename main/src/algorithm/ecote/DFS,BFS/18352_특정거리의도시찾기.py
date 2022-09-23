from collections import deque
import sys
input = sys.stdin.readline
def bfs(X,n):
    queue = deque([X])
    while queue:
        if n > road:
            break
        v = queue.popleft()
        for k in lst[v]:
            if visited[k] == 0:
                visited[k] = n
                if visited[k] == road:
                    ans.append(k)
                queue.append(k)
        n += 1

city, M, road , X = map(int,input().split())
lst = [[] for _ in range(city+1)]
visited = [0]*(city + 1)
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
# print(lst)
ans = []
bfs(X, 1)
# print(visited)
if ans == []:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)



