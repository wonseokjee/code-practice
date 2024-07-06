import heapq
N = int(input())
q = []
INF = int(1e9)
visited = [False] * (N)
distance = [INF] * (N)
graph = [[] for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if i <= j:
            graph[i].append((j, arr[j]))
print(graph)

def dijkstra():
    q = []
    heapq.heappush(q, (0,0))
    distance[0] = 0
    while q:
        node, dis = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (next[0], cost))
dijkstra()
print(distance)


