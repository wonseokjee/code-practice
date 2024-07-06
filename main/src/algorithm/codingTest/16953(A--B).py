from collections import deque
start, end = map(int, input().split())

def bfs(start,end):
    queue = deque([[start,0]])
    while queue:
        [num,cnt] = queue.popleft()
        if num == end:
            # print(num,cnt)
            return cnt
        elif num > end:
            continue
        else:
            # print(num)
            queue.append([num*2,cnt+1])
            queue.append([int(str(num)+'1'), cnt + 1])
    return -2
print(bfs(start,end)+1)