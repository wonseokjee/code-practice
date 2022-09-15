def inorder(n):#중위순회
    if n <= N:
        inorder(n*2)
        result.append(lst[n])
        inorder(n * 2+ 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst=[]
    for i in range(N+1):
        lst.append(i)
    result = []
    inorder(1)
    cnt1 = 0 # 루트에 저장된 값
    cnt2 = 0 # N/2번 노드에 저장된 값.
    for j in range(len(result)):
        if 1 == result[j]:#루트에 저장된 값이 1이면
           cnt1 = j+1
        if (N//2) == result[j]:#루트에 저장된 값이 N/2이면
            cnt2 = j+1
    print(f'#{tc} {cnt1} {cnt2}')

