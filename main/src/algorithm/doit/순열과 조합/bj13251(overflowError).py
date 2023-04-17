m = int(input())
rock = list(map(int, input().split()))
k = int(input())

def combi(x,y):
    num = 1
    for i in range(y-x+1, y+1):
        num *= i
    for j in range(1, x+1):
        num //= j
    return num

plsRock = sum(rock)
sameRock = 0
for i in range(m):
    if rock[i] >= k:
        sameRock += combi(k, rock[i])
ans = sameRock / combi(k, plsRock)
# print(round(ans,10))
print(ans)


