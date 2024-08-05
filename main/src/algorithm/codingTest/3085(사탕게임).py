import copy
N = int(input())
graph = [list(input()) for _ in range(N)]
ans = 0
#해당 좌표가 속한 행,열만 갯수 계산(연속)
def cal(x,y,graph):
    dic_x = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    dic_y = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    cnt = 0
    for i in graph[x]:
        dic_x[i] += 1
    cnt = max(cnt, max(dic_x.values()))
    for j in range(N):
        dic_y[graph[j][y]] += 1
    cnt = max(cnt, max(dic_y.values()))
    print(x,y,cnt)
    return cnt

#처음에 행, 열 별로 같은 것 계산
for i in range(N):
    x = cal(i,0,graph)
    y = cal(0,i,graph)
    ans = max(ans, x, y)
print(ans)
#오른쪽, 아래 만 교환해서 판단하기



