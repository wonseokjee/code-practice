import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
numb = 1
arr_i = 0
arr_stack = [1]
ans = []
while(arr_i<n):
    if arr[arr_i] >= numb:
        if not numb==1:
            arr_stack.append(numb)
        ans.append('+')
        if arr[arr_i] == numb:
            ans.append('-')
            arr_stack.pop()
            arr_i += 1
        numb += 1
    elif arr[arr_i] < numb:
        if arr_stack[-1] == arr[arr_i]:
            arr_stack.pop()
            ans.append('-')
            arr_i += 1
        else:
            break
if arr_stack:
    print('NO')
else:
    print(*ans, sep='\n')