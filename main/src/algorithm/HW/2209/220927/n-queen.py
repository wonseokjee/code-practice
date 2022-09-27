T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [False]*N
    arr = [[0]*N for _ in range(N)]
    cnt = 0
    # 2. dfs 정의
    def dfs(x,y):
        global cnt
        if visited[x] == False and arr[x][y] == 0 :
            visited[x] = True
            arr[x][y] = 1
            for k in all:
                ni = x + k[0]
                nj = y + k[1]
                if 0 <= ni < N and 0 <= nj < N :
                    if arr[ni][nj] == 1:
                        arr[x][y] = 0
                        visited[x] = False
                        break
            if visited[x] == True:
                for e in range(N): # 다음 열의 행들의 하나하나에 들어가기
                    ei = x + 1
                    ej = e
                    if 0 <= ei <N:
                        dfs(ei, ej) # dfs
                        visited[ei] = False
            if False not in visited:
                cnt += 1
            return


    # 1. 행,열 대각 범위 만들기
    all = []
    for a in range(N):
        all.append([a + 1,0]), all.append([- a - 1, 0]),all.append([0,a + 1]),all.append([0,-a - 1])
        all.append([a + 1, a + 1]), all.append([- a - 1, - a - 1]),
        all.append([- a - 1, a + 1]), all.append([a + 1, -a - 1])
    # print(all)
    for h in range(N):
        dfs(0,h)
        visited = [False] * N # visited 초기화
        arr = [[0] * N for _ in range(N)] # 배열 초기화
    print(f'#{tc} {cnt}')