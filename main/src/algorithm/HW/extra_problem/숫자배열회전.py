import sys
sys.stdin = open('숫자배열회전.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        arr_90 = []
        arr_180 = []
        arr_270 = []
        for j in range(N-1,-1,-1):
            arr_90.append(arr[j][i])
            arr_180.append(arr[N-i-1][j])
            arr_270.append(arr[N-j-1][N-i-1])

        print(*arr_90, sep='', end=' ')
        print(*arr_180, sep='', end=' ')
        print(*arr_270, sep='')

