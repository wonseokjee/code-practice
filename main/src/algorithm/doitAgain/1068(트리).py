n = int(input())
parent = list(map(int, input().split()))
k = int(input())
root = 0
arr = [[] for _ in range(n)]
visited = [False]*n
cnt = 0
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        arr[parent[i]].append(i)

def dfs(x):
    visited[x] = True
    for i in arr[x]:
        dfs(i)
dfs(k)
# print(arr)
# print(visited)
for j in range(n):
    if(len(arr[j]) == 0 and visited[j] == False):
        cnt += 1
if len(arr[k-1]) == 1 and arr[k-1][0]==k:
    cnt += 1

print(cnt)

# 5
# -1 0 1 1 1
# 1
