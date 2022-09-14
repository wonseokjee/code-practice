T = int(input())
for tc in range(1, T+1):
    N, q = map(int, input().split())
    arr = [0]*N
    for i in range(1, q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            arr[j] = i
    print(f'#{tc}', end=' ')
    print(*arr[:])
