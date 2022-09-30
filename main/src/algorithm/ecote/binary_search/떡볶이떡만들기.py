def binary_search(arr,target,start,end):
    if start > end:
        return '에라이'
    mid = (start+end)//2
    sm = 0
    for i in arr:
        if i > mid:
            sm += i-mid
    # print(sm)
    # print(mid)
    if sm == target:
        return mid
    elif sm > target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr,target,start,mid-1)
n,m = map(int, input().split())
arr = list(map(int,input().split()))


result = binary_search(arr,m,0,max(arr))
print(f'정답은 {result}')
# 4 6
# 19 15 10 17

# 15