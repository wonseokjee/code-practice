import sys
sys.setrecursionlimit(10**6)

while(True):
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    di = [[0,1],[-1,0],[1,0],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]] #방향판
    def dfs(x, y):
        arr[x][y] = 2
        for k in di:
            ni = x + k[0]
            nj = y + k[1]
            if 0<=ni<h and 0<=nj<w:
                if arr[ni][nj] == 1:
                    dfs(ni, nj)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    # print(arr)
    print(cnt)