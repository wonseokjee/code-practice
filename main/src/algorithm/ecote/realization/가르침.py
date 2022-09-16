from itertools import combinations

N, K = map(int, input().split())
basic = ['a','n','t','i','c']
result = []
for i in range(N):
    word = input()
    # word_cut = word[4:-4]
    word_else= []
    for c in word:
        if c in basic:
            continue
        elif c in word_else:
            continue
        else:
            word_else.append(c)
    result.append([word_else,1])
result_sort = sorted(result)

print(result)
print(result_sort)
cnt= -1
ans = []
for j in range(len(result)):
    if j == len(result)-1:
        result_sort[j][1] = cnt
        ans.append([len(result_sort[j][0]),result_sort[j][1]])
    elif result_sort[j][0] == result_sort[j+1][0]:
        cnt += -1
    else:
        result_sort[j][1] = cnt
        cnt = -1
        ans.append([len(result_sort[j][0]),result_sort[j][1]])
print(result_sort)
print(ans)
len_fin = 0
subsets = [[]]
subset=[[]]
for num in ans:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
        subset[y][0] += num[0]
        subset[y][1] += num[1]
print(subsets)
print(subset)


