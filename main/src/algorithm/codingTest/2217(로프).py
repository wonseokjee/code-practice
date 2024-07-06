N = int(input())
lst = [list(input()) for _ in range(N)]
dic = {}
# print(lst)
for item in lst:
    item.reverse()
    for i in range(len(item)):
        # print(10**i,item[i])
        if dic.get(item[i]):
            dic[item[i]] += 10**i
        else:
            dic[item[i]] = 10**i
# print(dic)
# print(lst)
dic_sort = sorted(dic.items(), key=lambda x:x[1], reverse=True)
cnt = 9
for sort in dic_sort:
    dic[sort[0]] = cnt
    cnt -= 1
# print(dic)
ans = 0
for i in range(len(lst)):
    lst[i].reverse()
    ins = ''
    for j in range(len(lst[i])):
        lst[i][j] = dic[lst[i][j]]
        ins += str(lst[i][j])
    ans += int(ins)
# print(dic_sort)
# print(lst)
print(ans)