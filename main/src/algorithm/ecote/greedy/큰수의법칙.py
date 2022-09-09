N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
run, rest = M // (K+1), M % (K+1)
cnt = 0
for i in range(run):
    cnt += arr[-1]*K
    cnt += arr[-2]
cnt += arr[-1]*rest
print(cnt)
# 5 8 3
# 2 4 5 4 6