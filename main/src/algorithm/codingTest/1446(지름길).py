n,d = map(int, input().split())
shortcut = [[] for _ in range(10001)]
road = [int(1e9)]*10001

for _ in range(n):
    s,e,sc = map(int, input().split())
    if not ((e-s < sc) or e>d):
        #입력받은 지름길을 시작칸에 넣어준다.
        shortcut[s].append((e, sc))

road[0] = 0
for j in range(d):
    # 지름길에서 거리를 모두 1로 연결한다.
    shortcut[j].append((j + 1, 1))
    for (e, sc) in shortcut[j]:
    # 지름길을 돌면서 최소값을 입력
        road[e] = min(road[e], sc+road[j])

print(road[d])


