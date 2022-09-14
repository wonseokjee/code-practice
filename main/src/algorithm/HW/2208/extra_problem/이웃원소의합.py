T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+2)]+[[0]+ list(map(int, input().split())) + [0] for _ in range(N)]+[[0]*(N+2)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    cnt_max = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt = 0
            if arr[i][j] != 0:
                for k in range(len(di)):
                    ni = i + di[k]
                    nj = j + dj[k]
                    cnt += arr[ni][nj]
                    if cnt > cnt_max:
                        cnt_max = cnt
    print(f'#{tc} {cnt_max}')
