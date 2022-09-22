def dfs(x,y,cnt):
    global num
    cnt += arr[x][y]
    if cnt >= num:
        return
    elif x == N-1 and y == N-1 and cnt < num:
        num = cnt
        return

    else:
        if y+1 <N:
            dfs(x,y+1,cnt)
        if x+1 < N:
            dfs(x+1,y,cnt)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = 10**6
    dfs(0,0,0)
    print(f'#{tc} {num}')