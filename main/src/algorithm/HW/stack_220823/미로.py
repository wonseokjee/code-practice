import sys
sys.stdin = open('미로.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    def dfs2(i, j):
        if arr[i][j] == 3:
            return 1
        else:
            arr[i][j] = 1
            for k,l in [[-1,0],[0,1],[0,-1],[1,0]]:
                if  0<=i+k<N and 0<=j+l<N:
                    if arr[i+k][j+l] != 1:
                        if dfs2(i+k,j+l):
                            return 1
            return 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                print(f'#{tc} {dfs2(i,j)}')


