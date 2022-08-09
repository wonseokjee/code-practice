T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    list_max = arr[0]
    list_min = arr[0]
    for num in arr:
        if num >= list_max:
            list_max = num
        if num < list_min:
            list_min = num
    print(f'#{tc} {list_max-list_min}')
