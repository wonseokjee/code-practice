import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] ==target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start,mid-1)
    else:
        return binary_search(arr, target, mid+1 ,end)




n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()
m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    print(binary_search(arr_n,i,0,n-1))



# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
