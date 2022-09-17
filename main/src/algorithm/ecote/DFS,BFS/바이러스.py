N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
# print(lst)
cnt = 0 # 바이러스에 걸리게 되는 컴퓨터수
vistied = [False] * (N+1)
#dfs정의
def dfs(v):
    vistied[v] = True
    global cnt
    cnt += 1
    for j in  lst[v]:
        if not vistied[j]:
            dfs(j)
dfs(1)
# 1번컴퓨터를 제외해야 하니까 cnt -1
print(cnt-1)