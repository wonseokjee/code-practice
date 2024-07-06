N = int(input())
case = 0
while(N != 0):
    case += 1
    dic = {}
    arr = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(N):
        x, y = map(str, input().split())
        if not dic.get(x):
            dic[x] = len(dic)+1
        if not dic.get(y):
            dic[y] = len(dic)+1
        arr[dic[x]].append(dic[y])
    visited = [False]*(N+1)
    def dfs(x,k):
        global cnt
        visited[x] = True
        for i in arr[x]:
            if i == k:
                cnt += 1
            if not visited[i]:
                dfs(i,k)
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i,i)
        # print(visited)
    print(case, cnt)
    N = int(input())