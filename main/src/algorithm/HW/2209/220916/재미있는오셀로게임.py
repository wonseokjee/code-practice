T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]


    for i in range(M):
        x,y,color = map(int, input().split())
