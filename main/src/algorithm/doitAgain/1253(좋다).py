import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
len_arr = len(arr)
print(arr)
for i in range(2,len_arr):
    start = 0
    end = i-1
    while(start<end):
        if arr[start]+arr[end] == arr[i]:
            cnt += 1
            break
        elif arr[start]+arr[end] > arr[i]:
            end -= 1
        else:
            start += 1

print(cnt)

# 3
# 0 0 0
# 0 0 1
# -5 -3 -2
# 10
# 1 3 5 6 8 10 13 15 18 21