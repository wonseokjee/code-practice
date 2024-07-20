N = int(input())
word = []
res = 0

for _ in range(N):
    W = input()
    word.append(W)

word.sort(key=len)
# print(word)

for i in range(N):
    cword = word[i]
    flag = False

    for j in range(i + 1, N):
        if cword == word[j][0:len(cword)]:
            flag = True
            break
    if not flag:
        res += 1

print(res)