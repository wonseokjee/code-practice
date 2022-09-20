from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 1. bfs정의하기
di = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y):
    arr[x][y] = 2
    queue = deque([x,y])
    for k in di:
        ni = x + k[0]
        nj = y + k[1]
        if 0<=ni<N and 0<= nj < M:


