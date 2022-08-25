T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    cnt_max= 0
    cnt_num = 0
    cnt_min = 0
    while len(arr) <= cnt_min:
        for i in range(cnt_min,len(arr)):
            if cnt < arr[i]:
                cnt = arr[i]
                cnt_num = i+1
        for j in range(cnt_min,cnt_num):
            cnt_max += arr[cnt_num-1] - arr[j]
        cnt_min = cnt_num
        cnt = 0
    print(f'#{tc} {cnt_max}')



