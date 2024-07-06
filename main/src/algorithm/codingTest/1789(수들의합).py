N = int(input())
ins = 0
cnt = 0
num = 1
while(N>ins):
    ins += num
    if ins>N:
        break
    num += 1
    cnt += 1
    # print(ins)
print(cnt)