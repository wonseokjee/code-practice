n,k = map(int,input().split())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)
dp = [0] + [10001 for _ in range(k)]
for num in lst:
    for i in range(num,k+1):
        dp[i] = min(dp[i], dp[i-num]+1)
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])