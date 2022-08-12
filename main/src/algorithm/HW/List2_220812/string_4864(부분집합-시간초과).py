import sys
sys.stdin = open('string_4864.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    str_1 = input()
    str_2 = input()
    check = 0
    for i in range(1, 1 << len(str_2)):
        s = []
        for j in range(len(str_2)):
            if i & (1 << j):
                s += str_2[j]
        subset = ''.join(s)
        if len(subset) <= len(str_1):
            if str_1 == subset:
                check += 1
        if check == 1:
            break
    print(f'#{tc} {check}')
