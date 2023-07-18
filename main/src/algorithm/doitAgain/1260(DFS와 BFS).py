from collections import deque
import sys
sys.setrecursionlimit(5000)
n,m,v = map(int, input().split())
arr = [[] for _ in range(1002)]
for put in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort()
visited = [False]*(1002)
def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for k in arr[x]:
        if not visited[k]:
            dfs(k)

def bfs(x):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([x])
    #현재 노드를 방문 처리
    visited[x] = True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #해당 원소와 연결된, 아직 방문하지 않은 원소들ㅇ르 큐에 삽입
        print(v, end=' ')
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
visited = [False]*(n+1)
print()
bfs(v)