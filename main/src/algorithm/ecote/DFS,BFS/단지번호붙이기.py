N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 1 # 전체 단지수 세기
ins = 0 # 단지내 주택수
num = [] # 단지별 주택수
di = [[0,1],[0,-1],[1,0],[-1,0]] # 방향판 우, 좌, 하, 상
# 1. dfs정의
def dfs(i,j):
    arr[i][j] = cnt # 단지 구분하기 2단지부터 시작
    global ins
    ins += 1 # 단지내 주택수
    for k in di: # 방향판 돌리기
        ni = i + k[0]
        nj = j + k[1]
        if 0<= ni < N and 0<= nj < N: #배열 이내이면
            if arr[ni][nj] == 1: # 값이 1이면 dfs돌리기
                dfs(ni, nj)

# 2. 배열에 dfs넣기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1 # 1과 구분 안되어서 2부터 시작하고 나중에 -1
            dfs(i,j)
            num.append(ins) # 단지내 주택수 값을 단지별 주택수에 넣기
            ins = 0 # 단지내 주택수 초기화
# print(arr) # 바뀐 배열
print(cnt - 1) # 전체단지수
result = sorted(num)
for i in result:
    print(i)



