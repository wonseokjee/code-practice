n = int(input())
cards = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))
dic = {}

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in num:
    if j in dic:
        print(dic[j],end= ' ')
    else:
        print(0, end=' ')