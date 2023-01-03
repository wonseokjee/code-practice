n = int(input())
m = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    connect_info = list(map(int, input().split()))
    for j in range(n):
        if connect_info[j]:
            arr[i].append(j+1)
plan = list(map(int, input().split()))
print(arr)
#바로 이전에 방문한 것만 방문처리?? if not visited통과했으면 초기화하고 방문처리??
