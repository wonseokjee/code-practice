def inorder(n): #완전이진트리
    if n <= N:
        inorder(n*2)
        inorder(n*2 + 1)
        if n*2<= N:
            if n*2+1<=N:
                lst[n] = lst[n * 2] + lst[n * 2 + 1]
                return
            lst[n] = lst[n * 2]

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)
    for i in range(M):
        x, y = map(int,input().split())
        lst[x] = y

    inorder(1)
    print(f'#{tc} {lst[L]}')
