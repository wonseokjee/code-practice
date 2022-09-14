def binary_search(page,x):             #두개를 비교해야 해서 함수 선언
    start = 1
    end = page
    cnt = 0
    while start <= end:
        c = (start + end) // 2
        if c == x:
            return cnt
        elif c < x:
            start = c
            cnt += 1
        elif c > x:
            end = c
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    page, A, B = map(int, input().split())

    A_result = binary_search(page, A)
    B_result = binary_search(page, B)

    if A_result > B_result:
        result = 'B'
    elif A_result < B_result:
        result = 'A'
    else:
        result = 0
    print(f'#{tc} {result}')
