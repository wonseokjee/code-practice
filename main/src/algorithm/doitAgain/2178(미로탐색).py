from collections import deque
n,m = map(int,input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    queue = deque([(0,0)])
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if n>x>=0 and m>y>=0 and arr[x][y]==1:
                queue.append((x,y))
                arr[x][y] = arr[a][b]+1
bfs()
print(arr[n-1][m-1])
