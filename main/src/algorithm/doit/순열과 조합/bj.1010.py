def combination(n, m):
    num = 1
    for i in range(m - n + 1, m + 1):
        num *= i
    for j in range(1, n+1):
        num //= j
    return num

t = int(input())
for tc in range(t):
    n,m = map(int, input().split())
    print(combination(n,m))



