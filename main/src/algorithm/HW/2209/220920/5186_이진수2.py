T = int(input())
for tc in range(1,T+1):
    n = input()
    N = float(n)
    ans = ''
    i = -1
    while N != 0:
        k = 2**i
        if N - k>= 0:
            N -= k
            ans += '1'
        else:
            ans += '0'
        i -= 1
        if i < -13:
            ans = 'overflow'
            break
    print(f'#{tc} {ans}')