T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_way = [list(map(int, input().split())) for _ in range(N)]
    p = int(input())
    c = list(int(input()) for _ in range(p))
    c_all = [0] * 5001
    for i in range(N):
        for j in range(bus_way[i][0], bus_way[i][1] + 1):
            c_all[j] += 1

    print(f'#{tc}', end=' ')
    for i in c:
        print(c_all[i], end=' ')
    print()
