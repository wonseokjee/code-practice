import sys
sys.stdin = open('달란트2.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    m, n = map(int, input().split())
    cnt = 0
    if m % n == 0:
        l = m//n
        cnt += l**n
    else:
        l = m // n  #l=3
        k = m - (l*n)
        big = (l+1)**k
        rest = l**(n-k)
        cnt = big*rest
    print(f'#{tc} {cnt}')