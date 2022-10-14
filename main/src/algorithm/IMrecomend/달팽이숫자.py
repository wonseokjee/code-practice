T = int(input())
for tc in range(1,T+1):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i,j = 0,0
    d = 0
    for a in range(1, N*N+1):
        arr[i][j] = a
        i += dx[d]
        j += dy[d]
        if i < 0 or i>=N or j < 0 or j >= N or arr[i][j] !=0:
            i, j = i-dx[d], j-dy[d]
            d = (d+1) % 4
            i,j = i+dx[d], j+dy[d]
    print(f'#{tc}')
    for k in range(N):
        for l in range(N):
            print(arr[k][l], end= ' ')
        print()





