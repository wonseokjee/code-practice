# T = int(input())
# for tc in range(1, T+1):

N = int(input())
arr = [map(int, input().split()) for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0
cnt_max  = 0
square = []
for i in range(N):
    for j in range(N):
            if arr[i][j] == 1:
                cnt+=1
                square.append([i,j])
                x = i
                y = j
                while True:
                    for k in range(di):
                        ni = x + di[k]
                        nj = y + dj[k]
                        if [ni, nj] in square:
                            cnt_max = cnt
                            break
                        if arr[ni][nj] == 1:
                            cnt += 1
                            x, y = ni, nj
                            square.append([ni,nj])




