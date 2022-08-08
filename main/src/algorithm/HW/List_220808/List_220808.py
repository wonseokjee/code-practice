import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 가로길이
    arr = list(map(int, input().split()))
    cnt = 0
    #조망권 찾기
    for idx in range(N):
        try:
            if arr[idx] == max([arr[idx], arr[idx+1], arr[idx+2], arr[idx-1], arr[idx-2]]):
                # print(arr[idx])
                t = arr[idx] - max([arr[idx+1], arr[idx+2], arr[idx-1], arr[idx-2]])
                cnt += t
        except: pass

    print(f'#{tc} {cnt}')

    #max 안쓰고 해보기

