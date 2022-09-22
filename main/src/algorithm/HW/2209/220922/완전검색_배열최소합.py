T = int(input())

def dfs(x,cnt):
    global num
    if cnt >= num:
        return

    if x == N:
        if cnt <= num:
            num = cnt

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, cnt+arr[x][i])
            visited[i] = False


for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    num = 10**3
    dfs(0,0)
    print(f'#{tc} {num}')

# 1
# 3
# 2 1 2
# 5 8 5
# 7 2 2