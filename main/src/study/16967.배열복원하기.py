h,w,x,y = list(map(int, input().split()))
arr = [list(map(int, input().split()))for _ in range(h+x)]
for i in range(h):
    for j in range(w):
        arr[i+x][j+y] -= arr[i][j]
        print(arr[i][j], end=' ')
    print('')
