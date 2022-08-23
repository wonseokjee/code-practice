import sys
sys.stdin = open('점점커지는당근의개수.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    cnt_max = 1
    for i in range(1,N):
        if arr[i] > arr[i-1]:
            cnt+= 1
            if cnt_max<cnt:
                cnt_max = cnt
        else:
            cnt = 1

    print(f'#{tc} {cnt_max}')
