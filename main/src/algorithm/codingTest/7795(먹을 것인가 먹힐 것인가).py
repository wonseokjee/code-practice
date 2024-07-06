T = int(input())
for tc in range(1, T+1):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    cnt = 0
    a_point = 0
    b_point = 0
    while(b_point < m):
        if a_point == n:
            break
        if a[a_point] > b[b_point]:
            cnt += m - b_point
            a_point += 1
        elif a[a_point] <= b[b_point]:
            b_point += 1
    print(cnt)
