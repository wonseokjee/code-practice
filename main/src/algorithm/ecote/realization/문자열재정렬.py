# K1KAA5CB7

S = input()
num = 0
str_alp = ''
for i in S:
    if i.isdigit():
       num += int(i)
    else:
        str_alp += i

st_alp = sorted(str_alp)
print(''.join(st_alp), end='')
print(str(num))

