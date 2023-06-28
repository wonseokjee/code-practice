import sys
from collections import deque
input = sys.stdin.readline
s, p = map(int, input().split())
arr = list(map(str, input()))
arr.pop()
a,c,g,t = map(int, input().split())
queue = deque()
a_1, c_1, g_1, t_1 = 0,0,0,0
cnt = 0
def select(x):
    global a_1
    global c_1
    global g_1
    global t_1
    if x == 'A':
        a_1 += 1
    elif x == 'C':
        c_1 += 1
    elif x == 'G':
        g_1 += 1
    elif x == 'T':
        t_1 += 1

def select_minus(x):
    global a_1
    global c_1
    global g_1
    global t_1
    if x == 'A':
        a_1 -= 1
    elif x == 'C':
        c_1 -= 1
    elif x == 'G':
        g_1 -= 1
    elif x == 'T':
        t_1 -= 1

while(len(arr)>0):
    if len(queue) < p:
        x = arr.pop()
        select(x)
        queue.append(x)
        if(len(queue)==p and a_1>=a and c_1>=c and g_1>=g and t_1>=t):
            cnt += 1
    else:
        x = arr.pop()
        select(x)
        queue.append(x)
        y = queue.popleft()
        select_minus(y)
        if(a_1>=a and c_1>=c and g_1>=g and t_1>=t):
            cnt += 1
print(cnt)

