from collections import deque
n,m = map(int, input().split())
arr = []
coin = []
#첫번째 동전만 방문했는지 판단(두번째 동전은 방향이 같게 움직이니까 동시에 떨어지거나 벽이면 어차피 못움직이는 걸로 판단하면 됨.)
visited_0 = [[False]*m for _ in range(n)]
visited_1 = [[False]*m for _ in range(n)]
for _ in range(n):
    lst = list(input())
    arr.append(lst)
    #동전 위치 파악하기
    if 'o' in lst:
        for i in range(len(lst)):
            if lst[i] == 'o':
                coin.append([len(arr)-1, i])
#방향판
dir = [(0,1),(0,-1),(1,0),(-1,0)]
# print(coin)
ans = 100000000000
#bfs
def bfs(coin):
    global ans
    queue = deque([coin,0])
    # print(queue)
    while queue:
        coin_sep = queue.popleft()
        # print(coin_sep)
        cnt = int(queue.popleft())
        visited_0[coin_sep[0][0]][coin_sep[0][1]] = True
        visited_1[coin_sep[1][0]][coin_sep[1][1]] = True
        if cnt > 10:
            ans = -1
            return
        for x,y in dir:
            dx_0 = coin_sep[0][0] + x
            dy_0 = coin_sep[0][1] + y
            dx_1 = coin_sep[1][0] + x
            dy_1 = coin_sep[1][1] + y
            # print(dx_0,dy_0,dx_1,dy_1)
            #첫번째 동전이 나가고 두번째 동전이 안에 있는 경우
            if ((dx_0<0 or dx_0>n) or (dy_0<0 or dy_0>=m)) and (0<=dx_1<n and 0<=dy_1<m):
                # print(f'cnt======{cnt+1}')
                if ans > cnt+1:
                    ans = cnt+1
                    return
            #두번째 동전이 나가고 첫번째 동전이 안에 있는 경우
            if ((dx_1<0 or dx_1>n) or (dy_1<0 or dy_1>=m)) and (0<=dx_0<n and 0<=dy_0<m):
                # print(f'cnt======{cnt+1}')
                if ans > cnt+1:
                    ans = cnt+1
                    return
            #둘중 하나라도 나가 있으면 out  or 둘다 범위 안에
            if (0<=dx_0<n and 0<=dy_0<m) and (0<=dx_1<n and 0<=dy_1<m):
                # print(dx_0, dy_0, dx_1, dy_1,111111111111111)
                if not (arr[dx_0][dy_0] == '#' and arr[dx_1][dy_1] == '#'):
                    # print(dx_0, dy_0, dx_1, dy_1, 22222222222222)
                    if arr[dx_0][dy_0] == '#':
                        dx_0 = coin_sep[0][0]
                        dy_0 = coin_sep[0][1]
                    elif arr[dx_1][dy_1] == '#':
                        dx_1 = coin_sep[1][0]
                        dy_1 = coin_sep[1][1]
                    # print(dx_0, dy_0, dx_1, dy_1, 333333333333333333)
                    if not (dx_0 == dx_1 and dy_0 == dy_1):
                        queue.append([[dx_0,dy_0],[dx_1,dy_1]])
                        queue.append(cnt+1)

bfs(coin)
if ans == 100000000000:
    ans = -1
print(ans)
