import sys
sys.stdin = open('string_4864.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    str_1 = input()
    str_2 = input()

    result = 0
    i = 0
    for j in range(len(str_2)):
        cnt = 1
        if str_1[i] == str_2[j]:
            for k in range(1, len(str_1)):
                try:
                    if str_1[i+k] == str_2[j+k]:
                        cnt += 1
                except:
                    pass
        if cnt == len(str_1):
            result += 1


    print(f'#{tc} {result}')

