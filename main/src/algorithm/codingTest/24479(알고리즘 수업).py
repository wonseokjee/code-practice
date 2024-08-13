N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
order = []
ans = [0 for _ in range(N)]
for _ in range(M):
    node, next = map(int, input().split())
    graph[node].append(next)
for i in range(1,N+1):
    if len(graph[i]) > 1:
        graph[i].sort()

# print(graph)

def dfs(r):
    order.append(r)
    for i in graph[r]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
dfs(R)
# print(order)
for j in range(len(order)):
    ans[order[j]-1] = j+1
# print(ans)
for k in ans:
    print(k)


