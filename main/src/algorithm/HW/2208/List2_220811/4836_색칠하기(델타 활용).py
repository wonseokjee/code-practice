T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for sqr in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        cnt = 0
        for i in range(10):
            for j in range(10):
                if color == 1:
                    if x1<= i <=x2 and y1 <= j <= y2:
                        arr[i][j] += 1
                if color == 2:
                    if x1<= i <=x2 and y1 <= j <= y2:
                        arr[i][j] += 2
                if arr[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')

