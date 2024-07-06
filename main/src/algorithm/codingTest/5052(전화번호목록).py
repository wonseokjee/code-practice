import sys
def input():
    return sys.stdin.readline().rstrip('\n')
T = int(input())
for tc in range(1,T+1):
    ans = 'YES'
    n = int(input())
    dic = {}
    number_list = [input() for i in range(n)]
    # print(number_list)
    for list in number_list:
        dic[list] = 1
    for number in number_list:
        sep_num = ''
        for sep in number:
            sep_num += sep
            if sep_num in dic and sep_num != number:
                ans = 'NO'
    print(ans)