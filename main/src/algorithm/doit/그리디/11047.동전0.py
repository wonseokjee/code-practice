N, K = map(int, input().split())
value = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 0

for i in value:
    if K // i != 0:
        cnt += K // i
        K = K % i
print(cnt)
