from collections import deque
m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])
# 시작점이 여러개일 경우가 있기 때문에
# 일단 시작점들을 queue에 넣고 bfs
def bfs():
    while queue:
        i, j = queue.popleft()
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            a = dx + i
            b = dy + j
            if 0 <= a <n and 0 <= b < m and box[a][b] == 0:
                box[a][b] = box[i][j] + 1
                queue.append([a,b])

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])


bfs()
ans = 0
for x in range(n):
    for y in range(m):
        if box[x][y] == 0:
            print(-1)
            exit()
        if box[x][y] > ans:
            ans = box[x][y]
print(ans-1)