def f(x, cnt, arr):
    global num
    if cnt > num: # 가지치기 1
        return
    if x == N - 1 and num>cnt:
        num = cnt
    else:
        bat = arr[x]
        for i in range(bat,0,-1): # 가지치기 2. 역순으로
            if x+i < N:
                f(x+i, cnt+1,arr)

T = int(input())
for tc in range(1,T+1):
    N, *ins = map(int, input().split())
    arr = []
    for a in ins:
        arr.append(a)
    arr.append(0)
    num = 10000
    f(0,0,arr)
    print(f'#{tc} {num-1}')


