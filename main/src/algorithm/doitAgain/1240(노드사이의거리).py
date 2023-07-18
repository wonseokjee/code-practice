n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = 0
visited = [False] * (n+1)
def dfs(start, end):
    global cnt
    visited[start] = True
    for y,z in graph[start]:
        if not visited[y]:
            cnt += z
            if y == end:
                print(cnt)
            dfs(y, end)
            cnt -= z

for i in range(n-1):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))
for j in range(m):
    x,y = map(int, input().split())
    dfs(x,y)
    visited = [False] * (n + 1)
    cnt = 0
