n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 0
def clean(x,y):
    global ans
    # print(x,y,d)
    graph[x][y] = 2
    ans += 1

def cannotClean(x,y,z):
    global r,c
    z = (z+2) % 4
    ins_x = x + dir[z][0]
    ins_y = y + dir[z][1]
    if 0<=ins_x<n and 0<=ins_y<m and graph[ins_x][ins_y] == 1:
        return False
    else:
        r = ins_x
        c = ins_y
        return True

def canClean(x,y,z):
    global r,c,d
    z = (z+3)%4
    while(True):
        ins_x = x + dir[z][0]
        ins_y = y + dir[z][1]
        if 0<=ins_x<n and 0<=ins_y<m and graph[ins_x][ins_y] == 0:
            r,c,d = ins_x,ins_y,z
            break
        else:
            z = (z+3)%4

while(True):
    if graph[r][c] == 0:
        clean(r,c)
    cnt = 0
    for x,y in dir:
        ins_r = x+r
        ins_c = y+c
        if 0<=ins_r<n and 0<=ins_c<m and graph[ins_r][ins_c] == 0:
            cnt += 1
            break
    if cnt == 0:
        if not cannotClean(r,c,d):
            break
    else:
        canClean(r,c,d)
print(ans)

# 7 7
# 4 2 1
# 1 1 1 1 1 1 1
# 1 0 0 0 1 0 1
# 1 0 1 1 0 0 1
# 1 0 0 0 0 1 1
# 1 0 0 1 0 0 1
# 1 0 0 0 0 0 1
# 1 1 1 1 1 1 1
