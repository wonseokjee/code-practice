# 1. 유효성 검사: 좌상, 우상, 상 체크
def correct(x,y):
    # 1있으면 False 없으면 True 반환
    for k in range(1,N+1):
        for l in direct:
            ni = x + k*l[0]
            nj = y + k*l[1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 1:
                    return False
    else:
        return True

# 2. 해당 행에 없는지 확인 visited로 체크
def check(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[x]:
            if correct(x,i):
                arr[x][i] = 1
                visited[x] = True
                check(x+1)
                visited[x] = False
                arr[x][i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    direct = [[-1,-1],[-1,0],[-1,1]]
    arr = [[0]*N for _ in range(N)]
    visited = [False]*N
    cnt = 0
    check(0)
    print(f'#{tc} {cnt}')