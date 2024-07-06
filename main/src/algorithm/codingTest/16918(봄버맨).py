r,c,n = map(int, input().split())
arr = [list(map(str, input())) for _ in range(r)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr_3 = [['O' for _ in range(c)] for _ in range(r)]
arr_mid = [['O' for _ in range(c)] for _ in range(r)]
arr_1 = [['O' for _ in range(c)] for _ in range(r)]

def boom(arr, arr_change):
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                arr_change[i][j] = '.'
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c:
                        arr_change[x][y] = '.'
boom(arr, arr_3)
boom(arr_3,arr_1)

def pp(arr):
    for i in range(r):
        line = "".join(arr[i])
        print(line)

if n%4 == 3:
    pp(arr_3)
elif n==1:
    pp(arr)
elif n%4==1 :
    pp(arr_1)
else:
    pp(arr_mid)


# 3 3 5
# OO.
# OOO
# OOO
#이 반례를 보면 n=1, n%4==1, n%4==3, n%2==0인 경우 4가지로 나뉜다.
#그래서 3일때 arr를 가지고 arr_3을 만들고
#5일때 arr_3을 가지고 arr_1을 만든다.
#깊은 복사해서 쓰는게 시간이 조금 더 걸린다.
