from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global short
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        if city_range[v] > short:
            break
        for k in city_info[v]:
            if not visited[k]:
                visited[k] = True
                city_range[k] = city_range[v]+1
                if city_range[k] == short:
                    ans.append(k)
                queue.append(k)
n,m,short,x = map(int, input().split())
visited = [False]*(n+1)
city_range = [0]*(n+1)
city_info = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
    a,b = map(int, input().split())
    city_info[a].append(b)

bfs(x)
if ans == []:
    ans.append(-1)
ans.sort()
for num in ans:
    print(num)
print(city_info)
print(city_range)


