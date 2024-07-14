a,b = list(map(list,input().split()))
# print(a,b)
ans = []
def check (lst):
    ins = []
    for i in lst:
        if i == '5' or i == '6':
            if len(ins) == 0:
                ins.append('5')
                ins.append('6')
            else:
                ins_lst = []
                for k in ins:
                    ins_lst.append(k + '5')
                    ins_lst.append(k + '6')
                ins = ins_lst
        else:
            if len(ins) == 0:
                ins.append(i)
            else:
                ins_lst = []
                for k in ins:
                    ins_lst.append(k + i)
                ins = ins_lst
    return ins
a_lst = check(a)
b_lst = check(b)
# print(a_lst,b_lst)
for i in a_lst:
    for j in b_lst:
        ans.append(int(i)+int(j))
print(min(ans),max(ans))
