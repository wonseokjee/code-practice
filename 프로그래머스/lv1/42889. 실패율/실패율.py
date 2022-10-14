def solution(N, stages):
    ins = []
    result = []
    len_sta = len(stages)
    for i in range(1,N+1):
        x = stages.count(i)
        if len_sta >0:
            y = x / len_sta
            len_sta -= x
        else:
            y =0
        ins.append([i,y])
    ins.sort(key=lambda k: (-k[1],k[0]))
    for j in ins:
        result.append(j[0])
    return result