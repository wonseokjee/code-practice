import sys
sys.stdin = open('GNS.txt', 'r')

T= int(input())
for test in range(1, T+1):
    tc, N = map(str, input().split())
    arr = list(map(str, input().split()))
    arr_num = ["ZRO","ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for i in arr_num:
        for j in arr:
            if i == j:
                result.append(i)
                arr.remove(j)
    print(f'{tc}\n')
    print(' '.join(result))


