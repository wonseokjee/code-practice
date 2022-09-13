S = input()
cnt = len(S)
for i in range(1, len(S)//2+1):# 단위가 절반 넘어가면 의미 없음. 2단위도 안됨.
    compare = '' #i와 같은 길이 비교
    save = '' #중간 저장
    num = 0 #중간 저장 갯수
    result = '' #최종
    for j in range(len(S)):
        compare += S[j] #문자 하나씩 compare에 저장.
        if i == len(compare): #i 길이와 같을때
            if save == '':#처음 중간저장할때
                save += compare #비교값을 중간저장값에 넣고
                num += 1 # num 올림
            elif save == compare: #비교값이 중간저장값과 같으면
                num += 1 #num 올리고
                if j == len(S)-1: #마지막 j까지 왔을때
                    if num == 1: # num=1 이면 앞에 정수 없이 알파벳만 추가
                        result += save #최종값에 중간값 추가
                    else:
                        result += str(num) + save #최종값에 알파벳앞에 정수도 추가
                    save = ''#save초기화 시킴
                    num= 1 #나중에 한번 더 더해주는데 여기는 잘끝났으므로 num1로 여기때문에 계속 틀림
            elif save != compare:#비교값과 중간값이 다르다면
                if num == 1:
                    result += save
                else:
                    result += str(num)+save
                num = 1# 숫자 초기화
                save = compare#비교값을 중간값으로
            compare = '' #if문 끝나서 비교값 초기화
    if j == len(S) - 1: #여기 추가 안해서 계속 틀림 마지막 save값의 num을 고려해야했는데 num이 그냥 1이라 가정해서
        if num == 1:
            result += save
        else:
            result += str(num) + save
    # print(result+compare)
    if cnt > len(result+compare): #최소값 찾기
        cnt = len(result+compare)
print(cnt)

# abcabcabcdabcfabcabcabczabcabcdddabc