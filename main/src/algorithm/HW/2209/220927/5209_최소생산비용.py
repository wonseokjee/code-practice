def f(x,cnt):
    global num
    if cnt >= num:
        return
    if x == N and num > cnt:
        num = cnt
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            f(x+1,cnt+arr[x][i])
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    num = 15000
    f(0,0)
    print(f'#{tc} {num}')