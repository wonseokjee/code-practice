import sys
sys.stdin = open('Ladder.txt', 'r')

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for s in range(100): #[99][s]인 정답찾아서 거꾸로 올라가기
        di = [0, 0, -1]
        dj = [1, -1, 0] # 방향 = [ 우 , 좌, 상 ] 상이 마지막 이어야 사다리 가능.
        if arr[99][s] == 2:
            i = 99 # 마지막 열 부터 시작
            j = s # 정답인 행부터 시작
            while i > 0: # i가 첫번째 열에 도착할 때까지
                for k in range(3):
                    ni = i + di[k] #
                    nj = j + dj[k]
                    if 0<=ni<100 and 0<=nj<100: #범위 이내에서만 동작할때
                        if arr[ni][nj] == 1: # 1을 찾으면
                            arr[ni][nj] = 0 #기존을 0으로 바꾸고, 흔적을 지우고고
                            i = ni
                            j = nj
            print(f'#{tc} {j}')



