import copy
from itertools import combinations
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
list_0 = []
list_2 = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            list_2.append([i,j])
        if graph[i][j] == 0:
            list_0.append([i,j])
combi_0 = list(combinations(list_0,3))
# print(len(combi_0))
def bfs():
    while queue:
        x,y = queue.popleft()
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            a = x+dx
            b = y+dy
            if 0<=a<n and 0<=b<m and graph_ins[a][b] == 0:
                graph_ins[a][b] = 2
                queue.append([a,b])


cnt_max = 0

for k in range(len(combi_0)):
    queue = deque(list_2)
    graph_ins = copy.deepcopy(graph)
    for x,y in combi_0[k]:
    # for x, y in [[5,7],[6,6],[7,5]]:
        graph_ins[x][y] = 1
    bfs()
    cnt_0 = 0
    for i in range(n):
        cnt_0 += graph_ins[i].count(0)
    if cnt_0 > cnt_max:
        cnt_max = cnt_0
print(cnt_max)