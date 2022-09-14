T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split(' '))
    cnt = 0
    idx = 0
    while idx < len(A):             # idx가 len(A)안에서 동작하도록
        if B == A[idx:idx+len(B)]:  # A[idx]부터 시작해서 B길이만큼의 문자열과 B가 같다면
            idx += len(B)-1         # B길이에서 -1뺀값(밑에서 더해줌. 중복 방지)을 더한다. B길이만큼 idx 점프
        idx += 1                    # 모든 경우 idx +1 이동
        cnt+=1                      # b와 같지 않은 경우와 같은 경우 수를 세었으니 +1
    print(f'#{tc} {cnt}')

