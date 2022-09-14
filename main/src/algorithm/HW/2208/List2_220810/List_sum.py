import sys
sys.stdin = open('List_sum.txt', 'r')

T = 10
for Test_case in range(1, 10+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_j = max_i =max_ii = max_100i = 0
    sum_ii = sum_100i = 0
    for i in range(100):
        sum_i =  sum_j = 0
        for j in range(100):
            sum_j += arr[i][j]      #행의 합
            if max_j <= sum_j:
                max_j = sum_j
        # print(max_j)
            sum_i += arr[j][i]      #열의 합
            if max_i <= sum_i:
                max_i = sum_i
        sum_ii += arr[i][i]
        if max_ii <= sum_ii:
            max_ii = sum_ii
        sum_100i += arr[i][99-i]
        if max_100i <= sum_100i:
            max_100i = sum_100i

        if max_i < max_j:
            max_i = max_j
        if max_i < max_ii:
            max_i = max_ii
        if max_i < max_100i:
            max_i = max_100i

    print(f'#{tc} {max_i}')