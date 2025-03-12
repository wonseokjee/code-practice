N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*N for _ in range(N)]
board[0][0] = 1
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            k = graph[i][j]
            if k > 0:
                if 0<=i+k<N :
                    board[i+k][j] += board[i][j]
                if 0 <= j + k < N:
                    board[i][j+k] += board[i][j]
print(board[N-1][N-1])