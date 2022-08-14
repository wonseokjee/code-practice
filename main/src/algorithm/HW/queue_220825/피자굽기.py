# import sys
# sys.stdin = open('그래프경로.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr = []                        #피자 리스트
    for idx, value in enumerate(list(map(int, input().split()))):
        arr.append((idx+1,value))   #enumerate사용해서 인덱스를 추가한 피자 리스트 생성
    arr_fire = []                   #화덕생성
    for i in range(n):              #화덕개수만큼 피자 넣기
        a = arr.pop(0)
        arr_fire.append(a)
    while len(arr_fire)>1:          #화덕에 피자가 1개 남을때까지
        a_round = list(arr_fire.pop(0))#화덕의 첫번째 피자
        a_round[1] = a_round[1]//2  #치즈개수 //2 연산
        if a_round[1] ==0:          #치즈 개수 0이면
            if len(arr) >= 1:       #arr의 인덱스 에러 방지(하나도 없을 경우 제외)
                a = list(arr.pop(0))#새 피자를 화덕에 넣기
                arr_fire.append(a)
        else:
            arr_fire.append(a_round)#치즈 남았으면 다시 넣어놓기
    print(f'#{tc} {arr_fire[0][0]}')
