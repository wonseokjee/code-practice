T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    # 2. 열마다 하나씩 들어가도록 조건 따지기
    def check(x,y,ins): #
        global cnt
        if ins == N:
            cnt += 1
        if x<N and y<N:
            # if visited[y] == False:
            #     visited[y] = True
            if correct(x,y):
                check(x+1,0, ins+1)
            else:
                check(x,y+1, ins)
                arr[x][y] = 0


    def correct(x,y): # 위 아래 옆 대각에 문제 없는지 확인
        for l in all:
            ni = x + l[0]
            nj = y + l[1]
            if 0<= ni <N and 0<= nj < N:
                if arr[ni][nj] == 1:
                    # visited[y] = False
                    return False
        else:
            arr[x][y] = 1
            return True


    # 1. 행,열 대각 범위 만들기
    all = []
    for a in range(N):
        all.append([a + 1,0]) ,all.append([0,a + 1]),all.append([0,-a - 1]),all.append([-a - 1,0]),
        all.append([a + 1, a + 1]),all.append([a + 1, -a - 1]),
        all.append([-a - 1, -a - 1]),all.append([-a - 1,a + 1])
    # print(all)

    for h in range(N):
        # visited = [False] * N # visited 초기화
        arr = [[0] * N for _ in range(N)] # 배열 초기화
        check(0,h,0)

    print(f'#{tc} {cnt}')