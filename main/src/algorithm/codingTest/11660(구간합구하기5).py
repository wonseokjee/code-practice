import sys
input = sys.stdin.readline
n,m = map(int,input().split())
array = [[0]*(n+1)]
for _ in range(n):
    k = list(map(int,input().split()))
    k.insert(0,0)
    array.append(k)
dp =[[0]*(n+1) for _ in range(n+1)]
dp[0][0] = array[0][0]
# print(dp)
# print(array)
for k in range(1,n+1):
    dp[k][1] = array[k][1] + dp[k-1][1]
    dp[1][k] = array[1][k] + dp[1][k-1]
# print(dp)
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + sum(array[i][:j+1])
# print(dp)
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(ans)
