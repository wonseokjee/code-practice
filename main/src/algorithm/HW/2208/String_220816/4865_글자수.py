T = int(input())
for tc in range(1, T+1):
    str_1 = list(set(input()))
    str_2 = list(input())
    dict_str = {str_key: 0 for str_key in str_1}
    for i in dict_str:
        for j in str_2:
            if i == j:
                dict_str[i] += 1
    max = 0
    for k in dict_str.keys():
        if max < dict_str[k]:
            max = dict_str[k]
    print(f'#{tc} {max}')