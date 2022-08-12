import  sys
sys.stdin = open('색칠하기2.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for sqr in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        cnt = 0
        di = [0 , 0, 1, -1]
        dj = [1, -1, 0, 0]                              #회전판
        for i in range(10):                             # 열 생성
            for j in range(10):                         # 행 생성
                if color == 1:                          # 색이 1이라면
                    if x1 <= i <= x2 and y1 <= j <= y2: # 해당 범위 판별
                        arr[i][j] += 1                  # 값을 1로 변경
                if color == 2:
                    if x1 <= i <= x2 and y1 <= j <= y2:
                        arr[i][j] += 2                  # 값을 2로 변경
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 1 or arr[i][j] == 2:    #배열의 값이 1 또는 2라면
                    del_same = 4                        #한 블럭의 테두리 값 4
                    for d in range(len(di)):
                        ni = i + di[d]                  #방향판 돌리기
                        nj = j + dj[d]
                        if 0<= ni <10 and 0<= nj <10:   #arr값 넘어가는 값 제외
                            if arr[i][j] == arr[ni][nj]:#4방향중 같은 값이 있으면 겹치는 테두리라고 판단
                                del_same += -1          # 테두리 값에서 -1
                    cnt += del_same                     #전체 테두리 값에 포함
    print(f'#{tc} {cnt}')










