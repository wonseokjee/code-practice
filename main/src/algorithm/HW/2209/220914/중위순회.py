def inord(n):
    if n <= N:              # 완전이진트리이기 때문에 마지막 정점만 확인하고 없으면 패스.
        inord(n * 2)        # 왼쪽 서브트리의 루트로 이동
        ans.append(lst[n])
        inord(n * 2 + 1)    # 오른쪽 서브트리의 루트로 이동


# T = int(input())
T = 10
for test_case in range(1, T + 1):
    N = int(input())        # 정점개수
    lst = [0] * (N + 1)     # 완전이진트리
    for i in range(1, N + 1):
        tlst = input().split()
        lst[i] = tlst[1]
        # a, b, *c = input().split()
        # tree[int(a)] = b


ans = []
inord(1)
print(f'#{test_case} {"".join(ans)}')


