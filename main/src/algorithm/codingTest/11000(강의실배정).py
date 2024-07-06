import heapq
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for case in range(N):
    start, end = map(int,input().split())
    lst.append([start,end])
lst.sort()

room = []
heapq.heappush(room, lst[0][1])

for i in range(1,N):
    if lst[i][0] >= room[0]:
        heapq.heappop(room)  # pop하면 가장 작은 원소를 pop
    heapq.heappush(room, lst[i][1])
print(len(room))