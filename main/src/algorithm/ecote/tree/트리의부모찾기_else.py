import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, v ,visited):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
        else:
            parent[v] = i

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
parent = [0]*(N+1)
# print(graph)
for _ in range(N-1):
    a, b = map(int, input().split())
    # print(a,b)
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
dfs(graph, 1, visited)
# print(parent)
for j in parent[2:]:
    print(j)