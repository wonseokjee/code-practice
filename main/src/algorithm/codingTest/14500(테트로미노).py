import itertools
sero = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
garo = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]
combi_sero = list(itertools.combinations(sero,2))
combi_garo = list(itertools.combinations(garo,2))
#한줄로 4칸짜리 테트로 가로형 세로형
tetro_line_garo = [[0,0],[0,1],[0,2],[0,3]]
tetro_line_sero = [[0,0],[1,0],[2,0],[3,0]]

#테트로 6칸 짜리중에 가능하지 않은 두칸 제외하는 리스트
sero_remove_lst = [[[1,0],[1,1]],[[1,0],[0,1]],[[1,0],[2,1]],[[1,1],[0,0]],[[1,1],[2,0]]]
garo_remove_lst = [[[0,1],[1,1]],[[0,1],[1,0]],[[0,1],[1,2]],[[1,1],[0,0]],[[1,1],[0,2]]]
def remove_combi(lst,x,y):
    if (x,y) in lst:
        lst.remove((x,y))
        pass
    else:
        lst.remove((y,x))
    return lst
for x,y in sero_remove_lst:
    combi_sero = remove_combi(combi_sero,x,y)
for a,b in garo_remove_lst:
    combi_garo = remove_combi(combi_garo,a,b)

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0
#6칸 테트로 세로형
for sero6_x in range(n-2):
    for sero6_y in range(m-1):
        x = sero6_x
        y = sero6_y
        sum_all = graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y]+ graph[x+2][y]+ graph[x+2][y+1]
        for a,b in combi_sero:
            sum_remove = sum_all - graph[x+a[0]][y+a[1]] - graph[x+b[0]][y+b[1]]
            ans = max(ans,sum_remove)
#6칸 테트로 가로형
for garo6_x in range(n-1):
    for garo6_y in range(m-2):
        x = garo6_x
        y = garo6_y
        sum_all = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y]+ graph[x+1][y+1]+ graph[x+1][y+2]
        for a,b in combi_garo:
            sum_remove = sum_all - graph[x+a[0]][y+a[1]] - graph[x+b[0]][y+b[1]]
            ans = max(ans,sum_remove)
#한줄로 4칸 가로형
for one4_garox in range(n):
    for one4_seroy in range(m-3):
        x = one4_garox
        y = one4_seroy
        sum_all = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3]
        ans = max(ans, sum_all)
#한줄로 4칸 세로형
for one4_garox in range(n-3):
    for one4_seroy in range(m):
        x = one4_garox
        y = one4_seroy
        sum_all = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y]
        ans = max(ans, sum_all)
print(ans)