from collections import deque
n,k = map(int,input().split())
visited = [0]*100002

def bfs():
    queue = deque([])
    queue.append(n)
    while(queue):
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x-1,x+1, 2*x):
            if 0 <= i <= 100000:
                if not visited[i]:
                    visited[i] = visited[x]+1
                    queue.append(i)
bfs()
