import itertools
n,k = map(int, input().split())

arr = [0] * n
combi = list(itertools.combinations(arr, k))
result = len(combi) % 10007
print(result)

# 메모리 초과