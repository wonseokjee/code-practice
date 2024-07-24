from collections import deque

m, n = map(int, input().split())
tomato = []
q = deque()
for i in range(n):
    t = list(map(int, input().split()))
    tomato.append(t)
    for j in range(m):
        # 순회하며 익은 토마토를 미리 큐에 저장
        if t[j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                # 만약 익지 않은 토마토가 있다면 기존의 익은 토마토 위치의 숫자에 +1을 한뒤 저장
                # 큐에 해당 위치 저장
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append((nx, ny))


bfs()

max_num = 0
for i in range(n):
    for j in range(m):
        # 만약 익지 않은 토마토가 있는 경우 -1를 출력하고 종료
        if tomato[i][j] == 0:
            print(-1)
            exit()
        # 익은 토마토의 숫자가 제일 큰 것을 찾기
        if tomato[i][j] > max_num:
            max_num = tomato[i][j]
# 1에서부터 카운트가 되었기 때문에 -1 을 하여 최종 정답 출력
print(max_num - 1)