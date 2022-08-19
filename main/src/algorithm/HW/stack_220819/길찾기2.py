visited = []
def dfs(v): #재귀

    visited[v]=1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


adjList = []
def dfs2(v):
    if v ==99:
        return 1
    else:
        visited[v] = 1
        for w in adjList[v]:
            if visited[w] == 0:
                if dfs2(w):
                    return 1
for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    ch1 = [0]*100   #from인덱스 to 원소
    ch2 = [0]*100
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1] #a,b를 두개씩 읽는 것.
        adjList[a].append(b)

