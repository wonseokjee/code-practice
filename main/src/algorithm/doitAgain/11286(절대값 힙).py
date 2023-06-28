import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0 :
        if heap:
            arr = heapq.heappop(heap)
            print(arr[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(x), x))