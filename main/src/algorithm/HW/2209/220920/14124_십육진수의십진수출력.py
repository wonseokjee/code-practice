T = int(input())
for tc in range(1,T+1):
    N = map(str, input())
    # 1. 십육진수 -> 이진수 딕셔너리 정의
    dic = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000'
        ,'9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    # 2.이진수로 변환하기
    ins = ''
    for i in N:
        ins += dic[i] # N에 들어온 값을 딕셔너리의 키로 찾아 밸류값 뽑아내기
    # print(ins) # 이진수로 잘 변환되었는지 확인
    # 3. 이진수를 십진수로 변환하기
    result = []
    ch = 0
    for j in range(len(ins)):
        ch = ch*2 + int(ins[j])
        if j%7==6:
            result.append(ch)
            ch = 0
    print(f'#{tc}',*result,ch)