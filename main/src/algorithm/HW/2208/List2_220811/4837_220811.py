T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = list(range(1,13))               #1,12까지의 부분집합 생성
    cnt = 0                             #해당하는 부분 집합 세는 변수
    for i in range(1<<12):              #모든 부분집합을 탐색
        subset_sum = 0                  #부분집합 하나의 합
        subset_len = 0                  #부분집합 하나의 길이
        for j in range(12):
            if i & (1<<j):              #i의 j번째 비트가 1이라면 부분집합에 포함.
                subset_sum += A[j]      #하나의 합에 리스트A의 j번째 값을 추가
                subset_len += 1         #하나의 길이에 추가
        if subset_len == N and subset_sum == K: #최종 조건 비교
            cnt+= 1
    print(f'#{tc} {cnt}')
