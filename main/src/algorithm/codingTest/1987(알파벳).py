import sys
# sys.setrecursionlimit(20000)
input = sys.stdin.readline
R,C = map(int,input().split())
graph = [input()for _ in range(R)]
visited = [False for _ in range(26)]
# print(graph)
cnt = 0
d = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(x,y,depth):
    global cnt
    visited[ord(graph[x][y])-65] = True
    depth += 1
    cnt = max(cnt,depth)
    for i in range(4):
        a, b = d[i][0], d[i][1]
        if 0 <= a+x <R and 0 <= b+y <C:
            if not visited[ord(graph[a+x][b+y])-65]:
                dfs(a+x,b+y,depth)
                visited[ord(graph[a+x][b+y])-65] = False
dfs(0,0,0)
print(cnt)
