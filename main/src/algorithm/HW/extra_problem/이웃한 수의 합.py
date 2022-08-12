T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_sum = -2000000000
    min_sum = 2000000000
    for i in range(N-1):
        cnt = arr[i] + arr[i+1]
        if cnt > max_sum:
            max_sum = cnt
        if cnt < min_sum:
            min_sum = cnt
    print(f'#{tc} {max_sum} {min_sum}')
