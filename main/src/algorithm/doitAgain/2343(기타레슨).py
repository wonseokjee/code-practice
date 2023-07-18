import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [[0] for _ in range(n)]
arr_cnt = 0
for i in range(n):
    arr_cnt += arr[i]
    arr_sum[i] = arr_cnt

