import sys
input = sys.stdin.readline
n,q = map(int, input().split())
duck = [int(input()) for _ in range(q)]
visited = [False] * (n+1)
for i in duck:
    go = i
    ins = 0
    while(go >= 0):
        if go == 0:
            # print(0)
            if ins == 0:
                visited[i] = True
            break
        binary = go // 2
        if visited[go]: 
            ins = go
        go = binary
    print(ins)

# 6 5
# 3
# 5
# 6
# 2
# 2