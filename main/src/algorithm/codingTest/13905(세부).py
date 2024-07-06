import heapq,sys
input = sys.stdin.readline

n,m = map(int, input().split())
s,e = map(int, input().split())
#최소값중에 가장 큰 것.
#노드 연결시 최대힙 쓰면 되지 않을까

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
INF = (10**6)+1
gold = [0] * (n+1)
for i in range(m):
    h1,h2,k = map(int, input().split())
    heapq.heappush(graph[h1], (-k, h2))
    heapq.heappush(graph[h2], (-k, h1))
arr = []
def bfs(s,e):
    q = []
    heapq.heappush(q,(-INF,s))
    while(q):
        x,y = heapq.heappop(q)
        for k, h in graph[y]:
            next = min(-k,-x)
            # print(next)
            if gold[h] < next:
                heapq.heappush(q,(-next,h))
                gold[h] = next
gold[s] = 0
bfs(s,e)
print(gold[e])