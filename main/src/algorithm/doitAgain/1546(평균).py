n = int(input())
arr = list(map(int, input().split()))
arr_max = max(arr)
arr_sum = sum(arr)
print((arr_sum/(n*arr_max))*100)