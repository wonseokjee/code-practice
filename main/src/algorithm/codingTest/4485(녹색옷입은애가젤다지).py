# from collections import deque
import heapq
cnt = 0
N = 130
INF = 10**7

def bfs():
    #queue로 하니까 tc2번 arr[1][4]가 이상하게 계산되어서
    #heapq로 하니까 잘됨.
    # queue = deque([[arr[0][0],0,0]])
    queue = [[arr[0][0], 0, 0]]
    while(queue):
        cnt, a, b = heapq.heappop(queue)
        if a == N-1 and b == N-1:
            break
        for dx,dy in [0,1],[0,-1],[1,0],[-1,0]:
            x = a + dx
            y = b + dy
            if 0 <= x < N and 0 <= y < N:
                if graph[x][y] > arr[x][y] + cnt:
                    graph[x][y] = arr[x][y] + cnt
                    # queue.append([graph[x][y], x, y])
                    heapq.heappush(queue,[graph[x][y], x, y])



while(N != 0):
    N = int(input())
    cnt += 1
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[INF]*N for _ in range(N)]
    graph[0][0] = arr[0][0]
    ans = INF
    bfs()
    # print(graph)
    print(f'Problem {cnt}: {graph[N-1][N-1]}')


