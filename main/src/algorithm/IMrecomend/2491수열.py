N = int(input())
arr = list(map(int, input().split()))
cnt_max = 1
cnt_up = 1
cnt_down = 1
for i in range(1,len(arr)):
    if arr[i] >= arr[i-1]:
        cnt_up += 1
        if cnt_up > cnt_max: cnt_max = cnt_up
    else:
        cnt_up = 1
    if arr[i] <= arr[i-1]:
        cnt_down += 1
        if cnt_down > cnt_max: cnt_max = cnt_down
    else:
        cnt_down = 1

print(cnt_max)