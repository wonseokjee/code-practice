T = int(input())
for tc in range(1,T+1):
    D,A,B,F = map(int, input().split())
    time = D / (A + B)
    time_live = time * F
    print(f'#{tc} {time_live:.6f}')