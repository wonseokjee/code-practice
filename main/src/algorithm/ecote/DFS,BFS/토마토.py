from collections import deque
import sys
input = sys.stdin.readline

M,N,H = map(int, input().split())

# 1. 3차원 배열
arr = [[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]

# 2. distance 3차원 배열
# 배열을 0부터 시작하면 모든 칸이 1(익은토마토)일 때 min함수쓰면 익지못하는 상황과 구분 안됨. 그래서 -1로 시작
distance = [[[-1]*M for _ in range(N)]for _ in range(H)]

# 3. 방향판(6방향)
dir = [[0,1,0], [0,-1,0],[1,0,0],[-1,0,0],[0,0,1],[0,0,-1]]

# 4. for 문으로 풀어보기(bfs는 모르겠음..)
queue = deque([])

for k in range(H):  # 5. 맨 처음 1(익은 토마토) 찾아서 queue와 distance에 넣기
    for i in range(N):
        for j in range(M):
                if arr[k][i][j] == 1:
                    queue.append([k,i,j])
                    arr[k][i][j] = 1
                    distance[k][i][j] = 0
                elif arr[k][i][j] == -1:
                    distance[k][i][j] = -2
# print(distance)   # distance에 잘들어갔는지 확인
while queue:        # 6. 큐가 빌때 까지
    # print(queue)  # queue에 올바른 값이(list인지 숫자 자체인지 헷갈릴수) 들어갔는지 확인
    z, x, y = queue.popleft() # 7. 큐에서 꺼내기
    # print(x,y,z)
    for d in dir:   # 8. 꺼내서 6방향 돌리기
        ni = x + d[0]
        nj = y + d[1]
        nz = z + d[2]
        if 0<= ni <N and 0<=nj<M and 0<=nz<H:
            if arr[nz][ni][nj] == 0: # 방문하지 않은 곳이면
                arr[nz][ni][nj] = 1 # 1로 처리하고
                queue.append([nz,ni,nj]) # 큐에 집어넣기
                distance[nz][ni][nj] = distance[z][x][y] + 1 #같은 수준의 값들은 같은 숫자로 표시
# print(distance) #distance에 최소일수 잘 들어갔는지 확인
cnt = 0
for e in distance:  # 9. distance에 -1있으면(토마토가 익지 못하는 상황)출력.
                    # 아니면 최대값 찾아서 출력
    for f in e:
        if -1 in f:
            cnt = -1
            break # break 문은 가장 가까운 for문만 빠져나와서
        if cnt < max(f):
            cnt = max(f)
    if cnt == -1: #여기서 최종적으로 빠져나가기 위해 한번더 break
        break
print(cnt)