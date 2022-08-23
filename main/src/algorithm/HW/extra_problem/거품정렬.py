import sys
sys.stdin = open('거품정렬.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for k in range(N):
        for i in range(N):
            if 0 <= i+1 < N:
                if arr[i] > arr[i+1]:
                    arr[i] , arr[i+1] = arr[i+1] , arr[i]
                    cnt += 1

    print(f'#{tc} {cnt}')
