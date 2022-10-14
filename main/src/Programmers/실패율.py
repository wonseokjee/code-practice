N = 5
stages = [2,1,2,6,2,4,3,3]
ins = []
result = []
len_sta = len(stages)
for i in range(1,N+1):
    x = stages.count(i)
    if len_sta >0: # len_sta가 이미 0이라면 나눗셈을 했을때 분모가 0이라 런타임 에러가 난다.
        y = x / len_sta
        len_sta -= x
    else:
        y =0
    ins.append([i,y]) # 번호와 나눗셈값을 동시 저장
# print(ins)
ins.sort(key=lambda k: (-k[1],k[0])) # 나눗셈 값으로 내림차순 저장, 겹치면 번호값으로 오름차순
print(ins)
for j in ins:
    result.append(j[0])
print(result)