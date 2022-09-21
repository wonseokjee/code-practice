from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,V = map(int, input().split())
node = [[] for _ in range(10001)]

for _ in range(M):
    x, y = map(int, input().split())
    node[y].append(x)
    node[x].append(y)
for i in range(M+1):
    node[i].sort()
# print(node)
#node를 인접행렬으로
dfs_vistied = [False]*(10001)
bfs_vistied = [False]*(10001)
def dfs(node, v , dfs_vistied):
    dfs_vistied[v] = True
    print(v, end=' ')
    for i in node[v]:
        if not dfs_vistied[i]:
            dfs(node, i, dfs_vistied)
dfs(node,V,dfs_vistied)

def bfs(node, start, vistied):
    #큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문처리
    bfs_vistied[start] = True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in node[v]:
            if not bfs_vistied[i]:
                queue.append(i)
                bfs_vistied[i] = True
print()
bfs(node, V, bfs_vistied)
# 15 14 1
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# 4 8
# 4 9
# 5 10
# 5 11
# 6 12
# 6 13
# 7 14
# 7 15
