def f(a,b,c):
    global cnt
    if cnt < c:
        return
    if a == 0 and b == N:
        if cnt > c:
            cnt = c
            return
    for j in mid:
        if j[0] == b:
            if j[1] == N:
                if cnt > c +j[2]:
                    cnt = c +j[2]
                    return
            else:
                f(i[0],i[1],i[2]+c)



T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    start = []
    mid = []
    cnt = 10**10
    for _ in range(E):
        a,b,c =map(int, input().split())
        if a ==0:
            start.append([a,b,c])
        else:
            mid.append([a,b,c])
    # print(start)
    # print(mid)
    for i in start:
        f(i[0],i[1],i[2])
    print(f'#{tc} {cnt}')