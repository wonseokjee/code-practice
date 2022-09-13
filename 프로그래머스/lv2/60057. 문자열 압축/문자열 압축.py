def solution(S):
    cnt = len(S)
    for i in range(1, len(S)//2+1):
        compare = ''
        save = ''
        num = 0
        result = ''
        for j in range(len(S)):
            compare += S[j]
            if i == len(compare):
                if save == '':
                    save += compare
                    num += 1
                elif save == compare:
                    num += 1
                    if j == len(S)-1:
                        if num == 1:
                            result += save
                        else:
                            result += str(num) + save
                        save = ''
                        num= 1
                elif save != compare:
                    if num == 1:
                        result += save
                    else:
                        result += str(num)+save
                    num = 1
                    save = compare
                compare = ''
        if j == len(S) - 1:
            if num == 1:
                result += save
            else:
                result += str(num) + save
        # print(result+compare)
        if cnt > len(result+compare):
            cnt = len(result+compare)
    return cnt