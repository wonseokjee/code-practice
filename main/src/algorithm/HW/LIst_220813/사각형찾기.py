# T = int(input())
# for tc in range(1, T+1):

N = int(input())
arr = [map(int, input().split()) for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0
square = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt+=1
            square.append([i,j])
            for k in range(di):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[ni][nj] ==1:


