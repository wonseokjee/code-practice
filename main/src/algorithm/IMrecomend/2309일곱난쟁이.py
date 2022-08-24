arr = [int(input()) for _ in range(9)]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

selection_sort(arr)
arr_sum = 0
for i in range(9):
    arr_sum += arr[i]

arr_del = []
for j in range(8):
    for k in range(j+1 , 9):
        if (arr[j] + arr[k] + 100) == arr_sum:
            arr_del.append(j)
            arr_del.append(k)
arr.pop(arr_del[0])
arr.pop(arr_del[1]-1)
for a in arr:
    print(a, end='\n')

