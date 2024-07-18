import heapq
N,K = map(int,input().split())
Tmin_heap = []
Imax_heap = []
cnt = 0
for _ in range(K):
    I,T = map(int,input().split())
    heapq.heappush(Tmin_heap,[T,I])
while Tmin_heap :
    t,i = heapq.heappop(Tmin_heap)
    # print(t,i)
    if cnt + t <= N:
        heapq.heappush(Imax_heap,[i,t])
        cnt += t
    else:
        a, b = heapq.heappop(Imax_heap)
        cnt -= b
        if cnt + t <= N and a < i:
            heapq.heappush(Imax_heap,[i,t])
            cnt += t
        else:
            heapq.heappush(Imax_heap, [a, b])
            cnt += b
# print(cnt)
ans = 0
for time, imp in Imax_heap:
    ans += time
print(ans)