r,c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
alpha = []
cnt = 0
def dfs(x,y,num):
    global cnt
    alpha.append(graph[x][y])
    if num > cnt:
        cnt = num
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if r>nx>=0 and c>ny>=0 and (not graph[nx][ny] in alpha):
            dfs(nx,ny,num+1)
            alpha.pop()
dfs(0,0,1)
print(cnt)



