from collections import deque
n,m = map(int, input().split())
lst = [[] for _ in range(n+1)]
visited = [0] * (n+1)
lst_hack_count = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    lst[b].append(a)
# print(lst)

def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        v = queue.popleft()
        for k in lst[v]:
            if not visited[k]:
                visited[k] = 1
                queue.append(k)
                lst_hack_count[k] = 1
                visited[k] = visited[v] + 1

for i in range(n):
    if lst_hack_count[i+1] == 0:
        bfs(i+1)
        lst_hack_count[i+1] = max(visited)
        # print(lst_hack_count)
    visited = [0] * (n + 1)

max_hack = max(lst_hack_count)
for i in range(len(lst_hack_count)):
    if lst_hack_count[i] == max_hack:
        print(i, end=' ')

# 8 7
# 1 8
# 3 1
# 3 2
# 5 3
# 4 3
# 6 4
# 7 6

# 8 8
# 2 8
# 3 1
# 3 2
# 5 3
# 4 3
# 6 4
# 7 6
# 8 3