N = int(input())
lst = [list(map(int, input().split())) for _ in range(2)]
ans = 0
lst[0].sort()
lst[1].sort(reverse=True)
# print(lst)
for i in range(N):
    ins = lst[0][i] * lst[1][i]
    ans += ins
print(ans)