import math


# 에라스토테네스의 체
def is_prime(n):
    lst = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if lst[i]:
            for j in range(i + i, n, i):
                lst[j] = False
    return [i for i in range(2, n + 1) if lst[i] == True]


ans = 0
a, b = map(int, input().split())
for i in is_prime(b):
    k = i
    l = 2
    while (math.pow(i,l) <= b):
        if (math.pow(i,l)) >= a:
            ans += 1
        l += 1

print(ans)
