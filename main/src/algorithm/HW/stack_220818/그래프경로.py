import sys
sys.stdin = open('그래프경로.txt', 'r')

def dfs2(S):
    if S == G:
        return 1
    else:
        visited[S] = 1
        for w in adjList[S]:
            if visited[w] == 0:
                if dfs2(w):
                    return 1


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
    cnt = 0
    if dfs2(S) == 1:
        cnt += 1
    print(f'#{tc} {cnt}')
