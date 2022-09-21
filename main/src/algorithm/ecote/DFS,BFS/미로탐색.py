from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 1. bfs정의하기
di = [[1,0],[-1,0],[0,1],[0,-1]]
distance = [[0]*M for _ in range(N)]
def bfs(x,y):
    global cnt
    arr[x][y] = 2
    distance[x][y] = 1
    queue = deque()
    queue.append([x,y])
    # print(queue)
    while queue:
        i ,j = queue.popleft()
        for k in di:
            ni = i + k[0]
            nj = j + k[1]
            if 0<= ni <N and 0 <= nj < M:
                if arr[ni][nj] == 1:
                    queue.append([ni,nj])
                    arr[ni][nj] = 2
                    distance[ni][nj] += distance[i][j] + 1

bfs(0,0)
# print(distance)
print(distance[N-1][M-1])

