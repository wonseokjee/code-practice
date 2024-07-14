import sys
import heapq
input = sys.stdin.readline
N,K = map(int, input().split())
jewels = [[*map(int,input().split())] for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewels.sort()
bags.sort()
# print(jewels,bags)
ans = 0
tmp=[]
for bag in bags:
    while jewels and jewels[0][0] <=bag:
        heapq.heappush(tmp,-jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        ans -= heapq.heappop(tmp)
# print(tmp)

# for k in bag:
#     while(jewel):
#         x = heapq.heappop(jewel)
#         if -x[0] <= k:
#             ans += -x[1]
#             # print(x)
#             break
print(ans)


# 6 3
# 1 65
# 100 65
# 5 99
# 2 99
# 3 99
# 7 99
# 3
# 2
# 1

# 4 4
# 1 100
# 2 200
# 13 300
# 10 500
# 10
# 10
# 10
# 14

# 9 5
# 4 5
# 4 9
# 4 10
# 8 55
# 14 20
# 9 15
# 8 55
# 8 5
# 11 54
# 10
# 5
# 4
# 15
# 20