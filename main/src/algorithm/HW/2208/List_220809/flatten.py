import sys
sys.stdin = open('flatten.txt', 'r')

T = 10
for tc in range(1 , T+1):
    dump_num = int(input())         #덤프 횟수
    arr = list(map(int, input().split()))
    num_max = 0                    #arr의 최대값의 배열
    num_min = 100-1      #arr의 최소값의 배열
    for i in range(dump_num):       #dump 횟수만큼 반복
        for j in range(len(arr)):
            if arr[j] >= arr[num_max]:         #최대값 찾기
                num_max = j
            if arr[j] <= arr[num_min]:         #최소값 찾기
                num_min = j
        if not num_max == num_min:
            arr[num_max] += -1
            arr[num_min] += 1

    print(f'#{tc} {arr[num_max]-arr[num_min]}')