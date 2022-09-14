T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):

            for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = di+i, dj+j
                if 0<= ni <N and 0<= nj < N:
                    answer += abs(arr[i][j]-arr[ni][nj])
    print(f'#{tc} {answer}')