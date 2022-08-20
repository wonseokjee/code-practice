T = int(input())
for tc in range(1,T+1):
    station = [0]*1001
    station_max = 0
    stop_max = 0
    N = int(input())
    for n in range(N):
        num,s,e = map(int,input().split())
        stop = 0

        for i in range(s, e+1):
            if num == 1:
                station[i] += 1

            elif num ==2:
                if s % 2 ==0:
                    if i % 2 ==0:
                        station[i] += 1
                else:
                    if i % 2 ==1 or i ==1:
                        station[i] += 1

            else :
                if s % 2 ==0:
                    if i % 4 ==0:
                        station[i] += 1
                else:
                    if i % 3 == 0 and i % 10 != 0:
                        station[i] += 1
        if e > station_max: station_max = e
    for j in range(station_max+1):
        if station[j] > stop_max: stop_max = station[j]
print(f'#{tc} {stop_max}')
