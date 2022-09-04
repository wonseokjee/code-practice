N = int(input())
arr = list(map(int, input().split()))
len_arr = len(arr)
sum_list = []
for i in range(1 << len_arr): #비트연산 부분집합
    sum = 0
    for j in range(len_arr):
        if i &(1<<j):
            sum += arr[j]
    sum_list.append(sum)
# print(sum_list)
max_list = max(sum_list)
for k in range(1, max_list): #부분집합의 최대값까지 for문
    if k not in sum_list: #부분집합에 없으면 출력 후 break
        print(k)
        break