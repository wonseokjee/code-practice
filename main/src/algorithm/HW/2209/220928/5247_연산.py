from collections import deque

def cal_bfs(x):
    global num
    cnt = 0
    queue = deque([])
    queue.append([x,cnt])
    while queue:
        a = queue.popleft()
        cnt = a[1]
        lst = [1, -1, a[0], -10]
        for i in lst:
            y = a[0] + i
            if y == M:
                num = cnt
                return
            queue.append([y,cnt+1])


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    num = 0
    cal_bfs(N)
    print(f'#{tc} {num+1}')