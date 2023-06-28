n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans= 0
ins = 0
for i in range(n):
    ins += arr[i]
    ans += ins
print(ans)