n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
# print(graph)
for i in range(n-2,-1,-1):
    # print(i)
    for j in range(i,-1,-1):
        if graph[i+1][j] > graph[i+1][j+1]:
            graph[i][j] += graph[i+1][j]
        else:
            graph[i][j] += graph[i + 1][j+ 1]
print(graph[0][0])

