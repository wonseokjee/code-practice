from collections import deque
f,s,g,u,d = map(int, input().split())
#f: 총 층수 s: 지금 있는 곳, g:도착할 층, u:위로 올라 갈 수 있는 층 d:아래로 내려갈 수 있는 층 수
visited = [True]+[False]*f
# print(visited)
ans = 0
def bfs(start, end, n):
    global ans
    queue = deque([[start,n]])
    while(queue):
        lst = queue.popleft()
        x = lst[0]
        n = lst[1]
        # print(x,n)
        if not visited[x]:
            # print(x,n)
            visited[x] = True
            if x == end:
                ans = n
                return
            y = x+u
            z = x-d
            if f >= y:
                if not visited[y]:
                    # print(f'y:{y}')
                    queue.append([y,n+1])
            if 0 < z:
                if not visited[z]:
                    # print(f'z:{z}')
                    queue.append([z,n+1])

if s==g:
    print(0)
else:
    bfs(s,g,0)
    if ans == 0:
        print("use the stairs")
    else:
        print(ans)
