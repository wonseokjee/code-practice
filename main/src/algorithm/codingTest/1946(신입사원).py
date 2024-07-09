import sys
input = sys.stdin.readline
T = int(input())

for _ in range(1,T+1):
    tc = int(input())
    lst = []
    for _ in range(tc):
        paper,interview = map(int,input().split())
        lst.append([paper,interview])
    lst.sort()
    cnt = 0
    high_score = lst[0][1]
    for a,b in lst:
        if b <= high_score:
            cnt += 1
            high_score = b
    print(cnt)











# 1
# 6
# 6 4
# 4 1
# 5 2
# 1 6
# 2 3
# 3 5
