import sys
sys.stdin = open('의석이의세로로말해요.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    for i in range(5):
        for j in range(15):
            if len(arr[i]) <= 15:
                arr[i].append('')
    arr_zip = list(map(list, zip(*arr)))
    print(f'#{tc}',end=' ')
    for k in range(15):
        print(*arr_zip[k], sep='', end='')
    print()
