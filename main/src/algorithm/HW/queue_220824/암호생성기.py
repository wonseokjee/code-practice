import sys
sys.stdin = open('암호생성기.txt','r')


for tc in range(10):
    T = int(input())
    arr = list(map(int, input().split()))
    k = 0
    while k == 0:
        for i in range(1,6):
            a = arr.pop(0) - i
            if a <= 0:
                arr.append(0)
                k += 1
                break
            arr.append(a)
    print(f'#{T}', *arr[:])