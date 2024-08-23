from collections import deque
tc = int(input())
for _ in range(tc):
    func = list(input())
    n = int(input())
    lst = input().strip("[]").split(",")
    #lst의 괄호를 빼주는 작업. lst에 '[]'만 있는 것을 if문으로 거르기
    # if len(lst) == 1 and len(lst[0]) == 2:
    #     lst = []
    # else:
    #     lst = list(lst)
    # print(func, lst)

    # D의 갯수를 세고 lst보다 많으면 바로 error 출력
    cnt_D = func.count('D')
    cnt_R = func.count('R')
    if cnt_D >= len(lst):
        print('error')
    else:
        # R이 홀수이면 flag = [1,0] 1이 pop 0이 popleft
        flag = [0,1]
        cnt = 0
        # R의 갯수가 홀수이면 reverse 짝수이면 순서대로
        if cnt_R % 2 == 1:
            lst.reverse()
            flag.reverse()
        lst = deque(lst)
        #flag를 만든다음 R이 나올때마다 맨앞, 맨뒤번갈아가게 D 나오면 R과 연관지어서 삭제
        for i in func:
            if i == 'R':
                cnt += 1
                if cnt == 2:
                    cnt = 0
            else:
                if flag[cnt] == 0:
                    lst.popleft()
                else:
                    lst.pop()
        ans = ','.join(list(lst))
        print(f'[{ans}]')

# 3
# RDD
# 3
# [2,1,2]
# DDR
# 2
# [1,2]
# D
# 3
# [1,2,3]

# 1
# R
# 1
# [12]
