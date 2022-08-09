T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    bus_stop = [0]*N
    for i in arr:
        bus_stop[i] = 1

    cnt = 0
    start = 0
    end = K
    for i in range(M):
        for j in range(end, start - 1, -1):
            if end >= N:
                break

            if bus_stop[j] == 1:
                start = j
                end = j + K
                cnt += 1
                break

    if end >= N:
        print(f"#{tc} {cnt}")
    else:
        print(f"#{tc} 0")





