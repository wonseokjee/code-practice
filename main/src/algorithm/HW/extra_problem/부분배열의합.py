import sys
sys.stdin = open('부분배열의합.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, n ,m = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt_max = 0
    for i in range(N-n+1):
        for j in range(N-m+1):
            cnt = 0
            for k in range(n):
                for l in range(m):
                    if arr[i+k][j+l] == 1:
                        cnt += 1
            if cnt > cnt_max:
                cnt_max = cnt
    print(f'#{tc} {cnt_max}')