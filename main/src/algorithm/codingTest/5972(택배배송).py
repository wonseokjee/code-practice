import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)#방문처리 기록용
INF = int(1e9)
distance = [INF] * (n+1)
for i in range(m):
    a,b, length = map(int, input().split())
    graph[a].append((b,length))
    graph[b].append([a, length])

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0],))
dijkstra(1)
print(distance[n])



