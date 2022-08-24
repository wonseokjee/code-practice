arr = [[0]*101 for _ in range(101)]
N= int(input())
cnt = 0
for black in range(N):
    x, y = map(int, input().split())
    for i in range(x, 10+x):
        for j in range(y, 10+y):
            arr[i][j] += 1
for k in range(100):
    for l in range(100):
        if arr[k][l] != 0:
            cnt += 1
print(cnt)