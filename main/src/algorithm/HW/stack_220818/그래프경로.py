import sys
sys.stdin = open('그래프경로.txt', 'r')

# def dfs2(S):
#     if S == G:
#         return 1
#     else:
#         visited[S] = 1
#         for w in adjList[S]:
#             if visited[w] == 0:
#                 if dfs2(w):
#                     return 1
#         return 0

def dfs(v):
        visited[v] = 1
        for w in adjList[v]:
            if visited[w] == 0:
                dfs(w)


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for i in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    S, G = map(int, input().split())
    visited = [0]*N

    result = 0
    dfs(S)
    if visited[G] == 1:
        result = 1
    print(f'#{tc} {result}')
