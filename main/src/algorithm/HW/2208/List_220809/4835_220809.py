T = int(input())
for tc in range(1,T+1):
    N, M = map(int, (input().split()))
    arr = list(map(int, input().split()))
    num_max = N * 1 # 최대값
    num_min = N * 10000 # 최소값
    # arr을 탐색 할 수. 처음부터 N-M+1 한 값까지
    for i in range(N-M+1):
        arr_sum = 0 #최대값 임시 저장
        # 구간의 갯수 M 만큼 찾아서 arr_sum에 저장.
        for j in range(i, i+M):
            arr_sum += arr[j]
        if arr_sum >= num_max: #max 값 찾기
            num_max = arr_sum
        if arr_sum < num_min: #min 값 찾기
            num_min = arr_sum
    print(f'#{tc} {num_max-num_min}')


