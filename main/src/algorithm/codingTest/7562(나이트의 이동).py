from collections import deque
T = int(input())
knight = [[-1,-2],[-2,-1],[-1,2],[-2,1],[1,-2],[2,-1],[1,2],[2,1]]
for tc in range(T):
    I = int(input())
    start = list(map(int,input().split()))+[0]
    end = list(map(int, input().split()))
    graph = [([False] * I) for _ in range(I)]
    queue = deque([start])
    ans = 0
    graph[start[0]][start[1]] = True
    while(queue):
        x,y,cnt = queue.popleft()
        if x == end[0] and y == end[1]:
            ans = cnt
            break
        for kni in knight:
            a = kni[0]+x
            b = kni[1]+y
            if 0<=a<I and 0<=b<I:
                if not graph[a][b]:
                    graph[a][b] = True
                    queue.append([a,b,cnt+1])
                    # print(a,b,cnt+1)
    print(ans)

