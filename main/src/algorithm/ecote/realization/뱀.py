n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
L = int(input())
turn = [list(map(str, input().split())) for _ in range(L)]
dx =[1, 0, -1, 0]#처음에 무조건 오른쪽으로 시작 그래서 i = 3
dy =[0,-1, 0, 1] #오른쪽이면(D)dx[0]부터 왼쪽으면 dx[2]
snake = [[1,1]] #처음 칸에 뱀이 들어있다고 가정. 큐처럼 사용
arr = [[0]*(n+1) for _ in range(n+1)] #1,1 부터 시작이라 한줄씩 더 늘림
i = 3
ni, nj = 1,1 #1,1부터 시작
cnt = 0
while(True):
    if cnt == 0: #처음 시작일때 빈 arr에 1을 넣어주기 위함.
        arr[ni][nj] = 1
    cnt += 1
    ni = ni + dx[i]
    nj = nj + dy[i]
    if 1 <= ni<n and 1 <= nj < n: #칸 밖으로 벗어날때 끝
        if arr[ni][nj] != 0: # 1과 부딪힐때 끝
            break
    else:
        break
    arr[ni][nj] = 1 # 배열에 뱀 표시
    snake.append([ni,nj]) #뱀 길이 및 큐처럼 쓰기 위함.
    if [ni,nj] in apple: #사과자리를 통과하면 pop안하고 그대로 길이 유지
        continue
    else:
        cut = snake.pop(0) #길이 줄이고 꼬리칸을 0으로
        arr[cut[0]][cut[1]] = 0
    if turn == []: #turn 리스트가 비어서 indexerror났음. 방지용
        continue
    elif cnt == int(turn[0][0]): #초와 회전초가 같으면
        if turn[0][1] == 'D': #오른쪽일때
            i += 1 #방향판 우회전
            if i == 4:# i가 밖으로 벗어나면 다시 0으로
                i = 0
        elif turn[0][1] =='L':
            i -= 1
            if i == -1:
                i = 3
        turn.pop(0) #다 쓴 turn 삭제
print(cnt)


#testcase
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L