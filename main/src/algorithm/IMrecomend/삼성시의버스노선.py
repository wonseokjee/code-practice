T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_stop = [0]*5001
    check_stop = []
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a,b+1):
            bus_stop[i] += 1
    P = int(input())
    for _ in range(P):
        c = int(input())
        check_stop.append(bus_stop[c])

    print(f'#{tc}', end=' ')
    print(*check_stop)
