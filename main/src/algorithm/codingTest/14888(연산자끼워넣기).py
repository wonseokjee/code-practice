from itertools import permutations
N = int(input())
lst = list(map(int,input().split()))
operator_num = list(map(int,input().split()))
operator_lst = []
for i in range(4):
    for _ in range(operator_num[i]):
        operator_lst.append(i)
per = list(permutations(operator_lst,N-1))
max_num = -100000000000000
min_num = 1000000000000000
def operator_convertor(x,y,z):
    if x == 0:
        return y+z
    elif x == 1:
        return y-z
    elif x == 2:
        return y*z
    else:
        if y < 0:
            return -(-y//z)
        else:
            return y // z

for k in per:
    ins = lst[0]
    for j in range(N-1):
        ins = operator_convertor(k[j],ins,lst[j+1])
    if ins > max_num:
        max_num = ins
    if ins < min_num:
        min_num = ins
print(max_num)
print(min_num)

# pypy....

