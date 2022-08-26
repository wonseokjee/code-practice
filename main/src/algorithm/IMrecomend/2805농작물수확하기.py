import sys
sys.stdin = open('2805농작물수확하기.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    mid = N//2
    cnt = 0
    for i in range(mid):#위 삼각형
        for j in range(mid-i,mid+i+1):
            cnt+= arr[i][j]
    for k in range(N):
        cnt += arr[mid][k]
    for a in range(N-1, mid, -1):#아래 삼각형
        for b in range(a-mid, N-(a-mid)):
            cnt += arr[a][b]
    print(f'#{tc} {cnt}')