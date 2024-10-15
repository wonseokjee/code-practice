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

