arr = [[0 for i in range(15)] for j in range(15)]
# print(arr)
for i in range(15):
    for j in range(15):
        if j == 0:
            arr[i][j] = 1
        if i == 0:
            arr[i][j] = j

        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
# print(arr)
# print(arr[1][3])
T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])
