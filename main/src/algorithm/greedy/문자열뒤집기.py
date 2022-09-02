N = list(map(int, input()))

cnt_0 = 0
cnt_1 = 0
k = 0
for i in range(len(N)):
    if i ==1:
        cnt_1 += 1
    else:
        cnt_0 += 1
if cnt_1> cnt_0:
    k = 1
cnt = []
result = 0
for j in range(len(N)):
    if j ==k:
        cnt.append(k)
    else:
        if cnt != []:
          result += 1
          cnt = []