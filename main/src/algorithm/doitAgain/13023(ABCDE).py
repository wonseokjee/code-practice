n,m = map(int, input().split())
arr = [[]for _ in range(n)]
visited = [False]*n

for i in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(x, depth):
    global ans

    if depth == 4:
        ans = 1
        return
    visited[x] = True
    for k in arr[x]:
        if not visited[k]:
            dfs(k, depth+1)
    visited[x] = False
ans = 0
for j in range(n):
    dfs(j,0)
    if ans == 1:
        break
    visited = [False] * n
print(ans)