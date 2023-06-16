n,m = map(int, input().split())
arr_sum = [0]*m
value_sum = 0
arr = list(map(int, input().split()))
for i in range(n):
    value_sum += arr[i]
    arr_sum[value_sum % m] += 1
ans = arr_sum[0]
for j in arr_sum:
    ans += (j*(j-1)//2)
print(ans)