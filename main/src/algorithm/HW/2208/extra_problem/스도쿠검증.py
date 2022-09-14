import sys
sys.stdin = open('스도쿠검증.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    #가로 세로 검증
    cnt = 0
    for i in range(9):
        cnt_row = 0
        cnt_column = 0
        for j in range(9):
            cnt_row += arr[i][j]
            cnt_column += arr[j][i]
        if cnt_row==45 and cnt_column==45:
            cnt += 0
        else:
            cnt += 1
    #3X3검증
    arr_3 = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for x, y in arr_3:
        cnt_3 = 0
        for k in range(3):
            for l in range(3):
                ni = x+k
                nj = y+l
                cnt_3 += arr[ni][nj]
        if not cnt_3 == 45:
            cnt += 1
    print(f'#{tc} {0 if cnt>0 else 1}')