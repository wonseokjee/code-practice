import math

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


n = int(input())
prime_one = [2, 3, 5, 7]


def dfs(v):
    if len(str(v)) == n:  # 만약, v가 n개수까지 도달했다면 해당 값 print
        print(v)
    else:
        for j in range(1, 10):  # 도달하지 못했다면 1-10까지 돌며, 소수 판별 후, 재귀 돌리기
            if is_prime_number(v * 10 + j):
                dfs(v * 10 + j)


for k in prime_one:
    dfs(k)
