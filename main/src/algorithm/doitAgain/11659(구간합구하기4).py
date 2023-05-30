import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0,0)
arr_sum = []
cnt = 0
for i in arr:
    arr_sum.append(i+cnt)
    cnt += i
# print(arr_sum)
for j in range(m):
    x, y = map(int, input().split())
    ans = arr_sum[y] - arr_sum[x-1]
    print(ans)



