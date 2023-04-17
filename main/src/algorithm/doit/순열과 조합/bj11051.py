N, K = map(int, input().split())
ans = 1
for i in range(N-K+1, N+1):
    ans *= i
for i in range(1, K+1):
    ans //= i
print(ans%10007)