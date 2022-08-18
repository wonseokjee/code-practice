T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    num_min, min_idx = 11, 0
    num_max, max_idx = 0, 0
    for i in range(len(arr)):
        if arr[i]<num_min:
            num_min = arr[i]
            min_idx = i
        if arr[i] >= num_max:
            num_max = arr[i]
            max_idx = i
    result = max_idx - min_idx
    if result < 0:
        result = -(result)
    print(f'#{tc} {result}')