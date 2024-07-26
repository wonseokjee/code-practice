from collections import deque

m, n = map(int, input().split())
tomato = []
q = deque()
for i in range(n):
    t = list(map(int, input().split()))
    tomato.append(t)
    for j in range(m):
        if t[j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append((nx, ny))


bfs()

max_num = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        if tomato[i][j] > max_num:
            max_num = tomato[i][j]
print(max_num - 1)