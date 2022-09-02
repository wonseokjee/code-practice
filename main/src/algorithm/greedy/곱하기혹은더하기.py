arr = list(map(int, input()))
print(arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] == 0:
        continue
    elif cnt == 0:
        cnt += arr[i]
    else:
        if cnt*arr[i] > cnt+arr[i]:
            cnt = cnt * arr[i]
        else:
            cnt += arr[i]
print(cnt)