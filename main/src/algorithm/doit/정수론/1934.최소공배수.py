#python 최고

import math
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    #시간초과
    # n = 1
    # k = 0
    # if a > b:
    #     a, b = b, a
    # while(True):
    #     if (b*n) % a == 0:
    #         print(b*n)
    #         break
    #     n += 1
    print(math.lcm(a,b))
