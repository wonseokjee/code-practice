import sys
sys.stdin = open('연속한1의개수.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = 0
    cnt_max = 0
    for i in arr:
        if i:
            cnt+=1
            if cnt_max < cnt:
                cnt_max = cnt
        else:
            if cnt_max < cnt:
                cnt_max = cnt
            else:
                cnt = 0
    print(f'#{tc} {cnt_max}')
