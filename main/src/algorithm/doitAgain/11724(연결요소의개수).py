import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
# print(arr)

visited = [False] * (n+1)
ans = 0

def dfs(x):
    visited[x] = True
    for j in arr[x]:
        if not visited[j]:
            dfs(j)

for k in range(1, n+1):
    if not visited[k]:
        dfs(k)
        ans += 1

print(ans)