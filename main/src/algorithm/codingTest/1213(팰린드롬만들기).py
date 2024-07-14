## 일단 한번 돌면서 알파벳 몇개 있는지 파악
##홀수개가 2개이상아면 아님.
# 일ㄷ단 짝수개 반으로 나눠서 더한다음 sort 하고
# 홀수개 더하고
# sort하고 reverse 한것을 더함.
lst = list(input())
dic = {}
sep_num = ''
half = ''
ans = ''
for alp in lst:
    if alp in dic:
        dic[alp] += 1
    else:
        dic[alp] = 1
for key in dic:
    # print(key, dic[key])
    if dic[key] % 2 > 0:
        sep_num += key
    half += key * (dic[key]//2)
# print(half)
if len(sep_num) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''.join(list(sorted(half)))
    half_reverse = ''.join(list(sorted(half,reverse=True)))
    ans = half + sep_num + half_reverse
    print(ans)