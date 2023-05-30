from itertools import permutations
n,k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    arr[i] = arr[i]-k
combi = list(permutations(arr,n))
for j in range(len(combi)):
    num = 0
    for k in range(n):
        num += combi[j][k]
        if num < 0:
            num = 0
            break
    if num > 0:
        ans += 1
print(ans)


