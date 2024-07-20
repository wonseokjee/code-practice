n,k = map(int,input().split())
things = [[0,0]]
for _ in range(n):
    weight, value = map(int,input().split())
    things.append([weight,value])
knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        weight = things[i][0]
        value = things[i][1]
        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight] + value)
print(knapsack[n][k])

