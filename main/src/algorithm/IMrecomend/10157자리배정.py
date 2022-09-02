C,R = map(int,input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
di = [1, 0,-1,0]
dj = [0,1, 0, -1]
i,j,dr =0,0,0
if K > C*R:
    cnt = 0
    print(cnt)
else:
    for x in range(1,K+1):
        arr[i][j] = x
        cnt = [j + 1, i + 1]
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dr = (dr + 1) % 4
            i, j = i + di[dr], j + dj[dr]
    print(*cnt)