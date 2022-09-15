def heap(n):
    if n*2+1<=N
        if lst[n] > lst[n*2]:
            lst[n], lst[n * 2] = lst[n * 2], lst[n]
        elif lst[n] > lst[n*2+1]:
            if lst[n] > lst[n * 2 + 1]:
                lst[n], lst[n * 2 + 1] = lst[n * 2 + 1], lst[n]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    for i in range(1,N+1):
        heap(i)
    print(lst)