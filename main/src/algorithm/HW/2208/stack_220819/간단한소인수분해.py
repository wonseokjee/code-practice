import sys
sys.stdin = open('간단한소인수분해.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = [0]*12 # 2^a, 3^b, 5^c, 7^d, 11^e
    number = [2,3,5,7,11]
    while N != 1:
        for i in number:
            if N % i == 0:
                N = N // i
                N_list[i-1] += 1
                break

    print(f'#{tc}', end=' ')
    for j in number:
        print(N_list[j-1], end=' ')
    print()