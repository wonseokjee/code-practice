N = int(input())
road = list(map(int,input().split()))
oil = list(map(int,input().split()))
min = 0
ins = 10000000000
for i in range(N-1):
    if ins > oil[i]:
        ins = oil[i]
    min += ins*road[i]
print(min)