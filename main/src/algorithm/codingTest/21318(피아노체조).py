import sys
input = sys.stdin.readline
n = int(input())
chart = list(map(int, input().split()))
chart_b = [0] * n
q = int(input())
cnt = 0
for i in range(1,n):
    if chart[i] - chart[i-1] >= 0:
        cnt += 1
        chart_b[i] = cnt
    else:
        chart_b[i] = cnt
print(chart_b)
for _ in range(q):
    x,y = map(int, input().split())
    ans = (y-x) - (chart_b[y-1]-chart_b[x-1])
    print(ans)