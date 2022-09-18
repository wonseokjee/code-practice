T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = -1
    for i in range(N):
        if i**3 > N:
            break
        elif i**3 ==N:
            ans = i
        if N == 1:
            ans = 1
    print(f'#{tc} {ans}')

# 3
# 27
# 7777
# 64
