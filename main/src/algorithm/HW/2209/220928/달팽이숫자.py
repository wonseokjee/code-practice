T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    cnt = 1
    arr[0][0] = 1
    i = 0
    j = 0
    k = 0
    for _ in range(N*N-1):
        while True:
            ni = i + dir[k][0]
            nj = j + dir[k][1]
            if 0<=ni <N and 0<=nj<N and arr[ni][nj]==0:
                cnt += 1
                arr[ni][nj] = cnt
                i,j = ni,nj
                break
            else:
                k = (k+1)%4

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])

