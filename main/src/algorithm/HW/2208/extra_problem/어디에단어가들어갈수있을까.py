import sys
sys.stdin = open('어디에단어가들어갈수있을까.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n,k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt_k = 0
    for i in range(n):
        cnt_length = 0
        cnt_height = 0
        for j in range(n):
           #가로방향
            if arr[i][j]:
                cnt_length += 1
            else:
                if cnt_length == k:
                    cnt_k += 1
                cnt_length = 0
            #세로방향
            if arr[j][i]:
                cnt_height += 1
            else:
                if cnt_height == k:
                    cnt_k += 1
                cnt_height = 0
        if cnt_height == k:
            cnt_k += 1
        if cnt_length == k:
            cnt_k += 1
    print(f'#{tc} {cnt_k}')