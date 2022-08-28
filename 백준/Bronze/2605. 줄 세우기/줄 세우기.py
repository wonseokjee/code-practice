N = int(input())
arr = list(map(int, input().split()))
result = [1]
for i in range(1,N):
        result.insert(len(result)-arr[i],i+1)
print(*result)