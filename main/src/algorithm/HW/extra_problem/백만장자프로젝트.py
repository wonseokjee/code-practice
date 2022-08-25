# T = int(input())
# for tc in range(1,T+1):
n = int(input())
arr = [(idx+1,value) for idx, value in enumerate(map(int, input().split()))]
cnt = 0
cnt_max= 0
cnt_num = 0
while len(arr) > 0:
    for i in range(len(arr)):
        if cnt < arr[i][1]:
            cnt = arr[i][1]
            cnt_num = arr[i][0]
    for j in range(len(arr[:arr[cnt_num-1][0]])):
        cnt_max += arr[cnt_num-1][1] - arr[j][1]
    for k in range(cnt_num):
        arr.pop(0)
        cnt = 0
print(cnt_max)



