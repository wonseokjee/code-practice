r,c,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
#공청기 찾는 for문
machine = []
save_num = 0
ins_num = 0
for i in range(r):
    if graph[i][0] == -1:
        machine.append([i,0])
##미세먼지 확산 하는 함수
def dust():
    graph_ins = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                cnt = 0
                diffusion = graph[i][j] // 5
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    x = i + dx
                    y = j + dy
                    if 0<=x<r and 0<=y<c and graph[x][y] != -1:
                        cnt += 1
                        graph_ins[x][y] += diffusion
                graph[i][j] -= diffusion * cnt
    return graph_ins
## 공청기 위
def start_machine(num, direct):
    x,y = machine[num]
    direct_num = 0
    start_x, start_y = x,y
    global ins_num
    global save_num
    while(True):
        m = start_x + direct[direct_num][0]
        n = start_y + direct[direct_num][1]

        if 0 <= m < r and 0 <= n < c:
            if m == x and n == y:
                return False
            ins_num = graph[m][n]
            graph[m][n] = save_num
            save_num = ins_num

            start_x = m
            start_y = n
        else:
            direct_num += 1

## 공청기 아래

for _ in range(t):
    ins = dust()
    #미세먼지 확산
    for i in range(r):
        for j in range(c):
            graph[i][j] = graph[i][j] + ins[i][j]
    start_machine(0,[[0,1],[-1,0],[0,-1],[1,0]])
    ins_num = 0
    save_num = 0
    start_machine(1, [[0,1],[1,0],[0,-1],[-1,0]])
    ins_num = 0
    save_num = 0
# print(graph)
ans = 0
for i in range(r):
    ans += sum(graph[i])
print(ans+2)