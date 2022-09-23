T = int(input())
for tc in range(1,T+1):
    N, top = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []
    sm = sum(arr)
    for i in range(1<<N):
        cnt = 0
        for j in range(N):
            if i & (1<<j):
               cnt += arr[j]
        if sm - cnt >= top:
            lst.append(sm-cnt)
    print(f'#{tc} {min(lst)-top}')