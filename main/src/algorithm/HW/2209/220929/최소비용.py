from collections import deque


def bfs(pay,x,y):
    queue = deque([])
    queue.append([x,y])
    while queue:
        i,j = queue.popleft()
        print(i,j)
        for k in dir:
            ni = i + k[0]
            nj = j + k[1]
            if 0<=ni<N and 0<=nj<N :
                y = 0
                if arr[ni][nj]-arr[i][j] > 0: # 배열의 높이차가 0보다 클때 y를 지정
                    y = arr[ni][nj]-arr[i][j]
                if pay[ni][nj] > pay[i][j]+y+1:
                    pay[ni][nj] = pay[i][j]+y+1
                    queue.append([ni,nj])

# def dfs(x,y,num): #런타임에러......
#     global cnt
#     if cnt < num:
#         return
#     if x==N-1 and y==N-1:
#         if cnt > num:
#             cnt = num
#         return
#     for k in dir:
#         ni = x + k[0]
#         nj = y + k[1]
#         if 0<=ni<N and 0<=nj<N and pay[ni][nj]==0:
#             pay[ni][nj] = 1
#             dfs(ni,nj,num+(arr[ni][nj]-arr[x][y])+1)
#             pay[ni][nj] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N) ]
    cnt = 1000*N*N*N
    pay = [[cnt]*N for _ in range(N)]
    pay[0][0] = 0
    dir = [[1,0],[-1,0],[0,1],[0,-1]]

    bfs(pay,0,0)
    # dfs(0,0,0)
    print(f'#{tc} {pay[N-1][N-1]}')