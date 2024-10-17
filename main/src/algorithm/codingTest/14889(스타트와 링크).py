from itertools import combinations, permutations
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
lst = []
for i in range(N):
    lst.append(i+1)
combi = list(combinations(lst,N//2))
# print(combi)
ans = 100000000000001
for i in range(len(combi)//2, len(combi)):
    j = len(combi) - i - 1
    # print(combi[i],combi[j])
    perm_i = list(permutations(combi[i],2))
    perm_j = list(permutations(combi[j], 2))
    sum_i = 0
    sum_j = 0
    for k in range(len(perm_i)):
        sum_i += graph[perm_i[k][0]-1][perm_i[k][1]-1] + graph[perm_i[k][1]-1][perm_i[k][0]-1]
        sum_j += graph[perm_j[k][0]-1][perm_j[k][1]-1] + graph[perm_j[k][1]-1][perm_j[k][0]-1]
    # print(sum_i, sum_j)
    if abs(sum_i-sum_j) < ans:
        ans = abs(sum_i-sum_j)
print(ans//2)