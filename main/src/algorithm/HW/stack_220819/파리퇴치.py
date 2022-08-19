import sys
sys.stdin = open('파리퇴치.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fly = []
    len_swing = M*M
    for k in range(M):
        for l in range(M):
            fly += [[k,l]]
    cnt_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(len_swing):
                di = i + fly[k][0]
                dj = j + fly[k][1]
                if 0<=di<N and 0<=dj<N:
                    cnt += arr[di][dj]
            if cnt > cnt_max: cnt_max = cnt
    print(f'#{tc} {cnt_max}')