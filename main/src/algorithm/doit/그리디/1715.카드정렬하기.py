import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))
# print(heap)
cnt = 0
while heap:
    x = heapq.heappop(heap)
    if heap:
        y = heapq.heappop(heap)
    else:
        break
    z = x + y
    heapq.heappush(heap,z)
    cnt += z
print(cnt)

