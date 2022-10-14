T = int(input())
for tc in range(1,T+1):
    n,m,k = map(int,input().split())
    arr = sorted(list(map(int, input().split())))
    cnt = 0
    ins = []
    ans = ''
    while arr:
        if cnt % m == 0 and cnt > 0:
            for _ in range(k):
                ins.append('bread')
        if arr[0] == cnt:
            arr.pop(0)
            if not ins:
                ans = 'Impossible'
                break
            else:
                ins.pop(0)
        cnt += 1
        ans = 'Possible'
    print(f'#{tc} {ans}')


