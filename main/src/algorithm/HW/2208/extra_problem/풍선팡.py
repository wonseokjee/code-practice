import sys
sys.stdin = open('풍선팡.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direct = [[0,1],[0,-1],[1,0],[-1,0]]
    cnt_max = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(1 , arr[i][j]+1):
                for l in direct:
                    ni = i + l[0] * k
                    nj = j + l[1] * k
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            if cnt_max< cnt:
                cnt_max = cnt
    print(f'#{tc} {cnt_max}')
