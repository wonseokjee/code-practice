h,w = map(int,input().split())
lst = list(map(int,input().split()))
graph = [[0]*h for _ in range(w)]
for i in range(w):
    cnt = 0
    while(cnt < lst[i]):
        graph[i][cnt] = 1
        cnt += 1
# print(graph)
ans = 0
for a in range(h):
    cnt = 0
    cnt_0 = 0
    for b in range(w):
        if graph[b][a] == 1:
            cnt += 1
            if cnt == 2:
                ans += cnt_0
                cnt_0 = 0
                cnt = 1
        if graph[b][a] == 0 and cnt == 1:
            cnt_0 += 1
print(ans)



