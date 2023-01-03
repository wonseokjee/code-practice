# -로 구분해서 나머지 다 더하고 -인것 빼주기
value = list(map(str, input().split('-')))
# print(value)
cnt = 0
for i in range(len(value)):
    plus = sum(list(map(int, value[i].split('+'))))
    if i == 0:
        cnt += plus
    else:
        cnt += -plus
print(cnt)
