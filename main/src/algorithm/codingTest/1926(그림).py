import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
ans = 0
color_cnt = 0
def dfs(x,y):
    global color_cnt
    graph[x][y] = 0
    color_cnt += 1
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        if 0 <= a < n and 0 <= b < m and graph[a][b]:
            dfs(a,b)

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            dfs(i,j)
            cnt += 1
            if color_cnt> ans:
                ans = color_cnt
            color_cnt = 0
print(cnt)
print(ans)
