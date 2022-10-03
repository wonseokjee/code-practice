import sys
input = sys.stdin.readline
def binary_search(arr, target, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        if i>mid:
            cnt += i-mid
    if cnt == target:
        return mid
    elif target < cnt:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)


n,m = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(arr,m,0,max(arr)))
