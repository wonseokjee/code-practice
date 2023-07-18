from collections import deque
def bfs(x,y):
    arr[x][y] = 2
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n>nx>=0 and m>ny>=0 and arr[nx][ny]==1:
                arr[nx][ny] = 2
                queue.append((nx,ny))



t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for tc in range(t):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        y,x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for j in range(n):
        for k in range(m):
            if arr[j][k]== 1:
                bfs(j,k)
                cnt += 1
    print(cnt)

