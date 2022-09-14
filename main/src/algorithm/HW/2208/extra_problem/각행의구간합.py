import sys
sys.stdin = open('각행의구간합.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n,k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt_max = 0
    for i in range(n):
        cnt = 0
        for j in range(i,i+k):
            if 0<= j <n:
               cnt += arr[i][j]
        if cnt_max <cnt : cnt_max = cnt

    print(f'#{tc} {cnt_max}')