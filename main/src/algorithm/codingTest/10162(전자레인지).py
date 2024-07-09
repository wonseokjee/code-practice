N = int(input())
K_300 = 0
K_60 = 0
K_10 = 0
K = N
while K > 0:
    if K >= 300:
        ans = K // 300
        les = K % 300
        K_300 = ans
        K = les
    if K >= 60:
        ans = K // 60
        les = K % 60
        K_60 = ans
        K = les
    if K >= 10:
        ans = K // 10
        K_10 = ans
        les = K % 10
        K = les
    if K > 0:
        K_10 = -1
        K = 0
if K_10 == -1:
    print(-1)
else:
    print(K_300, K_60, K_10)