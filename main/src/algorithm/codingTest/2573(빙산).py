#1년마다 근처에 붙어있는 물(0)과 맞닿아있는 갯수만큼 빙하가 녹음
#이중포문으로 하나씩 체크하면서 1년 보내기
#가장 처음 2덩어리 이상으로 분리된 시간(년) dfs로 연결되었는지 확인 (visited 있어야 할듯 )
#아직 남아있으면 1로 체크하고 방문했으면 2. 1이 남은 상태라면 분리
import copy
import sys
sys.setrecursionlimit(10000)
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dir_x = 1,-1,0,0
dir_y = 0,0,1,-1
def year():
    global graph
    graph_ins = copy.deepcopy(graph)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j]>0:
                for idx in range(4):
                    if graph[i+dir_x[idx]][j+dir_y[idx]] == 0 and graph_ins[i][j] > 0:
                        graph_ins[i][j] -= 1
    graph = graph_ins

def check_connect(x,y):
    for idx in range(4):
        dx = x + dir_x[idx]
        dy = y + dir_y[idx]
        if visited[dx][dy] > 0:
            visited[dx][dy] = 0
            check_connect(dx,dy)

ans = 0

while(True):
    year()
    visited = copy.deepcopy(graph)
    x,y = 0,0
    flag = True
    for i in range(1,n-1):
        for j in range(1,m-1):
            if visited[i][j]>0:
                x = i
                y = j
                break
    if x > 0 and y > 0:
        check_connect(x,y)
        ans += 1
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if visited[i][j] > 0:
                    flag = False
                    break

    else:
        ans = 0
        break
    if not flag:
        break
print(ans)



