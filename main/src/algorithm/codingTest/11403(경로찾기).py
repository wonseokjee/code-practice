N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
node = [[]*N for _ in range(N)]
# print(node)
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            node[a].append(b)
            # node[b].append(a)
# print(node)

def dfs(k,l):
    for i in node[k]:
        # print(k,i)
        if visited[l][i] == 0:
            visited[l][i] = 1
            dfs(i,l)
for i in range(N):
    dfs(i,i)
# print(visited)
for i in visited:
    print(*i)