import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lst = [-1]*n
stack = [0]
for i in range(1,n):
    while stack and arr[stack[-1]] < arr[i]:
        x = stack.pop()
        lst[x] = arr[i]
    stack.append(i)
print(*lst)





