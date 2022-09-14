T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for k in range(1, M+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if M % k == 0:
                    arr[i-1][j-1] = 1 - arr[i-1][j-1]
                    if k == M:
                        cnt += arr[i-1][j-1]
                    continue
                if (i+j) % k == 0 or (i+j) == k:
                    arr[i-1][j-1] = 1 - arr[i-1][j-1]
    print(f'#{tc} {cnt}')