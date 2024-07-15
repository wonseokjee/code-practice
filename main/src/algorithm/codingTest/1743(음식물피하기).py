import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1
# print(graph)
cnt = 0
def dfs(x,y):
    global tmp
    global cnt
    tmp += 1
    if cnt < tmp:
        cnt = tmp
    graph[x][y] = 0
    for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
        if 0 <= a+x < N and 0 <= b+y < M:
            if graph[x+a][y+b]:
                # print(a + x, b + y)
                dfs(x+a,y+b)
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            tmp = 0
            # print(f'dfs{i} {j}')
            dfs(i,j)
print(cnt)


