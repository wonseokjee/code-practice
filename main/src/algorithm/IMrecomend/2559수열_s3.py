# import sys
# n, k = map(int, input().split())
# arr = list(map(int, sys.stdin.readline().split()))
# cnt_max = -100*1000
# for i in range(n-k+1):
#     # cnt = 0
#     # for j in range(k):
#     #     cnt += arr[i+j]
#     cnt = sum(arr[i:i+k])
#     if cnt > cnt_max: cnt_max = cnt
# print(cnt_max)
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = -100 * 100000
test_sum = 0
for i in range(K):
    test_sum += num_list[i]

if test_sum > max_sum:
    max_sum = test_sum

for i in range(K, N):
    test_sum += num_list[i] - num_list[i-K]
    if test_sum > max_sum:
        max_sum = test_sum

print(max_sum)