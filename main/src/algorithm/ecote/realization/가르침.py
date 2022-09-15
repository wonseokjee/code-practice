N, K = map(int, input().split())
cnt = 5
result = 0
basic = ['a','n','t','i','c']
for i in range(N):
    word = input()



def pick(a):
    global cnt
    global result
    cnt_ins = 0
    word_ins = []
    for j in word:
        if j in basic:
            continue
        else:
            cnt_ins += 1
            word_ins.append(j)
    if cnt_ins + cnt <= K:
        result += 1
        for k in word_ins:
            basic.append(k)
        cnt += cnt_ins

print(result)
