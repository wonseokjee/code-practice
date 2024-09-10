from collections import deque
# N극은 0, s극은 1
# 맞닫는 부분은 2,6
# 1번 6 - 2번 2, 2번 6 - 3번 2, 3번 6 4번 2
wheel = []
for _ in range(4):
    one_wheel = list(input())
    queue = deque(one_wheel)
    wheel.append(queue)
K = int(input())
# 첫번째는 톱니바퀴번호 두번째는 방향이 1인경우 시계방향 -1인경우 반시계방향
lst = [list(map(int,input().split())) for _ in range(K)]
#회전하는 것은 가장 나중일
def rolling_wheel(num, dir):
    # 시계방향으로 회전
    if dir == '1':
        wheel[num-1].rotate(1)
    # 반시계방향으로 회전
    else:
        wheel[num-1].rotate(-1)

visited = [False, False, False, False]
def bfs_wheel(x, y):
    queue = deque([[x,y]])
    while(queue):
        num, dir = queue.popleft()
        visited[num-1] = True
        for d_num in [1,-1]:
            next_num = num+d_num
            if 0<next_num<=4 and visited[next_num-1] ==False:
                if next_num > num and wheel[num-1][6] == wheel[next_num][2]:
                    queue.append([next_num,dir*-1])
                if next_num < num and wheel[num-1][2] == wheel[next_num-1][6]:
                    queue.append([next_num, dir * -1])



        # rolling_wheel(num, dir)
for num,dir in lst:
    bfs_wheel(num,dir)
