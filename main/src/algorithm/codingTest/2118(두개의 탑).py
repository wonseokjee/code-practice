import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr_sum = [0 for _ in range(n+1)]
arr_cnt = 0
for i in range(n):
    arr_cnt += arr[i]
    arr_sum[i+1] = arr_cnt
print(arr_sum)


