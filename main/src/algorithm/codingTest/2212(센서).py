import heapq
N = int(input())
K = int(input())
lst = list(sorted(map(int, input().split())))
heap = []
if K >= N:
    print(0)
else:
    for i in range(1,N):
        ins = lst[i] - lst[i-1]
        heapq.heappush(heap, -ins)
    for j in range(K-1):
        heapq.heappop(heap)
    print(-sum(heap))