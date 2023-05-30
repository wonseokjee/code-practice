n = int(input())
arr = []
for _ in range(n):
    k = int(input())
    arr.append(k)
arr_sort = sorted(arr)
for i in arr_sort:
    print(i)