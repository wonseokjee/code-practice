# import sys
# sys.stdin = open('그래프경로.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(m):
        arr_pop = arr.pop(0)
        arr.append(arr_pop)
    print(f'#{tc} {arr[0]}')