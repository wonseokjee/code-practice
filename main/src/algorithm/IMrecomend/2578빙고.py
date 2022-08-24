arr = [list(map(int, input().split())) for _ in range(5)]
# count = [list(map(int, input().split())) for _ in range(5)]
count = []

for _ in range(5):
    count += list(map(int, input().split()))
#가로 방향판
#세로 방향판
#좌상대각선 방향판
#우상대각선 방향판
for k in range(25):
    for i in range(5):
        for j in range(5):
            if count[k] == arr[i][j]:
                arr[i][j] = 0
    if arr[i][j] == arr[i][j]:#우하대각
        pass
    if i + j == 4: # 우상대각
        pass


