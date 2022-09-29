T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
    spray = []
    cnt = 0

    for l in range(M): # spray 생성
        for m in dir:
            di = m[0] + l
            dj = m[1] + l
            spray.append([di,dj])
    for i in range(N):
        for j in range(N):
            num = arr[i][j]
            for k in spray:
                ni = i + k[0]
                nj = j + k[1]
                if 0<=ni<N and 0<=nj<N:
                    num += arr[ni][nj]
            if num > cnt:
                cnt = num
    print(num)