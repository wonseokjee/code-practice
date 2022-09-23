from collections import deque
import sys
input = sys.stdin.readline
def bfs(X):
    queue = deque([X])
    while queue:
        if visited[X] > road: # 최단거리를 입력한 visited[X]에 카운트해서 road보다 크면 break
            break
        v = queue.popleft()
        for k in lst[v]:
            if visited[k] == 0: # 방문하지 않았으면
                visited[k] = visited[v] + 1
                if visited[k] == road:
                    ans.append(k)
                queue.append(k)

city, M, road , X = map(int,input().split())
lst = [[] for _ in range(city+1)]
visited = [0]*(city + 1)
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
# print(lst)
ans = []
bfs(X)
# print(visited)
if ans == []:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)



