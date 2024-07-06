import heapq
n,m = map(int, input().split())
s,e = map(int, input().split())
#최소값중에 가장 큰 것.
#노드 연결시 최대힙 쓰면 되지 않을까
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    h1,h2,k = map(int, input().split())
    heapq.heappush(graph[h1], (-k, h2))
    heapq.heappush(graph[h2], (-k, h1))
ans = 0
# arr = []
def dfs(s,e, cnt):
    global ans
    visited[s] = True
    if cnt > ans:
        return
    if s == e:
        ans = cnt
        # arr.append(cnt)
    for k, h in graph[s]:
        if not visited[h]:
            dfs(h,e,max(cnt,k))
            visited[h] = False
dfs(s,e,-1000000)
# print(arr)
print(-ans)
# print(-min(arr))



