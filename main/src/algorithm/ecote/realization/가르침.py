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
cnt= 1
ans = []
for j in range(len(result)):
    if j == len(result)-1:
        if result_sort[j][0] == result_sort[j - 1][0]:
            result_sort[j][1] = cnt
        ans.append([len(result_sort[j][0]),result_sort[j][1]])
    elif result_sort[j][0] == result_sort[j+1][0]:
        cnt += 1
    else:
        result_sort[j][1] = cnt
        cnt = 1
        ans.append([len(result_sort[j][0]),result_sort[j][1]])
print(ans)
#비트연산자로 전체 구한다음. ans[][0]을 한계까지 더한다음 ans[][1]비교 가장 큰 값을 답으로 뽑아냄.


