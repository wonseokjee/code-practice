n,k = map(int,input().split())
lst = [[0,0]]
for _ in range(k):
    i, t = map(int,input().split())
    lst.append([i,t])
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        value = lst[i][0]
        time = lst[i][1]
        if time > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time]+value)
print(dp[k][n])