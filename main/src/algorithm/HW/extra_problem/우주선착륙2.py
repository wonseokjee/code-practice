import sys
sys.stdin = open('우주선착륙2.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    direct = [[-1,-1],[-1,0],[1,-1],[0,-1],[0,1],[-1,1],[1,0],[1,1]]
    len_dir = len(direct)
    cnt_landing = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(len_dir):

                ni = i + direct[k][0]
                nj = j + direct[k][1]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1
            if cnt >= 4:
               cnt_landing +=1
    print(f'#{tc} {cnt_landing}')