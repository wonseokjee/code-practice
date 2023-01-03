import math

def prime_list(n):
    # 에라스토테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    lst = [True] * (n+1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if lst[i]:
            for j in range(i + i, n+1, i):
                lst[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n+1) if lst[i] == True]


m, n = map(int, input().split())
for i in prime_list(n):
    if i >= m:
        print(i)
