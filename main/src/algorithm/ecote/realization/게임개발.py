N,M = list(map(int, input().split()))
a, b, head = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
compass = [0,1,2,3] #북 동 남 서
di = [[-1,0],[0,1],[1,0],[0,-1]]
cnt = 0
def dfs(a,b):
    arr[a][b]=1
    global cnt
    cnt += 1
    for i in range(4): #네방향
        ni = a+di[i][0]
        nj = b+di[i][1]
        if 0<= ni < N and 0<= nj < N:
            if arr[ni][nj]==0:
                dfs(ni,nj)
dfs(a,b)
print(cnt)

#input 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 0
# 1 1 0 1 1
# 1 0 0 0 1
# 1 1 0 1 1
