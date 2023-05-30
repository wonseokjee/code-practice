n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
count = 0
print(arr)
#플로이드 워셜
for k in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])
print(arr)


#최소시간 계산
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)