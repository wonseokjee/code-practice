from collections import deque

n = int(input())
m = int(input())
arr = [[] for _ in range(n)]
road_sep = []
visited = [False]*(n+1)
count = [0]*(n+1)
for i in range(n):
    connect_info = list(map(int, input().split()))
    for j in range(n):
        if connect_info[j]:
            arr[i].append(j+1)
            road_sep.append([i+1,j+1])
plan = list(map(int, input().split()))
find_plan = []
yes_no = 'YES'

def bfs(start, end):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if count[v] > 3:
            return False
        visited[v] = True
        for k in arr[v]:
            if k == end:
                return True
            if not visited[k]:
                queue.append(k)
                count[k] = count[v]+1


for i in range(m-1):
    if [plan[i],plan[i+1]] not in road_sep:
        find_plan.append([plan[i],plan[i+1]])

if not find_plan == []:
    for a,b in find_plan:
        if not bfs(a,b):
            yes_no = 'NO'
            break
print(yes_no)
# print(arr)
# print(road_sep)
# print(plan)
#바로 이전에 방문한 것만 방문처리?? if not visited통과했으면 초기화하고 방문처리??
#여행계획을 쪼개서 하나씩 비교. 있는것 통과 없는 것만 뽑아냄. 그걸 BFS 돌림



# 3
# 3
# 0 1 0
# 1 0 1
# 0 1 0
# 1 3 2