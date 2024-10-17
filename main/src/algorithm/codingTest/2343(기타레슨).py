n,m = map(int,input().split())
lst = list(map(int,input().split()))
start = max(lst)
end = sum(lst)
mid = (start+end) // 2
ans = 10000000001
#cnt가 m보다 작으면 start-mid
#크면 mid-end
while(start<=end):
    # print(start, mid, end)
    ins = 0
    cnt = 1
    for i in range(len(lst)):
        if ins + lst[i] > mid:
            cnt += 1
            ins = 0
        ins += lst[i]
    if cnt <= m and ans>mid:
        ans = mid

    if cnt <= m:
        end = mid-1
    else:
        start = mid+1
    mid = (start+end) // 2
print(ans)