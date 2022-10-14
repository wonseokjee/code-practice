def search(v,w,x,y,z):
    for a in range(v,x):
        for b in range(w,y):
            area[z] += arr[a][b]

def sep(x,y):
    search(0,0,x,y,0)
    search(0,y,x,N,1)
    search(x,0,N,y,2)
    search(x,y,N,N,3)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 100000000000
    for a in range(1,N):
        for b in range(1,N):
            area = [0,0,0,0]
            sep(a,b)
            # print(area)
            minus = max(area)-min(area)
            if cnt > minus:
                cnt = minus
    print(f'#{tc} {cnt}')
