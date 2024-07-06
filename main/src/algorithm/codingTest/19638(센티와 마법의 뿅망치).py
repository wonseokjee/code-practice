import heapq
n,height,limit = map(int, input().split())
arr = [int(input()) for _ in range(n)]
cnt = 0
heap = []
#최대힙 사용
for value in arr:
    heapq.heappush(heap, -value)

while(cnt < limit):
    x = -heap.pop(0)
    if x <= 1 or x < height:
        heapq.heappush(heap, -x)
        break
    x = x / 2
    cnt += 1
    heapq.heappush(heap, -x)

if int(-heap[0]) >= height:
    print("NO")
    print(int(-heap[0]))
else:
    print("YES")
    print(cnt)



