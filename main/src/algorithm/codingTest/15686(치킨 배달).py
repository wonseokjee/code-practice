from itertools import combinations
n,m = map(int,input().split())
graph = []
chicken = []
home = []
for a in range(n):
    line = list(map(int,input().split()))
    for b in range(n):
        if line[b] == 0:
            continue
        elif line[b] == 1:
            home.append([a,b])
        elif line[b] == 2:
            chicken.append([a,b])
    graph.append(line)
chicken_combi = list(combinations(chicken,m))

ans = 1000000000
for i in range(len(chicken_combi)):
    shortcut = 0
    for j in range(len(home)):
        home_x,home_y = home[j][0], home[j][1]
        ins = 101
        for k in range(len(chicken_combi[0])):
            chic_x,chic_y = chicken_combi[i][k][0], chicken_combi[i][k][1]
            length = abs(home_x-chic_x) + abs(home_y-chic_y)
            ins = min(ins,length)
        shortcut += ins
    ans = min(shortcut,ans)


# print(graph)
# print(home)
# print(chicken_combi)
print(ans)


