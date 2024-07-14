N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N-1,-1,-1):
    ans.insert(lst[i], str(i+1))
print(*ans)