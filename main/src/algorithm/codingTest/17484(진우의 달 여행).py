n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direct = [(1,-1), (1,0), (1,1)]
last_dir = [False]*3
ans = 10000000
def dfs(x,y,cnt,last_dir):
    global ans
    if x == n-1:
        cnt += graph[x][y]
        if ans > cnt:
            ans = cnt
        return
    for i in range(3):
        if m > y + direct[i][1] >= 0:
            if not last_dir[i]:
                dx = x + direct[i][0]
                dy = y + direct[i][1]
                last_dir = [False]*3
                last_dir[i] = True
                dfs(dx,dy,cnt+graph[x][y],last_dir)

for j in range(m):
    dfs(0,j,0,last_dir)
    last_dir = [False] * 3
print(ans)