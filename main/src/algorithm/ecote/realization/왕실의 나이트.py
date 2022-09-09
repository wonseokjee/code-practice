N = input()

width = ['a','b','c','d','e','f','g','h']#가로칸
ni_x=[2,2,-2,-2,1,-1,1,-1]#방향판 8가지 경우 모두
ni_y=[1,-1,1,-1,2,2,-2,-2]

cnt = 0
for i in range(8):
    if width[i] == N[0]: #N[0]만 거르기
       for j in range(1,9):
           if j == int(N[1]):# N[1]만 거르기
                for k in range(len(ni_y)): #방향판 돌리기
                    dx = i + ni_x[k]
                    dy = j + ni_y[k]
                    if 0<=dx < 8 and 1<=dy<9: #범위 안에서 찾기
                        cnt+=1
print(cnt)




