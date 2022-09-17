import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int, input().split())
arr = [[0 for _ in range(N)]for _ in range(M)]
# print(arr)
di = [[0,1],[0,-1],[1,0],[-1,0]] #방향판
cnt = 0 # 영역의 개수
num = [] # 분리된 개수
# dfs 정의
def dfs(x, y):
    arr[x][y] = 2
    global cnt
    cnt += 1
    for k in di:
        ni = x + k[0]
        nj = y + k[1]
        if 0 <= ni < M and 0<=nj < N:
            if arr[ni][nj] == 0:
                dfs(ni,nj)

for _ in range(K): # 직사각형들의 범위에 1표시
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
# print(arr)

for i in range(M):
    for j in range(N):
        if arr[i][j] ==0:
            dfs(i,j)
            num.append(cnt)
            cnt = 0

print(len(num))
print(*sorted(num))
