# import sys
# sys.stdin = open('단순이진암호코드.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    # 1.암호코드 정의
    pw = {'0001101':'0','0011001':'1', '0010011':'2','0111101':'3', '0100011':'4','0110001':'5',
                  '0101111':'6','0111011':'7', '0110111':'8','0001011':'9'}

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 2. 배열에서 1이 있는 지확인 있으면 break
    num = '' # 유효한 배열의 첫번째 줄
    for i in range(N):
        if '1' in arr[i]:
            num = arr[i]
            break
    # print(num) #1있는 첫번째 배열 넣기

    # 3. 배열의 길이를 뒤에서 0이 없는 길이까지
    len_num = len(num)-1
    while num[len_num] == '0':
        len_num -= 1
    # print(len_num) #길이 확인

    # 4. 7의 배수로 나눈 나머지부터 배열을 시작해서 7의 배수마다 찍기.
    #    코드찾기
    result = []
    for k in range((len_num-6)%7, len_num, 7):
        if not num[k:k + 7] =='0000000':
            result.append(int(pw[num[k:k+7]]))
    # print(result) # 복호화 잘 되었는지 확인

    # 5. 8개 숫자가 조건에 맞는지 확인
    num = (result[0]+result[2]+result[4]+result[6])*3 +(result[1]+result[3]+result[5]+result[7])
    # print(num) #숫자 확인

    # 6. 조건에 맞으면 숫자 아니면 0 출력
    print(f'#{tc} {sum(result) if num%10==0 else 0}')