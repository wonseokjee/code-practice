N = int(input())
arr = list(map(int, input().split()))
std = int(input())
def swap(arr,a):
    if arr[a] == 1:
        arr[a] = 0
    else:
        arr[a] = 1

for _ in range(std):
    gen, switch = map(int, input().split())
    #1. 남 녀 구분
    #2. 남자일때 자기가 받은 수의 배수의 상태를 바꿈.
    #3. 여자일때 받은수를 중심으로 대칭이면서 가장 많은 스위치를 포함하는 구간 찾기
    if gen == 1 :
        for i in range(1, len(arr)+1):
            if i % switch == 0 :
                swap(arr, i-1)
    else:
        arr_switch = switch - 1
        length = len(arr) - switch
        swap(arr, arr_switch)
        for j in range(1, length+1):
            if arr[arr_switch-j] == arr[arr_switch+j]:
                if 0<=arr_switch-j and arr_switch+j < len(arr):
                    swap(arr, arr_switch-j)
                    swap(arr, arr_switch+j)
            else:
                break
# print(arr)
for k in range(len(arr)):
    if (k+1) % 20 == 0:
        print(arr[k], end='\n')
    else:
        print(arr[k], end=' ')






# 21
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 2
# 1 3
# 2 4



