def f(x, cnt):
    global num
    if x == N and cnt > num:
        num = cnt
        return
    # if cnt > num:
    #     num = cnt
    #     return
    for i in range(N):
        if visited[i]:
            visited[i] = True
            f(x+1,cnt*arr[x][i])
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    num = 1
    for k in range(N):
        num = num *arr[k][0]
    f(0,1)
    print(num)