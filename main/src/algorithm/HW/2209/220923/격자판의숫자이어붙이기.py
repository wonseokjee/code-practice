def selct(x,y,cnt,n):
    if n <7:
        cnt += str(arr[x][y])
        for k in dir:
            ni = x+ k[0]
            nj = y + k[1]
            if 0<=ni<4  and 0<=nj<4:
                selct(ni,nj,cnt,n+1)
    else:
        num.add(cnt)

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    num = set()
    for i in range(4):
        for j in range(4):
            selct(i,j,'',0)
    # print(num)
    print(f'#{tc} {len(num)}')

